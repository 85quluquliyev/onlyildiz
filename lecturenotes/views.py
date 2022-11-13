from django.shortcuts import render,redirect
from .models import lectureCode,lectureNote

# Create your views here.

def lectureNotes(request):
    code = lectureCode.objects.all()
    ls = lectureNote.objects.all()
    note = request.GET.get('linkdata')

    if note == None:
        allnotes = ""
    else:
        allnotes = lectureNote.objects.filter(code__code=note)

    search_input = note

    
    context = {
        "allnotes" : allnotes,
        "code" : code,
        "search_input" : search_input,
    }

    return render(request, "lecturenotes/notespage.html", context)

    

def lectureNoteCreate(request):
    code = lectureCode.objects.all()

    if request.method == "POST":
        data = request.POST
 
        if data['code'] != '':
            getcode, created = lectureCode.objects.get_or_create(code=data['code'])
        else:
            getcode = None
        
        note = lectureNote.objects.create(
            code = getcode,
            description = data['comment'],
            title = data['title'],
            link = data['link'],
        )

        return redirect('notespage')


    context = {
        "code": code,
        }
    return render(request, "lecturenotes/notecreate.html", context)

