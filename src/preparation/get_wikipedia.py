# -*- coding: utf-8 -*-
import os
import sys
import warnings
warnings.filterwarnings("ignore")
# import func from another file in other directory
sys.path.insert(1, '../processing/')
# import get unique words
import feature_lesk as fl
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


def getArticleByWord(someWord, errwords):
    try:
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
    except:
        errwords.write(someWord+"\n")
        

def collectWikiArticle(uWords, start, end):
    errwords = open("../../data/raw/errorWords("+str(start)+"-"+str(end)+").txt", "w+", encoding='utf-8')
    for i, word in enumerate(uWords):
        # get a wikipedia page per term
        getArticleByWord(word, errwords)
        print(i+354, ". {} - created.".format(word))
    errwords.close()

if __name__ == '__main__':
    dfUWords = fl.getUniqueWords()
    # Sampe ayat ke 50 dulu unique wordnya
    listTerms = dfUWords.iloc[354:451,0].values
    collectWikiArticle(listTerms, 354, 451)
    print("======== Batas 1 =======")
    listTerms = dfUWords.iloc[451:551,0].values
    collectWikiArticle(listTerms, 451, 551)
    print("======== Batas 2 =======")
    listTerms = dfUWords.iloc[551:651,0].values
    collectWikiArticle(listTerms, 551, 651)
    print("======== Batas 3 =======")
    listTerms = dfUWords.iloc[651:751,0].values
    collectWikiArticle(listTerms, 651, 751)
    print("======== Batas 4 =======")








