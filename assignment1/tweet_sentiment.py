import sys
import json
import re

def hw():
    print 'Starting to process: %s' % (sys.argv[2])

def lines(fp):
    print '%s: %s lines' % (fp.name, len(fp.readlines()))
    fp.seek(0)

def compute_scores(tweets):
    p = re.compile(ur'(?![RT])(\b[A-Za-z]+\b)') # regex for whole words
    i = 1
    for tweet in tweets:
        score_sum = 0

        if tweet.get('text'):
            words = re.findall(p, tweet.get('text'))

            for w in words:
                score_sum += scores.get(w, 0)

            print "score for tweet %s: %s" % (i, score_sum)
            i += 1
        else:
            print 'not a tweet'

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

    # Process scores
    global scores
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary

    # Parse tweets jsonproblem_1_submission.txt
    tweets = []
    i=1
    print 'parsing json...'
    for line in tweet_file:
        tweets.append(json.loads(line))
        i += 1

    compute_scores(tweets)

if __name__ == '__main__':
    main()
