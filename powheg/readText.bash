#!/bin/bash
read -d "\n" a b c d e f g < $1
./create_powheg_tarball.sh $a $b $c $d $e $f $g
