try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

import urllib2
import os
COMMAND = 'youtube-dl http://www.youtube.com/watch?v=%s -o - | mplayer -vo matrixview:cols=400:rows=320 -'
dict = {}
list = {}
num = 0
search = str(raw_input('Press y for search: '))
if 'y' in search:
    searchQuery = str(raw_input('Search Query: ')).replace(' ', '+')
    LINK = 'https://www.youtube.com/results?search_query=%s' % searchQuery
else:
    LINK = 'https://www.youtube.com/'
print LINK
try:
    youtubeFile = urllib2.urlopen(LINK)
    youtuebHtml = youtubeFile.read()
    youtubeFile.close()
except:
    print 'Not connected to internet'
    exit()

soup = BeautifulSoup(youtuebHtml, 'lxml')
youtubeVideos = soup.find_all('a', {'class': 'yt-ui-ellipsis'})
for videoLink in youtubeVideos:
    temp = str(videoLink.contents)
    if '<' not in temp:
        num += 1
        print '%d %s' % (num, temp)
    list[num] = temp
    dict[temp] = str(videoLink['href'])[9:]

input = int(raw_input('>'))
id = dict[list[input]]
os.system(COMMAND % id)
