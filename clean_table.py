import csv, os, sys, urllib2

def main(in_file):
    url = "https://www.fjc.gov/sites/default/files/history/judges.csv"
    master_csv = in_file
    cleaned_master = _get_file_name(master_csv)
    _clean_csv(in_file, cleaned_master)

def _get_remote_csv(url):
    # Get new remote csv, save locally
    with open('lists/new_judges.csv','wb') as f:
        f.write(urllib2.urlopen(url).read())

def _get_local_csv(file_path):
    return csv.reader(file_path)

def _get_file_name(file_path):
    # Remove file extension
    return os.path.splitext(file_path)[0]+"_cleaned.csv"

def _clean_csv(in_file, out_file):
    with open(in_file, 'rb') as inp, open(out_file, 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[10] in (None, "") or row[10] == ("Death Month"):
                writer.writerow(row)
            
if __name__ == "__main__":
    main(sys.argv[1])
