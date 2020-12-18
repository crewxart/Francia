# -*- coding: utf-8 -*-

from odoo import models, fields, api

class factura(models.Model):
    _name='factura.factura'
    EmpresaMandante=fields.Char()
    Nombre=fields.Char()
    DireccionFactura=fields.Char()
    DireccionEntrega=fields.Char()
    Rut=fields.Integer() #### Validar datos
    comuna = fields.Char()
    Planilla = fields.Char()
    Local = fields.Char()
    Giro= fields.Char()
    nFactura=fields.Integer()
    LugarEmision=fields.Char()

    ### Producto
    producto_id = fields.Many2one('inventario.producto', string="Producto")


