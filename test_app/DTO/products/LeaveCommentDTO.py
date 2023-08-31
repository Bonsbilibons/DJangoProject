from dataclasses import dataclass
from test_app.models import Reviews
import datetime

@dataclass(frozen=True)
class LeaveCommentDTO:
    author: int
    title: str
    comment: str
    product: int
    created_at = str(datetime.datetime.now()).split('.')[0]