
#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -file s.py -mapper 'python3 s.py' -file r.py -reducer 'python3 r.py' -input /new -output /output


import os

with open("query.txt", 'w') as file:
    file.write(input("Enter Query: "))  
    file.close()

fd_query = open('query.txt','r')
in_query= fd_query.read()
in_query=(in_query.split())
#print(in_query)



if(in_query[0]=="SELECT"):
    table=in_query[in_query.index('FROM')+1].split('/')[1].split('.')[0]
    database=in_query[in_query.index('FROM')+1].split('/')[0]
   
    locMap=os.popen("readlink -f mapper.py").read()
    locRed=os.popen("readlink -f reducer.py").read()
    #os.system('cat '+table+'.csv | python3 mapper.py | python3 reducer.py')
    os.system("hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -file mapper.py -mapper 'python3 mapper.py' -file reducer1.py -reducer 'python3 reducer1.py' -input /"+database+"/"+table+".csv -output /output")
    print()
    print("#######################    OUTPUT     ########################")
    for i in in_query:
    	print(i,end=" ")
    print()
    os.system("hdfs dfs -cat /output/part-00000")
    print()
    os.system("hdfs dfs -rm -r /output")
   
elif(in_query[0]=="LOAD"):

    db_load=in_query[1].split('/')[0]
    db_table=in_query[1].split('/')[1].split('.')[0]
   
    os.system("hdfs dfs -mkdir /project/"+db_load)
    os.system("hdfs dfs -mkdir /project/"+db_load+"/"+db_table)
    os.system("hdfs dfs -touchz /project/"+db_load+"/"+db_table+"/"+db_table+".csv")
  
  
    f1=open(db_table+'.txt','w')
    for i in range(in_query.index('(')+1,in_query.index(')')):
        f1.write(in_query[i])
    f1.close()
  
    location=os.popen("readlink -f "+db_table+".txt").read()
  
    #print(location)
    os.system("hdfs dfs -put "+location.rstrip()+" /project/"+db_load)
   

elif(in_query[0]=="DELETE"):
   
    db_delete=in_query[1].split('/')[0]
    table_delete=in_query[1].split('/')[1].split('.')[0]
  
  
    os.system("hdfs dfs -rmr /project/"+db_delete+"/"+table_delete+".txt")
    os.system("hdfs dfs -rmr /project/"+db_delete+"/"+table_delete)

else:

    print("Invalid syntax")
