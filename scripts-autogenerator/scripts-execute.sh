#!/bin/bash

FILES=mysql/*l1d*l1i*

for f in $FILES
do
  nohup bash "$f" &
  sleep 1
done


