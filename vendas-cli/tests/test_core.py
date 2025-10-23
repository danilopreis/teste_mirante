from datetime import datetime
from vendas_cli.core import Sale, total_by_product, total_all_sales, best_selling_product

def make_sales():
    return [
        Sale("A", 10, 2, datetime(2025, 1, 1)),
        Sale("B", 5, 5, datetime(2025, 1, 2)),
        Sale("A", 10, 1, datetime(2025, 1, 3)),
    ]

def test_total_by_product():
    t = total_by_product(make_sales())
    assert t["A"] == 30
    assert t["B"] == 25

def test_total_all_sales():
    assert total_all_sales(make_sales()) == 55

def test_best_selling_product():
    assert best_selling_product(make_sales()) == ("B", 5)
