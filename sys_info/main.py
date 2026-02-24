from sys_info.system_psutil_socket import system_from_psutil
from sys_info.sensors_psutil import sensors_from_psutil


def get_system():
    system = system_from_psutil()
    return system


if __name__ == '__main__':
    print('System')
    print(get_system())
    print('Networks')
    # TODO!
    # Get network info, update network info periodically
    print('Sensors')
    sensors = sensors_from_psutil()
    print(sensors)

    # for camera streams take a look at
    # https://github.com/brean/video_stream_data
    # and its connected streaming solutions at DFKI gitlab
