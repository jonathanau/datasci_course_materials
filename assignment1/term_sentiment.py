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

def derive_sentiment_of_new_terms(subjectivity_lexicon, text):
    all_unigrams = text.split()
    new_unigrams = []
    score = 0

    for unigram in all_unigrams:
        if unigram in subjectivity_lexicon:
            score += subjectivity_lexicon[unigram]
        else:
            new_unigrams.append(unigram)

    for unigram in new_unigrams:
        print unigram, score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    subjectivity_lexicon = parse_afinn(sent_file)

    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            derive_sentiment_of_new_terms(subjectivity_lexicon, tweet["text"])

if __name__ == '__main__':
    main()
