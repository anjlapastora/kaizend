import argparse
import sys
import csv

parser = argparse.ArgumentParser(description="""Read a file to remove all products
                that don\'t have categories""")

parser.add_argument('filename', help='the CSV file to read')

parser.add_argument('outfilename', help='the CSV file to be written')

args = parser.parse_args()

try:
    f = open(args.filename)
    out = open(args.outfilename, 'w', newline='')
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    with f:
        csv_reader = csv.reader(f, delimiter=',')
        writer = csv.writer(out)
        for row in csv_reader:
            if row[25]:
                writer.writerow(row)
