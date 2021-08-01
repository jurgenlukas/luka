import requests
import pandas as pd
import matplotlib
import wordcloud
url='https://app.sports.qq.com/tokyoOly/medalsList?from=h5&medalsType=all&callback=jQuery111305439009884070249_1627469774560&_=1627469774561'

json = requests.get(url).json()

list=json['data']['data']['total']


# for r in list :
# 	print(r['nocRank'], 
#           r['nocName'].ljust(10), 
#           '金' + r['gold'], 
#           '银' + r['silver'], 
#           '铜' + r['bronze'], 
#           '排名' + r['nocRank'])

df=pd.DataFrame(list)
df1=df
#print(df)
df.rename(columns={'nocName':'name','nocGoldRank':'goldrank'}, inplace = True)
df = pd.DataFrame(df,columns = ['goldrank','name','gold','silver','bronze'])
u=df.to_html(buf=None, columns=None, col_space=None, header=True, index=True,na_rep='NaN',
    formatters=None, float_format=None, sparsify=None, index_names=True,justify=None,
    bold_rows=True,classes=None, escape=True, max_rows=None, max_cols=None,show_dimensions=False,
    notebook=False, decimal='.', border=None)

