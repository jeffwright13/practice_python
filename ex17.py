#!/c/Python27/python.exe

'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage (http://www.nytimes.com/)
'''

def main():
    from bs4 import BeautifulSoup
    import requests
    
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    
    title = soup.find_all(class_ = 'story-heading')
    print title

def something():
    pass

if __name__ == "__main__":
    main()