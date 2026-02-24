"""Get wireless information from /etc/proc/wireless."""
import re
from pathlib import Path


def get_wifi_strength():
    """Get Wifi Strength from /proc/net/wireless."""
    # this only works on ubuntu
    if not Path('/proc/net/wireless').exists():
        return float(0.0)
    with open('/proc/net/wireless', 'r', encoding='utf-8') as fd:
        text = fd.read()
        text = text.split('\n')
        if len(text[2]) < 1:
            return -1
        first_line = re.sub(r'[\s\|]{2,}', ' ', text[1]).split(' ')
        sec_line = re.sub(r'[\s\|]{2,}', ' ', text[2]).split(' ')
        index = first_line.index('link')
        wifi_strength = sec_line[index]
        return float(wifi_strength)


if __name__ == '__main__':
    print(get_wifi_strength())
