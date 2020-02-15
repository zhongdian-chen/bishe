from django.db import models

# Create your models here.

class FilmInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=40)
    type = models.CharField(null=False, max_length=40)
    origin = models.CharField(null=False, max_length=20)
    duration = models.IntegerField(null=False)
    releasetime = models.CharField(null=False, max_length=20)
    release = models.CharField(null=False, max_length=20)
    syncpsis = models.CharField(null=False, max_length=400)
    pic = models.ImageField(upload_to='img',null=True)






















# class FilmType(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(null=False, max_length=40)
#     comedy = models.CharField(null=True, max_length=20) #喜剧
#     romance = models.CharField(null=True, max_length=20) #爱情
#     action = models.CharField(null=True, max_length=20) #动作
#     drama = models.CharField(null=True, max_length=20) #剧情
#     war = models.CharField(null=True, max_length=20) #战争
#     adventure = models.CharField(null=True, max_length=20) #冒险
#     documentary = models.CharField(null=True, max_length=20) #记录
#     horror = models.CharField(null=True, max_length=20) #恐怖
#     thriller = models.CharField(null=True, max_length=20) #惊悚
#     mystery = models.CharField(null=True, max_length=20) #悬疑
#     crime = models.CharField(null=True, max_length=20) #犯罪
#     sci_fi = models.CharField(null=True, max_length=20) #科幻
#     cartoon = models.CharField(null=True, max_length=20) #卡通
#     ethical = models.CharField(null=True, max_length=20) #伦理
#     other = models.CharField(null=True, max_length=20) #其他
