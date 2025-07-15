#!/usr/bin/env bash

function usage() {
	echo "Usage: raindrops <number>" >&2
	exit 1
}

# check argument and if digit
if [ ! "$#" -eq 1 ] && ! [[ $1 =~ ^[0-9]+$ ]]; then
  usage
fi

output=""

if [ $(($1 % 3)) -eq 0 ]; then
	output="Pling"
fi

if [ $(($1 % 5)) -eq 0 ]; then
	output="${output}Plang"
fi

if [ $(($1 % 7)) -eq 0 ]; then
	output="${output}Plong"
fi

if [ -z $output ]; then
	echo "$1"
else
	echo "$output"
fi