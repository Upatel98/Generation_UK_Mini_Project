#---Mini-Project---

from src.ecosystem import database_stup, prnt_database, cls_database, inpt, clr_trmnl
from src.ecosystem import products, couriers, orders

database_stup()

while True:
  print('\n---Welcome---')
  print('[Index 0] ==> Exit App')
  print('[Index 1] ==> Products Menu')
  print('[Index 2] ==> Couriers Menu')
  print('[Index 3] ==> Orders Menu')
  entr = inpt(input('Enter Index: '), 4)
  clr_trmnl()

  if entr == 0:

    cls_database()
    print('Exit, Thank You')
    break

  elif entr == 1: 
    while True:
      print('\n---Product Menu---')
      print('[Index 0] ==> Return to Main Menu')
      print('[Index 1] ==> Products Menu')
      print('[Index 2] ==> Add New Item')
      print('[Index 3] ==> Update Item')
      print('[Index 4] ==> Delete an Item')
      entr = inpt(input('Enter Index: '), 6)
      clr_trmnl()

      if entr == 0:
        clr_trmnl()
        break

      elif entr == 1:
        prnt_database('products')

      elif entr == 2:
        products.add()
      
      elif entr == 3:
        products.updt()

      elif entr == 4:
        products.dlt()

  elif entr == 2: 
    while True: 
      print('\n---Courier Menu---')
      print('[Index 0] ==> Return to Main Menu')
      print('[Index 1] ==> Couriers')
      print('[Index 2] ==> Add Courier')
      print('[Index 3] ==> Update Courier')
      print('[Index 4] ==> Delete Courier')
      entr = inpt(input('Enter Index: '), 5)
      clr_trmnl()
    
      if entr == 0:
        clr_trmnl()
        break

      elif entr == 1:
        prnt_database('couriers')

      elif entr == 2:
        couriers.add()

      elif entr == 3:
        couriers.updt()
        
      elif entr == 4:
        couriers.dlt() 

  elif entr == 3:
    while True: 
      print('\n---Orders Menu---')
      print('[Index 0] ==> Return to Main Menu')
      print('[Index 1] ==> Orders Directory')
      print('[Index 2] ==> Add Customer Information')
      print('[Index 3] ==> Update Order Status')
      print('[Index 4] ==> Update Customer Information')
      print('[Index 5] ==> Delete Customer Information')
      entr = inpt(input('Enter Index: '), 6)
      clr_trmnl()

      if entr == 0:
        clr_trmnl()
        break

      elif entr == 1:
        prnt_database('orders')

      elif entr == 2:
        orders.add()
      
      elif entr == 3:
        orders.updt_status()
      
      elif entr == 4:
        orders.updt_info()
      
      elif entr == 5:
        orders.dlt()