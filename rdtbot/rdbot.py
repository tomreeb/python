#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('jabroni')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit("bottesting")
for submission in subreddit.hot(limit=100):
    # print(submission.title)

    # If we haven't replied to this post before
    # if comment.id not in posts_replied_to:
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if comment.id not in posts_replied_to:

                # Do a case insensitive search
                if re.search("jabroni", comment.body, re.IGNORECASE):
                    # Reply to the post
                    comment.reply("You keep on using this word "jabroni" and... it's awesome!")
                    print("Bot replying to : ", comment.id)
                    # print(comment.body)

                    # Store the current id into our list
                    posts_replied_to.append(comment.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
