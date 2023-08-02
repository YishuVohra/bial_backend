from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class TimeStampedSchema(BaseModel):
    created_at : Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()