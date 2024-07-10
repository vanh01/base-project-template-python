import functools
from flask import request

from ...resource import ResourceType, ActionType


def Access(resources: list[ResourceType], action: ActionType):
    def Inner(func):
        @functools.wraps(func)
        def check_permission(*args, **kwargs):
            # check permission of the account by something like token, id
            value = func(*args, **kwargs)
            return value

        return check_permission
    return Inner