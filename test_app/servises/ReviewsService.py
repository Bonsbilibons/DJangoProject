from test_app.models import Reviews
from test_app.DTO.products import LeaveCommentDTO

class ReviewsService():
    def get_all(self):
        return Reviews.objects.all()
    
    def get_by_id(self, id):
        return Reviews.objects.get(id = id)

    def filter_by_product_id(self, id):
        return Reviews.objects.filter(product_id = id)

    def delete_by_id(self, id):
        return Reviews.objects.get(id = id).delete()

    def leave_comment(self, dto: LeaveCommentDTO):
        review = Reviews()
        review.author = dto.author
        review.title = dto.title
        review.comment = dto.comment
        review.product = dto.product
        review.created_at = dto.created_at
        review.save()