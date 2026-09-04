from spatial import Point, PointSet


def main():
    print("=== GmE 205 Lab 2 Demonstration ===\n")

    p1 = Point("A", 121.0, 14.6, name="Manila", tag="poi")
    print("1. Basic Point Initialization:")
    print(f"   ID: {p1.id}, Lon: {p1.lon}, Lat: {p1.lat}")
    print(f"   Tuple representation: {p1.to_tuple()}\n")

    p2 = Point("B", 120.9842, 14.5995, name="Manila Center", tag="city")
    print("2. Spatial Distance Calculation:")
    print(f"   Is Point 1 a POI? {p1.is_poi()}")
    print(f"   Is Point 2 a POI? {p2.is_poi()}")
    print(f"   Distance between {p1.id} and {p2.id}: {p1.distance_to(p2):.2f} meters\n")

    sample_row = {"id": "C", "lon": 121.5, "lat": 14.2, "name": "Test Site", "tag": "poi"}
    p_from_dict = Point.from_row(sample_row)
    print("3. Constructed Point from Dictionary Row:")
    print(f"   ID: {p_from_dict.id}, Tuple: {p_from_dict.to_tuple()}, Tag: {p_from_dict.tag}\n")

    csv_path = "data/points.csv"
    print(f"4. Testing PointSet from CSV ('{csv_path}'):")
    
    try:
        pset = PointSet.from_csv(csv_path)

        print(f"   Total Point Count: {pset.count()}")
        print(f"   Bounding Box (min_lon, min_lat, max_lon, max_lat): {pset.bbox()}")

        # Filter by tag
        filtered_pset = pset.filter_by_tag("poi")
        print(f"   Filtered Points Count (tag='poi'): {filtered_pset.count()}")

    except FileNotFoundError:
        print(f"   [Warning] File '{csv_path}' not found. Ensure points.csv exists in the data/ folder.")


if __name__ == "__main__":
    main()