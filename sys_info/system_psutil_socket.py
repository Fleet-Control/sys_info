"""Get system information using psutil."""
import datetime
import socket

import psutil

from sys_info.model.system import System


def get_hostname():
    """Get Hostname from socket (low-level python internal lib)."""
    return socket.gethostname()


def get_uptime():
    """Get Uptime in seconds."""
    now = datetime.datetime.now()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    return (now - boot_time).seconds


def get_cpu_count():
    """Get number of CPU cores/threads."""
    return psutil.cpu_count()


def get_cpu_freq():
    """Get current, min and max CPU frequency."""
    freq = psutil.cpu_freq()
    return (freq.current, freq.min, freq.max)


def get_cpu_percent():
    """Get CPU utilization as percentage."""
    return psutil.cpu_percent()


def get_mem():
    """Get used and available memory."""
    mem = psutil.virtual_memory()
    return (mem.used, mem.available)


def get_disk_usage():
    """Get used and total disk space."""
    usage = psutil.disk_usage('/')
    return (usage.used, usage.total)


def system_from_psutil():
    """Create new System instance from psutil."""
    return System(
        hostname=get_hostname(),
        uptime=get_uptime(),
        cpu_count=get_cpu_count(),
        cpu_percent=get_cpu_percent(),
        cpu_freq=get_cpu_freq(),
        memory=get_mem(),
        disk_usage=get_disk_usage())


if __name__ == '__main__':
    print(system_from_psutil())
