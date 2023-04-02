from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import product_model
import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM user LEFT JOIN product on user.id = product.user_id WHERE user.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        user = cls(results[0])
        list_of_product = []
        for row in results:
            if row['product.id'] == None:
                break
            product_data = {
                **row,
                'id': row['product.id'],
                'created_at': row['product.created_at'],
                'updated_at': row['product.updated_at']
            }
            this_product = product_model.Product(product_data)
            list_of_product.append(this_product)
        user.product = list_of_product
        return user

    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            flash("First name required", "reg")
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash("last name required", "reg")
            is_valid = False
        if len(user_data['email']) < 1:
            flash("email required", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid Email format", "reg")
            is_valid = False
        else:
            data = {
                'email': user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash("email already registered")
                is_valid = False
        if len(user_data['password']) < 2:
            flash("Password is less than 2", "reg")
            is_valid = False
        return is_valid