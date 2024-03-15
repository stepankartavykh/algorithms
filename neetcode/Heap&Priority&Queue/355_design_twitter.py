from collections import deque, defaultdict


class Twitter:
    def __init__(self):
        self.order_counter = 0
        self.user_and_tweets = defaultdict(list)
        self.user_and_followers = defaultdict(set)

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.user_and_tweets[user_id].append((tweet_id, self.order_counter))
        self.order_counter += 1

    def getNewsFeed(self, user_id: int) -> list[int]:
        # TODO use mean heap!
        news_feed = (list(self.user_and_tweets.get(user_id) or [])).copy()
        users = self.user_and_followers.get(user_id)
        if users:
            for u_id in users:
                news_feed.extend(list(self.user_and_tweets.get(u_id) or []))
        news_feed.sort(key=lambda tw: tw[1], reverse=True)
        return [tw[0] for tw in news_feed[:10]]

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.user_and_followers[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.user_and_followers.get(follower_id):
            self.user_and_followers[follower_id].remove(followee_id)


if __name__ == '__main__':
    inputs = [
        (["postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"],
         [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]),
        (["Twitter", "postTweet", "getNewsFeed", "follow", "getNewsFeed", "unfollow", "getNewsFeed"],
         [[], [1, 1], [1], [2, 1], [2], [2, 1], [2]]),
        (["Twitter", "follow", "getNewsFeed"],
         [[], [1, 5], [1]])
    ]
    for input_ in inputs:
        twitter = Twitter()
        values = input_[1]
        for index, operation in enumerate(input_[0]):
            value = values[index]
            if operation == 'postTweet':
                twitter.postTweet(value[0], value[1])
            elif operation == 'getNewsFeed':
                print(f'newsfeed for user - {value[0]} = {twitter.getNewsFeed(value[0])}')
            elif operation == 'follow':
                twitter.follow(value[0], value[1])
            elif operation == 'unfollow':
                print(twitter.unfollow(value[0], value[1]))
