# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

    field1 = fields.Many2one('product.attribute', string='Attribute 1')
    field2 = fields.Many2one('product.attribute', string='Attribute 2')
    field3 = fields.Many2one('product.attribute', string='Attribute 3')
    field4 = fields.Many2one('product.attribute', string='Attribute 4')
    field5 = fields.Many2one('product.attribute', string='Attribute 5')

    @api.model
    def get_default_field1(self, fields):
        """This method gets the value of attribute 1 as field 1 from config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        field1 = self.env["ir.config_parameter"].get_param(
            "search_product_wizard.field1", default=None)
        return {'field1': (field1 and int(field1)) or False}

    @api.model
    def get_default_field2(self, fields):
        """
        This method gets the value of attribute 2 as field 2 from config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        field2 = self.env["ir.config_parameter"].get_param(
            "search_product_wizard.field2", default=None)
        return {'field2': (field2 and int(field2)) or False}

    @api.model
    def get_default_field3(self, fields):
        """
        This method gets the value of attribute 3 as field 3 from config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        field3 = self.env["ir.config_parameter"].get_param(
            "search_product_wizard.field3", default=None)
        return {'field3': (field3 and int(field3)) or False}

    @api.model
    def get_default_field4(self, fields):
        """
        This method gets the value of attribute 4 as field 4 from config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        field4 = self.env["ir.config_parameter"].get_param(
            "search_product_wizard.field4", default=None)
        return {'field4': (field4 and int(field4)) or False}

    @api.model
    def get_default_field5(self, fields):
        """
        This method gets the value of attribute 5 as field 5 from config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        field5 = self.env["ir.config_parameter"].get_param(
            "search_product_wizard.field5", default=None)
        return {'field5': (field5 and int(field5)) or False}

    @api.multi
    def set_field1(self):
        """
        This method sets the value of attribute 1 as field 1 in config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param(
                "search_product_wizard.field1", record.field1.id or '')

    @api.multi
    def set_field2(self):
        """
        This method sets the value of attribute 2 as field 2 in config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param(
                "search_product_wizard.field2", record.field2.id or '')

    @api.multi
    def set_field3(self):
        """
        This method sets the value of attribute 3 as field 3 in config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param(
                "search_product_wizard.field3", record.field3.id or '')

    @api.multi
    def set_field4(self):
        """
        This method sets the value of attribute 4 as field 4 in config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param(
                "search_product_wizard.field4", record.field4.id or '')

    @api.multi
    def set_field5(self):
        """
        This method sets the value of attribute 5 as field 5 in config
        parameters.
        ----------------------------------------------------------------
        @self : object pointer
        """
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param(
                "search_product_wizard.field5", record.field5.id or '')

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
