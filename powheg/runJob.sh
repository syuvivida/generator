#!/bin/bash

cd $1

export SCRAM_ARCH=slc6_amd64_gcc481; eval `scramv1 runtime -sh`

read -d "\n" a b c d e f g < $2
./create_powheg_tarball.sh $a $b $c $d $e $f $g



