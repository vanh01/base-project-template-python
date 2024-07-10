from .. import db
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.dialects.postgresql import ARRAY
from ..resource import ResourceType, ActionType

class Resource(db.Model):
    """ Resource Model for storing user permission """
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, primary_key=True)
    resource_type = Column(Enum(ResourceType), nullable=False)
    action_types = Column(ARRAY(Enum(ActionType)), nullable=False)
