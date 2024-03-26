'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net1 = Decimal('0')
    net2 = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            if item.amount >=-100000 and item.amount <=100000:
                net1 += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and item.quantity > 0 and item.quantity <=100 and item.amount > 0 and item.amount <=100000:
                net2 += Decimal(str(item.amount * item.quantity))
        else:
            return "Invalid item type: %s" % item.type

    if net1 > 1000000 or net2 > 1000000:
        return "Total amount payable for an order exceeded"

    if net1 != net2:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net1-net2)
    else:
        return "Order ID: %s - Full payment received!" % order.id