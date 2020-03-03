# -*- coding: utf-8 -*-
import sys
# import func from another file in other directory
sys.path.insert(1, '../preparation/')
# credential for GDrive and GSheet
import credentials as creds 
# convert google sheet to dataframe
import gspread_dataframe as gd
# k-fold cross validation
from sklearn.model_selection import KFold

def getCleanData():
    # get the credentials
    gClient = creds.credentialGoogle()
    # file sheet name
    fileName = "dataset-quran"
    # take worksheet 
    proc_sheet = creds.getWorksheet(gClient, fileName, "proceed-data")
    # Take a Data to be proccess
    data_df = gd.get_as_dataframe(proc_sheet)

    return data_df

def crossValidation(df):
    # data devided into 10 fold dan 1 iteration
    kf = KFold(n_splits=10, shuffle=False)    
    # looping for each fold
    for train_index, test_index in kf.split(df.values): 
        dfTrain, dfTest = df.iloc[train_index], df.iloc[test_index] 
        print("train : ", dfTrain, "-- test : ", dfTest)

if __name__ == '__main__':
    df = getCleanData().iloc[:,3:]
    crossValidation(df)