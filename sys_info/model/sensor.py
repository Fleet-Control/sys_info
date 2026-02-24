"""Sensor information from the system."""
from dataclasses import dataclass


@dataclass
class Sensor:
    """Simple sensor providing current data for debugging."""

    # sensor name
    name: str

    # currently measured value
    value: float

    # type, e.g. temp or battery_percent
    sensor_type: str
