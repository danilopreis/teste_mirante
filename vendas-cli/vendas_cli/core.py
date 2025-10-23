from __future__ import annotations
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable, List, Optional, Tuple


@dataclass
class Sale:
    product: str
    price: float
    quantity: int
    date: Optional[datetime] = None  # agora é opcional


def read_sales(path: str) -> List[Sale]:
    sales: List[Sale] = []

    with open(path, newline="", encoding="cp1252") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            try:
                product = (
                    row.get("product")
                    or row.get("Produto")
                    or row.get("produto")
                )
                price = float(
                    row.get("price")
                    or row.get("preco_unitario")
                    or row.get("valor")
                    or 0
                )
                quantity = int(float(row.get("quantity") or row.get("quantidade") or 1))

                # A coluna de data é opcional
                date = None
                date_str = row.get("date") or row.get("data")
                if date_str and isinstance(date_str, str) and date_str.strip():
                    # tenta identificar formato da data
                    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
                        try:
                            date = datetime.strptime(date_str.strip(), fmt)
                            break
                        except ValueError:
                            continue

                sales.append(Sale(product, price, quantity, date))
            except Exception as e:
                print(f"Linha ignorada: {row} — Erro: {e}")

    return sales


def filter_by_date(sales: Iterable[Sale], start: Optional[datetime], end: Optional[datetime]) -> List[Sale]:
    # Se nenhuma venda tiver data, retorna todas
    if all(s.date is None for s in sales):
        return list(sales)

    result = []
    for s in sales:
        if s.date is None:
            continue
        if start and s.date < start:
            continue
        if end and s.date > end:
            continue
        result.append(s)
    return result


def total_by_product(sales: Iterable[Sale]) -> Dict[str, float]:
    totals: Dict[str, float] = defaultdict(float)
    for s in sales:
        totals[s.product] += s.price * s.quantity
    return dict(totals)


def total_all_sales(sales: Iterable[Sale]) -> float:
    return sum(s.price * s.quantity for s in sales)


def best_selling_product(sales: Iterable[Sale]) -> Optional[Tuple[str, int]]:
    qtys: Dict[str, int] = defaultdict(int)
    for s in sales:
        qtys[s.product] += s.quantity
    if not qtys:
        return None
    return max(qtys.items(), key=lambda kv: kv[1])
