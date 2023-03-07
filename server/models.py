from django.db import models


class Specification(models.Model):
    full_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    cv = models.FileField(upload_to='static/cv/')
    picture = models.ImageField(upload_to='static/image/')
    about = models.TextField(max_length=500)
    age = models.IntegerField()
    email = models.EmailField()
    email2 = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    python = models.IntegerField()
    django = models.IntegerField()
    drf = models.IntegerField()
    git = models.IntegerField()
    database = models.IntegerField()
    docker = models.IntegerField()
    telegram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    stackoverflow = models.CharField(max_length=100)
    gitlab = models.CharField(max_length=100)
    discord = models.CharField(max_length=100)
    reddit = models.CharField(max_length=100)
    quora = models.CharField(max_length=100)
    leetcode = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Specifications'
        verbose_name_plural = 'Specifications'

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experience'

    def __str__(self):
        return self.title


class Education(models.Model):
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE, related_name='educations')
    title = models.CharField(max_length=100)
    fromm = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.title
