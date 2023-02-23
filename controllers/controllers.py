# -*- coding: utf-8 -*-
from odoo import http


class RetoOdooModule(http.Controller):
    @http.route('/reto', auth='public', website=True)
    def index(self, **kw):
        #user = self._uid
        return "Hello, world"

#     @http.route('/reto_odoo_module/reto_odoo_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reto_odoo_module.listing', {
#             'root': '/reto_odoo_module/reto_odoo_module',
#             'objects': http.request.env['reto_odoo_module.reto_odoo_module'].search([]),
#         })

#     @http.route('/reto_odoo_module/reto_odoo_module/objects/<model("reto_odoo_module.reto_odoo_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reto_odoo_module.object', {
#             'object': obj
#         })
