import datetime
import operator

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from matplotlib import pyplot as plt

# Create your views here.

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import PostForm, CourseForm, ProjectForm, TeacherForm, LanguageForm
from .models import Post, PontuacaoQuizz, Course, Project, Teacher, Language


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def about_page_view(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'portfolio/about.html', context)


def education_page_view(request):
    return render(request, 'portfolio/education.html')


def projects_page_view(request):
    projects = Project.objects.all()
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projects'))

    context = {
        'form': form,
        'projects': projects
    }
    return render(request, 'portfolio/projects.html', context)


def skills_page_view(request):
    return render(request, 'portfolio/skills.html')


def bachelors_page_view(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:bachelors'))

    context = {
        'form': form,
        'courses': courses
    }

    return render(request, 'portfolio/bachelorsDegree.html', context)


class AddMeal(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'portfolio/bachelorsDegree.html',
    success_url = reverse_lazy('portfolio:bachelors')


def web_page_view(request):
    return render(request, 'portfolio/web.html')


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')


def blog_page_view(request):
    posts = Post.objects.all()
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {
        'form': form,
        'posts': posts
    }

    return render(request, 'portfolio/blog.html', context)


def pontuacao_quizz(request):
    pontuacao = 0

    if request.POST['language'] == 'HTML':
        pontuacao += 5

    if request.POST['framework'] == 'Django':
        pontuacao += 5

    if request.POST['language1'] == 'JS':
        pontuacao += 5

    if request.POST['framework1'] == 'Django':
        pontuacao += 5

    return pontuacao


def desenha_grafico_resultados():
    participants = sorted(PontuacaoQuizz.objects.all(),
                          key=lambda t: t.pontuacao, reverse=True)

    names = []
    points = []

    for pt in participants:
        names.append(pt.nome)
        points.append(pt.pontuacao)

    plt.barh(names, points)
    plt.savefig("portfolio/static/portfolio/images/grafico.png"
                , bbox_inches='tight')


def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados()

    return render(request, 'portfolio/quizz.html')


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:blog'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Wrong Cridencials.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })


def add_Teacher_view(request):
    teachers = Teacher.objects.all()
    form = TeacherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))

    context = {
        'form': form,
        'teachers': teachers
    }

    return render(request, 'portfolio/addTeacher.html', context)


def add_Language_view(request):
    languages = Language.objects.all()
    form = LanguageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:about'))

    context = {
        'form': form,
        'langauges': languages
    }

    return render(request, 'portfolio/addLanguage.html', context)
