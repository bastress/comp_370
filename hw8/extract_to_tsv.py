import argparse
import json
import random
import csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output file", default="output.tsv")
    parser.add_argument("json_file", help="input reddit data json file")
    parser.add_argument("num_posts", help="num posts to output")
    args = parser.parse_args()
    
    with open(args.json_file, 'r') as jf:
        data = json.load(jf)

    data = data["data"]["children"]

    sample_list = [i for i in range(len(data))] if int(args.num_posts) >= len(data) else random.sample(range(0, len(data)), int(args.num_posts))

    with open(args.o, mode="w", newline="") as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(["name", "title", "coding"])

        for i in sample_list:
            entry = data[i]["data"]
            row = [
                entry.get("author_fullname", ""),
                entry.get("title", ""),
                ""
            ]
            writer.writerow(row)
    






if __name__ == "__main__":
    main()