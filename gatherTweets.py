# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:30:55 2014

@author: balikasg
"""
from  twitter import *

yourKeyword="jobs statistics" #the spaces are like AND <-- tweets with both jobs and statistics will be returned, in case you want OR use commas e.g. "jobs,statistics"


#We need the authentication parameters of your application. Register an application at https://dev.twitter.com/
auth=OAuth(consumer_key=' J89TwB986mgGAIClYCQ1JyuMV', 
           consumer_secret='bQ4QpnGdV4e3F57fP75zBbTo5AgnJVmtfsSGZ7wGRiz2BVywIk', 
           token='2168268127-BGgyopLJB4VWxHjCqzhG4bH4x7gNZ0KHWdUw82m', 
           token_secret='B2ycW4AZ3KT2ACXAU6aRcnG07SOuJsv5sFALbZ6lV3xMd') #authentication parameters of your application


def myStream(yourKeyword):        
    ts=TwitterStream(auth=auth) # Initialize the twitter srteam
    iterator=ts.statuses.filter(track=yourKeyword) #Start gathering tweets
    ur, cnt=[], 0
    for item in iterator: #Do something with the tweets, HEre we jus save them in the memory and we count them.
        ur.append(item)
        cnt+=1
        if cnt % 20 ==0:
            print cnt

