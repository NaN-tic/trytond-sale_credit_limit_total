# This file is part sale_credit_limit_total module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.tests.test_tryton import ModuleTestCase
from trytond.modules.company.tests import CompanyTestMixin


class SaleCreditLimitTotalTestCase(CompanyTestMixin, ModuleTestCase):
    'Test Sale Credit Limit Total module'
    module = 'sale_credit_limit_total'

del ModuleTestCase
