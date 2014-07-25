#!/bin/bash

fail_exit() { echo "$@" 1>&2; exit 1; }
failw_exit() { echo "$@"; exit 1; }

#set -o verbose
EXPECTED_ARGS=7

if [ $# -ne $EXPECTED_ARGS ]
then
    echo "Usage: `basename $0` process card tarballRepository tarballName produceWeights Nevents RandomSeed "
    echo "process names are: Dijet Zj WW hvq WZ  W_ew-BW Wbb Wj VBF_Hgg_H W Z  Wp_Wp_J_J VBF_Wp_Wp ZZ"  
    echo "Example: ./run_powheg_tarball.sh Z slc6_amd64_gcc481/powheg/V1.0/8TeV_Summer12/DYToEE_M-20_8TeV-powheg/v1/DYToEE_M-20_8TeV-powheg.input slc5_amd64_gcc462/8TeV/powheg Z true 1000 1212" 
    exit 1
fi

echo "   ______________________________________     "
echo "         Running Powheg                       "
echo "   ______________________________________     "

process=${1}
echo "%MSG-POWHEG process = $process"

cardinput=${2}
echo "%MSG-POWHEG location of the card = $cardinput"

tarballRepo=${3}
echo "%MSG-POWHEG precompiled tarball repository = $tarballRepo"

tarball=${4}
echo "%MSG-POWHEG precompiled tar ball file name = $tarball"

produceWeights=${5}
echo "%MSG-POWHEG Produce number of scale and PDF weights = $produceWeights"

nevt=${6}
echo "%MSG-POWHEG number of events requested = $nevt"

rnum=${7}
echo "%MSG-POWHEG random seed used for the run = $rnum"


seed=$rnum
file="events"
# Release to be used to define the environment and the compiler needed
export PRODHOME=`pwd`
export RELEASE=${CMSSW_VERSION}
export WORKDIR=`pwd`

# Get the input card
wget --no-check-certificate http://cms-project-generators.web.cern.ch/cms-project-generators/${cardinput} -O powheg.input  || fail_exit "Failed to obtain input card" ${cardinput}
card="$WORKDIR/powheg.input"

# initialize the CMS environment 
myDir=powhegbox_${process}
if [[ -e ${myDir} ]]; then
  mv ${myDir} old_${myDir}
  mv output.lhe old_output.lhe
fi

scram project -n ${myDir} CMSSW ${RELEASE}; cd ${myDir} ;  
eval `scram runtime -sh`

# force the f77 compiler to be the CMS defined one
#ln -s `which gfortran` f77
#ln -s `which gfortran` g77
export PATH=`pwd`:${PATH}

# FastJet and LHAPDF
#fastjet-config comes with the paths used at build time.
#we need this to replace with the correct paths obtained from scram tool info fastjet

newinstallationdir=`scram tool info fastjet | grep FASTJET_BASE |cut -d "=" -f2`
cp ${newinstallationdir}/bin/fastjet-config ./fastjet-config.orig

oldinstallationdir=`cat fastjet-config.orig | grep installationdir | head -n 1 | cut -d"=" -f2`
sed -e "s#${oldinstallationdir}#${newinstallationdir}#g" fastjet-config.orig > fastjet-config 
chmod +x fastjet-config

#same for lhapdf
newinstallationdirlha=`scram tool info lhapdf | grep LHAPDF_BASE |cut -d "=" -f2`
cp ${newinstallationdirlha}/bin/lhapdf-config ./lhapdf-config.orig
oldinstallationdirlha=`cat lhapdf-config.orig | grep prefix | head -n 1 | cut -d"=" -f2`
sed -e "s#prefix=${oldinstallationdirlha}#prefix=${newinstallationdirlha}#g" lhapdf-config.orig > lhapdf-config
chmod +x lhapdf-config

#svn checkout --username anonymous --password anonymous svn://powhegbox.mib.infn.it/trunk/POWHEG-BOX
# # retrieve the wanted POWHEG-BOX from the official repository 

LHA_BASE="`readlink -f "$LHAPATH/../../../"`"

LHA_BASE_OLD="`$LHA_BASE/bin/lhapdf-config --prefix`"
cat > lhapdf-config-wrap <<EOF
#!/bin/bash
"$LHA_BASE/bin/lhapdf-config" "\$@" | sed "s|$LHA_BASE_OLD|$LHA_BASE|g"
EOF
chmod a+x lhapdf-config-wrap

echo "Using a precompiled tar ball $tarball.tar.gz"
fn-fileget -c `cmsGetFnConnect frontier://smallfiles` ${tarballRepo}/${tarball}.tar.gz || true


if [[ -e ./${tarball}.tar.gz ]]; then
    tar xvzf ${tarball}.tar.gz
    cd ${process}
else
    echo "Error! The tar ball $tarball.tar.gz does not exist!"
    exit 1
fi



mkdir workdir
cd workdir
if [[ -e ../../pwggrid.dat ]]; then
 cp -p ../../*grid*.dat .
 cp -p ../../pwgubound.dat .
fi

cat ${card} | sed -e "s#SEED#${seed}#g" | sed -e "s#NEVENTS#${nevt}#g" > powheg.input

# Check if the powheg.input file contains the proper settings to calculate weights                                                                                                                             
if [ "$produceWeights" == "true" ];
then
    grep -q "storeinfo_rwgt 1" powheg.input ; test $? -eq 0 || failw_exit "No scale weights!"
    grep -q "pdfreweight 1" powheg.input ; test $? -eq 0 || failw_exit "No PDF weights!"
    cp -p powheg.input powheg.input.orig
    cat <<'EOF' >> powheg.input
lhrwgt_id 'c'
lhrwgt_descr 'muR=0.10000E+01 muF=0.10000E+01'
lhrwgt_group_name 'scale_variation'
lhrwgt_group_combine 'envelope'
EOF


fi

cat powheg.input
../pwhg_main &> log_${process}_${seed}.txt

if [ "$produceWeights" == "true" ];
then 
    cp -p pwgevents.lhe pwgevents.lhe.orig
    sed 's/storeinfo_rwgt 1/storeinfo_rwgt 0/g' powheg.input.orig > powheg.input.tmp
    echo -e "\ncompute_rwgt 1\n" >> powheg.input.tmp
    grep -q "storeinfo_rwgt 0" powheg.input.tmp ; test $? -eq 0 || failw_exit "Weights will be re-written!"
    grep -q "compute_rwgt 1" powheg.input.tmp ; test $? -eq 0 || failw_exit "Weights are not calculated!"

    echo -e "\ncomputing weights for 7 scale variation\n"
    iteration=-1
    lastfile=2
    counter=1000
    while [ $iteration -lt $lastfile ];
      do
      iteration=$(( iteration + 1 ))
      power1=`echo "2^$iteration" | bc`
      scale1=`echo "0.5*$power1" | bc`

      iter=-1
      last=2
      while [ $iter -lt $last ];
	do
	iter=$(( iter + 1 ))
	power2=`echo "2^$iter" | bc`
	scale2=`echo "0.5*$power2" | bc`
	rm -rf powheg.input	      
	if (( $(bc <<< "$scale1 <= 2*$scale2") == 1 && $(bc <<< "$scale1 >= 0.5*$scale2") == 1 )); 
	    then 
	    echo -e "\n doing scale ${scale1}, ${scale2}\n"
            sed  -e '/renscfact/s=1d0='$scale1'd0=' -e '/facscfact/s=1d0='$scale2'd0=' powheg.input.tmp > powheg.input

	    counter=$(( counter + 1 ))
	    echo -e "\nlhrwgt_id '${counter}'" >> powheg.input
	    echo -e "lhrwgt_descr 'muR=${scale1} muF=${scale2}'" >> powheg.input
	    echo -e "lhrwgt_group_name 'scale_variation'" >> powheg.input
	    echo -e "lhrwgt_group_combine 'envelope'" >> powheg.input

	    ../pwhg_main &>> reweightlog_${process}_${seed}.txt  
	    mv pwgevents-rwgt.lhe pwgevents.lhe
	    mv powheg.input powheg.input.${scale1}_${scale2}
	fi;      
      done
    done

    echo -e "\ncomputing weights for 52 CT10 PDF variation\n"
    iteration=11000
    lastfile=11052
    counter=2000
    while [ $iteration -lt $lastfile ];
      do
      iteration=$(( iteration + 1 ))
      echo -e "\n PDF set ${iteration}"
      cat powheg.input.tmp | sed '/lhans/s=11000='$iteration'=' > powheg.input

      counter=$(( counter + 1 ))
      echo -e "\nlhrwgt_id '${counter}'" >> powheg.input
      echo -e "lhrwgt_descr 'PDF set = ${iteration}'" >> powheg.input
      echo -e "lhrwgt_group_name 'PDF_variation'" >> powheg.input
      echo -e "lhrwgt_group_combine 'hessian'" >> powheg.input

      ../pwhg_main &>> reweightlog_${process}_${seed}.txt  
      mv pwgevents-rwgt.lhe pwgevents.lhe
      mv powheg.input powheg.input.${iteration}
    done

    rm -rf powheg.input*
    sed -e "/#new weight/d" -e "/<wgt id='c'>/d" -e "/<weight id='c'>/d" pwgevents.lhe > pwgevents.lhe.tmp
    mv pwgevents.lhe.tmp pwgevents.lhe 
    echo -e "\n finished computing weights ..\n" 
fi

cat pwgevents.lhe | grep -v "Random number generator exit values" > ${file}_final.lhe

ls -l ${file}_final.lhe
pwd
cp ${file}_final.lhe ${WORKDIR}/.


echo "Output ready with ${file}_final.lhe at $WORKDIR"
echo "End of job on " `date`
exit 0;
