# Generated by Django 5.0 on 2024-04-20 02:37

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='カテゴリ名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='店舗名')),
                ('price_max', models.PositiveIntegerField(default='0', verbose_name='価格（最大）')),
                ('price_min', models.PositiveIntegerField(default='0', verbose_name='価格（最小）')),
                ('seat', models.PositiveIntegerField(default='0', verbose_name='座席数')),
                ('address', models.CharField(default='', max_length=200, verbose_name='住所')),
                ('tel', models.CharField(default='', max_length=11, verbose_name='電話番号')),
                ('open_time', models.TimeField(default='', verbose_name='営業時間(開始)')),
                ('close_time', models.TimeField(default='', verbose_name='営業時間(終了)')),
                ('close_day', models.CharField(default='', max_length=20, verbose_name='定休日')),
                ('catch_copy', models.CharField(default='', max_length=30, verbose_name='キャッチコピー')),
                ('explanation', models.TextField(default='', max_length=300, verbose_name='説明')),
                ('img', models.ImageField(blank=True, default='img/noImage.png', upload_to='photos', verbose_name='店舗画像')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='NagoyameshiApp.category', verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(default='', max_length=150, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(default='', max_length=50, verbose_name='氏名')),
                ('furigana', models.CharField(default='', max_length=50, verbose_name='フリガナ')),
                ('birthday', models.DateField(default='2000-01-01', verbose_name='生年月日')),
                ('zipcode', models.CharField(default='', max_length=8, verbose_name='郵便番号')),
                ('address', models.CharField(default='', max_length=100, verbose_name='住所')),
                ('tel', models.CharField(default='', max_length=13, verbose_name='電話番号')),
                ('works', models.CharField(blank=True, default='', max_length=20, verbose_name='ご職業')),
                ('subscription', models.BooleanField(default='False', verbose_name='サブスク契約')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NagoyameshiApp.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default='', verbose_name='予約日')),
                ('time', models.TimeField(choices=[('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30')], default='', verbose_name='予約時間')),
                ('number_of_persons', models.PositiveIntegerField(default='', verbose_name='人数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NagoyameshiApp.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='評価')),
                ('comment', models.TextField(default='', verbose_name='コメント')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NagoyameshiApp.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('restaurant', 'user')},
            },
        ),
    ]
