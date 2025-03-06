from odoo import models, fields, api

class ApprenticeMentor(models.Model):
    """  
    types of models 
    model.Model      => Default  model (regular model) =>stored in the db
    model.Transient  => Simplied access rights 
    model.Abstract   => A super model that can be inherited 
    """
    _name = 'apprentice.mentor'
    _description = "Apprentices Mentors "
    _inherit = ['mail.thread', 'mail.activity.mixin']
    


    name = fields.Many2one('res.partner', string='Name')
    email = fields.Char('email',  compute="compute_email",  readonly=True)

    @api.depends('name')
    def compute_email(self):
        for rec in self:
            if rec.name:
                # 'email' is a field on res.partner, not a separate model
                rec.email = rec.name.email
            else:
                rec.email = False