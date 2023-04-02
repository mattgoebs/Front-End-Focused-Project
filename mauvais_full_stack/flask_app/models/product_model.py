from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model
from flask import flash

class Product:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.type = data['type']
        self.style = data['style']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO product (name, price, type, style, image, user_id) VALUES (%(name)s, %(price)s, %(type)s, %(style)s, %(image)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM product;"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_product = []
            for row in results:
                this_product = cls(row)
                all_product.append(this_product)
            return all_product
        return []

    @classmethod
    def update(cls, data):
        query = "UPDATE product SET name = %(name)s, price = %(price)s, type = %(type)s, style = %(style)s, image = %(image)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
