import heapq
from collections import defaultdict

class Tweet:
    def __init__(self, time,  tweet_id):
        self.time = time
        self.tweet_id = tweet_id


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.following = set()
        self.tweets = []
    
class Twitter:

    def __init__(self):
        self.twitter = {}
        self.time = 0
        self.feedLimit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.twitter:
            self.twitter[userId] = User(userId)

        user = self.twitter[userId]

        user.tweets.append(Tweet(self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:        
        if userId not in self.twitter:
            return []

        max_heap = []
        user = self.twitter[userId]

        for tweet in user.tweets:
            heapq.heappush(max_heap, (-tweet.time, tweet.tweet_id))
        
        for follower in user.following:
            user = self.twitter[follower]
            for tweet in user.tweets:
                heapq.heappush(max_heap, (-tweet.time, tweet.tweet_id))
            
        ans = []
        while max_heap:
            t, tweet_id = heapq.heappop(max_heap)
            ans.append(tweet_id)

            if len(ans) == self.feedLimit:
                break

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        
        if followerId not in self.twitter:
            self.twitter[followerId] = User(followerId)
        
        if followeeId not in self.twitter:
            self.twitter[followeeId] = User(followeeId)

        self.twitter[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.twitter:
            return
        
        self.twitter[followerId].following.discard(followeeId)



