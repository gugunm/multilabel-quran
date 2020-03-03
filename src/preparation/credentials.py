# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def credentialGoogle():
    # Authentication GDrive and GSheet
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../../tesis-gugunm-f0d88704925a.json', scope)
    gClient = gspread.authorize(creds)
    return gClient

def getWorksheet(gClient, fileName, sheetName):
    # Get file sheet
    spreadSheet = gClient.open(fileName)
    # Take worksheet
    return spreadSheet.worksheet(sheetName)
