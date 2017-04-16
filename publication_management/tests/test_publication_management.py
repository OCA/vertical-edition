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


def test_fields(self):
    for field_name in self.field_names:
        self.assertTrue(field_name in self.columns)
        if field_name in self.required_fields:
            self.assertTrue(self.columns[field_name].required)


class test_publication_management(common.TransactionCase):
    def setUp(self):
        super(test_publication_management, self).setUp()
        self.publication_mgmt_model = self.env['publication.management']
        self.columns = self.publication_mgmt_model._columns
        self.field_names = [
            'title', 'name', 'image', 'image_medium', 'author', 'genre',
            'category'
        ]

        self.required_fields = [
            'title', 'name', 'author'
        ]

    test_fields = test_fields

    def test_create_set_sequence(self):
        """  Test if the name follow the sequence of the model
        """
        publication = self.publication_mgmt_model.create({
            'name': 'publication1',
            'title': 'title1',
            'author': 'author1',
        })
        self.assertRegexpMatches(
            publication.name, 'PM\d{3}'
        )


class test_publication_genre(common.TransactionCase):
    def setUp(self):
        super(test_publication_genre, self).setUp()
        self.publication_genre_model = self.env['publication.genre']
        self.columns = self.publication_genre_model._columns

        self.field_names = ['name']
        self.required_fields = ['name']

    test_fields = test_fields


class test_publication_category(common.TransactionCase):
    def setUp(self):
        super(test_publication_category, self).setUp()
        self.publication_category_model = self.env['publication.category']
        self.columns = self.publication_category_model._columns

        self.field_names = ['name']
        self.required_fields = ['name']

    test_fields = test_fields
