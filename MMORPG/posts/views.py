from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView, TemplateView


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    object_list = Post.objects.all()
    ordering = '-id'

    # @method_decorator(login_required, name='dispatch')
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('posts'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        # context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('posts'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


# class AddPostView(View):
#
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'add_post.html', {'form': form, 'modal_id': 'myModal'})
#
#     def post(self, request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             # Здесь можно добавить автора поста (если используется модель User)
#             # post.author = request.user
#             post.save()
#             return redirect('posts')
#         return render(request, 'add_post.html', {'form': form, 'modal_id': 'myModal'})

# class AddPostView(View):
#
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'posts.html', {'form': form})
#
#     def post(self, request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return JsonResponse({'success': True})
#         return JsonResponse({'success': False})
