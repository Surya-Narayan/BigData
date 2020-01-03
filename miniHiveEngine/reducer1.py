#!usr/bin/python3

import os
import sys

aggrflag=0
data=list()
dat=list()
aggr=["MIN","MAX","AVG"]

def average(x):
	s=0
	for i in x:
		s+=float(i)
	return s/len(x)

for l in sys.stdin:
	data.append(l.strip())

while "" in data:
	data.remove("")

for i in aggr:
	if i in data:
		aggrflag=1
		arg=i
		break

if aggrflag:
	data.remove(arg)
	try:
		for i in data:
			dat.append(float(i))
		if arg == "MIN":
			res = min(dat)
		elif arg == "MAX":
			res = max(dat)
		elif arg == "AVG":
			res = average(dat)
	except ValueError:
		res="Invalid Datatype"
	print(res)
else:
	for i in data:
		print(i)
