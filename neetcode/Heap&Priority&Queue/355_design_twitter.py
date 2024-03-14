from collections import deque


class Twitter:

    def __init__(self):
        self.order_counter = 0
        self.user_and_tweets = dict()
        self.user_and_followers = dict()

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        if user_id in self.user_and_tweets:
            self.user_and_tweets[user_id].appendleft((tweet_id, self.order_counter))
        else:
            self.user_and_tweets[user_id] = deque([(tweet_id, self.order_counter)])
        self.order_counter += 1

    def getNewsFeed(self, user_id: int) -> list[int]:
        users = self.user_and_followers.get(user_id)
        if not users:
            return []
        all_tweets = []
        for u_id in users:
            all_tweets.extend(self.user_and_tweets.get(u_id))
        all_tweets.sort(key=lambda tw: tw[1])
        return [tw[0] for tw in all_tweets[:10]]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.user_and_followers:
            self.user_and_followers[follower_id].add(followee_id)
        else:
            self.user_and_followers[follower_id] = {followee_id}

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        followers = self.user_and_followers.get(follower_id)
        if followee_id in followers:
            self.user_and_followers[follower_id].remove(followee_id)


if __name__ == '__main__':
    inputs = [
        (["postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
         [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]),
    ]
    for input_ in inputs:
        twitter = Twitter()
        values = input_[1]
        for index, operation in enumerate(input_[0]):
            func = getattr(twitter, operation)
            value = values[index]
            if operation == 'postTweet':
                twitter.postTweet(value[0], value[1])
            elif operation == 'getNewsFeed':
                print(f'newsfeed for user - {value[0]} = {twitter.getNewsFeed(value[0])}')
            elif operation == 'follow':
                twitter.follow(value[0], value[1])
            elif operation == 'unfollow':
                print(twitter.unfollow(value[0], value[1]))
