#!/usr/bin/env python
import csv, os, sys, urllib2
import datetime

def main(scope):
    '''
    **********************************************************************************
    TODO: Create _accused objects
    TODO: Get filtered csv lists and extract usable stuff
    TODO: init new _accused class with name, party, hometown, DOB, etc. Put in list
    TODO: Do the candidate csv stuff
    TODO: Search for stuff for each _accused in list
    **********************************************************************************
    '''
    now = datetime.datetime.now()
    curr_year = str(now.year)
    
    jdg_url = "https://www.fjc.gov/sites/default/files/history/judges.csv"
    can_url = "https://www.fec.gov/files/bulk-downloads/"+curr_year+"/candidate_summary_"+curr_year+".csv"
    
    _clean_judge_csv(_get_remote_csv(jdg_url),scope)

def _get_remote_csv(url):
    # Get new remote csv, return a reader for it
    res = urllib2.urlopen(url)
    return csv.reader(res)

def _get_local_csv(file_path):
    return csv.reader(file_path)

def _get_file_name(file_path):
    # Remove file extension
    return os.path.splitext(file_path)[0]+"_cleaned.csv"

def _clean_judge_csv(in_writer,scope=None):
    '''
    Remove "Terminated" judges from csv writer passed to it.

    Filter either 'r': Replublican, or 'd': Democrat, or '': All judges.

    Write to new csv in lists/ directory.
    '''
    party = None
    # get output file label
    if scope is None:
        party = "all"
    elif scope in ( "r","republican","R","Republican"):
        party = "repub"
    elif scope in ("d","democrat","D","Democrat","democratic","Democratic"):
        party = "democrat"
        
    out_file = "lists/judges_"+party+".csv"

    # open the output file, filter the csv defined by the csv writer parameter and write it
    with open(out_file, 'wb') as out:
        writer = csv.writer(out)
        if scope is None:
            for row in in_writer:
                if row[43] in (None, "") or row[0] == ("nid"):
                    writer.writerow(row)
        elif scope is "r":
            for row in in_writer:
                if (row[43] in (None, "") and row[22] in ("Republican", "None (reassignment)", None, "")) or row[0] == ("nid"):
                    writer.writerow(row)
        elif scope is "d":
            for row in in_writer:
                if (row[43] in (None, "") and row[22] in ("Democratic", "Democrat")) or row[0] == ("nid"):
                    writer.writerow(row)
            
if __name__ == "__main__":
    main(sys.argv[1])
