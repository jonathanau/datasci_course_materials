from __future__ import division

from collections import defaultdict
import json
import sys


def main():
    tweet_file = open(sys.argv[1])
    occurrences = defaultdict(int)

    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            unigrams = tweet["text"].split()
            for unigram in unigrams:
                occurrences[unigram] += 1

    total = sum(occurrences.values())
    for unigram in occurrences:
        print unigram, occurrences[unigram] / total

if __name__ == '__main__':
    main()
