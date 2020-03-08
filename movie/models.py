from django.db import models

# Create your models here.


class UserRegisterInfo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    phone = models.CharField(null=False, max_length=11, verbose_name='手机号')
    username = models.CharField(null=False, max_length=20, verbose_name='用户名')
    userpwd = models.CharField(null=False, max_length=100, verbose_name='登陆密码')

# class UserPersonInfo(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name='序号')
#     username = models.CharField(null=False,max_length=20, verbose_name='用户名')
#     realname = models.CharField(null=False,max_length=20, verbose_name='真实姓名')
#     idcard = models.CharField(null=False,max_length=20, verbose_name='身份证')
#     sex = models.BooleanField(null=False,verbose_name='性别')


class FilmInfo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    title = models.CharField(null=False, max_length=40, verbose_name='电影名')
    type = models.CharField(null=False, max_length=40, verbose_name='类型')
    origin = models.CharField(null=False, max_length=20, verbose_name='发行国家')
    duration = models.IntegerField(null=False, verbose_name='时长')
    releasetime = models.CharField(null=False, max_length=20, verbose_name='上映日期')
    release = models.CharField(null=False, max_length=20, verbose_name='上映具体时间和地点')
    syncpsis = models.CharField(null=False, max_length=400, verbose_name='剧情介绍')
    pic = models.CharField(null=False, max_length=100, verbose_name='电影图片',default='null')


class CeleList(models.Model):
    title = models.CharField(null=False, max_length=20, verbose_name='电影名')
    type = models.CharField(null=False, max_length=20, verbose_name='职位')
    name = models.CharField(null=False, max_length=20, verbose_name='名字')
    pic = models.CharField(null=False, max_length=100, verbose_name='照片')
    # pic = models.ImageField()


class ImgList(models.Model):
    title = models.CharField(null=False, max_length=20, verbose_name='电影名')
    pic = models.CharField(null=False, max_length=100, verbose_name='照片')


















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
