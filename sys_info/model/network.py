"""Provide network information."""
from dataclasses import dataclass


@dataclass
class Network:
    """Provide information about a known network."""

    # Currently active SSID
    current_ssid: str

    # the default wifi strength
    wifi_strength: float

    # main ipv4 address of wifi
    wifi_ipv4: str

    # list of available connection names
    connections: list

    # true if a connection exists (or configured as AP)
    connected: bool = False
