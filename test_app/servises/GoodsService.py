import json
from test_app.models import Products,Categories


class GoodsService():
    def get_all(self , item):
        self.item = item
        return item.objects.all()

    def get_goods(self , id):
        self.id = id
        products = Products.objects.all()
        json_data = []
        for product in products:
                json_obj = {
                    'id': product.id, 
                    'name': product.name,
                    'description': product.description,
                    'cost': product.cost,
                    'status': product.status,
                    'amount' : product.amount,
                    'category_name' : product.category.name ,
                    'category_id' : product.category.id
                }
                if id == 0 :
                     json_data.append(json_obj)
                else:
                    if json_obj['category_id'] == id :  
                         json_data.append(json_obj)
        return json_data