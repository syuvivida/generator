#!/bin/bash


iteration=300
lastfile=400

while [ $iteration -lt $lastfile ]; 
do
  iteration=$(( iteration + 1 ))
  echo "iter" $iteration  
  
  bsub -q 1nw $PWD/runJob.sh $iteration   

done
