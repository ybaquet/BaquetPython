from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request, 'django.html', {'title':'Ex01 : Django, framework web.'})

def affichage(request):
    return render(request, 'affichage.html', {'title':'Ex01 : Processus d’affichage d’une page statique.'})

def templates(request):
    return render(request, 'templates.html', {'title':'Ex01 : Moteur de template.'})
