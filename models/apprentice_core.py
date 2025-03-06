from odoo import models, fields, api
import datetime

class Apprentice(models.Model):
    _name = 'apprentice.apprentice'
    _description = 'Apprentice Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'



    # Simple  Fields
    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    today = fields.Date.today()

    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], string='Level', default='beginner')
    email = fields.Char(string='Email')
    amount = fields.Float(string='Amount')
    date = fields.Date(string='Date of registration')
    text_field = fields.Text(string='text_field')
    html_field = fields.Html(string="Html field")
    binary_field = fields.Binary(string='binary_field')
    age = fields.Integer('Age', compute= "compute_age")
    

    # Relational fields
    mentor_id = fields.Many2one('apprentice.mentor', string="Mentor", help="The  mentor linked to the apprentice")


    @api.depends('date_of_birth')
    def compute_age(self):
        "Compute the age  of this  person"
        for  record in self:
            age = record.today.year - record.date_of_birth.year
        record.age = age