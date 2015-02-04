# -*- encoding: utf-8 -*-
#
# OpenERP, Open Source Management Solution
# This module copyright (C) 2013 Savoir-faire Linux
# (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openerp.tests import common


class test_product_template(common.TransactionCase):
    def setUp(self):
        super(test_product_template, self).setUp()
        self.product_template_model = self.env['product.template']

    def testCalculateBookWeight(self):
        """Test if the maths are right here."""
        product_template = self.product_template_model.create(
            {'name': 't_name'}
        )

        # more than one set of values is test to avoid to
        # have a special case that would fit the case by chance.

        weight = product_template.calculate_book_weight(
            page_height=0.2286,
            page_width=0.1524,
            page_weight=0.083,
            page_count=290,
            cover_weight=0.03,
        )
        self.assertAlmostEqual(weight, 0.449, places=3)

        weight = product_template.calculate_book_weight(
            page_height=0.2159,
            page_width=0.1397,
            page_weight=0.103,
            page_count=100,
            cover_weight=0.03,
        )
        self.assertAlmostEqual(weight, 0.185, places=3)

        weight = product_template.calculate_book_weight(
            page_height=0.2286,
            page_width=0.1524,
            page_weight=0.089,
            page_count=500,
            cover_weight=0.03,
        )
        self.assertAlmostEqual(weight, 0.805, places=3)
