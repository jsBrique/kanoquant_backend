from flask_restplus import Namespace, Resource, fields
from flask_login import login_required
from .chrome import gf_API
import json
ns = Namespace('api', description='api')

success_model = ns.model('Success', {
    'message': fields.String
})


@ns.route('', endpoint='index')

class IndexPage(Resource):

    @ns.marshal_with(success_model)
    def get(self):
        """
        Example url
        """
        return {'message': 'Success'}
