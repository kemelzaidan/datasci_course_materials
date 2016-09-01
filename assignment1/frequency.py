import sys, json, re, operator

def hw():
    print 'Starting to process: %s' % (sys.argv[1])

def lines(fp):
    print '%s: %s lines' % (fp.name, len(fp.readlines()))
    fp.seek(0)

def parse_tweet_file(tweet_file):
    tweets = []
    i=1
    for line in tweet_file:
        # print 'Parsing line %s' % (i)
        tweets.append(json.loads(line))
        i += 1

    return tweets

def get_percent(amount, total):
    return float(amount)/total*100

def print_sorted_by_value(dict):
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    for term, freq in sorted_dict:
        percentage = get_percent(freq, number_of_terms)
        print '%s %s' % (term, round(percentage, 4))

    print 'Total: %s terms' % (len(dict))

def clean_str(str):
    # URL REGEX
    url_re = re.compile(ur'(https?:\/\/)?([\da-z\.-]+)\.([a-z]{2,6})([\/\w\.-]*)*\??(\w+=\w+&?)*\/?')
    http_re = re.compile(ur'(https?:\/\/)') # http(s):// regex
    mention_re = re.compile(ur'@\w+')

    str = str.lower()
    str = str.replace('RT ', '') # cleans RT
    str = str.replace(u'\u2026', '') # cleans unicode ...
    str = re.sub(url_re, '', str) # cleans URL
    str = re.sub(http_re, '', str) # cleans http(s)://
    str = re.sub(mention_re, '', str) # cleans mentions

    # print str # debug-only
    return str

def main():
    tweet_file = open(sys.argv[1])
    hw()
    lines(tweet_file)
    tweets = parse_tweet_file(tweet_file)

    # Compute term frequency
    words_re = re.compile(ur"(\w+['[a-z]{1,2}]?)|#\w+") # regex for whole words
    # words_re = re.compile(ur"((\w+'t)|#\w+|\w+)") # regex for whole words and hashtags

    global number_of_terms
    number_of_terms = 0
    unique_terms = {}

    # Get frequency of each word
    for tweet in tweets:
        if tweet.get('text'): # real tweets have text field
            text = clean_str(tweet.get('text')) # cleans str
            words = re.findall(words_re, text) # apply regex and get only words
            number_of_terms += len(words)
            # print words # debug-only

            for w in words:
                if w in unique_terms:
                    unique_terms[w] += 1
                else:
                    unique_terms.setdefault(w, 1)

    print_sorted_by_value(unique_terms)

if __name__ == '__main__':
    main()
