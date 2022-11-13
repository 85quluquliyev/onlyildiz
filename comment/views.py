from django.shortcuts import render, redirect
from .models import allLink, allComment

# Create your views here.

def commentResearchPage(request):   
    alllink = allLink.objects.all()
    comment = request.GET.get('linkdata')

    if comment == None:
        allcomment = ""
    else:
        allcomment = allComment.objects.filter(link__link=comment)

    search_input = comment

    
    context = {
        "allcomment" : allcomment,
        "alllink" : alllink,
        "search_input" : search_input,
    }



    return render(request, 'comment/commentresearchpage.html' , context)

def commentCreatePage(request):
    alllink = allLink.objects.all()

    if request.method == "POST":
        data = request.POST
 
        if data['link'] != '':
            getlink, created = allLink.objects.get_or_create(link=data['link'])
        else:
            getlink = None

        if 'bad' in data:
            bad = True
        else:
            bad = False
        
        comment = allComment.objects.create(
            link = getlink,
            description = data['comment'],
            title = data['title'],
            bad = bad,
        )

        return redirect('commentresearchpage')


    context = {
        "alllink": alllink,
        }
    return render(request, 'comment/commentcreatepage.html', context)
