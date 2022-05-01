# Cart class
import pandas as pd
from Inventory import Inventory


class Cart:
  def __ini__(self,username):
    self.userName = username
    self.ISBN = None
    self.quantity = None
    self.itemList = pd.DataFrame(columns=['ISBN', 'Quantity', 'Price'], dtype=object)