from django.db import models

class poempoem(models.Model):
    poemid = models.IntegerField()  # 序號
    poemen1 = models.TextField()  # 英文
    poemen2 = models.TextField()  # 英文
    poemen3 = models.TextField()  # 英文
    poemen4 = models.TextField()  # 英文

    poemcn1 = models.TextField()  # 中文
    poemcn2 = models.TextField()  # 中文
    poemcn3 = models.TextField()  # 中文
    poemcn4 = models.TextField()  # 中文


class poem(models.Model):
    poemid = models.IntegerField()  # 序號
    poemen = models.TextField()  # 英文
    poemcn = models.TextField()  # 中文

# insert into fbot_app_mbkk ()

class mbkkstyle(models.Model):
    # mbid = models.IntegerField()
    # mbname = models.CharField(max_length=256)
    # mbstyle = models.CharField(max_length=64)
    # mbtakeaway = models.CharField(max_length=64)
    # mblat = models.FloatField()
    # mblng = models.FloatField()
    # mburl = models.CharField(max_length=256)
    # mbimgurl=models.CharField(max_length=256)
    # mbaddress=models.CharField(max_length=256)
    # mbprice=models.CharField(max_length=64)
    # mbview = models.TextField()
    # mbcontact=models.CharField(max_length=32)
    # mbservice = models.TextField()
    # mbaward=models.CharField(max_length=256)

    mbuserid = models.CharField(max_length=64)
    mbfoodstyle = models.CharField(max_length=32)

