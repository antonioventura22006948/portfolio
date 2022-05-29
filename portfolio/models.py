from django.db import models


# Create your models here.

def resolution_path(instance, filename):
    return f'/images/'


class Post(models.Model):
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title[:50]


class PontuacaoQuizz(models.Model):
    name = models.CharField(max_length=30)
    points = models.IntegerField()

    def __str__(self):
        return self.name[:50]


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name[:50]


class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name[:50]


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='projects/')
    year_made = models.CharField(max_length=4)

    def __str__(self):
        return self.title[:50]


class Course(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.TextField()
    languages = models.ManyToManyField(Language)
    theory_professors = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    practical_professor = models.ManyToManyField(Teacher, related_name='courses')
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name[:50]
