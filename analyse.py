"""Classify Ibadan wards as large or small by area.

Usage:
    python analyse.py
    python analyse.py wards.csv

A ward is classified as large when its area is at least 10 km².
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

LARGE_THRESHOLD_KM2 = 10.0
DEFAULT_INPUT = Path(__file__).with_name("wards.csv")


def classify_ward(area_km2: float) -> str:
    """Return the size label for one ward area."""
    return "large" if area_km2 >= LARGE_THRESHOLD_KM2 else "small"


def analyse_file(path: Path) -> list[dict[str, str | float]]:
    """Read a CSV file and return classified ward records."""
    results: list[dict[str, str | float]] = []
    with path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        required_columns = {"ward", "area_km2"}
        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError("CSV must contain the columns: ward, area_km2")

        for row_number, row in enumerate(reader, start=2):
            try:
                area = float(row["area_km2"])
            except (TypeError, ValueError) as error:
                raise ValueError(f"Invalid area on CSV row {row_number}") from error
            if area < 0:
                raise ValueError(f"Area cannot be negative on CSV row {row_number}")
            results.append(
                {
                    "ward": row["ward"].strip(),
                    "area_km2": area,
                    "classification": classify_ward(area),
                }
            )
    return results


def main() -> None:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    results = analyse_file(input_path)
    print(f"Analysed {len(results)} wards")
    print(f"Large threshold: {LARGE_THRESHOLD_KM2:.1f} km²")
    print("\n" + f"{'Ward':<24}{'Area (km²)':>12}  Classification")
    print("-" * 52)
    for result in results:
        print(
            f"{str(result['ward']):<24}{float(result['area_km2']):>12.1f}"
            f"  {result['classification']}"
        )


if __name__ == "__main__":
    main()
