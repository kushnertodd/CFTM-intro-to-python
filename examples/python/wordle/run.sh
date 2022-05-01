for f in *.txt
do 
  echo ==========
  echo $f
  echo ----------
  for w in `cat $f`; do
    python3 etaoinshrdlu.py $w
  done
done
