
from odoo import fields, models

class Pet(models.Model):
    _name = 'pet'
    _description = 'pets'

    name = fields.Char(string = 'Nombre de la mascota', required = True)
    age = fields.Integer(string = 'Edad de la mascota')
    breed = fields.Char(string = 'Raza de la mascota', help='Aqui va la raza')
    last_name = fields.Char(string = 'Apellido', default='Garcia')

    owner = fields.Many2one('res.partner', string='Propietario')