from __future__ import division
from __future__ import print_function

from collections import defaultdict
import json
import sys


def extract_hashtags(twitter_hashtag_dictionaries):
    hashtags = []
    for hashtag_dictionary in twitter_hashtag_dictionaries:
        hashtags.append(hashtag_dictionary["text"])
    return hashtags

def print_top_n_hashtags(hashtag_occurrences, n):
    sorted_occurrences = sorted(hashtag_occurrences.items(),
            key=lambda t: t[1], reverse=True)
    for i in range(n):
        print(*sorted_occurrences[i])

def main():
    tweet_file = open(sys.argv[1])
    occurrences = defaultdict(int)

    for line in tweet_file:
        tweet = json.loads(line)
        if "entities" in tweet and "hashtags" in tweet["entities"]:
            hashtags = extract_hashtags(tweet["entities"]["hashtags"])
            for hashtag in hashtags:
                occurrences[hashtag] += 1

    print_top_n_hashtags(occurrences, 10)

if __name__ == '__main__':
    main()
