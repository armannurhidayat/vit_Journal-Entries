# -*- coding: utf-8 -*-
from odoo import http

# class VitJurnalEntry(http.Controller):
#     @http.route('/vit_jurnal_entry/vit_jurnal_entry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_jurnal_entry/vit_jurnal_entry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_jurnal_entry.listing', {
#             'root': '/vit_jurnal_entry/vit_jurnal_entry',
#             'objects': http.request.env['vit_jurnal_entry.vit_jurnal_entry'].search([]),
#         })

#     @http.route('/vit_jurnal_entry/vit_jurnal_entry/objects/<model("vit_jurnal_entry.vit_jurnal_entry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_jurnal_entry.object', {
#             'object': obj
#         })