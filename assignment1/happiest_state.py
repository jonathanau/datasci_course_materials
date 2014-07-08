from __future__ import division

from collections import defaultdict
import json
from random import shuffle
import re
import sys


def parse_afinn(input_file):
    scores = {}
    for line in input_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def compute_sentiment_score(sentiment_lexicon, text):
    unigrams = text.split()
    score = 0
    for unigram in unigrams:
        if unigram in sentiment_lexicon:
            score += sentiment_lexicon[unigram]
    return score

def determine_state(location):
    states = [
            'AK',
            'AL',
            'AR',
            'AS',
            'AZ',
            'CA',
            'CO',
            'CT',
            'DC',
            'DE',
            'FL',
            'GA',
            'GU',
            'HI',
            'IA',
            'ID',
            'IL',
            'IN',
            'KS',
            'KY',
            'LA',
            'MA',
            'MD',
            'ME',
            'MI',
            'MN',
            'MO',
            'MP',
            'MS',
            'MT',
            'NA',
            'NC',
            'ND',
            'NE',
            'NH',
            'NJ',
            'NM',
            'NV',
            'NY',
            'OH',
            'OK',
            'OR',
            'PA',
            'PR',
            'RI',
            'SC',
            'SD',
            'TN',
            'TX',
            'UT',
            'VA',
            'VI',
            'VT',
            'WA',
            'WI',
            'WV',
            'WY',
    ]

    # Since this method returns the first state that matches, we shuffle the
    # list to avoid biasing towards states that appear earlier in the list above
    shuffle(states)

    for state in states:
        match = re.search(r'\b' + state + r'\b', location)
        if match:
            return state
    return None

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    subjectivity_lexicon = parse_afinn(sent_file)

    sentiment_totals = defaultdict(int)
    sentiment_counts = defaultdict(int)

    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            score = compute_sentiment_score(subjectivity_lexicon, tweet["text"])
            state = determine_state(tweet["user"]["location"])
            if state:
                sentiment_totals[state] += score
                sentiment_counts[state] += 1

    max_sentiment = ()  # (state, average_sentiment)
    for state in sentiment_totals:
        average = sentiment_totals[state] / sentiment_counts[state]
        if not max_sentiment or average > max_sentiment[1]:
            max_sentiment = state, average

    print max_sentiment[0]

if __name__ == '__main__':
    main()
