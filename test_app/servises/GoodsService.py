import json
from test_app.models import Products,Categories
import datetime
from test_app.functions.functions import handle_uploaded_file
from test_app.DTO.products import CreateProductDTO
from test_app.DTO.products import UpdateProductDTO

class GoodsService():
    def get_all(self):
        return Products.objects.all()

    def get_goods_by_category_id(self, category_id):
        return Products.objects.filter(category_id = category_id)

    def get_by_id(self , id):
        return Products.objects.get(id = id)

    def delete_by_id(self , id):
        return Products.objects.get(id = id).delete()

    def create_goods(self, dto: CreateProductDTO):
        product = Products()
        product.name = dto.name
        product.description = dto.description
        product.status = dto.status
        product.cost = dto.cost
        product.amount = dto.amount
        if dto.file != '':
            product.icon = handle_uploaded_file(dto.file)
        product.category = dto.category
        product.created_at = dto.created_at
        product.updated_at = dto.updated_at
        product.save()

    def update_goods(self, id, dto: UpdateProductDTO):
        product = Products.objects.get(id = id)
        product.name = dto.name
        product.description = dto.description
        product.status = dto.status
        product.cost = dto.cost
        product.amount = dto.amount
        if dto.file != '':
            product.icon = handle_uploaded_file(dto.file)
        product.category = dto.category
        product.updated_at = dto.updated_at
        product.save()
