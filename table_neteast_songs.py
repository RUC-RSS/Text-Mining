import pandas as pd
import re
from urllib.request import urlretrieve
from urllib.error import HTTPError
import os
import argparse

regex = re.compile('\[.*?\]\[info\]player\.')
songName = []
albumName = []
musicUrl = []
albumPic = []
artistName = []

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description="enter a the log file location and the destinatiton")
	parser.add_argument("-l", help="enter the location of log file")
	parser.add_argument("-d", help="enter the location of the destination")
	args = parser.parse_args()

	#with open('/Users/manchongleong/Library/Containers/com.netease.163music/Data/Documents/storage/Logs/music.163.log') as inputfile:
	with open(args.l) as inputfile:
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

	for i in range(len(songName)):
		print("The song going to be downloaded is: " + songName[i])
		#os.chdir('/Users/manchongleong/Desktop/netEaseMusic/')
		os.chdir(args.d)
		fileName = artistName[i] + ' - ' + songName[i] + '.mp3'
		#print(fileName.replace(' ','\ '))
		#urlretrieve(musicUrl[i], fileName.replace(' ','\ ').replace('/','_'))
		try:
			urlretrieve(musicUrl[i], fileName.replace('/','_'))
		except urllib.error.HTTPError as e:
			print(e)