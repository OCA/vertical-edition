# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
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
    'name': 'Base Format',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Others',
    'summary': 'This module allows to manage dimensions.',
    'description': """
Base Format
===========
This module allows to manage dimensions.
Specifics features for Book Industry : certain format of book (lxL) by country, perhaps usable for other activity.

Contributors
------------

* Jordi Riera (jordi.riera@savoirfairelinux.com)
* Mathieu BENOIT (mathieu.benoit@savoirfairelinux.com)
* William BEVERLY (william.beverly@savoirfairelinux.com)
* Bruno JOLIVEAU (bruno.joliveau@savoirfairelinux.com)

More informations
-----------------

Module developped and tested with Odoo version 8.0
For questions, please contact our support services (support@savoirfairelinux.com)

""",
    'depends': [
        'base',
        'product',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'base_format_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
}
