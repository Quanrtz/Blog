from django.shortcuts import render, redirect
from .models import Economy, It, Sports, ToDo
from .forms import EconomyForm, ItForm, SportsForm
from django.views.decorators.http import require_http_methods


def index(request):
    tasks = Economy.objects.order_by('-id')
    return render(request, 'templates/main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'templates/main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = EconomyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = EconomyForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'templates/main/create.html', context)


def index1(request):
    TI = It.objects.order_by('-id')
    return render(request, 'templates/main/index__.html', {'title': 'Главная страница сайта', 'TI': TI})





def create1(request):
    error = ''
    if request.method == 'POST':
        form = ItForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home1')
        else:
            error = 'Форма была неверной'

    form = ItForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'templates/main/create__.html', context)



def index2(request):
    sp = Sports.objects.order_by('-id')
    return render(request, 'templates/main/_index_.html', {'title': 'Главная страница сайта', 'sp': sp})

def create2(request):
    error = ''
    if request.method == 'POST':
        form = SportsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home2')
        else:
            error = 'Форма была неверной'

    form = SportsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'templates/main/_create_.html', context)






def index4(request):
    todos = ToDo.objects.all()
    return render(request, 'templates/main/General.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

# Create your views here.


# Create your views here.
