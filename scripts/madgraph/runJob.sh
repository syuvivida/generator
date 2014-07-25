#!/bin/tcsh

cd /afs/cern.ch/user/s/syu/scratch0/CMSSW_5_3_2_patch4/src

setenv SCRAM_ARCH slc5_amd64_gcc462; eval `scramv1 runtime -csh`

cd /afs/cern.ch/work/s/syu/madgraph/MG5v1.1

./produceMadgraph.sh $1 10 100000

