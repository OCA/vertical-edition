# -*- encoding: utf-8 -*-
#
# OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
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


class test_base_format(common.TransactionCase):
    def setUp(self):
        super(test_base_format, self).setUp()
        self.base_format_model = self.env['base.format']

    def test_fields(self):
        """ Test the setup of fields so they can't be changed easily. """
        columns = self.base_format_model._columns
        field_names = [
            'name', 'format_uom', 'width', 'height', 'comment', 'active'
        ]

        required_fields = ['name']

        for field_name in field_names:
            self.assertTrue(field_name in columns)
            if field_name in required_fields:
                self.assertTrue(columns[field_name].required)
