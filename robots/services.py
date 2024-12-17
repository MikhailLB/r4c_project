from datetime import datetime

from robots.models import Robot
from robots.validators import robot_serializer


def create_robot(data):

    """Сервис для создания записи в БД """

    robot_serializer(data)

    created_datetime = datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
    serial = f"{data['model']}-{data['version']}"

    try:
        robot = Robot.objects.create(
            model=data['model'],
            version=data['version'],
            serial=serial,
            created=created_datetime
        )
    except Exception as e:
        raise ValueError(f"Не удалось создать объект: {str(e)}")

    return robot