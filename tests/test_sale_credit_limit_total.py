# This file is part of the sale_credit_limit_validation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.tests.test_tryton import doctest_teardown
from trytond.tests.test_tryton import doctest_checker
from trytond.pool import Pool
from trytond.exceptions import UserError


class SaleCreditLimitTotalTestCase(ModuleTestCase):
    'Test Sale Credit Limit Total module'
    module = 'sale_credit_limit_total'

del ModuleTestCase

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleCreditLimitTotalTestCase))
    suite.addTests(doctest.DocFileSuite(
            'scenario_sale_credit_limit_total.rst',
            tearDown=doctest_teardown, encoding='utf-8',
            checker=doctest_checker,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
