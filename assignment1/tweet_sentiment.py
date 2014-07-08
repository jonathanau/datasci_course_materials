import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def parse_afinn(input_file):
    scores = {}
    for line in input_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def score(sentiment_dictionary, text):
    unigrams = text.split()
    score = 0
    for unigram in unigrams:
        if unigram in sentiment_dictionary:
            score += sentiment_dictionary[unigram]
    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiment_dictionary = parse_afinn(sent_file)
    
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            print score(sentiment_dictionary, tweet["text"])
        else:
            print 0

if __name__ == '__main__':
    main()
