import requests, csv, os, datetime
from scipy import io
import datacollector

cwd = os.getcwd()
os.chdir(r'D:\Programme\Dev\FinancialDataRegression')


with open('companies.txt','r')as companies:
    companies =companies.readlines()

for i in range(0,len(companies)):
    if (companies[i].find('(')<0) or (companies[i].find(')')<0):
        break
    #Get the ticker symbol
    idx_TS1 = companies[i].find('(')
    idx_TS2 = companies[i].find(')')
    tickersymbl = companies[i][idx_TS1+1:idx_TS2]
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+tickersymbl+'?period1=-252378000&period2=1527112800&interval=1d&events=history&crumb=YIPm78g.WM5'

    r = requests.put(url,auth=requests.auth.HTTPBasicAuth('user', 'pass'))
    content = r.content.decode('utf-8')
    content = content.split('\n')
    content = datacollector.prep_save_file(content,tickersymbl)
    file_ticker =cwd+'/FinancialDataRegression/data//' + tickersymbl + '.mat'
    io.savemat(file_ticker,{tickersymbl+'_header':content[0],tickersymbl+'content':content[1:]})