from flask_restx import Namespace, fields


class AccountDto:
    api = Namespace('account', description='account related operations')
    account = api.model('account', {
        'email': fields.String(required=True, description='account email address'),
        'username': fields.String(required=True, description='account username'),
        'password': fields.String(required=True, description='account password'),
        'public_id': fields.String(description='account Identifier')
    })
