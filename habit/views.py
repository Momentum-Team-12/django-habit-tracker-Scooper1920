from django.shortcuts import render,redirect,get_object_or_404
from .models import Habit
from .forms import HabitForm
# Create your views here.
def list_habits(request):
    habits=Habit.objects.all()

    return render(request, "habit/list_habits.html",
                    {"habits":habits})



def habit_detail(request,pk):
    habit = Habit.objects.get(pk=pk)
    context = {
        'habit':habit
    }
    return render(request, 'habit/habit_detail.html',context)


def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habit/add_habit.html", {"form":form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')

    else:
        return render(request, "habit/delete_habit.html",
                  {"habit": habit})