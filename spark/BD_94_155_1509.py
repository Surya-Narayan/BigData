from __future__ import print_function

import re
import sys
from operator import add

from pyspark.sql import SparkSession


def avg(urls):
    parts = re.split(r',+',urls)
    return parts[0],int(parts[2])/int(parts[3])
    

def computeContribs(urls, rank):
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    parts = re.split(r',+', urls)
    return parts[0],parts[1]
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: pagerank <file> <iterations> <weights>", file=sys.stderr)
        sys.exit(-1)
    if(int(sys.argv[3])==0):
        first=0.80
        second=0.20
    if(int(sys.argv[3])>0):
        first=sys.argv[3]*0.01
        second=1-first	
    # Initialize the spark context.
    spark = SparkSession\
        .builder\
        .appName("PythonPageRank")\
        .getOrCreate()
    
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    #print(lines.collect())
    
    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()
    #print(links.collect())
    inter_ranks = lines.map(lambda urls: avg(urls)).distinct().reduceByKey(add)
    ranks=inter_ranks.map(lambda x:(x[0],max(x[1],1))).sortBy(lambda x:(x[1],x[0]),False)
    #t = ranks.collect()
    #print(ranks)
    
    iterations=0
    #print("RANKS:",ranks.collect())
    #print(ranks.collect())
    if(int(sys.argv[2])!=0): #Non-convergence case:
        for iteration in range(int(sys.argv[2])):
            contribs = links.join(ranks).flatMap(lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
            #contribs.collect()
            ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank*first + second).sortBy(lambda x:(x[1],x[0]),False)
          
    else:
   
        conv=1.0
        while(abs(conv)>0.0001):
            contribs = links.join(ranks).flatMap(lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
            t = ranks.sortBy(lambda x:(x[1],x[0]),False).collect()
            ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank*first + second).sortBy(lambda x:(x[1],x[0]),False)
	    #print(ranks.collect()[0][1])
                       
            conv = t[1][1] - ranks.collect()[1][1]
            iterations+=1
            #conv = conv +1
        
    for (link, rank) in ranks.collect():#sortBy(lambda x:(x[1],x[0]),False).collect():
        print("%s,%.14s" % (link, rank))
    print("ITERATIONS:",iterations)
    #ranks.collect().sort(key = lambda x: x[1],reverse = True)
    #print(ranks.collect())
    

    spark.stop()
