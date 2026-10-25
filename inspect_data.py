"""Summarise two numeric columns from the settlement CSV.

Usage:
    uv run inspect_data.py
    uv run inspect_data.py port_harcourt_settlements.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

DEFAULT_INPUT = Path(__file__).with_name("port_harcourt_settlements.csv")
SUMMARY_COLUMNS = ("block_area_sqm", "building_count")


def summarise_column(values: list[float]) -> dict[str, float | int]:
    """Return a summary dictionary for one numeric column."""
    if not values:
        return {"count": 0, "minimum": None, "maximum": None, "mean": None}
    return {
        "count": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "mean": sum(values) / len(values),
    }


def inspect_data(path: Path) -> dict[str, dict[str, float | int]]:
    """Read the CSV and return summaries for the two settlement columns."""
    columns = {name: [] for name in SUMMARY_COLUMNS}
    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        required = {"block_id", *SUMMARY_COLUMNS}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain block_id, block_area_sqm, and building_count"
            )
        for row in reader:
            for column in SUMMARY_COLUMNS:
                raw = row[column].strip()
                if raw == "":
                    continue
                columns[column].append(float(raw))
    return {column: summarise_column(values) for column, values in columns.items()}


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    summaries = inspect_data(path)
    print(f"File: {path.name}")
    print(f"Rows read with DictReader: {sum(item['count'] for item in summaries.values()) // len(SUMMARY_COLUMNS)}")
    for column, summary in summaries.items():
        print(f"{column}: {summary}")


if __name__ == "__main__":
    main()
