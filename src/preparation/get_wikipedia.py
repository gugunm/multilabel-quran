# -*- coding: utf-8 -*-
import os
import wikipedia
import wikipediaapi

def getPageNameList(someWord):
    pageTitles = wikipedia.search(someWord)
    titleList = []
    for title in pageTitles:
        try:
            wikipedia.page(title)
            titleList.append(title)
        except wikipedia.exceptions.DisambiguationError: # as e:
            continue
            # CUKUP LEVEL 1 AJA
            #for disamTitle in e.options:
            #    if ('disambiguation' not in disamTitle.lower()):
            #        titleList.append(disamTitle)
        except wikipedia.exceptions.PageError:
            continue
    return titleList

def createDir(dirName, path= "../../data/wiki/"):
    try:
        os.mkdir(path+dirName) 
        print("Directory '%s' created" %dirName) 
        return str(path+dirName)
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        return str(path+dirName)

def saveSummaryToTxt(title, summary, pathDir):
    # di encoding='utf-8' biar semua format str bisa di masukin ke file
    fileName = open(pathDir+"/"+str(title)+".txt", "w+", encoding='utf-8')
    fileName.write(summary)
    fileName.close()

def mainWikipedia(someWord):
    # Create dir for someWord
    pathDir = createDir(someWord)
    # get list of page related to someWord
    titleList = getPageNameList(someWord)
    # Remove duplicate page title in list
    titleList = list(dict.fromkeys(titleList))
    for t in titleList:
        try:
            wiki = wikipediaapi.Wikipedia('en')
            summaryPage = wiki.page(t).text
            #print(len(summaryPage), " -- Type : ", type(summaryPage), " -- Titile : ", t, "\n", summaryPage)
            if summaryPage:
                saveSummaryToTxt(t, summaryPage, pathDir)
        except:
            continue

if __name__ == '__main__':
    mainWikipedia("allah")






