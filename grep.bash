#! /bin/bash

usage_exit() {
    echo "Usage: $0 [options] PATTERN ..." 1>&2
    echo "Options:" 1>&2
    echo "  -r: recursive" 1>&2
    exit 1
}

while getopts rh OPT
do
    case $OPT in
        r)  recursive=1
            ;;
        h)  usage_exit
            ;;
        \?) usage_exit
            ;;
    esac
done

shift $((OPTIND - 1))
if [[ $# -lt 1 ]]; then
   usage_exit
fi

pattern="$1"
shift

for file in "$@";do
    while read line;do
	if [[ $line =~ $pattern ]];then
	    echo "$file:$line"
	fi
    done < "$file"
done
