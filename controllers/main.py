from odoo import http
from odoo.http import request
class PetController(http.Controller):
    @http.route('/pet', auth='user', type='json')
    def get_pets(self, *args, **kwargs):
        print(args, kwargs)
        print(request.jsonrequest)
        return request.env.user