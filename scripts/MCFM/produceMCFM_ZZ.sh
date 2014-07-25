#!/bin/sh

if [ -z $7 ] ; then
    echo "Usage: $0 [PROC] [STRING] [NITER] [PDFGROUP] [PDFSET] [CM] [MMIN]"
    echo "If PDFSET is -1, will do PDF error evalulation."
    echo "PROC 81: with gamma*, PROC 86: no gamma*"
    exit 1
fi

let k=$RANDOM
echo $k
i=`date '+%s'`
echo $i
#let SEED=$i+$k
let SEED=$k
echo $SEED

PROC=$1
STRING=$2
NITER=$3
PDFGROUP=$4
PDFSET=$5
CM=$6
MMIN=$7
INCLUSIVE=true

FILENAME=mcfm_${PROC}_${CM}GeV_m${MMIN}_${PDFGROUP}_${PDFSET}_${STRING}.DAT

echo "JOB index " $JOB
echo "SEED = " $SEED
echo Will do: $PROC $STRING $NITER $PDFGROUP $PDFSET $CM $MMIN
echo "sqrt(s) = " $CM " GeV"
echo "M(ll) >" $MMIN " GeV/c^2"
echo "Output file name: " $FILENAME

cat > ${FILENAME} << EOF
'6.1'		[file version number]

[Flags to specify the mode in which MCFM is run]
.false.		[evtgen]
.false.		[creatent]
.false.		[skipnt]
.false.		[dswhisto]
.false.		[writetop]
.false.		[writedat]
.false.		[writegnu]
.true.		[writeroot]

[General options to specify the process and execution]
${PROC}	        [nproc]
'tota'  	[part 'lord','real' or 'virt','tota']
'${STRING}${JOB}'            ['runstring']
${CM}d0		[sqrts in GeV]
+1		[ih1 =1 for proton and -1 for antiproton]
+1		[ih2 =1 for proton and -1 for antiproton]
120d0		[hmass]
-1.0d0		[scale:QCD scale choice]
-1.0d0		[facscale:QCD fac_scale choice]
.false.         [dynamicscale, of the four momentum sum of outgoing parton]
.false.		[zerowidth]
.false.		[removebr]
10		[itmx1, number of iterations for pre-conditioning]
${NITER}	[ncall1]
10		[itmx2, number of iterations for final run]
${NITER}	[ncall2]
${SEED}		[ij, seed]
.false.		[dryrun]
.true.		[Qflag]
.true.		[Gflag]

[Heavy quark masses]
172.5d0		[top mass]
4.75d0		[bottom mass]
1.5d0		[charm mass]

[Pdf selection]
'cteq66m'	        [pdlabel]
4		        [NGROUP, see PDFLIB]
46		        [NSET - see PDFLIB]
${PDFGROUP}.LHgrid      [LHAPDF group]
${PDFSET}  	        [LHAPDF set]

[Jet definition and event cuts]
${MMIN}d0	[m34min]
14000d0 	[m34max]
${MMIN}d0	[m56min]
14000d0		[m56max]
.true.          [inclusive *****]
'ankt'		[algorithm]
0d0		[ptjet_min]
0d0		[|etajet|_min]
20d0		[|etajet|_max]
0.5d0		[Rcut_jet]  
.false.		[makecuts]
20d0		[ptlepton_min]
2.5d0     	[|etalepton|_max]
0d0		[ptmin_missing]
5d0		[ptlepton(2nd+)_min]
2.5d0	        [|etalepton(2nd+)|_max]
0.0d0		[minimum (3,4) transverse mass] 
0.0d0	        [R(jet,lept)_min]
0.0d0		[R(lept,lept)_min]
0d0		[Delta_eta(jet,jet)_min]
.false.		[jets_opphem]
0		[lepbtwnjets_scheme]
0d0             [ptmin_bjet]
0d0		[etamax_bjet]

[Settings for photon processes]
.false.         [fragmentation included]
'BFGsetII'      [fragmentation set]
80d0            [fragmentation scale]
20d0		[ptmin_photon]
1.44d0		[etamax_photon]
0.7d0           [R(photon,lept)_min]
0.7d0           [cone size for isolation]
0.15d0		[epsilon_h, energy fraction for isolation]

[Anomalous couplings of the W and Z]
0.0d0		[Delta_g1(Z)]
0.0d0		[Delta_K(Z)]
0.0d0		[Delta_K(gamma)]
0.0d0		[Lambda(Z)]
0.0d0		[Lambda(gamma)]
0.0d0		[h1(Z)]
0.0d0		[h1(gamma)]
0.0d0		[h2(Z)]
0.0d0		[h2(gamma)]
0.0d0		[h3(Z)]
0.0d0		[h3(gamma)]
0.0d0		[h4(Z)]
0.0d0		[h4(gamma)]
2.0d0		[Form-factor scale, in TeV]

[How to resume/save a run]
.false.		[readin]
.false.		[writeout]
''		[ingridfile]
''		[outgridfile]

[Technical parameters that should not normally be changed]
.false.		[debug]
.true.		[verbose]
.false.		[new_pspace]
.false.		[virtonly]
.false.		[realonly]
.true.		[spira]
.false.		[noglue]
.false.		[ggonly]
.false.		[gqonly]
.false.		[omitgg]
.false.		[vanillafiles]
1		[nmin]
2		[nmax]
.true.		[clustering]
.false.		[realwt]
0		[colourchoice]
1d-2		[rtsmin]
1d-4		[cutoff]
1d0		[aii]
1d0		[aif]
1d0		[afi]
1d0		[aff]
1d0             [bfi]
1d0             [bff]
EOF
#

#echo doing: cp $FILENAME ..
#cp $FILENAME ..


exit
