# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # Zapisz atrybuty name, price, quantity
        if price < 0 or quantity < 0:
            raise ValueError('Price and Quantity cannot be lower than 0')

        self.name = name
        self.price = price
        self.quantity = quantity
        

    def add_stock(self, amount: int):
        # Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount >= 0:
            self.quantity += amount
        else:
            raise ValueError('Amount cannot be lower than 0')

    def remove_stock(self, amount: int):
        # Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if (amount < 0) or (amount > self.quantity):
            raise ValueError('Incorrect value to remove')
        else:
            self.quantity -= amount

    def is_available(self) -> bool:
        # Zwroc True jesli quantity > 0
        return self.quantity > 0

    def total_value(self) -> float:
        # Zwroc price * quantity
        return self.price * self.quantity
    
    def apply_discount(self, percent: float):
    #Obniza cene o podany procent (0-100)
        if percent < 0 or percent > 100:
            raise(ValueError)
        if percent == 0:
            pass
        elif percent == 100:
            self.price = 0
        else:
            self.price = round(percent * 0.01 * self.price, 2)
