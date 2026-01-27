class Product:   
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self): 
        return str(self.name) + " " + str(self.price)


class Phone(Product):
    def __init__(self, name, price, color):
        Product.__init__(self,name,price) #
        self.color = color  
   
    def __str__(self):
        return super().__str__() + " " + str(self.color) 
    

class TV(Product):
    def __init__(self, name, price, screenSize):
        super().__init__(name,price) 
        self.screenSize = screenSize 
    
    def __str__(self):
        return super().__str__() + " " + str(self.screenSize) 
