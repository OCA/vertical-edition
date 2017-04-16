# -*- encoding: utf-8 -*-
# #############################################################################
#
# OpenERP, Open Source Management Solution
# This module copyright (C) 2014 Savoir-faire Linux
# (<http://www.savoirfairelinux.com>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

import logging
from openerp.osv import fields, orm
from openerp import api
from openerp import tools
import ast

_logger = logging.getLogger(__name__)


class publication_management(orm.Model):
    """
    Publication Management table
    """
    _name = 'publication.management'
    _description = 'Publication Management'

    def create(self, cr, uid, vals, context=None):
        vals['name'] = self.pool.get('ir.sequence').get(
            cr, uid, 'seq.publication.management'
        )
        return super(publication_management, self).create(
            cr, uid, vals, context
        )

    @api.multi
    def _get_image(self, name, args):
        return dict(
            (p.id, tools.image_get_resized_images(p.image)) for p in self)

    @api.one
    def _set_image(self, name, value, args):
        return self.write({'image': tools.image_resize_image_big(value)})

    _store_image = {'publication.management': (
        lambda self, cr, uid, ids, c={}: ids, ['image'], 10
    ),
    }

    _columns = {
        'partner_id': fields.many2one('res.partner', string='Partner'),
        'title': fields.char('Title', size=128, required=True,
                             translate=False),
        'name': fields.text('Description', required=True, readonly=True),
        'image': fields.binary(
            'Image',
            help="This field holds the image used as avatar for this contact,"
                 "limited to 1024x1024px"
        ),
        'image_medium': fields.function(
            _get_image,
            fnct_inv=_set_image,
            string="Medium-sized photo",
            type="binary", multi="_get_image",
            store=_store_image,
            help="Medium-sized image of this publication. It is automatically "
                 "resized as a 128x128px image, with aspect ratio preserved. "
                 "Use this field in form views or some kanban views.."
        ),
        'author': fields.char('Author', size=128, required=True,
                              translate=False),
        'genre': fields.many2many('publication.genre', id1='publication_id',
                                  id2='publication_genre_id',
                                  string='Genre'),
        'category': fields.many2many('publication.category',
                                     id1='publication_id',
                                     id2='publication_category_id',
                                     string='Category'),
    }

    _defaults = {
        'partner_id': lambda self, *a, **kw: self._get_parent_id(
            *a, **kw
        ),
    }

    def _get_parent_id(self, cr, uid, ids, context=None):
        """Return the parent_id"""
        user = self.pool.get('res.users').browse(
            cr, uid, uid, context=context
        )
        return user.partner_id.parent_id.id


    @api.multi
    def action_view_versions(self):
        act_obj = self.pool.get('ir.actions.act_window')
        mod_obj = self.pool.get('ir.model.data')
        context = self._context
        result = mod_obj.xmlid_to_res_id(self._cr, self._uid,
                                         'product.product_template_action',
                                         raise_if_not_found=True)
        result = act_obj.read(self._cr, self._uid, result, context=context)
        prod_tmpl_ids = [prod.id for prod in self.version]
        map_ids = ','.join(map(str, prod_tmpl_ids))
        result['domain'] = "[('id','in',[%s])]" % map_ids
        return result


class publication_genre(orm.Model):
    """
    Genre of product
    """
    _name = 'publication.genre'
    _description = "Genre of publication"

    _columns = {
        'name': fields.char('Name', size=128, required=True),
        'partner_id': fields.many2one('res.partner', string='Partner'),
    }

    def create(self, cr, uid, vals, context=None):
        # Adding a condition here or even if a PM is created with a
        # partner_id in the context, the partner_id will be the one from
        # the user.
        if not vals.get('partner_id'):
            user = self.pool.get('res.users').browse(cr, uid, uid)
            vals['partner_id'] = user.partner_id.parent_id.id
        return super(publication_genre, self).create(
            cr, uid, vals, context
        )


class publication_category(orm.Model):
    """
    Category of product
    """
    _name = 'publication.category'
    _description = "Category of publication"

    _columns = {
        'name': fields.char('Name', size=128, required=True),
        'partner_id': fields.many2one('res.partner', string='Partner'),
    }

    def create(self, cr, uid, vals, context=None):
        # Adding a condition here or even if a PM is created with a
        # partner_id in the context, the partner_id will be the one from
        # the user.
        if not vals.get('partner_id'):
            user = self.pool.get('res.users').browse(cr, uid, uid)
            vals['partner_id'] = user.partner_id.parent_id.id
        return super(publication_category, self).create(
            cr, uid, vals, context
        )
