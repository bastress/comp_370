from argparse import ArgumentParser
import json
import os
import importlib.util

current_dir = os.path.dirname(os.path.abspath(__file__))
newsapi_path = os.path.join(current_dir, 'newsapi.py')

spec = importlib.util.spec_from_file_location("newsapi", newsapi_path)
newsapi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(newsapi)


def main():
    parser = ArgumentParser()
    parser.add_argument("-k", help="newsapi key", required=True)
    parser.add_argument("-b", help="number of days to look back", default=10)
    parser.add_argument("-i", help="input json file", required=True)
    parser.add_argument("-o", help="output directory", required=True)
    args = parser.parse_args()

    with open(args.i) as f:
        data = json.load(f)

    for name in data:
        keywords = ' '.join(data[name])
        result = newsapi.fetch_latest_news(args.k, keywords, args.b)
        filename = os.path.join(args.o, name + ".json")

        with open(filename, 'w') as json_file:
            json.dump(result, json_file, indent=4)


if __name__=="__main__":
    main()
