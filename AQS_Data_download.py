from urllib.request import urlopen
from urllib.error import HTTPError
import argparse
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os
import pandas as pd
import datetime
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description = "enter a link")
        parser.add_argument("-url", help = "enter a link")
        args = parser.parse_args()
    except HTTPError as e:
        print("the error is as followings:/n", e)
    else:
        dateTimeRecord={}
        htmlcontext = urlopen(args.url)
        bsObj = BeautifulSoup(htmlcontext,"html.parser")
        # Ozone (44201)	SO2 (42401)	CO (42101)	NO2 (42602)
        contextOzone = bsObj.findAll("a",{"href":re.compile(".*daily_44201_20.*\.zip")})
        contextSO2 = bsObj.findAll("a",{"href":re.compile(".*daily_42401_20.*\.zip")})
        contextCO = bsObj.findAll("a",{"href":re.compile(".*daily_42101_20.*\.zip")})
        contextNO2 = bsObj.findAll("a",{"href":re.compile(".*daily_42602_20.*\.zip")})
        contextOzone8hr = bsObj.findAll("a",{"href":re.compile(".*8hour_44201_20.*\.zip")})
        contextCO8hr = bsObj.findAll("a",{"href":re.compile(".*8hour_42101_20.*\.zip")})
        currentWorkingDirectory = os.getcwd()
        print("Begin to download the daily data\n")
        print("Going to download the data for Ozone\n")
        for file in contextOzone:
            downLink = "https://aqs.epa.gov/aqsweb/airdata/" + file["href"]
            fileName = file["href"]
            print("The file going to be downloaded is: " + file["href"])
            print("It will be in: " + currentWorkingDirectory)
            urlretrieve(downLink, fileName)
            print("Download " + fileName + " successfully!")
            print("The time for finishing downloading " + fileName + " is " + str(datetime.datetime.now()) + ".\n")
            dateTimeRecord[fileName] = [str(datetime.datetime.now())]
        print("Going to download the data for SO2\n")
        for file in contextSO2:
            downLink = "https://aqs.epa.gov/aqsweb/airdata/" + file["href"]
            fileName = file["href"]
            print("The file going to be downloaded is: " + file["href"])
            print("It will be in: " + currentWorkingDirectory)
            urlretrieve(downLink, fileName)
            print("Download " + fileName + " successfully! \n")
            print("The time for finishing downloading " + fileName + " is " + str(datetime.datetime.now()) + ".\n")
            dateTimeRecord[fileName] = [str(datetime.datetime.now())]
        print("Going to download the data for CO\n")
        for file in contextCO:
            downLink = "https://aqs.epa.gov/aqsweb/airdata/" + file["href"]
            fileName = file["href"]
            print("The file going to be downloaded is: " + file["href"])
            print("It will be in: " + currentWorkingDirectory)
            urlretrieve(downLink, fileName)
            print("Download " + fileName + " successfully! \n")
            print("The time for finishing downloading " + fileName + " is " + str(datetime.datetime.now()) + ".\n")
            dateTimeRecord[fileName] = [str(datetime.datetime.now())]
        for file in contextNO2:
            downLink = "https://aqs.epa.gov/aqsweb/airdata/" + file["href"]
            fileName = file["href"]
            print("The file going to be downloaded is: " + file["href"])
            print("It will be in: " + currentWorkingDirectory)
            urlretrieve(downLink, fileName)
            print("Download " + fileName + " successfully! \n")
            print("The time for finishing downloading " + fileName + " is " + str(datetime.datetime.now()) + ".\n")
            dateTimeRecord[fileName] = [str(datetime.datetime.now())]
        print("\n\nFinished downloading the Daily data. Now begin to download the 8-hour data\n")
        print("Going to download the data for Ozone\n")
        for file in contextOzone8hr:
            downLink = "https://aqs.epa.gov/aqsweb/airdata/" + file["href"]
            fileName = file["href"]
            print("The file going to be downloaded is: " + file["href"])
            print("It will be in: " + currentWorkingDirectory)
            urlretrieve(downLink, fileName)
            print("Download " + fileName + " successfully! \n")
            print("The time for finishing downloading " + fileName + " is " + str(datetime.datetime.now()) + ".\n")
            dateTimeRecord[fileName] = [str(datetime.datetime.now())]
        print("Going to download the data for SO2\n")
        for file in contextCO8hr:
            downLink = "https://aqs.epa.gov/aqsweb/airdata/" + file["href"]
            fileName = file["href"]
            print("The file going to be downloaded is: " + file["href"])
            print("It will be in: " + currentWorkingDirectory)
            urlretrieve(downLink, fileName)
            print("Download " + fileName + " successfully! \n")
            print("The time for finishing downloading " + fileName + " is " + str(datetime.datetime.now()) + ".\n")
            dateTimeRecord[fileName] = [str(datetime.datetime.now())]

        allContext = bsObj.find_all("table")
        contextDaily = allContext[2]
        context8Hr = allContext[11]
        fileName = []
        asDate = []
        for line in context8Hr.find_all("td"):
            if bool(re.search(r'20[0-9]{2}\.zip', str(line))):
                fileNameRe = re.search('zip\"\>(.+?)\<\/a\>', str(line))
                asDateRe = re.search('As\ of\ (.+?)\<\/td\>', str(line))
                dateTimeRecord[fileNameRe.group(1)].append(asDateRe.group(1))
                #fileName.append(fileNameRe.group(1))
                #asDate.append(asDateRe.group(1))
        for line in contextDaily.find_all("td"):
            if bool(re.search(r'20[0-9]{2}\.zip', str(line))):
                fileNameRe = re.search('zip\"\>(.+?)\<\/a\>', str(line))
                asDateRe = re.search('As\ of\ (.+?)\<\/td\>', str(line))
                dateTimeRecord[fileNameRe.group(1)].append(asDateRe.group(1))
                #fileName.append(fileNameRe.group(1))
                #asDate.append(asDateRe.group(1))
        '''
        nameDictWithDate = dict(zip(fileName, asDate))
        nameDictWithDateDf = pd.DataFrame(
            {'File Name': fileName,
             'As Date': asDate})
        nameDictWithDateDf.to_csv(asOfDate, sep='\t')
        '''
        dateTimeRecordDf = pd.DataFrame.from_dict(dateTimeRecord, orient='index')
        dateTimeRecordDf.to_csv('asDate_downloadDate.csv')
