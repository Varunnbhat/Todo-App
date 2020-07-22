from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo_.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.   
def home(request):          #just a basic view that returns the home page
    todo_items = Todo.objects.all().order_by("-added_date")  #order the data in reverse order an display the same
    return render(request, 'main/index.html', {"todo_items": todo_items         #assign todo object to todo_items
    })

#function to capture the data from form.
@csrf_exempt
def add_todo(request):
    print(request.POST)
    current_date = timezone.now()
    content = request.POST["content"]
    print(current_date)
    print(content)
    created_obj = Todo.objects.create(added_date = current_date, text = content)
    print(created_obj)
    print(created_obj.id)
    length_of_todos = Todo.objects.all().count()
    print(length_of_todos)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect("/")