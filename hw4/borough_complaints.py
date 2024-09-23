from argparse import ArgumentParser
import pandas as pd


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", help="the input CSV file", required=True)
    parser.add_argument("-s", help="start date (format: MM/DD/YYYY)", required=True)
    parser.add_argument("-e", help="end date (format: MM/DD/YYYY)", required=True)
    parser.add_argument("-o", default="stdout", help="output file")
    args = parser.parse_args()

    # Convert the user-provided start and end dates to datetime objects
    start_date = pd.to_datetime(args.s, format="%m/%d/%Y")
    end_date = pd.to_datetime(args.e, format="%m/%d/%Y")

    df = pd.DataFrame(columns=["complaint type", "borough", "count"])

    chunksize = 1000

    # Read the input file in chunks
    for chunk in pd.read_csv(args.i, chunksize=chunksize):
        # Loop through each row in the chunk
        for _, row in chunk.iterrows():
            # Convert the date from the second column (date is in row[1]) to datetime
            event_date = pd.to_datetime(row.iloc[1], format="%m/%d/%Y %I:%M:%S %p")
            
            # Check if the event date is within the start and end date range
            if start_date <= event_date <= end_date:
                complaint_type = row.iloc[5]  # column 5 is 'Complaint Type'
                borough = row.iloc[25]  # column 25 is 'Borough'

                # Check if this complaint type and borough already exist in the DataFrame
                match = (df['complaint type'] == complaint_type) & (df['borough'] == borough)

                if match.any():
                    # Increment the count if the combination exists
                    df.loc[match, 'count'] += 1
                else:
                    # If the combination doesn't exist, add a new row with count 1
                    new_row = {"complaint type": complaint_type, "borough": borough, "count": 1}
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Sort the DataFrame for better readability
    df = df.sort_values(by=["complaint type", "borough"]).reset_index(drop=True)

    # Output to either file or stdout
    if args.o == "stdout":
        print(df.to_csv(index=False))
    else:
        df.to_csv(args.o, index=False)


if __name__ == "__main__":
    main()