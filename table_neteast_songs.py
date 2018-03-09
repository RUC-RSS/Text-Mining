import pandas as pd
import re
regex = re.compile('\[.*?\]\[info\]player\.')
songName = []
albumName = []
musicUrl = []
albumPic = []
artistName = []

with open('/Users/manchongleong/Library/Containers/com.netease.163music/Data/Documents/storage/Logs/music.163.log') as inputfile:
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

