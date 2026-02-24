from sys_info.system_psutil_socket import system_from_psutil


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
    # TODO!
    # get all sensors, print out sensor values periodically
