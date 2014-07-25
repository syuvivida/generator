#!/bin/tcsh

setenv mw 80.398
set x = `echo "$1 * $mw" | bc`  
echo $x
