#!/bin/bash
if [ -z "$2" ] ; then
  echo usage: $0 letters fixed
  exit
fi
letters=$1
fixed=$2
python3 wordle-dict.py dict5.txt $letters $fixed
