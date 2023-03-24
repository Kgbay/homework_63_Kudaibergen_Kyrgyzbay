from django.views.generic import ListView, RedirectView

class IndexView(ListView):
    template_name = 'index.html'
