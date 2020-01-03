#!/usr/bin/python3
import sys
import itertools

final_dict=dict()
pre=[]
ano=[]
one=[]
rr=dict()
some=dict()

for line in sys.stdin:
	line=line.strip()
	array=line.split("_")
	
	key1,key2,val1,val2=array[0],array[1],int(array[2]),int(array[3])
	if((key1,key2) not in final_dict):
		final_dict[key1,key2]=(val1,val2)
		
	else:
		d=final_dict[key1,key2]
		final_dict[key1,key2]=(val1+d[0],val2+d[1])

for k,v in final_dict.items():
	runrate=(v[0]/float(v[1]))
	final_dict[k]=(runrate,v[1])


for j in sorted(final_dict.items(),reverse=True,key=lambda x:x[1]):
	pre.append(j)		

for i in range(len(pre)):
	if(pre[i][0][0] not in ano):
		if(int(pre[i][1][1])>9):
			ano.append(pre[i][0][0])
			rr[pre[i][0][0],pre[i][0][1]]=(pre[i][1][0],pre[i][1][1])
	
for k,v in sorted(rr.items(),reverse=False,key=lambda x:x[0]):
	print(k[0]+","+k[1])

