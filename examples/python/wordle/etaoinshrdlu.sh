if [ -z "$1" ] ; then
  echo usage $0 file
  exit
fi
for w in `cat $1`; do
    python3 etaoinshrdul.py $w
done
