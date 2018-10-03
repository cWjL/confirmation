#!/usr/bin/env python
import csv, os, sys, traceback, time
import datetime, argparse, colorama
from colorama import Fore, Style

b_prefix = "["+Fore.RED+"*"+Style.RESET_ALL+"] "
g_prefix = "["+Fore.GREEN+"*"+Style.RESET_ALL+"] "

args = None

parser = argparse.ArgumentParser()
parser.add_argument("-r", action='store_true',dest='repub',help='Get republican data')
parser.add_argument("-d",action='store_true',dest='demo',help='Get democrat data')
parser.add_argument("-m",action='store',dest='money',help='Minimum campaign money in coffers')

def main():
    '''
    **********************************************************************************
    TODO: Create _accused objects
    TODO: Get filtered csv lists and extract usable stuff
    TODO: init new _accused class with name, party, hometown, DOB, etc. Put in list
    TODO: Search for stuff for each _accused in list
    **********************************************************************************
    '''
    global b_prefix
    global g_prefix
    global args
    args = parser.parse_args()
    who = None
    now = datetime.datetime.now()
    curr_year = str(now.year)
    
    jdg_url = "https://www.fjc.gov/sites/default/files/history/judges.csv"
    can_url = "https://www.fec.gov/files/bulk-downloads/"+curr_year+"/candidate_summary_"+curr_year+".csv"

    print(g_prefix+"Gathering remote files..")
    try:
        can_rem = _get_remote_csv(can_url)
        jdg_rem = _get_remote_csv(jdg_url)
    except urllib2.HTTPError as e:
        print(b_prefix+"HTTP Error: " + str(e.reason))
        print(b_prefix+"Exiting...")
        sys.exit(1)
    except urllib2.URLError as e:
        print(b_prefix+"URL Error: " + str(e.reason))
        print(b_prefix+"Exiting...")
        sys.exit(1)
    except Exception as e:
        print(b_prefix+"Generic Exception: " + str(e.message))
        print(b_prefix+"Exiting...")
        sys.exit(1)
    print(g_prefix+"Remote files successfully retrieved")
    time.sleep(2)
    
    print(g_prefix+"Filtering csv files..")
    try:
        if args.repub:
            who = "r"
            _clean_candidate_csv(can_rem,who,args.money)
            _clean_judge_csv(jdg_rem,who)
        elif args.demo:
            who = "d"
            _clean_candidate_csv(can_rem,who,args.money)
            _clean_judge_csv(jdg_rem,who)
        else:
            _clean_candidate_csv(can_rem,who,args.money)
            _clean_judge_csv(jdg_rem,who)
    except Exception as e:
        print(b_prefix+"CSV processing error")
        print(b_prefix+"Exiting...")
        sys.exit(1)

    sys.exit(0)

def _get_remote_csv(url):
    # Get new remote csv, return a reader for it
    res = urllib2.urlopen(url)
    return csv.reader(res)

def _get_local_csv(file_path):
    return csv.reader(file_path)

def _get_file_name(file_path):
    # Remove file extension
    return os.path.splitext(file_path)[0]+"_cleaned.csv"

def _clean_candidate_csv(in_writer,scope=None,funds=None):
    '''

    Remove candidates who's campaign donation reciepts total < funds

    Filter either 'r': Replublican, or 'd': Democrat, or '': All judges.

    Write to new csv in lists/ directory.

    '''
    party = None
    money = None
    
    if funds is not None:
        money = funds

    if scope is None:
        party = "all"
    elif scope in ( "r","republican","R","Republican"):
        party = "repub"
    elif scope in ("d","democrat","D","Democrat","democratic","Democratic"):
        party = "democrat"
        
    out_file = "lists/candidates_"+party+".csv"

    with open(out_file, 'wb') as out:
        writer = csv.writer(out)
        if scope is None:
            #something
            for row in in_writer:
                writer.writerow(row)
        elif scope is "r":
            #something
            for row in in_writer:
                if (row[6] in ("REP","REPUBLICAN","r","R") and int(float(row[8])) > 300000) or row[0] == ("Link_Image"):
                    writer.writerow(row)
        elif scope is "d":
            #something
            for row in in_writer:
                if (row[6] in ("DEM","DEMOCRAT","DEMOCRATIC","d","D") and int(float(row[8])) > 300000) or row[0] == ("Link_Image"):
                    writer.writerow(row)

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
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2
    colorama.init()
    main()
