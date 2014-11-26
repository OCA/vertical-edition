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

_logger = logging.getLogger(__name__)
logging.basicConfig()
_logger.setLevel(logging.DEBUG)

from openerp.osv import fields, orm
from openerp.tools.translate import _


class base_format(orm.Model):
    """ This model stores dimensions."""
    _name = "base.format"
    _description = "This model stores dimensions."

    _columns = {
        'name': fields.char('Name', required=True, translate=True, select=True,
                            size=64),
        'format_uom': fields.many2one('product.uom', string='Format UoM'),
        "width": fields.float('Width'),
        "height": fields.float('Height'),
        "comment": fields.text('Comment'),
        "active": fields.boolean('Active'),
    }

    _sql_constraints = [
        ("name_unique", "unique(name)",
         _("Can't be duplicate value for the field 'Name'!")),
    ]

    _defaults = {
        'active': True,
    }
