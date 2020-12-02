from flask import render_template, request, redirect
from saleapp import app, utils, login
from saleapp.admin import *
from flask_login import login_user
import os


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)


@app.route("/products")
def product_list():
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    products = utils.read_products(cate_id=cate_id,
                                   kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)

    return render_template('product-list.html',
                           products=products)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)

    return render_template('product-detail.html',
                           product=product)


@app.route('/login', methods=['post'])
def login_usr():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')

        user = utils.check_login(username=username,
                                 password=password)
        if user:
            login_user(user=user)

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route('/register', methods=['get','post'])
def register():
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')
        if password == confirm:
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('username')
            f = request.files["avatar"]
            avatar_path = 'images/upload/%s' % f.filename
            f.save(os.path.join(app.root_path, 'static/', avatar_path))
            if utils.register(name=name, username=username,
                              email=email, avatar=avatar_path):
                return redirect('/')
            else:
                err_msg = "He thong co loi, vui long dang nhap lai sau"
        else:
            err_msg = "May khau khong dung !!"

    return render_template('register.html', err_msg=err_msg)


def add_or_update_mark():
    return render_template("mark-add.html")


if __name__ == "__main__":
    app.run(debug=True)
