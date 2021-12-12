from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from blog.models import Post
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from django.core.paginator import Paginator

class PostListView(LoginRequiredMixin,View):
    def get(self, request):
        post_list = Post.objects.filter(author=request.user)
        paginator = Paginator(post_list, 2) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/post_list.html', {'page_obj': page_obj})
        
        
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    
    # fields = '__all__'
    fields = ('title', 'body',)
    # context_object_name = 'page_obj'
    template_name='blog/post_create.html'
    login_url = reverse_lazy('login')
    # success_url = reverse_lazy('blog:post_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_details', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    fields = '__all__'
    context_object_name = 'post'
    template_name='blog/post_details.html'
    login_url = reverse_lazy('login')
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = '__all__'
    context_object_name = 'post'
    template_name='blog/post_update.html'
    login_url = reverse_lazy('login')
    # success_url = reverse_lazy('blog:post_list')
    def get_success_url(self):
        return reverse('blog:post_details', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostUpdateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    template_name='blog/post_delete.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('blog:post_list')

