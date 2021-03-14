#!/bin/bash
prog=$1
files=$(ls ./inputs)

g++ prog
rm ./tempos/tempos.txt
for file in $files
do
	./a.out < ./inputs/$file >> ./tempos/tempos.txt
done

