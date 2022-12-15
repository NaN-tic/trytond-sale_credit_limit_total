# This file is part sale_credit_limit_total module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import party
from . import sale

def register():
    Pool.register(
        party.Party,
        sale.Configuration,
        sale.ConfigurationCompanyCreditLimitAmount,
        sale.Sale,
        module='sale_credit_limit_total', type_='model')
