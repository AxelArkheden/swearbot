import praw
from settingsParser import read_settings
from profiler import slur_sum
from outputHandler import sort_submission


creds = read_settings("settings.txt")

reddit = praw.Reddit('swearBot')

sub_reddit = reddit.subreddit(creds["subreddit"])

submissions = sub_reddit.mod.modqueue(limit=5)

resultList = [(s, slur_sum(s.selftext)) for s in submissions]

sort_submission(resultList)

for s in resultList:
    print("%s %s" %(s[0].title, s[1],))

