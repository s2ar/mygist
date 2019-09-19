from django.http import HttpResponse
from django.shortcuts import render
from django.template  import loader


from .models import Note


def index(request):

    template = loader.get_template('note/index.html')
    notes = Note.objects
    content = {'notes': notes}

    return render(request, 'note/index.html', content)
    #return HttpResponse(template.render(content, request))

