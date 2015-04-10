# -*- encoding: utf-8 -*-
#
# OpenERP, Open Source Management Solution
# This module copyright (C) 2013 Savoir-faire Linux
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

import logging
from openerp import models

_logger = logging.getLogger(__name__)


class product_template(models.Model):
    _inherit = 'product.template'

    @staticmethod
    def calculate_book_weight(page_height=0, page_width=0, page_weight=0,
                              page_count=0, cover_weight=0):
        """Calculate the weight of a book.
        :param page_height: meter
        :param page_width: meter
        :param page_weight: kilogram
        :param page_count: number of pages
        :param cover_weight: kilogram
        :return: Float, Book weight (kg)
        """
        one_page_weight = page_height * page_width * page_weight
        return one_page_weight * page_count / 2 + cover_weight
