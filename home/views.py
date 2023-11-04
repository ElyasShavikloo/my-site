from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from home.forms import ContactUsForm
from home.models import Message


def home(request):
    return render(request, 'home/index.html', {})


def about(request):
    return render(request, 'home/about.html', {})


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home:main')

    def form_valid(self, form):
        form_data = form.cleaned_data
        Message.objects.create(**form_data)

        return super().form_valid(form)


