#!/bin/sh

if [ -z $6 ] ; then
    echo "Usage: $0 [PROC] [STRING] [PDFGROUP] [MINCUT] [SCALE] [QCDSCALE]"
    exit 1
fi

export mw=80.398
export mz=91.1867
export mt=172.5

if (( $1 >= 61 && $1 <= 69 ));  then

    echo "This is a WW production"
    SCALE=`echo "$5 * $mw" | bc`
    QCDSCALE=`echo "$6 * $mw" | bc`
    echo "SCALE:" $SCALE
    echo "QCDSCLE:" $QCDSCALE

elif (( $1 >= 81 && $1 <= 90 )) ; then

    echo "This is a ZZ production"
    SCALE=`echo "$5 * $mz" | bc`
    QCDSCALE=`echo "$6 * $mz" | bc`
    echo "SCALE:" $SCALE
    echo "QCDSCLE:" $QCDSCALE

elif (( $1 >= 71 && $1 <= 80 )); then

    echo "This is a WZ production"
    SCALE=`echo "$5 * 0.5 * ($mw + $mz)" | bc`
    QCDSCALE=`echo "$6 * 0.5 * ($mw + $mz)" | bc`
    echo "SCALE:" $SCALE
    echo "QCDSCLE:" $QCDSCALE

elif (( $1 >=141 && $1 <= 151 )); then

    SCALE=`echo "$5 * $mt" | bc`
    QCDSCALE=`echo "$6 * $mt" | bc`
    echo "SCALE:" $SCALE
    echo "QCDSCLE:" $QCDSCALE

else
    echo "Not valid option!"
    SCALE=-1
    QCDSCALE=-1
    echo "SCALE:" $SCALE
    echo "QCDSCLE:" $QCDSCALE
fi

## You need to add space between "==" and other numbers.
## 
## For this comparison, I prefer using float comparison,
## not string comparison, in this way, your $5 and $6 could be 
## 0.000, 0.00, 0.0000, or 0, instead of exactly "0.0

#if [ $5 == "0.0" ] && [ $6 == "0.0" ]; then
#    SCALE=-1
#    QCDSCALE=-1
#fi

if [ $(echo "$5 == 0"|bc) -eq 1 ] && [ $(echo "$6 == 0"|bc) -eq 1 ]; then
    SCALE=-1
    QCDSCALE=-1
    echo "SCALE:" $SCALE
    echo "QCDSCLE:" $QCDSCALE
fi

PROC=$1
STRING=$2
PDFGROUP=$3
MINCUT=$4
INCLUSIVE=true
SHORT=`echo "$3" |cut -c1-5`
FILENAME=${SHORT}_${PROC}_${5}_${6}_cut${MINCUT}_${STRING}.DAT
echo "Output file name: " $FILENAME

cat > ${FILENAME} << EOF
'6.6'		[file version number]

[Flags to specify the mode in which MCFM is run]
.false.		[evtgen]
.false.		[creatent]
.false.		[skipnt]
.false.		[dswhisto]
.false.		[writetop]
.false.		[writedat]
.false.		[writegnu]
.true.		[writeroot]
.false.         [writepwg] 

[General options to specify the process and execution]
${PROC}	        [nproc]
'tota'  	[part 'lord','real' or 'virt','tota']
'${STRING}${JOB}'            ['runstring']
8000d0		[sqrts in GeV]
+1		[ih1 =1 for proton and -1 for antiproton]
+1		[ih2 =1 for proton and -1 for antiproton]
126d0		[hmass]
${SCALE}d0      [scale:QCD scale choice]
${QCDSCALE}d0  	[facscale:QCD fac_scale choice]
.false.         [dynamicscale, of the four momentum sum of outgoing parton]
.false.		[zerowidth]
.false.		[removebr]
10		[itmx1, number of iterations for pre-conditioning]
10000    	[ncall1]
10		[itmx2, number of iterations for final run]
10000   	[ncall2]
1089		[ij]
.false.		[dryrun]
.true.		[Qflag]
.true.		[Gflag]

[Heavy quark masses]
173.2d0		[top mass]
4.75d0		[bottom mass]
1.5d0		[charm mass]

[Pdf selection]
'cteq66m'	        [pdlabel]
4		        [NGROUP, see PDFLIB]
46		        [NSET - see PDFLIB]
${PDFGROUP}.LHgrid      [LHAPDF group]
-1       	        [LHAPDF set]

[Jet definition and event cuts]
${MINCUT}       [m34min]
14000d0 	[m34max]
${MINCUT}       [m56min]
14000d0		[m56max]
.true.          [inclusive]
'ankt'		[algorithm]
15d0		[ptjet_min]
0d0		[|etajet|_min]
3d0		[|etajet|_max]
0.5d0		[Rcut_jet]  
.false.		[makecuts]
0d0		[ptlepton_min]
99d0     	[|etalepton|_max]
0d0		[ptmin_missing]
0d0		[ptlepton(2nd+)_min]
99d0	        [|etalepton(2nd+)|_max]
0.0d0		[minimum (3,4) transverse mass] 
0.0d0	        [R(jet,lept)_min]
0.0d0		[R(lept,lept)_min]
0d0		[Delta_eta(jet,jet)_min]
.false.		[jets_opphem]
0		[lepbtwnjets_scheme]
0d0             [ptmin_bjet]
99d0		[etamax_bjet]

[Settings for photon processes]
.false.         [fragmentation included]
'BFGsetII'      [fragmentation set]
80d0            [fragmentation scale]
20d0		[ptmin_photon]
2.5d0		[etamax_photon]
10d0            [ptmin_photon2]
0.7d0           [R(photon,lept)_min]
0.4d0           [R(photon,photon)_min]
0.7d0           [cone size for isolation]
0.4d0		[epsilon_h, energy fraction for isolation]

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

exit
