# -*- coding: utf-8 -*-
from odoo import http

# class Factura(http.Controller):
#     @http.route('/factura/factura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/factura/factura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('factura.listing', {
#             'root': '/factura/factura',
#             'objects': http.request.env['factura.factura'].search([]),
#         })

#     @http.route('/factura/factura/objects/<model("factura.factura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('factura.object', {
#             'object': obj
#         })