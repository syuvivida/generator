#!/bin/bash

cd $1

export SCRAM_ARCH=slc6_amd64_gcc491; eval `scramv1 runtime -sh`

read -d "\n" a b c d e f g h < $2

if [[ $d == *PWD* ]]; then
 sub=`echo "${d##*/}"`
 d=$1"/"$sub
 echo $d
fi

./create_powheg_tarball.sh $a $b $c $d $e $f $g $h



