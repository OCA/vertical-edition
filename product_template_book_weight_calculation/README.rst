Product Template Book Weight Calculation
========================================

Implementation of the maths to calculate the weight of a book.

The maths for the calculation are following:

a(x/2) + b

where:
* a = Weight of one page of the book (Height (m) * Width (m) *
Weight of the paper (kg))
* b = Number of pages of the book
* c = Weight of the cover

Installation
============

No special step to install the module.

Configuration
=============

No special step to configure the module.

Usage
=====

The module implements a simple method to calculate the weight
of a book. To use it, call *calculate_book_weight* from a *product.template*
record with *page_height*, *page_width*, *page_weight*, *page_count* and
*cover_weight* as parameters.

For further information, please visit:

 * https://www.odoo.com/forum/help-1

More information
----------------

Module developed and tested with Odoo version 8.0.
For questions, please contact our support services
<support@savoirfairelinux.com>


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/vertical-edition/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/vertical-edition/issues/new?body=module:%20product_template_book_weight_calculation%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Jordi RIERA <jordi.riera@savoirfairelinux.com>
* Bruno JOLIVEAU <bruno.joliveau@savoirfairelinux.com>
* Guillaume AUGER <guillaume.auger@savoirfairelinux.com>


Maintainer
----------

.. image:: http://odoo-community.org/logo.png
:alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
