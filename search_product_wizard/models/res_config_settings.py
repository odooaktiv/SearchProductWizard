# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    field1 = fields.Many2one('product.attribute', string='Attribute 1')
    field2 = fields.Many2one('product.attribute', string='Attribute 2')
    field3 = fields.Many2one('product.attribute', string='Attribute 3')
    field4 = fields.Many2one('product.attribute', string='Attribute 4')
    field5 = fields.Many2one('product.attribute', string='Attribute 5')

    @api.model
    def get_values(self):
        """
        This method gets the value of attributes from config parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        res = super(ResConfigSettings, self).get_values()
        ir_config_parameter_obj = self.env['ir.config_parameter']
        field1 = ir_config_parameter_obj.get_param(
            'search_product_wizard.field1', False)
        field2 = ir_config_parameter_obj.get_param(
            'search_product_wizard.field2', False)
        field3 = ir_config_parameter_obj.get_param(
            'search_product_wizard.field3', False)
        field4 = ir_config_parameter_obj.get_param(
            'search_product_wizard.field4', False)
        field5 = ir_config_parameter_obj.get_param(
            'search_product_wizard.field5', False)
        res.update(field1=field1 and int(field1) or False,
                   field2=field2 and int(field2) or False,
                   field3=field3 and int(field3) or False,
                   field4=field4 and int(field4) or False,
                   field5=field5 and int(field5) or False)
        return res

    @api.multi
    def set_values(self):
        """
        This method sets the value of attributes in config parameters.
        --------------------------------------------------------------
        @self : object pointer
        """
        super(ResConfigSettings, self).set_values()
        IrConfigParams = self.env['ir.config_parameter']
        IrConfigParams.set_param(
            'search_product_wizard.field1', self.field1.id)
        IrConfigParams.set_param(
            'search_product_wizard.field2', self.field2.id)
        IrConfigParams.set_param(
            'search_product_wizard.field3', self.field3.id)
        IrConfigParams.set_param(
            'search_product_wizard.field4', self.field4.id)
        IrConfigParams.set_param(
            'search_product_wizard.field5', self.field5.id)

    @api.onchange('field1', 'field3', 'field4', 'field5')
    def onchange_field2(self):
        """
        This method filters the Product attributes as per its usage.
        Used Product attribues will not appear again.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.field1:
            domain.append(('id', '!=', self.field1.id))
        if self.field3:
            domain.append(('id', '!=', self.field3.id))
        if self.field4:
            domain.append(('id', '!=', self.field4.id))
        if self.field5:
            domain.append(('id', '!=', self.field5.id))
        return {'domain': {'field2': domain}}

    @api.onchange('field1', 'field2', 'field4', 'field5')
    def onchange_field3(self):
        """
        This method filters the Product attributes as per its usage.
        Used Product attribues will not appear again.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.field1:
            domain.append(('id', '!=', self.field1.id))
        if self.field2:
            domain.append(('id', '!=', self.field2.id))
        if self.field4:
            domain.append(('id', '!=', self.field4.id))
        if self.field5:
            domain.append(('id', '!=', self.field5.id))
        return {'domain': {'field3': domain}}

    @api.onchange('field1', 'field2', 'field3', 'field5')
    def onchange_field4(self):
        """
        This method filters the Product attributes as per its usage.
        Used Product attribues will not appear again.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.field1:
            domain.append(('id', '!=', self.field1.id))
        if self.field2:
            domain.append(('id', '!=', self.field2.id))
        if self.field3:
            domain.append(('id', '!=', self.field3.id))
        if self.field5:
            domain.append(('id', '!=', self.field5.id))
        return {'domain': {'field4': domain}}

    @api.onchange('field1', 'field2', 'field3', 'field4')
    def onchange_field5(self):
        """
        This method filters the Product attributes as per its usage.
        Used Product attribues will not appear again.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.field1:
            domain.append(('id', '!=', self.field1.id))
        if self.field2:
            domain.append(('id', '!=', self.field2.id))
        if self.field3:
            domain.append(('id', '!=', self.field3.id))
        if self.field4:
            domain.append(('id', '!=', self.field4.id))
        return {'domain': {'field5': domain}}
