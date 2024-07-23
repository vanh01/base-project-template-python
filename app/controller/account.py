import logging
from flask import request
from flask_restx import Resource

from ..util.dto import AccountDto

from ..resource import ResourceType, ActionType
from ..helper.decorator.permission import Access
from ..helper.decorator.rate_limiter import rate_limited, Period
from ..service.account import get_all_accounts, create_account, get_account_by_id

api = AccountDto.api
_account = AccountDto.account

logger = logging.getLogger(__name__)

@api.route("")
class AccountList(Resource):
    @api.doc('list_of_registered_accounts')
    @api.marshal_list_with(_account, envelope='data')
    @Access(resources=[ResourceType.ACCOUNT], action=ActionType.READ)
    @rate_limited(rate=100, per=Period.MINUTE)
    def get(self):
        """List all registered accounts"""
        return get_all_accounts(), 200

    @api.response(201, 'Account successfully created.')
    @api.doc('create a new account')
    @api.expect(_account, validate=True)
    @Access(resources=[ResourceType.ACCOUNT], action=ActionType.CREATE)
    def post(self):
        """Creates a new Account """
        account = request.json
        new_account = create_account(account)
        if new_account is None:
            return "Something went wrong!", 500
        return new_account.id, 200


@api.route("/<public_id>")
@api.param('public_id', 'The Account identifier')
@api.response(404, 'Account not found.')
class Account(Resource):
    @api.doc('get a account')
    @api.marshal_with(_account)
    def get(self, public_id):
        return get_account_by_id(public_id), 200

@api.route("/oauth/google/login")
class AccountGoogle(Resource):
    @api.doc('login with google')
    def get(self):
        pass

@api.route("/oauth/google/callback")
@api.param('code', 'code from google')
class AccountGoogleCallback(Resource):
    @api.doc('google callback')
    def get(self):
        pass
