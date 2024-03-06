from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service_choices = [
        ('lashes', 'Наращивание ресниц'),
        ('manicure', 'Маникюр'),
        ('haircut', 'Стрижка'),
        ('hairstyle', 'Укладка'),
    ]
    service = models.CharField(max_length=20, choices=service_choices)

    time_choices = [
        ('9:00', '9:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
    ]
    time = models.CharField(max_length=20, choices=time_choices)

    def __str__(self):
        return f"{self.name} - {self.service} - {self.time}"


class Post(models.Model):
    title_choices = [
        ('lashes', 'Наращивание ресниц'),
        ('manicure', 'Маникюр'),
        ('haircut', 'Стрижка'),
        ('hairstyle', 'Укладка'),
    ]
    title = models.CharField(max_length=20, choices=title_choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title