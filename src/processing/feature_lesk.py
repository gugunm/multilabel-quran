# -*- coding: utf-8 -*-
import sys
# import func from another file in other directory
sys.path.insert(1, '../preparation/')
# credential for GDrive and GSheet
import credentials as creds 
# convert google sheet to dataframe
import gspread_dataframe as gd
# for converting str to list
import ast
# pandas datframe
import pandas as pd

def createUniqueWords(fileName="dataset-quran", 
                      wsNameCleanData="proceed-data", 
                      wsNameUniqueWords="unique-words"):
    uWords = []
    dfClean = creds.getAsDataframe(fileName, wsNameCleanData)
    wsUniqueWords = creds.getWorksheet(creds.credentialGoogle(), fileName, wsNameUniqueWords)    
    # convert dataframe ayat alquran to list
    listCleanToken = dfClean.iloc[:,3].apply(ast.literal_eval)  
    for terms in listCleanToken:
        for term in terms:
            if term not in uWords:
                uWords.append(term)
    dfUWords = pd.DataFrame(uWords, columns=["terms"])
    # Real data Already proceed then store in sheet "proceed-data" 
    gd.set_with_dataframe(wsUniqueWords, dfUWords)
    return dfUWords

def getUniqueWords(fileName = "dataset-quran", wsNameUniqueWords = "unique-words"):
    wsUniqueWords = creds.getWorksheet(creds.credentialGoogle(), fileName, wsNameUniqueWords)
    dfUWords = gd.get_as_dataframe(wsUniqueWords, usecols=[0])
    return dfUWords

#def mainLeskAlgorithm():
    # get a unique words from dataset
    
#if __name__ == '__main__':
    # Runing once only, to create unique words
    #df = createUniqueWords()
    
    # Get unique words from google sheet
    #print(getUniqueWords())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    