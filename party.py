# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from decimal import Decimal

from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    @classmethod
    def get_credit_amount(cls, parties, name):
        pool = Pool()
        Currency = pool.get('currency.currency')
        Sale = pool.get('sale.sale')
        Uom = pool.get('product.uom')
        User = pool.get('res.user')

        amounts = super(Party, cls).get_credit_amount(parties, name)

        user = User(Transaction().user)
        if not user.company:
            return amounts
        currency = user.company.currency

        sales = Sale.search([
                ('party', 'in', [p.id for p in parties]),
                ('state', 'in', ['confirmed', 'processing']),
                ])

        for sale in sales:
            amount = 0
            if (sale.sale_credit_limit_amount and
                    sale.sale_credit_limit_amount == 'total_amount'):
                for line in sale.lines:
                    if line.type != 'line':
                        continue
                    quantity = line.credit_limit_quantity
                    if not quantity:
                        continue
                    for invoice_line in line.invoice_lines:
                        if invoice_line.type != 'line':
                            continue
                        invoice = invoice_line.invoice
                        if invoice and invoice.move:
                            quantity -= Uom.compute_qty(
                                invoice_line.unit, invoice_line.quantity,
                                line.unit, round=False)

                    if quantity > 0:
                        # Apply only when quantity > 0 for consistency with what
                        # sale_credit_limit module does
                        for tax in line.taxes:
                            if not line.unit_price or not tax.rate:
                                continue
                            amount += Currency.compute(
                                sale.currency,
                                Decimal(str(quantity)) * line.unit_price, currency,
                                round=False) * tax.rate

            amounts[sale.party.id] = currency.round(
                    amounts[sale.party.id] + amount)
        return amounts
