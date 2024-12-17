from django.core.exceptions import ValidationError
from datetime import datetime

def robot_serializer(data):

    """Сериализатор для JSON данных с ендпоинта add-robot"""

    required_fields = ['model', 'version', 'created']

    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Поле {field} обязательно!")

    try:
        datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValidationError("Некорректный формат! Ожидаемый формат: 'YYYY-MM-DD HH:MM:SS'")

    if len(data['model'])  > 2:
        raise ValidationError("Поле 'model' должно содержать не более 2 символов.")

    if len(data['version'])  > 2:
        raise ValidationError("Поле 'version' должно содержать не более 2 символов.")
