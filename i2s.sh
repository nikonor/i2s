#!/bin/bash

# cat list_4_test.txt | awk '{print $1}' | while read i; do ./i2s.sh $i; done | grep error
# ./i2s.sh 912; ./i2s.sh 912912 ; ./i2s.sh 912912912; ./i2s.sh 901;  ./i2s.sh 901901;  ./i2s.sh 901901901; 


if [ "$1" == "" ]
	then
		echo "Use: ./i2s.sh <integer dig> [<last integer dig>]"
	else
		if [ "$2" != "" ];
			then 
				jot $1 $2 | while read s;
				 do 
					perl=`./i2s.pl --get $s`
					python=`./i2s.py --get $s`
					if [ "$perl" != "$python" ];
						then
							echo
							echo "error"
							echo $1
							echo "pl:"$perl
							echo "py:"$python
							echo
					fi
				done

			else
				perl=`./i2s.pl --get $1`
				python=`./i2s.py --get $1`
				if [ "$perl" != "$python" ];
					then
						echo
						echo "error"
						echo $1
						echo "pl:"$perl
						echo "py:"$python
						echo

				fi
		fi
fi
