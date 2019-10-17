# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re

df = pd.read_csv('C:/Users/Ziemek/Documents/GitHub/Analize-DataBases/Lab1/AnalysisData/pewCSV.csv', error_bad_lines=False)
print(open('C:/Users/Ziemek/Documents/GitHub/Analize-DataBases/Lab1/AnalysisData/pewCSV.csv').read())