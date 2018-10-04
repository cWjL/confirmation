from bs4 import BeautifulSoup
import sys,time,progressbar

class some():
    '''
        Search "http://media.cq.com/members/" for doxx on congressional members
            dob
            current city
            college attended
    '''
    def __init__(self):
        '''
            init
        '''
        self.__MAXX = 50000
        self.__BASE_URL ="http://media.cq.com/members/"
        self.__MASTER_LIST = []
        
    def get_some_doxx(self):
        '''
            get as much data as you can, and print a progess bar while you're 
            doing it
        '''
        for _index in bar(range(1, self.__MAX+1)):
            fp = urllib2.urlopen(_URL+str(index))
            site_bytearray = fp.read()
            fp.close()
            
            bs_data = BeautifulSoup(site_bytearray,'lxml')
            tmplist = bs_data.find('div', id='member_headline')
            tmplist = bs_data.find_all('span',{'class':'sub_heading'})
            new_list = []