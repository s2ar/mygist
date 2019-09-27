# from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
# from django.template import loader
from .models import Note, Category
from .forms import NoteForm


def index(request):

    # template = loader.get_template('note/index.html')
    categories = Category.objects.all()
    notes = Note.objects.all()
    context = {'notes': notes, 'categories': categories}

    return render(request, 'note/index.html', context)
    # return HttpResponse(template.render(content, request))


def by_category(request, category_id):
    notes = Note.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'notes': notes, 'categories': categories,
               'current_category': current_category}
    return render(request, 'note/by_category.html', context)


class NoteCreateView(CreateView):
    template_name = 'note/create.html'
    form_class = NoteForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
