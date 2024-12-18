import argparse
import json
import re


def build_word_ranking_list(fname, stop_words):
    with open(fname, 'r') as f:
        data = json.load(f)
    
    words = {}
    for post in data:
        title = post["data"]["title"].lower()
        title_words = re.findall(r'\w+', title)
        
        for word in title_words:
            if word not in stop_words:
                words[word] = words[word] + 1 if word in words else 1

    return [[word, words[word]] for word in sorted(words, key=words.get, reverse=True)[:10]]


def create_word_lists_json(args):
    data = {}
    stop_words = []
    if args.s:
        with open(args.s, 'r') as sf:
            stop_words = json.load(sf)["stop_words"]

    for in_file in args.filenames:
        data[in_file] = build_word_ranking_list(in_file, stop_words)

    with open(args.o, 'w') as f:
        json.dump(data, f, indent=4)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output json file name", default="output.json")
    parser.add_argument("-s", help="json file with key stop_words and value list of stop words", required=False)
    parser.add_argument("filenames", nargs="+", help="list of file names to process")
    args = parser.parse_args()
    create_word_lists_json(args)


if __name__ == "__main__":
    main()