#!/usr/bin/env python3
import sys, time, progressbar
from bs4 import BeautifulSoup

def main():
    '''
        http://media.cq.com/members/95  member numbers start at 1
    '''
    _MAX = 5
    _URL = "http://media.cq.com/members/"
    _MASTER_LIST = []
    bar = progressbar.ProgressBar()
    print("[*] Starting download\n")
    for index in bar(range(1, _MAX+1)):
        fp = urllib2.urlopen(_URL+str(index))
        site_bytearray = fp.read()
        fp.close()
        
        bs_data = BeautifulSoup(site_bytearray,'lxml')
        name = bs_data.find('div', {'id':'member_headline'})
        tmplist = bs_data.find_all('span',{'class':'sub_heading'})
        new_list = []
        new_list.append(["Name:", name.text])
        print(new_list)
        sys.exit(0)
        for item in tmplist:
            new_list.append([item.text, item.next_sibling])
        _MASTER_LIST.append(new_list)
        time.sleep(2)
        
    print("[*] _MASTER_LIST length: "+str(len(_MASTER_LIST)))
    print("[*] _MASTER_LIST content: ")
    for item in _MASTER_LIST:
        print("[*] NEW LIST")
        for info in item:
            if isinstance(info[1], str):
                print("[+] "+ info[1])
            else:
                print("[X] Not a string value")
    print("[*] Exiting")
    sys.exit(0)
    # fp = urllib2.urlopen(url)
    # site_bytearray = fp.read()
    # fp.close()
    # print("_MASTER_LIST length: "+str(len(_MASTER_LIST)))
    # sys.exit(0)
    # bs_data = BeautifulSoup(site_bytearray,'lxml')
    # tmplist = bs_data.find_all('span',{'class':'sub_heading'})
    # new_list = []
    # for item in tmplist:
        # new_list.append([item.text, item.next_sibling])
        # #print('{:<25} {}'.format(item.text, item.next_sibling))

    # for item in new_list:
        # print(item)
        
    # sys.exit(0)
    
if __name__ == "__main__":
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2
    main()
