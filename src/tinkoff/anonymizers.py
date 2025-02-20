import random
from hattori.base import BaseAnonymizer, faker

from tinkoff.models import CreditNotification, PaymentNotification


class TinkoffCreditNotificationAnonimizer(BaseAnonymizer):
    model = CreditNotification
    attributes = [
        ('first_name', faker.first_name),
        ('last_name', faker.last_name),
        ('middle_name', faker.middle_name),
        ('monthly_payment', faker.pydecimal(left_digits=5, right_digits=2, positive=True)),
        ('phone', faker.phone_number),
        ('email', faker.email),
    ]


class TinkoffPaymentNotificationAnonimizer(BaseAnonymizer):
    model = PaymentNotification
    attributes = [
        ('card_id', faker.uuid4),
        ('rebill_id', lambda: random.randint(100500, 10005000)),
        ('amount', faker.pydecimal(left_digits=5, right_digits=2, positive=True)),
        ('pan', faker.uuid4),
        ('token', faker.uuid4),
    ]
