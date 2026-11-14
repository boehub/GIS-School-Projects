#!/usr/bin/env python3
"""Clean latitude/longitude columns in a point CSV before importing it into a GIS.

Fixes problems that make web-GIS CSV imports silently drop or misplace points:
  * non-breaking spaces and stray whitespace inside coordinate values
  * a "lat, long" pair stored in a single cell
  * a UTF-8 byte-order mark on the header row
Rows that still cannot be parsed, or that fall outside valid ranges, are reported.

Usage:
    python3 clean_csv_coordinates.py input.csv output.csv [--lat lat] [--lon long]
"""
import argparse
import csv
import re
import sys

NUM = re.compile(r"-?\d+(?:\.\d+)?")


def clean(text):
    return (text or "").replace(" ", " ").strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--lat", default="lat", help="latitude column name (default: lat)")
    ap.add_argument("--lon", default="long", help="longitude column name (default: long)")
    a = ap.parse_args()

    with open(a.src, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    for col in (a.lat, a.lon):
        if col not in fields:
            sys.exit(f"Column '{col}' not found. Columns: {fields}")

    fixed, bad = 0, []
    for i, row in enumerate(rows, start=2):  # start=2: header is line 1
        before = (row[a.lat], row[a.lon])
        lat_t, lon_t = clean(row[a.lat]), clean(row[a.lon])
        if lat_t and not lon_t:                      # "37.39, -121.97" stored in one cell
            parts = NUM.findall(lat_t)
            if len(parts) == 2:
                lat_t, lon_t = parts
        nums = (NUM.fullmatch(lat_t), NUM.fullmatch(lon_t))
        if not all(nums) or not (-90 <= float(lat_t) <= 90 and -180 <= float(lon_t) <= 180):
            bad.append((i, before))
            continue
        row[a.lat], row[a.lon] = lat_t, lon_t
        if (lat_t, lon_t) != before:
            fixed += 1

    with open(a.dst, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} rows read, {fixed} coordinate pairs repaired, {len(bad)} unusable")
    for line, vals in bad:
        print(f"  line {line}: {vals!r}")


if __name__ == "__main__":
    main()
