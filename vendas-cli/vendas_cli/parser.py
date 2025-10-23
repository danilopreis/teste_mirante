from __future__ import annotations
import argparse
from datetime import datetime
from typing import Optional, Tuple

DATE_FMT = "%Y-%m-%d"

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vendas-cli",
        description="Processa CSV de vendas e gera relatórios",
    )
    parser.add_argument("path", help="Caminho para o arquivo CSV de vendas")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--start", help=f"Data inicial (inclusive) formato {DATE_FMT}")
    parser.add_argument("--end", help=f"Data final (inclusive) formato {DATE_FMT}")
    return parser

def parse_dates(start: Optional[str], end: Optional[str]) -> Tuple[Optional[datetime], Optional[datetime]]:
    def _p(s: Optional[str]) -> Optional[datetime]:
        if s is None:
            return None
        return datetime.strptime(s, DATE_FMT)
    return _p(start), _p(end)
