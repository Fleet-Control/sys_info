"""Get Network information from NetworkManager."""
try:
    import gi
    gi.require_version('NM', '1.0')
    from gi.repository import NM
    nmc = NM.Client.new(None)
    devs = nmc.get_devices()
    NETWORK_MANAGER = True
except ImportError:
    NETWORK_MANAGER = False
except ValueError:
    NETWORK_MANAGER = False


def get_wifi_strength():
    """Get Wifi strength from first found Wifi device."""
    global devs
    for device in devs:
        if device.get_device_type() != NM.DeviceType.WIFI:
            continue
        for ap in device.get_access_points():
            return float(ap.get_strength())
    return 0.0


if __name__ == '__main__':
    print(get_wifi_strength())
