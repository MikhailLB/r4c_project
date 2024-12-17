from django.core.mail import send_mail


def send_mail_service(email, robot):

    subject = f"Робот {robot.model} {robot.version} доступен для заказа!"
    message = f"Добрый день!\nнедавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}. Этот робот теперь в наличии. \n\nЕсли вам подходит этот вариант - пожалуйста, свяжитесь с нами"
    send_mail(subject, message, 'robots@shop.com', [email])