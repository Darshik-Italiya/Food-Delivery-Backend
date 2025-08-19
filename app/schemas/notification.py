from pydantic import BaseModel
from datetime import datetime
from ..models.notification import NotificationType


class NotificationCreate(BaseModel):
    user_id: int
    message: str
    type: NotificationType


class NotificationOut(BaseModel):
    id: int
    user_id: int
    message: str
    type: NotificationType
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
