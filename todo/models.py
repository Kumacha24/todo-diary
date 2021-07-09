from django.db import models
from django.conf import settings
from django.utils import timezone

# class Todo(models.Model):
#   """Todoデータベースには
#   ・書いたユーザー
#   ・Todoのタイトル
#   ・Todoの中身
#   ・期日
#   ・作成日
#   ・達成日
#   ・優先度
#   ・分類
#   を入れたい
#   """
#   author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#   title = models.CharField(max_length=20)
#   content = models.TextField(null=True)
#   deadline = models.DateField()
#   created_at = models.DateTimeField(default=timezone.now())
#   #priority
#   achieve_date = models.DateField()
#   #grouping

  
#   def __str__(self):
#     return 
