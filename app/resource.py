from enum import Enum

# this is all resources
class ResourceType(Enum):
    ACCOUNT = 10
    RESOURCE = 20

# this is all actions
class ActionType(Enum):
    READ = 10
    CREATE = 20
    UPDATE = 30
    DELETE = 40
