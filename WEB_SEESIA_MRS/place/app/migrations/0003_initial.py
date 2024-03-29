# Generated by Django 5.0 on 2023-12-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('service', models.CharField(choices=[('lashes', 'Наращивание ресниц'), ('manicure', 'Маникюр'), ('haircut', 'Стрижка'), ('hairstyle', 'Укладка')], max_length=20)),
                ('time', models.CharField(choices=[('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '12:00'), ('14:00', '12:00'), ('15:00', '12:00'), ('16:00', '12:00'), ('17:00', '12:00'), ('18:00', '12:00'), ('19:00', '12:00')], max_length=20)),
            ],
        ),
    ]
