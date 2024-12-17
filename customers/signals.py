from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.services import send_mail_service
from orders.models import Order
from robots.models import Robot

@receiver(post_save, sender=Robot)
def send_email_when_robot_in_stock(sender, instance, created, **kwargs):
    # Сигнал для получения информации о доступности робота


    """
                        *** КОММЕНТАРИЙ **
    Отправка писем на почту, как и уведомления и другие действия,
    завершения которых не обязательно ждать пользователю, обычно реализуются с помощью
    celery, однако, так как это тестовое задание я не стал сильно нагружать проект

    """
    if created:
        serial = instance.serial
        orders = Order.objects.filter(robot_serial=serial)

        if orders:
            for order in orders:

                customer_email = order.customer.email
                send_mail_service(email=customer_email, robot=instance)