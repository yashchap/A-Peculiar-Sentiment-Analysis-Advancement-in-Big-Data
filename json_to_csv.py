###Converts Json format file to csv
#1) It takes archived json file and using gzip it decompress the file.
#2) Take that file to Pandas dataframe.
#3) dataframe to csv for further data manipulation.

import pandas as pd
import gzip
from pandas.io import sql
import csv

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df,orient='index')

def main():
	df = getDF('Data/reviews_Musical_Instruments_5.json')
	fields=['asin','reviewText','overall']
	df.to_csv("Data/Musical_Instruments.csv",sep="\t",columns=fields)


if __name__ == '__main__':
	main()
