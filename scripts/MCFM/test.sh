#!/bin/sh

export mw=80.398
x=`echo "$1 * $mw" | bc`  
echo $x
