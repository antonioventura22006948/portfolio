from django.contrib import admin

# Register your models here.
from .models import Post, PontuacaoQuizz, Course, Language, Project, Teacher

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Course)
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(Teacher)

