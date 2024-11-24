import argparse
import pandas as pd
import json


def build_network(input_file, output_file):
    data = pd.read_csv(input_file)

    unwanted_words = ["others", "ponies", "and", "all"]
    filtered_data = data[~data['pony'].str.contains('|'.join(unwanted_words), case=False, na=False)]

    line_counts = filtered_data['pony'].value_counts()

    top_101_ponies = line_counts.head(101).index.tolist()
    
    # Add a column to indicate if a row is for a top 101 pony
    data['is_top_101'] = data['pony'].isin(top_101_ponies)

    # Initialize relationship matrix
    relationship_matrix = pd.DataFrame(0, index=top_101_ponies, columns=top_101_ponies)

    # Iterate through the original dataset
    for i in range(len(data) - 1):
        current_row = data.iloc[i]
        next_row = data.iloc[i + 1]
        
        # Check if the next line is in the same episode and involves two different top 101 ponies
        if (
            current_row['title'] == next_row['title'] and
            current_row['is_top_101'] and next_row['is_top_101'] and  
            current_row['pony'] != next_row['pony']
        ):
            # Increment the value between the two characters
            pony1 = current_row['pony']
            pony2 = next_row['pony']
            relationship_matrix.loc[pony1, pony2] += 1
            relationship_matrix.loc[pony2, pony1] += 1
    
    # Convert the relationship matrix into JSON format
    relationship_dict = relationship_matrix.to_dict()

    # Save the relationship network as a JSON file
    with open(output_file, 'w') as f:
        json.dump(relationship_dict, f, indent=4)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output json file", default="interaction_network.json")
    parser.add_argument("-i", help="input csv file", required=True)
    args = parser.parse_args()

    build_network(args.i, args.o)


if __name__ == "__main__":
    main()