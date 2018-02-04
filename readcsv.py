from reviewcount import calculate_point
import pandas as pd
import operator
import numpy as np


def main():
	df_data = pd.read_csv("Data/Musical_Instruments.csv",sep="\t",usecols=['asin','overall','reviewText'])

	df = df_data[['asin','overall']]
	d={}
	list=[]
	rating_group = df.groupby(df['asin'])
	avg_rating_grp = rating_group.mean()
	no_of_records = len(avg_rating_grp)

	for i in range(no_of_records):
	    if avg_rating_grp['overall'][i] == 5.0:
	        d[avg_rating_grp.index.get_level_values('asin')[i]]=avg_rating_grp['overall'][i]
	        list.append(avg_rating_grp.index.get_level_values('asin')[i])
	print(d)
	print("Number of products with high rating(5 stars):",len(list))

	#counting reviews

	d_p={}
	err_count=0
	df = df_data[['asin','reviewText']]
	review_grp = df.groupby(df['asin']).sum()
	for i in range(len(review_grp)):
	    if review_grp.index.get_level_values('asin')[i] in list:
	        text = review_grp['reviewText'][i]
	        result = calculate_point(str(text).lower())
	        if result < 0:
	            err_count+=1
	        d_p[review_grp.index.get_level_values('asin')[i]]=result

	final_dic=sorted(d_p.items(),key=operator.itemgetter(1),reverse=True)
	print(final_dic)
	print("Error(%):",((err_count/len(list))*100))

if __name__ == '__main__':
	main()

