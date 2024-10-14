import argparse
import json
from get_gazette_trending import get_trending_articles_info


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output file name", required=True)

    args = parser.parse_args()

    articles_info = get_trending_articles_info()

    with open(args.o, 'w') as outfile:
        json.dump(articles_info, outfile, indent=4)


if __name__ == "__main__":
    main()

