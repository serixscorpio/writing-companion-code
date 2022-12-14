"""client2."""
import api


def offset(amount):
    result = api.expensive_calculation()  # function looked up in module api
    return result + amount
