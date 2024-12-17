from django.core.exceptions import ValidationError

from customers.models import Customer


def order_serializer(data):

    """Сериализатор для JSON данных заказа"""

    required_fields = ['email', 'robot_serial']

    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Поле {field} обязательно!")

    if Customer.objects.filter(email=data['email']).exists():
        raise ValidationError(f"Пользователь с E-mail {data['email']} уже существует!")

    if len(data['robot_serial'])  > 5:
        raise ValidationError("Поле 'robot_serial' должно содержать не более 5 символов.")

    if len(data['email']) > 255:
        raise ValidationError("Поле 'email' должно содержать не более 2 символов.")
