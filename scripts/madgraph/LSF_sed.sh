#!/bin/bash


iteration=66
lastfile=67

while [ $iteration -lt $lastfile ]; 
do
  iteration=$(( iteration + 1 ))
  echo "iter" $iteration  
  filename=(`head -n $iteration input | tail -1`)
  echo $filename
  sed 's/INPUT/'$filename'/g;s/zj_zjj_xqcut5_qcut10.root/zj_zjj_xqcut5_qcut10_'$iteration'.root/g' genOnly_qcut10.py >& genOnly_qcut10_$iteration.py
  bsub -q 1nw $PWD/runJob.sh $iteration
done
