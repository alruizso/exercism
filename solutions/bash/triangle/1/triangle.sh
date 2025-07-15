#!/usr/bin/env bash

v=$1
n=0

assign_number(){
    if echo $1 | grep -qe '\.'; then
        decimal=`echo $1 | cut -d'.' -f2`
        return $decimal
    fi
    return $1
}

assign_number $2
a=$?
assign_number $3
b=$?
assign_number $4
c=$?

if [ $a -eq 0 -o $b -eq 0 -o $c -eq 0 ];then echo 'false'; exit 0; fi
if ! [ $(($a + $b)) -ge $c -a $(($b + $c)) -ge $a -a $(($a + $c)) -ge $b ]; then
    echo 'false'
    exit 0
fi

case $v in
    equilateral)
        if [ $a -eq $b -a $a -eq $c -a $b -eq $c ]; then
            echo 'true'
            exit 0
        fi
        echo 'false'
        ;;
    isosceles)
        if [ $a -eq $b ]; then n=$((n+1)); fi
        if [ $a -eq $c ]; then n=$((n+1)); fi
        if [ $b -eq $c ]; then n=$((n+1)); fi
        if [ $n -ge 1 ]; then
            echo 'true'
            exit 0
        fi
        echo 'false'
        ;;
    scalene)
        if [ $a -ne $b -a $a -ne $c -a $b -ne $c ]; then
            echo 'true'
            exit 0
        fi
        echo 'false'
        ;;
    *)
        echo 'error'
        ;;
esac