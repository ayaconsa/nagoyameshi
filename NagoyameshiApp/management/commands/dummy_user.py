from django.core.management.base import BaseCommand
from NagoyameshiApp.models.custom_user import CustomUser
from faker import Faker
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = "Creates 100 dummy users"

    def handle(self, *args, **kwargs):

        # Fakerオブジェクトを作成
        fake = Faker('ja-JP') # 日本語対応

        # ダミーデータを生成してSQLite3データベースに保存
        for _ in range(100):  # 100行のダミーデータを生成
            name = fake.name()
            furigana = fake.kana_name()
            email = fake.email()
            birthday = fake.date_of_birth()
            zipcode = fake.zipcode()
            address = fake.address()
            tel = fake.phone_number()
            works = fake.job()
            password = make_password(fake.password())

            CustomUser.objects.create(
                name=name, 
                furigana=furigana, 
                email=email, 
                birthday=birthday, 
                zipcode=zipcode, 
                address=address, 
                tel=tel, 
                works=works, 
                password=password, 
                )
            
        self.stdout.write(self.style.SUCCESS('Successfully created dummy users'))