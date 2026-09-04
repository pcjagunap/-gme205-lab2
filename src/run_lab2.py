import json
import os
import matplotlib.pyplot as plt
from spatial import PointSet


def main():
    # 1. Ensure the output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    csv_path = "data/points.csv"
    print(f"Loading data from '{csv_path}'...")

    # Load data using PointSet
    pset = PointSet.from_csv(csv_path)

    # 2. Extract Data for Plotting
    lons = [p.lon for p in pset.points]
    lats = [p.lat for p in pset.points]
    tags = [p.tag for p in pset.points]

    # Create Scatter Plot
    plt.figure(figsize=(8, 6))
    
    # Optional styling: color points based on whether they are POIs
    for p in pset.points:
        color = "red" if p.is_poi() else "blue"
        plt.scatter(p.lon, p.lat, c=color, edgecolors="k", alpha=0.7)
        plt.annotate(p.name or p.id, (p.lon, p.lat), textcoords="offset points", xytext=(5, 5), ha="left")

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("GmE 205 Lab 2 - Spatial Objects Preview")
    plt.grid(True, linestyle="--", alpha=0.5)

    # Save plot to output/lab2_preview.png
    plot_path = os.path.join(output_dir, "lab2_preview.png")
    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved visualization plot to '{plot_path}'")

    # 3. Compute Metrics for JSON Summary Report
    total_count = pset.count()
    bbox = pset.bbox()

    # Optional: Calculate tag counts
    tag_counts = {}
    for p in pset.points:
        tag_key = (p.tag or "untagged").lower()
        tag_counts[tag_key] = tag_counts.get(tag_key, 0) + 1

    report_data = {
        "total_point_count": total_count,
        "bounding_box": {
            "min_lon": bbox[0],
            "min_lat": bbox[1],
            "max_lon": bbox[2],
            "max_lat": bbox[3],
        },
        "counts_per_tag": tag_counts,
    }

    # Save JSON report to output/lab2_report.json
    json_path = os.path.join(output_dir, "lab2_report.json")
    with open(json_path, mode="w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)
    print(f"Saved summary report to '{json_path}'")


if __name__ == "__main__":
    main()