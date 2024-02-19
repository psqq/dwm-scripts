
if [ ! -z $1 ]; then
dir1=$1
bg1=$(find $dir1 -type f | shuf -n 1)
fi

if [ ! -z $2 ]; then
dir2=$2
bg2=$(find $dir2 -type f | shuf -n 1)
fi

feh --bg-fill "$bg1" "$bg2"
