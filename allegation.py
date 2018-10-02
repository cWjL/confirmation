import csv, os, sys, urllib2

def main(in_file, scope):
    '''
    Get list from url, save as judges-MASTER.csv

    Filter list per user parameters
    
    Save new list as judges-MASTER_cleaned.csv

    init new _accused class with name, party, hometown, DOB, ... for each name in judges-MASTER_cleaned.csv.  Put in list

    Search for stuff for each _accused in list
    
    '''
    url = "https://www.fjc.gov/sites/default/files/history/judges.csv"

    cleaned_master = _get_file_name(in_file)
    
    _clean_judge_csv(in_file, cleaned_master, scope)

def _get_remote_csv(url):
    # Get new remote csv, save locally
    with open('lists/new_judges.csv','wb') as f:
        f.write(urllib2.urlopen(url).read())

def _get_local_csv(file_path):
    return csv.reader(file_path)

def _get_file_name(file_path):
    # Remove file extension
    return os.path.splitext(file_path)[0]+"_cleaned.csv"

def _clean_judge_csv(in_file, out_file, scope=None):
    # Clean out dead judges
    with open(in_file, 'rb') as inp, open(out_file, 'wb') as out:
        writer = csv.writer(out)
        if scope is None:
            for row in csv.reader(inp):
                if row[43] in (None, "") or row[0] == ("nid"):
                    writer.writerow(row)
        elif scope is "r":
            for row in csv.reader(inp):
                if (row[43] in (None, "") and row[22] in ("Republican", "None (reassignment)", None, "")) or row[0] == ("nid"):
                    writer.writerow(row)
        elif scope is "d":
            for row in csv.reader(inp):
                if (row[43] in (None, "") and row[22] in ("Democratic", "Democrat")) or row[0] == ("nid"):
                    writer.writerow(row)
            
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])