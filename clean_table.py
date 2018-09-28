import csv, os, sys

def main(in_file):
    cleaned = _get_file_name(in_file)+"_cleaned.csv"
    _clean_csv(in_file, cleaned)


def _get_file_name(file_path):
    # Remove file extension
    return os.path.splitext(file_path)[0]

def _clean_csv(in_file, out_file):
    with open(in_file, 'rb') as inp, open(out_file, 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[10] in (None, "") or row[10] == ("Death Month"):
                writer.writerow(row)
            
if __name__ == "__main__":
    main(sys.argv[1])
