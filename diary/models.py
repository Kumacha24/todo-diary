from django.db import models
from django.conf import settings
from django.utils import timezone


# class Diary(models.Model):
#   """Diaryデータベースには
#   ・書いた人
#   ・タイトル
#   ・内容
#   ・作成日時
#   ・更新日時
#   ・公開日時
#   """
#   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#   title  = models.CharField(max_length=20)
#   text   = models.TextField()
#   created_date = models.DateTimeField(default=timezone.now)
#   updated_date = models.DateTimeField(blank=True, null=True)
#   published_date = models.DateTimeField(blank=True, null=True)
#   # image

#   def publish(self):
#     self.published_date = timezone.now()
#     self.save()

#   def __str__(self):
#     return self.title
