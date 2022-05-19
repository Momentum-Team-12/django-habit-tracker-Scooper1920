from django.shortcuts import render,redirect,get_object_or_404
from .models import Habit
from .forms import HabitForm
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import logout
from .models import CustomUser
# Create your views here.

@login_required
def list_habits(request):
    habits=Habit.objects.all()

    return render(request, "habit/list_habits.html",
                    {"habits":habits})


@login_required
def habit_detail(request,pk):
    habit = Habit.objects.get(pk=pk)
    context = {
        'habit':habit
    }
    return render(request, 'habit/habit_detail.html',context)

@login_required
def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habit/add_habit.html", {"form":form})

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')

    else:
        return render(request, "habit/delete_habit.html",
                  {"habit": habit})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habit/edit_habit.html", {
        "form": form,
        "habit": habit
    })


def log_out(request,user):
    logout(request,user)
    return redirect ('log_out')