from products import *

class Cart:
    def __init__(self):
        self.__productsList = []   
        self.__cartValue = 0
      
    def addProduct(self,product): 
        if isinstance (product, Product): 
            if product not in self.__productsList: 
                self.__productsList.append(product)
                self.calculateCart()
    
    def removeProduct(self,product):
        if product in self.__productsList:
            self.__productsList.remove(product)
            self.calculateCart()

    def clearCart(self):
            self.__productsList.clear()
            self.__cartValue = 0
    
    def isEmpty(self):
        return len(self.__productsList) == 0
    
    def calculateCart(self): 
        self.__cartValue = 0 
        for el in self.__productsList:
            self.__cartValue += el.price 

    def __str__(self): 
        strData = "Cart info, products list:" 
        for el in self.__productsList: 
            strData += "\n - " + str(el)
        strData += "\n products count: " + str(len(self.__productsList))
        strData += "\n cart value: " + str(self.__cartValue)
        return strData