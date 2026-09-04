import csv
import math


class Point:
    """
    Represents a spatial point feature with identity, coordinates, 
    and optional attributes.
    """

    def __init__(self, id, lon, lat, name=None, tag=None):
        # Enforce spatial validity (Section B.3)
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")

        self.id = str(id)
        self.lon = float(lon)
        self.lat = float(lat)
        self.name = name
        self.tag = tag

    def to_tuple(self) -> tuple[float, float]:
        """Return the coordinate as a (lon, lat) tuple."""
        return (self.lon, self.lat)

    def distance_to(self, other) -> float:
        """Calculates distance to another Point in meters using Haversine formula."""
        return self.haversine_m(self.lon, self.lat, other.lon, other.lat)

    @staticmethod
    def haversine_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
        """Pure spatial math function to compute spherical distance in meters."""
        R = 6371000.0  # Earth's mean radius in meters

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = (
            math.sin(dphi / 2) ** 2
            + math.cos(phi1) 
            * math.cos(phi2) 
            * math.sin(dlambda / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    @classmethod
    def from_row(cls, row: dict):
        """Constructs a Point instance from a dictionary row."""
        return cls(
            id=str(row["id"]),
            lon=float(row["lon"]),
            lat=float(row["lat"]),
            name=row.get("name"),
            tag=row.get("tag"),
        )

    def is_poi(self) -> bool:
        """Determines if the point is tagged as a Point of Interest (POI)."""
        return (self.tag or "").lower() == "poi"


class PointSet:
    """
    Represents a spatial collection of Point objects and provides set-level operations.
    """

    def __init__(self, points=None):
        self.points = points if points is not None else []

    @classmethod
    def from_csv(cls, path: str):
        """Constructs a PointSet by reading a CSV file containing point data."""
        points = []
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    points.append(Point.from_row(row))
                except (ValueError, KeyError):
                    continue
        return cls(points)

    def count(self) -> int:
        """Returns the total number of points in the collection."""
        return len(self.points)

    def bbox(self) -> tuple[float, float, float, float]:
        """
        Computes the bounding box of all points in the set.
        Returns: (min_lon, min_lat, max_lon, max_lat)
        """
        if not self.points:
            return (0.0, 0.0, 0.0, 0.0)

        lons = [p.lon for p in self.points]
        lats = [p.lat for p in self.points]

        return (min(lons), min(lats), max(lons), max(lats))

    def filter_by_tag(self, tag: str):
        """Returns a new PointSet containing only points matching the given tag."""
        target_tag = tag.lower()
        matching_points = [
            p for p in self.points if (p.tag or "").lower() == target_tag
        ]
        return PointSet(matching_points)