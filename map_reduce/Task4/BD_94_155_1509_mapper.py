#!/usr/bin/python3
import sys
stadium=""
file=sys.stdin
for line in file:
	line_array=line.strip()
	listm=line_array.split(',')
	if(len(listm)>=7):
		if(listm[8]=='0'):
			j=int(listm[7])	
			print(stadium,listm[4],j,1,sep='_')
			if(listm[1]=='venue'):
				if(listm[1]=='venue' and len(listm)==3):
					stadium=mylist[2]
				if(listm[1]=='venue' and len(listm)==4):
					stadium=str(str(listm[2])+","+str(listm[3]))
	else:
		if(listm[1]=='venue'):
			if(listm[1]=='venue' and len(listm)==3):
				stadium=listm[2]
			if(listm[1]=='venue' and len(listm)==4):
				stadium=str(str(listm[2])+","+str(listm[3]))
