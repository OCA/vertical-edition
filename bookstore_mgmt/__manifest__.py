# Copyright 2024 (APSL-Nagarro) - Miquel Alzanillas, Antoni Marroig
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Bookstore Management",
    "summary": """Bookstore management system for Odoo""",
    "author": "APSL-Nagarro, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-edition",
    "category": "Product",
    "license": "AGPL-3",
    "maintainers": ["peluko00", "miquelalzanillas"],
    "version": "17.0.3.0.0",
    "depends": ["product"],
    "data": [
        "security/bookstore_security.xml",
        "security/ir.model.access.csv",
        "views/product.xml",
        "views/bookstore_mgmt.xml",
    ],
}
