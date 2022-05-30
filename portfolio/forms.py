from django import forms
from django.forms import ModelForm
from .models import Post, Course, Language, Teacher, Project


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s | %s" % (obj.name, obj.field1)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'author': 'Author',
            'title': 'Title',
            'description': 'Description',
            'link': 'Link'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Link is an optional field',
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        # inserção de classes CSS para formatação de cada campo do formulário



        languages = CustomMMCF(
            queryset=Language.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

        practical_professor = CustomMMCF(
            queryset=Teacher.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

        projects = CustomMMCF(
            queryset=Project.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Name',
            'age': 'Age',
            'description': 'Description',
            'languages': 'Languages',
            'theory_professors': 'Theory Professor',
            'practical_professor': 'Practical Professors',
            'projects': 'Projects'
        }

        help_texts = {
            'languages': 'No language available add him <a href= "add_language"> -> click here </a>',
            'theory_professors': 'No teacher available add him <a href= "add_teacher" > -> click '
                                 'here '
                                 '</a>',
            'practical_professor': 'No teacher available add him <a href= "add_teacher"> -> click '
                                   'here '
                                   '</a>',
            'projects': 'No project available create one <a href= "projects"> -> click here </a>',
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Name',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
        }


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Name',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
        }


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'year_made': 'Year',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
        }
