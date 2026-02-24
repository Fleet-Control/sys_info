from sys_info.model.sensor import Sensor

import psutil


def get_temp_psutil():
    temperatures = psutil.sensors_temperatures(fahrenheit=False)
    sensors = []
    for name in temperatures:
        for temp in temperatures[name]:
            label = name
            if temp.label:
                label = f'{name}.{temp.label}'
            sensor = Sensor(
                name=label, value=temp.current, sensor_type='temp')
            sensors.append(sensor)
    return sensors


def get_max_coretemp_psutil():
    """Get main temperature sensor."""
    temperatures = psutil.sensors_temperatures(fahrenheit=False)
    for name in temperatures:
        if name == 'coretemp':
            return max([t.current for t in temperatures[name]])
    return None


def get_battery():
    return Sensor(
        name='battery',
        value=psutil.sensors_battery().percent,
        sensor_type='battery_percent')


def sensors_from_psutil():
    sensors = [get_battery()]
    sensors += get_temp_psutil()
    return sensors


if __name__ == '__main__':
    for sensor in sensors_from_psutil():
        print(sensor.name, sensor.value, sensor.sensor_type)


# TODO: sensors_fans
