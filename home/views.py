from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView
from home.forms import ContactUsForm
from home.models import Message, Project


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def credentials(request):
    return render(request, 'home/credentials.html')


def suggestion(request):
    return render(request, 'home/suggestion.html')


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home:main')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)

        return super().form_valid(form)


class ProjectsListView(ListView):
    model = Project
    template_name = 'home/projects.html'


class ProjectDetailsView(DetailView):
    model = Project
    template_name = 'home/project_details.html'

