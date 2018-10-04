#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup

def main(url):
    '''
        http://media.cq.com/members/95  member numbers start at 1
    '''
    fp = urllib2.urlopen(url)
    site_bytearray = fp.read()
    fp.close()
    
    #bs_data = BeautifulSoup(site_str,features="html.parser")
    bs_data = BeautifulSoup(site_bytearray,'lxml')
    tmplist = bs_data.find_all('span',{'class':'sub_heading'})
    new_list = []
    for item in tmplist:
        new_list.append([item.text, item.next_sibling])
        #print('{:<25} {}'.format(item.text, item.next_sibling))

    for item in new_list:
        print(item)
        
    sys.exit(0)
    
if __name__ == "__main__":
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2
    main(sys.argv[1])
