# Generated by Django 5.0 on 2024-06-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NagoyameshiApp', '0002_customuser_stripe_subscription_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(verbose_name='予約日'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_persons',
            field=models.PositiveIntegerField(verbose_name='人数'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30')], verbose_name='予約時間'),
        ),
    ]