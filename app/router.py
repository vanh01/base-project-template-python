from flask_restx import Api

from .controller.account import api as account_ns

def map_namespacev1(blp):
    api = Api(blp,
              title='FLASK RESTAPI',
              version='1.0',
              description='a template for flask web service'
            )
    api.add_namespace(account_ns, path='/account')