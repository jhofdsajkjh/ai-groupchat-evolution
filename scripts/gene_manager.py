#!/usr/bin/env python3
"""基因库管理CLI"""
import json, sys, argparse
from pathlib import Path

GENE_BANK = Path(__file__).parent.parent / "gene_bank.json"

def load_bank():
    with open(GENE_BANK, "r", encoding="utf-8") as f:
        return json.load(f)

def cmd_list(bank, category=None):
    cats = [category] if category else ["function", "class", "import", "decorator"]
    for cat in cats:
        genes = bank["genes"].get(cat, [])
        print(f"\n[{cat.upper()}] ({len(genes)} genes)")
        for g in genes:
            print(f"  - {g.get("name", "unknown")} ({g.get("source", "")})")

def cmd_stats(bank):
    total = bank["stats"]["total"]
    last = bank["stats"].get("last_update", "never")
    print(f"Total genes: {total}")
    print(f"Last update: {last}")
    for cat, genes in bank["genes"].items():
        print(f"  {cat}: {len(genes)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="基因库管理")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--category", choices=["function", "class", "import", "decorator"])
    parser.add_argument("--stats", action="store_true")
    args = parser.parse_args()
    
    bank = load_bank()
    if args.list:
        cmd_list(bank, args.category)
    elif args.stats:
        cmd_stats(bank)
    else:
        parser.print_help()
