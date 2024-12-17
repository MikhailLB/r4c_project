from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    robot_serial = models.CharField(max_length=5,blank=False, null=False)

    class Meta:
        indexes = [
            models.Index(fields=['customer']),
            models.Index(fields=['robot_serial']),
        ]

    def __str__(self):
        return f'{self.customer} {self.robot_serial}'
