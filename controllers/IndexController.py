from models.database_operations import database_operations as database
from config import DBNAME,STORAGE_URL

def index():

    path = DBNAME+"/category" 
    success,resp = database().read(path)
    print(resp)
    return success,resp

def Signup(username, password):
    data = {
        "username": username,
        "password": password
    }

    path = DBNAME+"/users" 
    resp = database().create(path,data)
    print(resp)
    return 1,resp

def Login(username, password):
    data = {
        "username": username,
        "password": password
    }

    path = DBNAME+"/users" 
    success,resp,key = database().query_data_user(path,data)

    return success,resp['username']


def category(category):

    path = DBNAME+"/category/"+category 
    success,resp = database().read(path)
    print(resp)
    return success,resp

def showCart(data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)
    print(resp)
    if 'cart' not in resp or len(resp['cart']) == 0:
        return 0,"Your cart is empty."
    return success,resp['cart']

def showOrders(data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)
    print(resp)
    if 'orders' not in resp or len(resp['orders']) == 0:
        return 0,"Your orders list is empty."
    return success,resp['orders']

def orderCancel(data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)

    if success == 1 :

        # Iterate over each order
        if 'orderId' in data:

            path = DBNAME+"/users/"+key+"/orders" 
            delete = database().delete_by_key(path,data['orderId'])

            print(delete)
                
            return 1,"success"
        else:
            return 0,"Failed"
    else:
        return 0,"Failed"


def addToCart(cart_item,data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)

    if success == 1 :
        path = DBNAME+"/users/"+key+"/cart" 
        resp = database().create(path,cart_item)
        print(resp)
        return 1,resp
    else:
        return 0,resp

def addToOrders(orders,data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)

    if success == 1 :
        processed_keys = set()

        # Iterate over each order
        for order in orders:
            order_key = order['key']
            if order_key in processed_keys:
                continue  # Skip if the key has already been processed
            processed_keys.add(order_key)

            path = DBNAME+"/users/"+key+"/orders" 
            create = database().create(path,order)

            print(create)

            path = DBNAME+"/users/"+key+"/cart" 
            delete = database().delete_by_key(path,order_key)

            print(delete)
            
        return 1,"success"
    else:
        return 0,"Failed"
    
def submitBlog(data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)
    if success == 1 :
        path = "/blogs"
        bucket_name = DBNAME
        success,url = database().upload_image(path,bucket_name,data['blog_image'])

        if success == 1 :
            data['blog_image'] = url
            path = DBNAME+"/blogs/"+key
            resp = database().create(path,data)
            print(resp)
            return 1,resp
        else:
            return 0,resp
        
def update_profile(data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)
    if success == 1 :
        path = "profile/"
        bucket_name = DBNAME
        bucket_name = STORAGE_URL
        success,url = database().upload_image(path,bucket_name,data['profile_image'])

        if success == 1 :
            data['profile_image'] = url
            path = DBNAME+"/users/"+key
            resp = database().update(path,data)
            print(resp)
            return 1,resp
        else:
            return 0,resp
        

def getUser(data):
    path = DBNAME+"/users"

    success,resp,key = database().query_data_user(path,data)
    print(resp)
    
    return success,resp

    

