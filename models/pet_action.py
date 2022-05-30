
from odoo import fields, models

class PetAction(models.Model):
    _name = 'pet.action'
    _description = 'descripcion a'

    name = fields.Char(string = 'Accion ejecutada', required = True)

    pet_id = fields.Many2one('pet', string = 'Mascota')