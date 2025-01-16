# Copyright 2024 (APSL-Nagarro) - Miquel Alzanillas, Antoni Marroig
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models


class Product(models.Model):
    _name = "product.product"
    _inherit = ["product.product", "google.books.mixin"]
