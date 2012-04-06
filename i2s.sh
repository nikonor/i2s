#!/bin/bash

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
					if [ "$perl" == "$python" ];
						then
							echo "ok:"$perl"=="$python
						else
							echo
							echo "error:"$perl"<>"$python
							echo
					fi
				done

			else
				perl=`./i2s.pl --get $1`
				python=`./i2s.py --get $1`
				if [ "$perl" == "$python" ];
					then
						echo "ok:"$perl"=="$python
					else
						echo "error:"$perl"<>"$python
				fi
		fi
fi
