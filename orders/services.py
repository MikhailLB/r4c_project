from customers.models import Customer
from orders.models import Order
from orders.serializers import order_serializer
from robots.models import Robot


def create_order(data):
    # Сервис для создания записи в БД

    """
            ****ПРИМЕЧАНИЕ****
    Сначала я начал реализовывать полную цепочку работы ордеров (
    создание -> проверка на наличие -> если есть в наличии, удаляем один экземпляр -> выполняем заказ во вьюхе -> удаляем заказ из списка)
    Потом я понял, что это задание не рассчитано на такой функционал, поэтому тут реализовано только создание order для проверки 3 задания

     """

    order_serializer(data)

    try:

        Customer.objects.create(email=data['email'])
        customer = Customer.objects.get(email=data['email'])

        order =  Order.objects.create(
            customer=customer,
            robot_serial=data['robot_serial'],
        )
    except Exception as e:
        raise ValueError(f"Не удалось создать заказ: {str(e)}")

    return order
