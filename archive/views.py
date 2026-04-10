from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import ArchiveEntry

def home(request):
    return render(request, 'archive/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entry-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class ArchiveEntryListView(LoginRequiredMixin, ListView):
    model = ArchiveEntry
    template_name = 'archive/entry_list.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return ArchiveEntry.objects.filter(user=self.request.user)

class ArchiveEntryCreateView(LoginRequiredMixin, CreateView):
    model = ArchiveEntry
    template_name = 'archive/entry_form.html'
    fields = ['title', 'description', 'file_attachment']
    success_url = reverse_lazy('entry-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
