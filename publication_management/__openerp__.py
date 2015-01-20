# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
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
##############################################################################

{
    'name': 'Publication Management',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Sale',
    'summary': '',
    'description': """
Publication Management
======================
This module adds a new menu entry, "publication (en), oeuvre (fr)".
It was created in order to regroup different versions (product.product) under
one same parent publication.
It also adds search and kanban views.

Contributors
------------

* Jordi Riera <jordi.riera@savoirfairelinux.com>
* Mathieu Benoit <mathieu.benoit@savoirfairelinux.com>
* William Beverly <william.beverly@savoirfairelinux.com>
* Bruno Joliveau <bruno.joliveau@savoirfairelinux.com>
* El Hadji Dem  <elhadji.dem@savoirfairelinux.com>

More information
-----------------
Module developed and tested with Odoo version 8.0
For questions, please contact our support services
(support@savoirfairelinux.com)
""",
    'depends': [
        'product',
        'sale',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'publication_management_view.xml',
        'publication_management_sequence.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/publication.category.csv',
        'demo/publication.genre.csv',
        'demo/publication_management.xml',
    ],
    'test': [],
    'installable': True,
}
