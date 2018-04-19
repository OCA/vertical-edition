import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-vertical-edition",
    description="Meta package for oca-vertical-edition Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-product_template_book_weight_calculation',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
