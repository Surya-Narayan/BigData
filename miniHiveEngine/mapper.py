#!usr/bin/python3
import os
import sys
import re
import csv

q=open("query.txt","r")
com=q.read()
com=com.split()
q.close()
#print(com)

#print(line)
#if SELECT operation
if com==["exit"]:
	print("Exiting..")
elif com[0]=="SELECT":
	table=com[com.index("FROM")+1].split('/')[1].split('.')[0]
	db=com[com.index("FROM")+1].split('/')[0]
	#fd=open(table+".csv","r")
	#infile = fd.read()
	#fd.close()
	infile = sys.stdin
	line=list()
	for l in infile:
		line.append(l.strip())
	#print(line)
	
	fd_Sch=open(table+".txt","r")
	sch = fd_Sch.read().strip('\n')
	fd_Sch.close()
	#print(schema)
	sch=sch.split(',')
	#print(sch)
	
	#print(infile)
	out=list()
	#print(com)
	#next(infile)
	#line=infile.strip()
	#line=infile.split('\n')
	#if a WHERE clause exists
	#print(com)
	if com[1][:3] not in ["MAX","MIN","AVG"]:
		if "WHERE" not in com:
			ind=list()
			#If it is a select all operation
			if com[1]=="*":
				for l in line:
					l=l.split(',')
					#print(l)
					stri=""
					for i in range(len(l)):
						stri+=str(l[i])+","
					out.append(stri[:(len(stri)-1)])
			else:
				for co in com[1].split(','):
					if (co in sch):
						ind.append(sch.index(co))
				for l in line:
					l=l.split(',')
					#print(l)
					stri=""
					for i in range(len(ind)):
						stri+=str(l[ind[i]])+','
					out.append(stri[:(len(stri)-1)])
		else:
			#print(com[com.index("WHERE")+1])
			if "="==com[com.index("WHERE")+2]:
				condcol=com[com.index("WHERE")+1]
				if "\n" in condcol:
					condcol.remove("\n")
				#print(cond)
				condval=com[com.index("=")+1]
				ind=list()
				if com[1]=="*":
					for l in line:
						l=l.split(',')
						#print(condcol,sch)
						if l[sch.index(condcol)]==condval:
							stri=""
							for i in range(len(l)):
								stri+=str(l[i])+','
							out.append(stri[:(len(stri)-1)])
				else:
					for co in com[1].split(','):
						if co in sch:
							ind.append(sch.index(co))
					for l in line:
						l=l.split(',')
						#print(l)
						if l[sch.index(condcol.rstrip('\n\n'))]==condval:
							stri=""
							for i in range(len(ind)):
								stri+=str(l[ind[i]])+','
							out.append(stri[:(len(stri)-1)])
			if ">" == com[com.index("WHERE")+2]:
				condcol=com[com.index("WHERE")+1]
				#print(cond)
				condval=com[com.index(">")+1]
				ind=list()
				if com[1]=="*":
					for l in line:
						l=l.split(',')
						if float(l[sch.index(condcol)])>float(condval):
							stri=""
							for i in range(1,len(l)):
								stri+=str(l[i])+','
							out.append(stri[:(len(stri)-1)])
				else:
					for co in com[1].split(','):
						if co in sch:
							ind.append(sch.index(co))
					for l in line:
						l=l.split(',')
						#print(l)
						if float(l[sch.index(condcol)])>float(condval):
							stri=""
							for i in range(len(ind)):
								stri+=str(l[ind[i]])+','
							out.append(stri[:(len(stri)-1)])
			if "<" == com[com.index("WHERE")+2]:
				#print(cond)
				condcol=sch.index(com[com.index("WHERE")+1])
				condval=com[com.index("<")+1]
				ind=list()
				if com[1]=="*":
					for l in line:
						l=l.split(',')
						if float(l[condcol])<float(condval):
							stri=""
							for i in range(1,len(l)):
								stri+=str(l[i])+','
							out.append(stri[:(len(stri)-1)])
				else:
					for co in com[1].split(','):
						if co in sch:
							ind.append(sch.index(co))
					for l in line:
						l=l.split(',')
						#print(l)
						if float(l[condcol])<float(condval):
							stri=""
							for i in range(len(ind)):
								stri+=str(l[ind[i]])+','
							out.append(stri[:(len(stri)-1)])
	else:
		if "MIN" in com[1]:
			arg="MIN"
		elif "MAX" in com[1]:
			arg="MAX"
		elif "AVG" in com[1]:
			arg="AVG"
		print(arg)
		#print(com[1])
		com[1]=com[1][4:(len(com[1])-1)]
		#print(com[1])
		if "WHERE" not in com:
			ind=list()
			#If it is a select all operation
			if com[1]=="*":
				for l in line:
					l=l.split(',')
					#print(l)
					stri=""
					for i in range(len(l)):
						stri+=str(l[i])+","
					out.append(stri[:(len(stri)-1)])
			else:
				for co in com[1].split(','):
					if (co in sch):
						ind.append(sch.index(co))
				#print(ind)
				for l in line:
					l=l.split(',')
					#print(l)
					stri=""
					for i in range(len(ind)):
						stri+=str(l[ind[i]])+','
					#print(stri)
					out.append(stri[:(len(stri)-1)])
		else:
			#print(com[com.index("WHERE")+1])
			if "="==com[com.index("WHERE")+2]:
				condcol=com[com.index("WHERE")+1]
				if "\n" in condcol:
					condcol.remove("\n")
				#print(cond)
				condval=''
				condval=com[com.index("=")+1]
				#print(condval)
				ind=list()
				if com[1]=="*":
					for l in line:
						l=l.split(',')
						#print(condcol,sch)
						if l[sch.index(condcol)]==condval:
							stri=""
							for i in range(len(l)):
								stri+=str(l[i])+','
							out.append(stri[:(len(stri)-1)])
				else:
					for co in com[1].split(','):
						if co in sch:
							ind.append(sch.index(co))
					for l in line:
						l=l.split(',')
						#print(l)
						if l[sch.index(condcol.rstrip('\n\n'))]==condval:
							stri=""
							for i in range(len(ind)):
								stri+=str(l[ind[i]])+','
							out.append(stri[:(len(stri)-1)])
			if ">" == com[com.index("WHERE")+2]:
				condcol=com[com.index("WHERE")+1]
				#print(cond)
				condval=com[com.index(">")+1]
				ind=list()
				if com[1]=="*":
					for l in line:
						l=l.split(',')
						if float(l[sch.index(condcol)])>float(condval):
							stri=""
							for i in range(1,len(l)):
								stri+=str(l[i])+','
							out.append(stri[:(len(stri)-1)])
				else:
					for co in com[1].split(','):
						#print(co,sch)
						if co in sch:
							ind.append(sch.index(co))
					#print(line) 
					for l in line:
						l=l.split(',')
						#print(l)
						print(l[sch.index(condcol)],condval)
						if float(l[sch.index(condcol)])>float(condval):
							stri=""
							for i in range(len(ind)):
								stri+=str(l[ind[i]])+','
							out.append(stri[:(len(stri)-1)])
			if "<" == com[com.index("WHERE")+2]:
				#print(cond)
				condcol=sch.index(com[com.index("WHERE")+1])
				condval=com[com.index("<")+1]
				ind=list()
				if com[1]=="*":
					for l in line:
						l=l.split(',')
						if float(l[condcol])<float(condval):
							stri=""
							for i in range(1,len(l)):
								stri+=str(l[i])+','
							out.append(stri[:(len(stri)-1)])
				else:
					for co in com[1].split(','):
						if co in sch:
							ind.append(sch.index(co))
					for l in line:
						l=l.split(',')
						#print(l)
						if float(l[condcol])<float(condval):
							stri=""
							for i in range(len(ind)):
								stri+=str(l[ind[i]])+','
							out.append(stri[:(len(stri)-1)])
					
				
	for ou in out:
		print("%s"%(ou))
		
