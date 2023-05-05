#!/usr/bin/python3
""" program that uses Decorators to check for collected reports """


def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap
@decor
def invoice(num):
    print("INVOICE #" + num)

print("Enter an invoice: ")
invoice(input())
