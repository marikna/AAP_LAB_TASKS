# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancje Product do testow."""
        # Stworz instancje Product, np. Product("Laptop", 2999.99, 10)
        self.product = Product('Laptop', 3999.99, 2)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        """Sprawdz, czy dodanie towaru zwieksza quantity."""
        # Wywolaj add_stock i sprawdz nowa wartosc quantity
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 7)

    def test_add_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        # Uzyj self.assertRaises(ValueError) i wywolaj add_stock z ujemna wartoscia
        with self.assertRaises(ValueError):
            self.product.add_stock(-2)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
        # Wywolaj remove_stock i sprawdz nowa wartosc quantity
        self.product.remove_stock(1)
        self.assertEqual(self.product.quantity, 1)

    def test_remove_stock_too_much_raises(self):
        """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""
        # Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.remove_stock(3)

    def test_remove_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        # Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.remove_stock(-1)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        """Sprawdz, czy produkt z quantity > 0 jest dostepny."""
        # Uzyj self.assertTrue
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""
        # Stworz produkt z quantity=0 i uzyj self.assertFalse
        self.product.remove_stock(2)
        self.assertFalse(self.product.is_available())

    # --- Testy total_value ---

    def test_total_value(self):
        """Sprawdz, czy total_value zwraca price * quantity."""
        # Uzyj self.assertEqual
        self.assertEqual(self.product.total_value(), 7999.98)


if __name__ == "__main__":
    unittest.main()
