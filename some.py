from bs4 import BeautifulSoup
import sys,time,progressbar
from include.accused import accused

class some():
    '''
        Search "http://media.cq.com/members/" for doxx on congressional members
            dob
            current city
            college attended
    '''
    def __init__(self, scope=None):
        '''
            init
        '''
        if scope is None:
            self.__MAXX = 50000
        else:
            self.__MAXX = scope
        self.__BASE_URL ="http://media.cq.com/members/"
        self.__MASTER_LIST = []
        self.__ACCUSED_LIST = []
        
    def get_some(self):
        '''
            get as much data as you can, and print a progess bar while you're 
            doing it
        '''
        for _index in bar(range(1, self.__MAX+1)):
            new_list = []
            
            fp = urllib2.urlopen(_URL+str(index))
            site_bytearray = fp.read()
            fp.close()
            
            bs_data = BeautifulSoup(site_bytearray,'lxml')
            name = bs_data.find('div', {'id':'member_headline'}) # get name
            if name.text in ("No Member ID"): # skip missing members
                continue
                
            tmplist = bs_data.find_all('span',{'class':'sub_heading'}) # get remaining data
            
            new_list.append(["Name:", name.text]) # prime list with target name
            
            for _item in new_list:
                new_list.append([_item.text, _item.next_sibling])
                
            self.__MASTER_LIST.append(new_list)
            time.sleep(2) # don't DoS __BASE_URL
            
    def list_some(self):
        tar_data = []
        for _item in __MASTER_LIST:
            # TODO filter text in __MASTER_LIST 
            # add to __ACCUSED_LIST, call from get_some() after data is 
            # compiled
            
'''
>>>str = "June 9, 1933; Meridian, Ca
>>>strlst = str.split(';')
>>>strlst
['June 9, 1933', ' Meridian, Calif.']
>>>strlst = [x.strip(' ') for x in strlst]
>>>strlst
['June 9, 1933', 'Meridian, Calif.']
    '''