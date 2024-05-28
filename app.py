from flask import Flask,request,render_template, redirect, url_for, session, jsonify
from controllers import IndexController as main
from controllers import EmailController as email
#Flask initialization
app = Flask(__name__)
app.secret_key = "ecommerce"
app.config['SECRET_KEY'] = "ecommerce"

@app.route("/index")
def index():
    success,resp = main.index()
    if success != 1:
        return redirect(url_for('error_page', message=resp))
    else:
        username = session['username'] 
        return render_template("index.html", resp=resp,username=username)
@app.route("/shop")
def shop():
    success,resp = main.index()
    if success != 1:
        return redirect(url_for('error_page', message=resp))
    else:
        username = session['username'] 
        return render_template("shop.html", resp=resp,username=username)
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create-blog")
def create_blog():
    return render_template("create_blog.html")

@app.route("/services")
def services():
    success,resp = main.index()
    if success != 1:
        return redirect(url_for('error_page', message=resp))
    else:
        username = session['username'] 
        return render_template("services.html", resp=resp,username=username)

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route('/login-form', methods=['POST'])
def login_form():
    username = request.form['username']
    password = request.form['password']
    # Do something with the username and password, like saving to a database
    print(f"Username: {username}, Password: {password}")
    success,resp = main.Login(username,password)
    print(resp)
    if success != 1:
        return render_template('error_page.html', message=resp)
    else:
        session['username'] = resp
        text = "Bringing you the goods…"
        return render_template("welcome.html", text=text)
    
@app.route('/signup-form', methods=['POST'])
def signup_form():
    username = request.form['username']
    password = request.form['password']
    # Do something with the username and password, like saving to a database
    print(f"Username: {username}, Password: {password}")
    success,resp = main.Signup(username,password)
    print(resp)
    if success != 1:
        return render_template('error_page.html', message=resp)
    else:
        session['username'] = username
        text = "Bringing you the goods…"
        return render_template("welcome.html", text=text)


@app.route('/category/<category>')
def category(category):
    success,resp = main.category(category=category)
    if success != 1:
        # return redirect(url_for('error', message=resp))
        return render_template('error.html', message=resp)

    else:
        username = session['username']
        return render_template("category.html", resp=resp,category=category,username=username)
    
@app.route('/cart')
def cart():
    data = {
        "username": session['username']
    }

    success,resp = main.showCart(data)
    if success != 1:
        # return redirect(url_for('error', message=resp))
        return render_template('error.html', message=resp)

    else:
        username = session['username']
        return render_template("cart.html", resp=resp,username=username)

@app.route('/more-info', methods=['POST'])
def moreInfo():
    data = request.json
    itemId = data.get('itemId')

    item_name = data.get('name')
    item_image = data.get('image')
    item_price = data.get('price')
    item_description = data.get('description')

    
    # Add the item to the cart
    item = {
        'id': itemId,
        'name': item_name,
        'image': item_image,
        'price': item_price,
        'description': item_description,
    }
    items_dict = {
        itemId: item
    }

    data = {
        "username": session['username']
    }    

    username = session['username']
    return render_template("info.html", resp=items_dict)
    

@app.route('/myorders')
def myorders():
    data = {
        "username": session['username']
    }

    success,resp = main.showOrders(data)
    if success != 1:
        # return redirect(url_for('error', message=resp))
        return render_template('error.html', message=resp)

    else:
        username = session['username']
        return render_template("myorders.html", resp=resp,username=username)


@app.route('/order-cancel', methods=['POST'])
def orderCancel():
    # Get the order data from the request
    order_data = request.json

    data = {
        "username": session['username'],
        "orderId": order_data.get('orderId')

    }
    success,resp = main.orderCancel(data)
  
    if success != 1:
        return render_template('error.html', message=resp)
    else:
        return jsonify({'message': 'Order Cancelled successfully'}), 200
    
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Get item details from the POST request
    data = request.json
    item_id = data.get('id')
    item_name = data.get('name')
    item_image = data.get('image')
    item_price = data.get('price')
    
    # Add the item to the cart
    cart_item = {
        'id': item_id,
        'name': item_name,
        'image': item_image,
        'price': item_price
    }
    cart = []

    cart.append(cart_item)
    data = {
        "username": session['username']
    }    
    success,resp = main.addToCart(cart_item,data)
    if success != 1:
        # return redirect(url_for('error', message=resp))
        return render_template('error.html', message=resp)

    else:
        return jsonify({'message': 'Item added to cart successfully'}), 200
    

@app.route('/order', methods=['POST'])
def order():
    # Get the order data from the request
    order_data = request.json

    processed_keys = set()
    orders = []

    cart_order = {
        'items': order_data.get('items'),
        'totalAmount': order_data.get('totalAmount'),
        'shipping': order_data.get('shipping'),
        'discountCode': order_data.get('discountCode')
    }


    for item in cart_order['items']:

        if item['itemId'] in processed_keys:
            continue  # Skip if the item key has already been processed
        processed_keys.add(item['itemId'])
    
        item_name = item['name']
        item_price = item['price']
        print(f"Item: {item_name}, Price: ${item_price}")
        order = {
            'key': item['itemId'],
            'quantity': item['quantity'],
            'name': item['name'],
            'price': item['price'],
            'image': item['image'],
            'shipping': cart_order['shipping'],
            'discountCode': cart_order['discountCode'],
        }


    
    orders.append(order)

    resp = email.send_order_email(cart_order)
    data = {
        "username": session['username']
    }    
    success,resp = main.addToOrders(orders,data)
    if success != 1:
        return render_template('error.html', message=resp)
    else:
        return jsonify({'message': 'Order added successfully'}), 200


@app.route("/order-confirmed")
def order_confirmed():
    text = "Confirming Your Order"
    return render_template("welcome.html",text=text)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form['name']
    mail = request.form['email']

    # Send the subscription email
    resp = email.send_subscription_email(name, mail)

    # Redirect to a thank you page or back to home
    return redirect(url_for('index'))

@app.route('/submit_blog', methods=['POST'])
def submit_blog():
    # Get form data
    country = request.form['country']
    author_name = request.form['author_name']
    author_email = request.form['author_email']
    blog_title = request.form['blog_title']
    blog_content = request.form['blog_content']
    blog_image = request.files['blog_image']

    # Save blog details to Firestore

    data = {
        'country': country,
        'author_name': author_name,
        'author_email': author_email,
        'blog_title': blog_title,
        'blog_content': blog_content,
        'blog_image': blog_image,
        'username' : session['username']
    }
    success,resp = main.submitBlog(data)

    # Return response
    return jsonify({
        'message': 'Blog submitted successfully'
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)
    # app.run()