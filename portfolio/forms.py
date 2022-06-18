from django import forms
from django.forms import ModelForm
from .models import Post, Course, Language, Teacher, Project, Person, Link, TFC


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s | %s" % (obj.name, obj.field1)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'title': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Title...'}),
            'description': forms.Textarea(attrs={'class': 'field', 'placeholder': 'Add Description...'}),
            'author': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add your name...'}),
            'link': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add a link...', }),
            'image': forms.FileInput(attrs={'class': 'field', 'placeholder': 'Add a image...'})

        }

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

        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Name...'}),
            'age': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Age...'}),
            'description': forms.Textarea(attrs={'classe': 'field', 'placeholder': 'Add Description...'}),

            'theory_professors': forms.Select(choices=Teacher.objects.all().order_by('name')),

        }

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Name...'}),

        }

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Name...'}),

        }

        # texto a exibir junto à janela de inserção
        labels = {
            'name': 'Name',
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'title': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Title...'}),
            'description': forms.Textarea(attrs={'class': 'field', 'placeholder': 'Add Description...'}),
            'image': forms.FileInput(attrs={'class': 'field', 'placeholder': 'Add Image...'}),
            'ano_de_realizacao': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Year...'})
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'year_made': 'Year',
        }


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Name...'}),

        }

        labels = {
            'name': 'Name',
        }


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'link': forms.URLInput(attrs={'class': 'field', 'placeholder': 'Add Link...'}),
        }

        labels = {
            'link': 'Link',
        }


class TFCForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'year': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Year...'}),
            'title': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Add Title...'}),
            'description': forms.Textarea(attrs={'class': 'field', 'placeholder': 'Add Description...'}),
            'image': forms.FileInput(attrs={'class': 'field', 'placeholder': 'Add Image...'}),
            'file': forms.FileInput(attrs={'class': 'field', 'placeholder': 'Add File...'}),
        }

        students = CustomMMCF(
            queryset=Person.objects.all(),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'field', 'placeholder': 'Add Students...'})
        )

        advisors = CustomMMCF(
            queryset=Teacher.objects.all(),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'field', 'placeholder': 'Add Advisors...'})
        )

        links = CustomMMCF(
            queryset=Link.objects.all(),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'field', 'placeholder': 'Add Links...'})
        )

        # texto a exibir junto à janela de inserção
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
        }

        help_texts = {
            'students': 'No students available add him <a href= "add_person"> -> click </a>',
            'advisors': 'No teachers available add him <a href= "add_teacher" > -> click </a>',
            'links': 'No project available create one <a href= "add_links"> -> click here </a>',
        }
