
from odoo import fields, models

class PetAction(models.Model):
    _name = 'pet.action'

    name = fields.Char(string = 'Accion ejecutada', required = True)

    pet_id = fields.Many2one('pet', string = 'Mascota')