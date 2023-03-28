from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin

from instagram_app.forms import PostForm
from instagram_app.models import Post


class PostDetail(DetailView):
    template_name = 'post.html'
    model = Post


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'developer']).exists()


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_view', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'post_update.html'
    form_class = PostForm
    model = Post

    def get_success_url(self):
        return reverse('post_view', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'post_confirm_remove.html'
    model = Post
    success_url = reverse_lazy('index')
