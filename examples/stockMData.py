
# minute data
# 1,2,3,5,8,13,21,34,55,89,144,233,377
# 915 - 959
#1000 - 1059 ( 60)
#1100 - 1159 (60)
#
#1500 - 1530 (60)

import timewindow
class StockMeta:
    def __init__(self, ltp =0, totp=0.0, totq=0,avgp=0.0):
        self.ltp = ltp
        self.totp = totp
        self.totq = totq
        if(avgp==0):
            self.avgp = totp/totq
        else:
            self.avgp = avgp


    def update(self, ltp,tq):
        self.ltp = ltp
        calcPrice = ltp *tq
        self.totq += tq
        self.totp +=calcPrice
        self.avgp = self.totp /self.totq

    def __add__(self, other):
        ltp = other.ltp
        totq = self.totq + other.totq
        totp = self.totp + other.totp
        avgp = totp / totq
        return StockMeta(ltp,totp,totq,avgp)

    def stkprint(self):
        print(f"totprice= {self.totprice} totqty = {self.totalqty} avgprice = {self.avgp}")

class stockSummary:
    twoMinuteData ={}
     # [2 stockMeta],[3,stockMeta]

class stockOneMinSummary:
    oneMinuteData={}
    twoMinuteData = {}
    threeMinuteData ={}
    fiveMinuteData = {}

    def updateOtherStocks(self,timewind):
        if(timewind % 2 == 0):
            self.twoMinuteData[timewind] = self.oneMinuteData[timewind-1] + self.otherMinuteData[timewind]
        if(timewind % 3 == 0):
            self.threeMinuteData[timewind] = self.twoMinuteData[timewind-1] + self.otherMinuteData[timewind]
        if(timewind % 3 == 0):
            self.fiveMinuteData[timewind] = self.twoMinuteData[timewind-1] + self.otherMinuteData[timewind]
def addStock(self, Stock):
        timewind = timewindow.getTimeWindow(Stock.time)
        print(timewind)
        if timewind in self.oneMinuteData.keys():
            self.oneMinuteData[timewind].add(Stock.ltp,Stock.ltq)
        else:
            self.oneMinuteData[timewind] = StockMeta(Stock.ltp,Stock.ltq)

def stkprint(self):
    for stkmeta in self.oneMinuteData.keys():
        self.oneMinuteData[stkmeta].stkprint()

def sumStock(self,stk1,stk2):
    stk3 = StockMeta()


class Stock:
    def __init__(self, ltp=0.0, time=0,ltq=0,tbq=0,tsq=0,secid=''):
        self.ltp = ltp
        self.time = time
        self.ltq = ltq
        self.tbq = tbq
        self.tsq = tsq
        self.secid = secid


#test = Stock(1,1695874292,1,100,100,123)
#stkSum = stockOneMinSummary()
#stkSum.addStock(test)

#test2 = Stock(1,1695874292,1,100,100,123)
#stkSum.addStock(test2)
#stkSum.stkprint()

