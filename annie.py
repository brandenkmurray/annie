# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 15:01:03 2015

@author: branden
"""

#!/usr/bin/env python
import tweepy, random
#from our keys module (keys.py), import the keys dictionary
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
terms = ['Annie are you okay',
         'Annie are you OK']


 
#list of specific strings we want to check for in Tweets
t = ['Annie, are you okay?',
    'Annie are you okay?',
    'Are you ok Annie?',
    'Annie, are you okay??',
    'Are you okay Annie?',
    'Annie, are you OK?',
    'Annie are you OK?',
    'Are you OK Annie?',
    'Is Annie okay?',
    'Are you ok, Annie?',
    'Annie are you okay',
    'Annie are you ok']

#List of responses to be chosen at random
response = ['HELP MEEEEEEE',
            "SAVE ME I'M DYING",
            "No.",
            "DO I LOOK OKAY?",
            "I'M IN THE BEDROOM, HELP!"]

#File that stores list of tweets replied to.
#This is so that it doesn't reply to the same tweet multiple times
filename=open('/home/branden/Documents/annieFiles/tweetlist.txt','rw+')
twtList = filename.readlines()

for trms in terms:
    twt = api.search(q=trms, count=3)  
    for s in twt:
        if (str(s.id) + '\n') not in twtList and s.retweeted==False:
            for i in t:
                if i in s.text:
                    if (str(s.id) + '\n') not in twtList:
                        twtList.append(str(s.id)+'\n')
                        filename.writelines(str(s.id)+'\n')
                        sn = s.user.screen_name
                        m = "@"+ sn + " " + random.choice(response)
#                       m = "@%s HELP ME I'M DYING" % (sn)
                        s = api.update_status(m, s.id)

#Close and Save file.                  
filename.close()