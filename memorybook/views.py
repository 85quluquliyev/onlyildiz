from django.shortcuts import render, redirect
from .models import Memory


def memorybook(request):
    memories = Memory.objects.all()

    context = {
        "memories" : memories
    }

    return render(request, 'memorybook/memorybook.html',context)

def memoryCreate(request):
    memories = Memory.objects.all()
    if request.method == "POST":
        data = request.POST
        Memory.objects.create(note=data['note'])
        return redirect('memorybook')

    return render(request, 'memorybook/memorycreate.html')


