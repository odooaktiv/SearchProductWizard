# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        """
        This method is used to get the product attribute values as per the
        top attribute selection.
        --------------------------------------------------------------------
        @self : object pointer
        """
        fieldv1 = self.browse([self._context.get('fieldv1')])
        fieldv2 = self.browse([self._context.get('fieldv2')])
        fieldv3 = self.browse([self._context.get('fieldv3')])
        fieldv4 = self.browse([self._context.get('fieldv4')])
        fieldv5 = self.browse([self._context.get('fieldv5')])
        state = self._context.get('state')
        domain = []
        attribute_list = []
        final_attribute_list = []
        attribute_vlaue = self.search(args)

        if state:
            for field in [fieldv1, fieldv2, fieldv3, fieldv4, fieldv5]:
                if field.id:
                    attribute_list.append(field)
            if attribute_list:
                for value in attribute_vlaue:
                    flag = False
                    for attr_lst in attribute_list:
                        count = 0
                        attr_list = [attr.id for attr in attribute_list]
                        attr_list.append(value.id)
                        for product in attr_lst.product_ids:
                            if bool(set(attr_list).intersection
                                    (product.attribute_value_ids.ids)):
                                sorted_list = list(set(attr_list) & set(
                                    product.attribute_value_ids.ids))
                                if len(attr_list) == len(sorted_list):
                                    count += 1

                        if count > 0:
                            flag = True
                    if flag:
                        final_attribute_list.append(value.id)

            if attribute_list:
                domain.append(('id', 'in', final_attribute_list))

            recs = self.search(domain + args, limit=limit)

            return recs.name_get()
        else:
            return super(ProductAttributeValue, self)\
                .name_search(name=name, args=args,
                             operator=operator, limit=limit)
