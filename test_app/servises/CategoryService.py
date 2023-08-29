from test_app.models import Categories

class CategoryService():
    def get_all(self):
        return Categories.objects.all()
    
    def get_by_id(self, id):
        return Categories.objects.get(id = id)
