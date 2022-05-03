# Inventory class

import numpy as np
import pandas as pd
from Book import Book

class Inventory:
  def __init__(self):
    self.inventoryFile = 'InventoryList.csv'
    self.inventoryList = pd.read_csv(self.inventoryFile)

  ## adds quantity of items back to inventory, this function gets called in Cart class
  ## when item is deleted from Cart
  def addBackQuantity(self, ISBN, quantity):
    self.inventoryList.loc[self.inventoryList['ISBN'] == ISBN, 'Quantity'] += quantity
    self.inventoryList.to_csv(self.inventoryFile, encoding='utf-8', index=False)

  
  def delInventory(self,ISBN,quantity):
    self.inventoryList.loc[self.inventoryList.ISBN == ISBN, "Quantity"] -= quantity
    self.inventoryList.to_csv(self.inventoryFile, encoding='utf-8', index=False)

  def checkItemQuantity(self,ISBN,quantity):
    if (self.inventoryList.loc[self.inventoryList['ISBN'] == ISBN, 'Quantity'].iloc[0]) >= quantity:
      return True
    else:
      return False

  
  def printInventory(self):
    book = Book()
    inventory_list = book.readBookFile.merge(self.inventoryList, on = 'ISBN')

    print("************ Inventory List ***********\n")
    print(inventory_list)

