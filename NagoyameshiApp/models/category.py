from django.db import models

class Category(models.Model):
        
    name = models.CharField(max_length=10, default='', verbose_name="カテゴリ名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    class Meta:
        app_label = 'NagoyameshiApp'