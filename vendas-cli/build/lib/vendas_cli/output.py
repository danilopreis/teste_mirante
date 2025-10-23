from __future__ import annotations
import json
from typing import Dict, Optional
from vendas_cli.core import Sale

def format_text(totals: Dict[str, float], total_all: float, best: Optional[tuple]) -> str:
    lines = ["Relatório de Vendas", "Produto | Valor", "----------------"]
    for prod, val in totals.items():
        lines.append(f"{prod}: {val:.2f}")
    lines.append(f"Valor total: {total_all:.2f}")
    if best:
        lines.append(f"Produto mais vendido: {best[0]} ({best[1]})")
    return "\n".join(lines)

def format_json(totals: Dict[str, float], total_all: float, best: Optional[tuple]) -> str:
    payload = {
        "totals": totals,
        "total_all": total_all,
        "best_selling": {"product": best[0], "quantity": best[1]} if best else None,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)
