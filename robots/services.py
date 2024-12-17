from datetime import datetime, timedelta
from django.db.models import Count

from robots.models import Robot
from robots.serializers import robot_serializer


def create_robot(data):

    """Сервис для создания записи в БД """

    robot_serializer(data)

# Очевидно, можно было сделать автоматическое добавление даты через настройки поля в модели, но в задании дату передают мануально
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


def get_weekly_data():

    """Возвращает агрегированные данные о производстве роботов за последнюю неделю"""

    one_week = datetime.now() - timedelta(weeks=1)
    robots = (
        Robot.objects.filter(created__gte=one_week)
        .values('model', 'version')
        .annotate(count=Count('id'))
        .order_by('model', 'version')
    )

    return robots