"""Summarise numeric columns in the Port Harcourt settlement data.

Run with:
    uv run summary.py
"""

from __future__ import annotations

import csv
from pathlib import Path

DEFAULT_INPUT = Path(__file__).with_name("port_harcourt_settlements.csv")
SUMMARY_COLUMNS = ("block_area_sqm", "building_count")


def read_rows(path: Path) -> list[dict[str, str]]:
    """Read CSV records by column name with DictReader."""
    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        required = {"block_id", *SUMMARY_COLUMNS}
        if not required.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain block_id, block_area_sqm, and building_count"
            )
        return list(reader)


def summarise_column(rows: list[dict[str, str]], column: str) -> dict[str, float | int]:
    """Return count, smallest, largest, and average for one numeric column."""
    values = []
    for row in rows:
        raw = row.get(column, "").strip()
        if raw:
            values.append(float(raw))
    if not values:
        return {"count": 0, "smallest": None, "largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values),
    }


def summarise_all(rows: list[dict[str, str]], columns: tuple[str, ...]) -> dict[str, dict[str, float | int]]:
    """Return a summary dictionary for every requested column."""
    return {column: summarise_column(rows, column) for column in columns}


# Run the refactored functions on the real Month 1 settlement data.
rows = read_rows(DEFAULT_INPUT)
summaries = summarise_all(rows, SUMMARY_COLUMNS)
print(f"File: {DEFAULT_INPUT.name}")
print(f"Rows read with DictReader: {len(rows)}")
for column, summary in summaries.items():
    print(
        f"{column}: count={summary['count']}, "
        f"smallest={summary['smallest']}, "
        f"largest={summary['largest']}, "
        f"average={summary['average']}"
    )
