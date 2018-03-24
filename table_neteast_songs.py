import pandas as pd
import re
from urllib.request import urlretrieve
from urllib.error import HTTPError
import os
import argparse
from hanziconv import HanziConv
import signal
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # All the code to run the thing

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

regex = re.compile('\[.*?\]\[info\]player\.')
songName = []
albumName = []
musicUrl = []
albumPic = []
artistName = []


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print("Log file is found.")
            print("It is in " + os.path.join(root, name) + "\n\n\n")
            return os.path.join(root, name)


if __name__ == '__main__':
    print('Going to find your log file, it will take a while....')


    parser = argparse.ArgumentParser(description="enter a the log file location and the destinatiton")
    parser.add_argument("-l", help="enter the location of log file", default='/')
    parser.add_argument("-d", help="enter the location of the destination", default=os.getcwd())
    parser.add_argument("-n", help="enter the name of the song or artist", default='.ALL')
    parser.add_argument("-c", help="traditional or simplified chinese", default='simp')
    args = parser.parse_args()

    logPath = find('music.163.log', args.l)
    #with open('/Users/manchongleong/Library/Containers/com.netease.163music/Data/Documents/storage/Logs/music.163.log') as inputfile:
    #with open(args.l) as inputfile:
    with open(logPath) as inputfile:
    	for line in inputfile:
    	    if re.search(regex, line):
    	    	for splitLine in line.split(''','''):
    	    	    if 'songName' in splitLine:
    	    	    	songName.append(splitLine.split('''"''')[-2])
    	    	    elif 'albumName' in splitLine:
    	    	    	albumName.append(splitLine.split('''"''')[-2])
    	    	    elif 'artistName' in splitLine:
    	    	    	artistName.append(splitLine.split('''"''')[-2])
    	    	    elif 'musicurl' in splitLine:
    	    	    	musicUrl.append(splitLine.split('''"''')[-2])
    	    	    elif 'jpg' in splitLine:
    	    			albumPic.append(splitLine.split('''"''')[-2])

    for i in range(len(musicUrl)):

    	#os.chdir('/Users/manchongleong/Desktop/netEaseMusic/')
    	os.chdir(args.d)
    	fileName = artistName[i] + ' - ' + songName[i] + '.mp3'

    	if args.n == '.ALL':
    	    print("The song going to be downloaded is: " + songName[i])
    	    try:
    	    	signal.alarm(50)
    	    	if args.c == 'trad':
    	    	    urlretrieve(musicUrl[i], HanziConv.toTraditional(fileName.replace('/', '_')))
    	    	    print("Downlod " + HanziConv.toTraditional(fileName) + " successfully!\n\n")
    	    	else:
    	    	    urlretrieve(musicUrl[i], fileName.replace('/', '_'))
    	    	    print("Downlod " + fileName + " successfully!\n\n")
    	    except HTTPError as e:
    		print(e)
    		print("Your link for this song is expired, please listen to that song again to renew the name.\n\n")
    	    except TimeoutException:
    		print("It took 120 secs, skip this song.\n\n")
    		continue
    	else:
    	    if (HanziConv.toSimplified(args.n) in fileName):
    		print("The song going to be downloaded is: " + songName[i])
    		#print(fileName.replace(' ','\ '))
    		#urlretrieve(musicUrl[i], fileName.replace(' ','\ ').replace('/','_'))
    		try:
    		    signal.alarm(50)
    		    if args.c == 'trad':
    		    urlretrieve(musicUrl[i], HanziConv.toTraditional(fileName.replace('/','_')))
    		    print("Downlod " + HanziConv.toTraditional(fileName) + " successfully!\n\n")
    		    else:
    			urlretrieve(musicUrl[i], fileName.replace('/','_'))
    			print("Downlod " + fileName + " successfully!\n\n")
    		    except HTTPError as e:
    			print(e)
    			print("Your link for this song is expired, please listen to that song again to renew the name.\n\n")
    		    except TimeoutException:
    			print("It took 120 secs, skip this song.\n\n")
    			continue

""""
musicLibrary = pd.DataFrame(
    {'songName': songName,
     'albumName': albumName,
     'artistName': artistName,
     'musicUrl': musicUrl,
     'albumPic': albumPic,
     })

#for sN, abN, atN, mU, aP in musicLibrary.iterrows():
for sN in musicLibrary.iterrows():
	#print("The song going to be downloaded is: " + sN)
	print(sN.songName)
"""

