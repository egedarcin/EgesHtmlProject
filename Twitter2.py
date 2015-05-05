#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-oauth-post
#  - posts a status message to your timeline
#-----------------------------------------------------------------------

from twitter import *

# what should our new status be?
new_status = "testing testing"

# these tokens are necessary for user authentication
# (created within the twitter developer API pages)
consumer_key = "N7e5kWDuVUZUIQvECbWLxMs4l"
consumer_secret = "LGXwsNRAAZADnmXa1aq9fZu8AheOZCzC3jLqw3BzR83y7LVSBn"
access_key = "3162862942-ZeaQlEbeiDieXoJr7pdQr4BSLqXH2ZwGDncsWgh"
access_secret = "aN0lX8gEsaSAKGETBrem2ybdbM4BGEoAj1A1gIyIjwxjV"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

# post a new status
# twitter API docs: https://dev.twitter.com/docs/api/1/post/statuses/update
results = twitter.statuses.update(status = new_status)
print ("updated status: %s" % new_status)
