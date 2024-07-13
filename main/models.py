from django.db import models


class Home(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


class Our_service(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    info = models.TextField()


class Our_team(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    info = models.TextField()
    twiter = models.URLField(max_length=255, blank=True)
    gmail = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)


class Contact_us(models.Model):
    name = models.CharField(max_length=233)
    phone = models.CharField(max_length=233)
    print(1)
    subject = models.CharField(max_length=233)
    message = models.TextField()

    def __str__(self):
        return self.name


class Working_hours(models.Model):
    info = models.TextField()
    phone = models.CharField(max_length=233)
    email = models.EmailField()
    aweek = models.CharField(max_length=233)
    hour1 = models.TimeField()
    hour2 = models.TimeField()


class Testemonial(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    img = models.ImageField()