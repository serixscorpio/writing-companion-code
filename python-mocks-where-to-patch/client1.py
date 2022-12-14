"""client"""
from api import expensive_calculation


def offset(amount):
    result = expensive_calculation()  # function looked up in module client1
    return result + amount
