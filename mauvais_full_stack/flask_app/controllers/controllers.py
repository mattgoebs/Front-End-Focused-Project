from flask_app import app
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_app.models.product_model import Product
from flask_app.models.user_model import User
from flask_app.__init__ import DATABASE
import base64
from werkzeug.utils import secure_filename
import os
import sys


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/product/black-slim-tee")
def blackslimtee():
    return render_template("Black-Slim.html")

@app.route("/product/grey-oversized-tee")
def greyoversizedtee():
    return render_template("Grey-Oversized.html")

@app.route("/product/black-drop-shoulder")
def blackdropshoulderuct():
    return render_template("Black-Drop-Sweatshirt.html")

@app.route("/product/ice-grey-slim-tee")
def icegreyslimtee():
    return render_template("Ice-Grey-Slim-Tee.html")

@app.route("/product/ecru-slim-tee")
def ecruslimtee():
    return render_template("Ecru-Slim-Tee.html")

@app.route("/product/black-monogram")
def blackmonogram():
    return render_template("product.html")

@app.route("/product/navy-badge")
def navybadge():
    return render_template("Navy-Badge.html")

@app.route("/product/navy-slim-tee")
def navyslimtee():
    return render_template("Navy-Slim.html")


@app.route("/admin", methods=['POST'])
def admin():
    if 'user_id' not in session:
        return redirect('/log')
    data = {
        **request.form,
        'user_id': session['user_id']
    }

    # target = os.path.join(APP_ROOT, '../static/img/') 
    # if not os.path.isdir(target):
    #     os.mkdir(target)
    # else:
    #     print("Couldn't create upload directory: {}".format(target))
    # print(request.files.getlist("file"))
    # for admin in request.files.getlist("file"):
    #     print(admin)
    #     print("{} is the file name".format(admin.filename))
    #     filename = admin.filename
    #     destination = "/".join([target, filename])
    #     print("Save it to:", destination)
    #     admin.save(destination)
    
    return render_template("admin.html")


@app.route("/product/create", methods=['POST'])
def process_product():
    if 'user_id' not in session:
        return redirect('/log')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    # id = Product.create(data)

    # img = request.files['img']
    # if not img:
    #     return 'No img Uploaded', 400

    # filename = secure_filename(img.filename)
    # mimetype = img.mimetype

    # image = Product(image = img.read(), mimetype=mimetype, name=filename)
    # DATABASE.session.add(image)
    # DATABASE.session.commit()

    # target = os.path.join(APP_ROOT, '../static/img/') 
    # if not os.path.isdir(target):
    #     os.mkdir(target)
    # else:
    #     print("Couldn't create upload directory: {}".format(target))
    # print(request.files.getlist("file"))
    # for process_product in request.files.getlist("file"):
    #     print(process_product)
    #     print("{} is the file name".format(process_product.filename))
    #     filename = process_product.filename
    #     destination = "/".join([target, filename])
    #     print("Save it to:", destination)
    #     process_product.save(destination)


    return render_template("gallery.html")



# @app.route('/admin/<filename>')
# def send_image(filename):
#     return send_from_directory("img", filename)


@app.route("/gallery", methods=['GET'])
def gallery():
    if 'user_id' not in session:
        return redirect('/log')
    user = User.get_by_id({'id': session['user_id']})

    image_name = os.listdir('./flask_app/static/img')


    # image=image.query.all()
    # base64_image = [base64.b64encode(image).decode("utf-8") for image.image in image]

    return render_template("gallery.html", logged_user=user, image_name=image_name)

@app.route("/gallery/black-slim-tee")
def product_page():
    return render_template("product.html")

@app.route("/shopping-cart")
def shopping_cart():
    return render_template("shopping-cart.html")