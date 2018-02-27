import requests
import matplotlib.pyplot as plt
import datetime as dt

def history(s,c):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&allData=true'\
            .format(s,c)
    page = requests.get(url)
    data = page.json()['Data']
    d = dt.datetime
    newdata=[[data[i]['close'],d.fromtimestamp(data[i]['time'])] for i in range(len(data))]
    return newdata

def currentprice(s,c):
    newdata=history(s,c)
    url='https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(s,c)
    data=requests.get(url).json()
    currentprice=data[comparison_symbol]
    newdata[-1][0]=currentprice
    return newdata


symbol=input("enter cryptosymbol: ").upper()
comparison_symbol=input("enter comparison currency symbol: ").upper()

while True:
    newdata=currentprice(symbol,comparison_symbol)
    x=[newdata[i][-1] for i in range(len(newdata))]
    y=[newdata[i][0] for i in range(len(newdata))]
    plt.plot(x,y)
    plt.scatter(x[-1],y[-1],s=20,c='yellow')
    plt.title(symbol+' To '+comparison_symbol+'(last updated at:'+str(dt.datetime.now())+')')
    plt.ylabel('Price In'+comparison_symbol)
    plt.xlabel('Year')
    plt.show()
    inp=input("The prices are updated.Do you wish to have a look at it again?(yes/no): ").lower()
    if inp=="no":
        break;

