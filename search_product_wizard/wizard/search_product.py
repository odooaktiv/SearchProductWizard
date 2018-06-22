# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class SearchProduct(models.TransientModel):
    """ Search Product Wizard Object for fetching all 
    the products as per the Product Attributes """
    _name = 'search.product'

    field1 = fields.Many2one(
        'product.attribute', string='Attribute 1')
    field2 = fields.Many2one('product.attribute', string='Attribute 2')
    field3 = fields.Many2one('product.attribute', string='Attribute 3')
    field4 = fields.Many2one('product.attribute', string='Attribute 4')
    field5 = fields.Many2one('product.attribute', string='Attribute 5')
    fieldv1 = fields.Many2one('product.attribute.value', string='Value 1')
    fieldv2 = fields.Many2one('product.attribute.value', string='Value 2')
    fieldv3 = fields.Many2one('product.attribute.value', string='Value 3')
    fieldv4 = fields.Many2one('product.attribute.value', string='Value 4')
    fieldv5 = fields.Many2one('product.attribute.value', string='Value 5')
    location_id = fields.Many2one(
        'stock.location', string='Location')
    product_id = fields.Many2one(
        'product.product', string='Product')
    product_qty = fields.Float(string='Quantity', default=1)
    production_date = fields.Datetime(string='Production Date', default=datetime.datetime.now())
    count_product = fields.Integer(
        string="Filtered Product  Count", compute='_compute_count_product')
    show_product_lines_ids = fields.One2many(
        'show.product.lines', 'search_product_id', 'Product Content')
    state = fields.Selection(
        [('new', 'New'), ('final', 'Final')], default='new')

    @api.model
    def default_get(self, fields):
        """
        This method is used to fetch the products attributes as per the 
        configuration.
        --------------------------------------------------------------------
        @self : object pointer
        """
        res = super(SearchProduct, self).default_get(fields)
        ir_config_parameter_obj = self.env['ir.config_parameter']
        ir_config_parameter_recs = ir_config_parameter_obj.search([])
        for recs in ir_config_parameter_recs:
            if recs.key == 'search_product_wizard.field1' and recs.value:
                res['field1'] = int(ir_config_parameter_obj.get_param('search_product_wizard.field1', False))
            if recs.key == 'search_product_wizard.field2' and recs.value:
                res['field2'] = int(self.env['ir.config_parameter'].get_param('search_product_wizard.field2', False))
            if recs.key == 'search_product_wizard.field3' and recs.value:
                res['field3'] = int(self.env['ir.config_parameter'].get_param('search_product_wizard.field3', False))
            if recs.key == 'search_product_wizard.field4' and recs.value:
                res['field4'] = int(self.env['ir.config_parameter'].get_param('search_product_wizard.field4', False))
            if recs.key == 'search_product_wizard.field5' and recs.value:
                res['field5'] = int(self.env['ir.config_parameter'].get_param('search_product_wizard.field5', False))
        return res

    @api.onchange('field2', 'field3', 'field4', 'field5')
    def onchange_field1(self):
        """
        This method filters the Product attributes as per its usage.
        Used Product attribues will not appear again.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.field2:
            domain.append(('id', '!=', self.field2.id))
        if self.field3:
            domain.append(('id', '!=', self.field3.id))
        if self.field4:
            domain.append(('id', '!=', self.field4.id))
        if self.field5:
            domain.append(('id', '!=', self.field5.id))
        return {'domain': {'field1': domain}}

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

    @api.onchange('fieldv1', 'fieldv2', 'fieldv3', 'fieldv4', 'fieldv5')
    def onchange_product_id(self):
        """
        This method is used to fetch all the products in the one to many
        field as per the selectin of ptoduct values.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.fieldv1:
            domain.append(('attribute_value_ids', '=', self.fieldv1.id))
        if self.fieldv2:
            domain.append(('attribute_value_ids', '=', self.fieldv2.id))
        if self.fieldv3:
            domain.append(('attribute_value_ids', '=', self.fieldv3.id))
        if self.fieldv4:
            domain.append(('attribute_value_ids', '=', self.fieldv4.id))
        if self.fieldv5:
            domain.append(('attribute_value_ids', '=', self.fieldv5.id))
        return {'domain': {'product_id': domain}}

    @api.multi
    @api.depends('fieldv1', 'fieldv2', 'fieldv3', 'fieldv4', 'fieldv5')
    def _compute_count_product(self):
        """
        This method is used to count to number of relevant products as per
        the selection of attributes and values.
        --------------------------------------------------------------------
        @self : object pointer
        """
        domain = []
        if self.fieldv1:
            domain.append(('attribute_value_ids', '=', self.fieldv1.id))
        if self.fieldv2:
            domain.append(('attribute_value_ids', '=', self.fieldv2.id))
        if self.fieldv3:
            domain.append(('attribute_value_ids', '=', self.fieldv3.id))
        if self.fieldv4:
            domain.append(('attribute_value_ids', '=', self.fieldv4.id))
        if self.fieldv5:
            domain.append(('attribute_value_ids', '=', self.fieldv5.id))
        self.count_product = self.env['product.product'].search_count(domain)
        if self.count_product == 1:
            self.product_id = self.env['product.product'].search(domain).id
        else:
            self.product_id = False


    @api.multi
    def get_product_list(self):
        """
        This method is used to get all the ist of products and update the
        list as per the change in product attributes or its values.
        --------------------------------------------------------------------
        @self : object pointer
        """
        result = []
        line_obj = self.env['show.product.lines']
        domain = []
        if self.fieldv1:
            domain.append(('attribute_value_ids', '=', self.fieldv1.id))
        if self.fieldv2:
            domain.append(('attribute_value_ids', '=', self.fieldv2.id))
        if self.fieldv3:
            domain.append(('attribute_value_ids', '=', self.fieldv3.id))
        if self.fieldv4:
            domain.append(('attribute_value_ids', '=', self.fieldv4.id))
        if self.fieldv5:
            domain.append(('attribute_value_ids', '=', self.fieldv5.id))
        get_products_ids = self.env['product.product'].search(domain)
        for product_line in get_products_ids:
            result.append(line_obj.create({'product_id': product_line.id,
                                   'location_id': product_line.location_id.id,
                                   'reg_product_id': self.id,
                                   'default_code': product_line.default_code
                                   }).id)
        self.show_product_lines_ids = [(6, 0, result)]
        if self.count_product == 1:
            self.product_id = self.env['product.product'].search(domain).id
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'search.product',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'new',
            }

    def get_products_in_report(self):
        """
        This method is called from Search Product Wizard to get all the 
        products in report.
        ----------------------------------------------------------------
        @self : object pointer
        """
        result = []
        line_obj = self.env['show.product.lines']
        domain = []
        if self.fieldv1:
            domain.append(('attribute_value_ids', '=', self.fieldv1.id))
        if self.fieldv2:
            domain.append(('attribute_value_ids', '=', self.fieldv2.id))
        if self.fieldv3:
            domain.append(('attribute_value_ids', '=', self.fieldv3.id))
        if self.fieldv4:
            domain.append(('attribute_value_ids', '=', self.fieldv4.id))
        if self.fieldv5:
            domain.append(('attribute_value_ids', '=', self.fieldv5.id))
        get_products_ids = self.env['product.product'].search(domain)
        for product_line in get_products_ids:
            result.append(line_obj.create({'product_id': product_line.id,
                                   'location_id': product_line.location_id.id,
                                   'reg_product_id': self.id,
                                   'default_code': product_line.default_code
                                   }).id)
        self.show_product_lines_ids = [(6, 0, result)]

        return self.show_product_lines_ids

    @api.multi
    def print_product_report(self):
        """
        This method is called when print button is pressed from Search
        Product Wizard.
        ----------------------------------------------------------------
        @self : object pointer
        """
        return self.env['report'].get_action(self, 'search_product_wizard.search_product_template')


class ShowProductLines(models.TransientModel):
    _name = 'show.product.lines'

    search_product_id = fields.Many2one('search.product', string='Searched Product')
    product_id = fields.Many2one('product.product', 'Product')
    default_code = fields.Char('Internal Reference')
