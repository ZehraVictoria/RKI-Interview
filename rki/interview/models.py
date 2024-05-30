from pydantic import BaseModel
from datetime import date
from typing import Optional

class Candidate(BaseModel):
    """Model for an interview candidate."""

    id: int
    full_name: str
    experiences: list[str]
    birthday: Optional[date] = None
