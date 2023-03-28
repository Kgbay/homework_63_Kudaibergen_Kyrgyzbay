from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin

from instagram_app.forms import CommentForm
from instagram_app.models import Comment


class CommentDetail(DetailView):
    template_name = 'comment.html'
    model = Comment


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'developer']).exists()


class CommentCreateView(GroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = 'comment_create.html'
    model = Comment
    form_class = CommentForm
    success_message = 'Комментарий создан'

    def get_success_url(self):
        return reverse('comment_view', kwargs={'pk': self.object.pk})


class CommentUpdateView(GroupPermissionMixin, SuccessMessageMixin, UpdateView):
    template_name = 'comment_update.html'
    form_class = CommentForm
    model = Comment
    success_message = 'Комментарий обновлен'

    def get_success_url(self):
        return reverse('comment_view', kwargs={'pk': self.object.pk})


class CommentDeleteView(GroupPermissionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'comment_confirm_remove.html'
    model = Comment
    success_url = reverse_lazy('index')
    success_message = 'Комментарий удален'
