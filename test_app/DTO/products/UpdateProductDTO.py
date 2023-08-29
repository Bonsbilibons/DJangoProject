from dataclasses import dataclass
from test_app.models import Categories
import datetime

@dataclass(frozen=True)
class UpdateProductDTO:
    name: str
    description: str
    status: str
    cost: int
    amount: int
    file: str
    category: Categories
    updated_at = str(datetime.datetime.now()).split('.')[0]