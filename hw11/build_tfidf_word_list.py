import argparse
import json
import re
from math import log


def build_word_ranking_dict(fname, stop_words):
    with open(fname, 'r') as f:
        data = json.load(f)
    
    words = {}
    for post in data:
        title = post["data"]["title"].lower()
        title_words = re.findall(r'\w+', title)
        
        for word in title_words:
            if word not in stop_words:
                words[word] = words[word] + 1 if word in words else 1

    return words


def create_word_lists_json(args):
    master_word_dict = {}
    data = {}
    stop_words = []
    if args.s:
        with open(args.s, 'r') as sf:
            stop_words = json.load(sf)["stop_words"]

    # Get list of dictionaries of word counts for each file
    for in_file in args.filenames:
        data[in_file] = build_word_ranking_dict(in_file, stop_words)

        for word in data[in_file]:
            master_word_dict[word] = master_word_dict[word] + 1 if word in master_word_dict else 1

    # Replace word count with tfidf score
    tfidfs = {}
    for fname in data:
        words = []
        for word in data[fname].keys():
            idf = log(len(data) / master_word_dict[word], 10)
            tfidf = round(data[fname][word] * idf, 2)
            words.append([word, tfidf])
        tfidfs[fname] =  sorted(words, key=lambda x: x[1], reverse=True)[:10]

    with open(args.o, 'w') as f:
        json.dump(tfidfs, f, indent=4)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output json file name", default="output.json")
    parser.add_argument("-s", help="json file with key stop_words and value list of stop words", required=False)
    parser.add_argument("filenames", nargs="+", help="list of file names to process")
    args = parser.parse_args()
    create_word_lists_json(args)


if __name__ == "__main__":
    main()