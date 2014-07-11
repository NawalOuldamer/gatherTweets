# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:30:55 2014

@author: balikasg
"""
from  twitter import *

yourKeyword="jobs statistics" #the spaces are like AND <-- tweets with both jobs and statistics will be returned, in case you want OR use commas e.g. "jobs,statistics"


#We need the authentication parameters of your application. Register an application at https://dev.twitter.com/
auth=OAuth(consumer_key='%%%', 
           consumer_secret='%%%', 
           token='%%%%%', 
           token_secret='%%%') #authentication parameters of your application. Replace %%% with your tokens


       
ts=TwitterStream(auth=auth) # Initialize the twitter srteam
iterator=ts.statuses.filter(track=yourKeyword) #Start gathering tweets
ur, cnt=[], 0
for item in iterator: #Do something with the tweets, HEre we jus save them in the memory and we count them.
  ur.append(item)
  cnt+=1 # The first file will have 9999 tweets!
  if cnt % 10000 ==0:
    print cnt
    with open('tweetsVol%d.json' %cnt/10000, 'w') as out:
      json.dump(ur, out, indent=2)
    ur=list()

