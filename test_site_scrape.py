import urllib.request
import sys
from bs4 import BeautifulSoup

def main(url):
    '''
        http://media.cq.com/members/95  member numbers start at 1
    '''
    fp = urllib.request.urlopen(url)
    site_bytearray = fp.read()
    fp.close()
    
    site_str = site_bytearray.decode("utf8")
    
    bs_data = BeautifulSoup(site_str,features="html.parser")
    div = bs_data.find("div", class_="member_biography")
    #div = bs_data.find(id='member_headline')
    print(div)
    sys.exit(0)
    
if __name__ == "__main__":
    main(sys.argv[1])