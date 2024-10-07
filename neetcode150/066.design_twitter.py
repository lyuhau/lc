from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.tweet_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_id, tweetId))
        self.tweet_id += 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for followee in self.followers[userId] | {userId}:
            tweets.extend(self.tweets[followee])
        tweets.sort(reverse=True)
        return [tweet[1] for tweet in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
