from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 10
    queryset = Note.objects.order_by('-updated_at')

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content', 'archived']
    template_name = 'notes/note_form.html'

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content', 'archived']
    template_name = 'notes/note_form.html'

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note_list')
