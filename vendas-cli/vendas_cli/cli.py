from __future__ import annotations
import sys
from vendas_cli.parser import build_arg_parser, parse_dates
from vendas_cli.core import read_sales, filter_by_date, total_by_product, total_all_sales, best_selling_product
from vendas_cli.output import format_text, format_json

def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    start, end = parse_dates(args.start, args.end)
    sales = filter_by_date(read_sales(args.path), start, end)
    totals = total_by_product(sales)
    total_all = total_all_sales(sales)
    best = best_selling_product(sales)
    out = format_json(totals, total_all, best) if args.format == "json" else format_text(totals, total_all, best)
    print(out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
