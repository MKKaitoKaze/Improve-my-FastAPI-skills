from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
from enum import Enum
from typing import List
from typing import Optional

users = [
    {"id": 1, "role": "admin", "name": "Max"},
    { "id": 2, "role": "moderator", "name": "Olexandr"},
    { "id": 3, "role": "smoker", "name": "Sasha"},
    { "id": 4, "role": "member", "name": "Yaroslav", "degree": [
        {"id": 1, "created_time": "2024-01-01T00:00:00", "type_degree": "new member"}
    ]},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "Hamster", "side": "buy", "price": 0.06, "amount": 5000000},
    {"id": 2, "user_id": 2, "currency": "Blum", "side": "sell", "price": 0.5, "amount": 50000},
    {"id": 3, "user_id": 3, "currency": "MemeFi", "side": "buy", "price": 0.0005, "amount": 23000000}
]

class DegreeType(Enum):
    new_member = "new member"
    advanced = "advanced"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_time: datetime
    type_degree: DegreeType

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=10)
    side: str
    prise: float = Field(ge=0)
    amount: int

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []
