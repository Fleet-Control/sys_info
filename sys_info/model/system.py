"""Provide system information."""
from dataclasses import dataclass


@dataclass
class System:
    """Provide general system information."""

    hostname: str

    # uptime in seconds
    uptime: int

    # number of CPU cores/threads
    cpu_count: int

    # current, min and max CPU frequency
    cpu_freq: list[float]

    # CPU utilization
    cpu_percent: float

    # used memory used and available
    memory: list[float]

    # get used and total disk space
    disk_usage: list[float]
