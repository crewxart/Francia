# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Categoria(models.Model):
    _name = 'inventario.categoria'
    name = fields.Char(string="Nombre", required= True)
    categoria_ids= fields.One2many(
        'inventario.producto',
        'categoria_id',
        string="Categorías"
    )

class producto(models.Model):
    _name = 'inventario.producto'

    nombre = fields.Char()
    descripcion = fields.Char()
    costoNeto = fields.Float()
    precioVenta = fields.Float()
    categoria_id = fields.Many2one('inventario.categoria', string="Categoria")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class detalle(models.Model):
    _name= 'producto.detalle'
    stock = fields.Float()
    variacionPN = fields.Float()
    variacionPV = fields.Float()
    estadoProducto= fields.Char()
    