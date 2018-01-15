#!/usr/bin/env python

from bs4 import BeautifulSoup
import subprocess
from urllib.request import urlopen
from urllib.parse import quote
import re
import sys

search = ' '.join(sys.argv[1:])
query = "https://www.youtube.com/results?search_query={}".format(
        quote(search))

try:
    youtubeFile = urlopen(query)
    youtuebHtml = youtubeFile.read()
    youtubeFile.close()
except:
    print("Not connected to the internet")
    exit()

soup = BeautifulSoup(youtuebHtml, "lxml")
videos = soup.find_all('a', {"class": "yt-ui-ellipsis"})
endings = []
num = 0
reg = re.compile("^/user/")
for link in videos:
    temp = str(link.contents[0])
    if (not reg.match(link["href"])):
        print("{}: {}".format(num + 1, temp))
        num += 1
        endings.append(str(link["href"]))

ind = int(input('> '))
ending = endings[ind - 1]
videos = subprocess.check_output(
        ["youtube-dl", "-g",
            "http://www.youtube.com{}".format(ending)]).decode("utf-8")
video = videos.split("\n")[0]
print(video)
subprocess.call(["mpv", video])
