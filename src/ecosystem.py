import pymysql, os
from dotenv import load_dotenv

#---Connection to LocalHost---
load_dotenv()
connection = pymysql.connect( 
    host = os.getenv("mysql_host"), 
    user = os.getenv("mysql_user"),
    password = os.getenv("mysql_pass"),
    database = os.getenv("mysql_db"))

#---Clear Terminal---
clr_trmnl = lambda: os.system('cls')

#---Check Float---
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#---Input Loop---
def inpt(entr, x):
    while True:
        try:
            if int(entr) not in list(range(0, x)):
                print('Invalid Index')
                entr = input('Re-Enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Re-Enter Index: ')
            continue
        else:
            break
    return int(entr) 

#---SQL Input Loop---
def sql_inpt(entr, table):
    while True:
        cursor = connection.cursor()
        cursor.execute(f'SELECT id FROM {table}')
        try:
            if int(entr) not in [x[0] for x in cursor.fetchall()]:
                print('Invalid Index')
                entr = input('Re-Enter Index: ')
                continue
        except ValueError:
            print('Invalid Index')
            entr = input('Re-Enter Index: ')
            continue
        else:
            break

    return int(entr)

#---Table Count---
def count(table):
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(id) FROM {table}")
    x = cursor.fetchall()[0][0]
    return x 

#---Setup Database---
def database_stup():
    with open('src/mini_project_db.sql', 'r') as file:
        file = file.read()
        sqlfile = file.split(';')
        for command in sqlfile:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
 
#---Print Database---
def prnt_database(table):

    if table == 'products':
        print('\n---Product List---')
        if count('products') > 0:
            cursor = connection.cursor()
            cursor.execute('SELECT id, name, price FROM products')
            rows = cursor.fetchall()
            for row in rows:
                print(f'[Index {row[0]}] ==> [Name: {row[1]} , Price: {row[2]}]')
        else: print('Table is Empty - Unable to Print')   
    
    elif table == 'couriers':
        print('\n---Courier List---')
        if count('couriers') > 0:
            cursor = connection.cursor()
            cursor.execute('SELECT id, name, number FROM couriers')
            rows = cursor.fetchall()
            for row in rows:
                print(f'[Index {(row[0])}] ==> [Name: {row[1]} , Number: {row[2]}]')
        else: print('Table is Empty - Unable to Print')

    elif table == 'orders':
        print('\n---Order Directory---')
        if count('orders') > 0:
            cursor = connection.cursor()
            cursor.execute('SELECT id, customer_name, customer_address, customer_number, customers_order, courier, status FROM orders')
            rows = cursor.fetchall()
            for row in rows:
                print(f'[Index {row[0]}]:\n[Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Order: {row[4]}, Courier: {row[5]}, Status: {row[6]}]\n')
        else: print('Table is Empty - Unable to Print')

#---Close Database---
def cls_database():
    cursor = connection.cursor()
    cursor.close()
    connection.close()
    print('\nProducts Database Uploaded')
    print('Couriers Database Uploaded')
    print('Orders Database Uploaded')

#---Product Class---
class products:
    def __init__(self):
        pass

    #---Add Product---
    def add():
        print('\n---Add New Item---')
        
        name =  input('\nEnter Name: ')
        while True:
            price = input('Enter Price: ')
            if isfloat(price) == True:
                break
            else:
                print('Invalid Price Value')
                continue
    
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO products (name, price) VALUES ('{name}', '{price}')")
        connection.commit()

        prnt_database('products')

    #---Update Product---
    def updt():
        if count('products') > 0:
                
            print('\n---Update Item---')
            prnt_database('products')
            
            entr = input('Enter Item Index to Update: ')
            entr = sql_inpt(entr, 'products')

            new_name = input('\nEnter New Name: ')
            new_price = input('Enter New Price: ')
            
            if new_name == '' or new_price == '':
                print('One\Both Inputs Empty - No Update')
            else:
                while True:
                    if isfloat(new_price) == True:
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE products SET name='{new_name}', price='{new_price}' WHERE id='{entr}'")
                        connection.commit()
                        break
                    else:
                        print('Invalid Price Value')
                        new_price = input('Enter Price: ')
                        continue

            prnt_database('products')
        
        else: print('Table is Empty - Unable to Update')

    #---Delete Product---
    def dlt():
        if count('products') > 0:
                
            print('\n---Delete Item---')
            prnt_database('products')

            entr = input('\nEnter Item Index to Delete: ')
            entr = sql_inpt(entr, 'products')

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM products WHERE id = '{entr}'")
            connection.commit()

            prnt_database('products')
        
        else: print('Table is Empty - Unable to Delete')

#---Courier Class---
class couriers:
    def __init__(self):
        pass
        
    #---Add Courier---    
    def add():
        print('\n---Add New Courier---')
        
        name = input('Enter Courier Name: ')

        while True:
            number = input('Enter Courier Number: ')
            if number.isdigit() == True and len(number) == 11 and number[:2] == '07':
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO couriers (name, number) VALUES ('{name}', '{number}')")
                connection.commit()
                break
            else:
                print('Invalid Phone Number - 11 Digit Beginning with 07')
                continue
        
        prnt_database('couriers')

    #---Update Courier---    
    def updt():
        if count('couriers') > 0:
            
            print('\n---Update Courier---')
            prnt_database('couriers')
            
            entr = input('\nEnter Courier Index to Update: ')
            entr = sql_inpt(entr, 'couriers')

            new_name = input('\nEnter Courier Name: ')
            new_number = input('Enter Courier Phone Number: ')

            if new_name == '' or new_number == '':
                print('One\Both Inputs Empty - No Update')
            else:
                while True:
                    if new_number.isdigit() == True and len(new_number) == 11 and new_number[:2] == '07':
                        cursor = connection.cursor()
                        cursor.execute(f"UPDATE couriers SET name = '{new_name}', number = '{new_number}' WHERE id = '{entr}'")
                        connection.commit()
                        break
                    else:
                        print('Invalid Phone Number - 11 Digit Beginning with 07')
                        new_number = input('Enter Courier Phone Number: ')
                        continue

            prnt_database('couriers')
            
        else: print('Table is Empty - Unable to Update')

    #---Delete Courier---    
    def dlt():
        if count('couriers') > 0:
        
            print('\n---Delete Courier---')
            prnt_database('couriers')
            
            entr = input('Enter Courier Index to Delete: ')
            entr = sql_inpt(entr, 'couriers')

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM couriers WHERE id = '{entr}'")
            connection.commit()

            prnt_database('couriers')

        else: print('Table is Empty - Unable to Delete')

#---Order Class---
class orders:
    def __init__(self):
        pass
        
    #---Add Order---
    def add():
        print('\n---New Order Information---')
    
        while True:
            n = 0
            customer_name = input('Name: ')
            for x in customer_name:
                if x.isdigit() == True:
                    n += 1
                    print('No Numerical Values Allowed')
                    continue
                else:
                    pass
            if n == 0: break
        
        customer_address = input('Address: ')
        
        while True:
            customer_number = input('Phone Number: ')
            if customer_number.isdigit() == True and len(customer_number) == 11 and customer_number[:2] == '07':
                break
            else:
                print('Invalid Phone Number - 11 Digit Beginning with 07')
                continue
        print('')
        prnt_database('products')
        customer_order = input('Choose Order List: ')
        print('')
        prnt_database('couriers')
        courier = input('\nChoose Courier Index: ')
        courier = sql_inpt(courier, 'couriers')

        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO orders (customer_name, customer_address, customer_number, customers_order, courier, status) VALUES ('{customer_name}', '{customer_address}', '{customer_number}', '{customer_order}', '{courier}', 'Preparing')")
        connection.commit()

        prnt_database('orders')

   #---Update Order Status---
    def updt_status():
        if count('orders') > 0:

            print('\n---Update Order Status---')
            prnt_database('orders')

            entr = input('Choose Order Information Index: ')
            entr = sql_inpt(entr, 'orders')
            print('\n---Change Order Status---\n[Index 0] ==> Preparing\n[Index 1] ==> Awaiting Pickup\n[Index 2] ==> Out-for-Delivery\n[Index 3] ==> Delivered')
            updte_status = input('Enter Index to Update Order Status: ')
            updte_status = inpt(updte_status, 4)

            cursor = connection.cursor()

            if updte_status == 0:
                cursor.execute(f"UPDATE orders SET status = 'Preparing' WHERE id = '{entr}'")
            elif updte_status == 1:
                cursor.execute(f"UPDATE orders SET status = 'Awaiting Pickup' WHERE id = '{entr}'")
            elif updte_status == 2:
                cursor.execute(f"UPDATE orders SET status = 'Out-for-Delivery' WHERE id = '{entr}'")
            elif updte_status == 3:
                cursor.execute(f"UPDATE orders SET status = 'Delivered' WHERE id = '{entr}'")

            connection.commit()

            prnt_database('orders')
        
        else: print('Table is Empty - Unable to Update')

   #---Upadte Order Info---
    def updt_info():
        if count('orders') > 0:

            print('\n---Update Order Information---')
            prnt_database('orders')

            entr = input('Enter Order Index to Update: ')
            entr = sql_inpt(entr, 'orders')

            while True:
                n = 0
                customer_name = input('Name: ')
                for x in customer_name:
                    if x.isdigit() == True:
                        n += 1
                        print('No Numerical Values Allowed')
                        continue
                    else:
                        pass
                if n == 0: break
            
            customer_address = input('Address: ')
            while True:
                customer_number = input('Phone Number: ')
                if customer_number.isdigit() == True and len(customer_number) == 11 and customer_number[:2] == '07':
                    break
                else:
                    print('Invalid Phone Number - 11 Digit Beginning with 07')
                    continue
            
            prnt_database('products')
            customer_order = input('Choose Order List: ')
            prnt_database('couriers')
            courier = input('Choose Courier Index: ')
            courier = sql_inpt(courier, 'couriers')

            cursor = connection.cursor()
            cursor.execute(f"UPDATE orders SET customer_name = '{customer_name}', customer_address = '{customer_address}', customer_number = '{customer_number}', customers_order = '{customer_order}', courier = '{courier}' WHERE id = '{entr}'")
            connection.commit()

            prnt_database('orders')
            
        else: print('Table is Empty - Unable to Update ')
    
    #---Delete Order---
    def dlt():
        if count('orders') > 0:
            
            print('\n---Delte Order---')
            prnt_database('orders')
                
            entr = input('Enter Order Index to Delete: ')
            entr = sql_inpt(entr, 'orders')

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM orders WHERE id = '{entr}'")
            connection.commit()

            prnt_database('orders')
                
        else: print('Table is Empty - Unable to Delete')