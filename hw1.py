# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:26:31 2020

@author: Berk Kilic
"""

import random
priceList = {}


class Portfolio:
    
    #Function to construct the class
    def __init__(self):
        self.account = 0
        self.stocksOnHand ={}
        self.mutualsOnHand = {}
        self.transactionHistory = "----TRANSACTION HISTORY---- \n"
   
    #Function to add cash
    def addCash(self, amount):
        self.amount = amount
        #To check if the amount desired to add into account is positive
        if (amount > 0): 
            self.account += amount
            self.transactionHistory += "You have added " + str("{:.2f}".format(amount))+ " amount of cash to your account. \n\n"
        else:
            self.transactionHistory += "Warning! Negative cash cannot be added to portfolio. \n"
    
    #Function to withdraw cash
    def withdrawCash(self,amount):
        self.amount = amount
        #To check if the amount desired to withdrawn from account is positive
        if (amount > 0): 
            self.account -= amount
            self.transactionHistory += "You have withdrawn " + str("{:.2f}".format(amount))+ " amount of cash to your account. \n Your new account balance is: " + str("{:.2f}".format(self.account))+ "\n\n"
        else:
            self.transactionHistory += "Warning! Negative cash cannot be withdrawn from portfolio. \n"
    
    #function to buy stocks
    def buyStock(self, amountOfShares, Stock):
        self.amountOfShares = amountOfShares
        self.account -= (Stock.price * self.amountOfShares)
        self.transactionHistory += "You have purchased " + str(self.amountOfShares) + " amount of shares from the price of " + str("{:.2f}".format(Stock.price)) +"\n" + "Your new account balance is: " + str("{:.2f}".format(self.account)) +"\n\n"
        self.stocksOnHand[Stock.name] = amountOfShares
        
    #Function to buy mutual fund
    def buyMutualFund(self, amountOfShares, MutualFund):
        self.amountOfShares = amountOfShares
        self.account -= self.amountOfShares
        self.transactionHistory += "You have purchased " + str(self.amountOfShares) + " amount of mutual fund from the price of " + str("{:.2f}".format(self.amountOfShares)) +"\n" + "Your new account balance is: " + str("{:.2f}".format(self.account)) +"\n\n"
        self.mutualsOnHand[MutualFund.name] = amountOfShares     
    
    #Function to sell stocks
    def sellStock(self, name, shares):
        self.name = name
        self.shares = shares
        sellPrice = random.uniform(0.5, 1.5) * priceList[name]
        self.account += self.shares * sellPrice
        self.stocksOnHand[name] -= shares
        self.transactionHistory += "You have sold " + str(self.shares) + " amount of stock from the price of " + str("{:.2f}".format(sellPrice)) +"\n" + "Your new account balance is: " + str("{:.2f}".format(self.account)) +"\n\n"
  
    #Function to sell mutual funds    
    def sellMutualFund(self, name, shares):
        self.name = name
        self.shares = shares
        sellPrice = random.uniform(0.9, 1.2)
        self.account += self.shares * sellPrice
        self.mutualsOnHand[name] -= self.shares
        self.transactionHistory += "You have sold " + str(self.shares) + " amount of mutual funds from the price of " + str("{:.2f}".format(sellPrice)) +"\n" + "Your new account balance is: " + str("{:.2f}".format(self.account)) +"\n\n"
   
    #Prints the portfolio contents.
    def printPortfolio(self): 
        print("Portfolio: \nCash: "+ str("{:.2f}".format(self.account)))
        print("\nStocks: ")
        print(self.stocksOnHand)
        print("\nMutual Funds: ")
        print(self.mutualsOnHand)
        
    #Returns the portfolio as string
    def __str__(self): 
        return str(self.printPortfolio())
        
        
        
        
    #Function to print transaction history
    def history(self):
        print(self.transactionHistory)
        
        
        
#Defines the stock class        
class Stock:
     
    #Function to construct the class
     def __init__(self, price, name):
        self.price = price
        self.name = name
        priceList[name] = price
     
#Defines the mutual fund class        
class MutualFund:
    
    #Function to construct the class
     def __init__(self, name):
        self.name = name        
        
      
#MAIN class to run the function
if __name__ == '__main__': #Add this if you want to run the test with this script.
    portfolio = Portfolio()
    portfolio.addCash(300.50)
    s = Stock(20, "HFH")
    portfolio.buyStock(5, s)
    mf1 = MutualFund("BRT")
    mf2 = MutualFund("GHT")
    portfolio.buyMutualFund(10.3, mf1)
    portfolio.buyMutualFund(2, mf2)
    print(portfolio)
    portfolio.sellMutualFund("BRT", 3)
    portfolio.sellStock("HFH", 1)
    portfolio.withdrawCash(50)
    portfolio.history()

    
    