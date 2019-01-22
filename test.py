import praw
from settings_parser import readSettings

creds = readSettings("settings.txt")

reddit = praw.Reddit('swearBot')

subreddit = reddit.subreddit(creds["subreddit"])

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

