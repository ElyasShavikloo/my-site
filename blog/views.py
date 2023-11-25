from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Article, Category, Like, CommentModel


class BlogListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/blogs.html'
    paginate_by = 3


def search(request):
    result = request.GET.get('result')
    articles = Article.objects.filter(title__icontains=result)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/results.html', context={'articles': object_list})


def categories(request, pk=None):
    category = Category.objects.get(id=pk)
    articles = category.articles.all()

    return render(request, 'blog/results.html', context={'articles': articles})


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'blog/blog_details.html'

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.method == 'POST':
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = CommentModel.objects.get(id=parent_id)
                body = request.POST.get('body')
                CommentModel.objects.create(body=body, article=self.object, user=request.user, parent_id=parent_comment)
            else:
                body = request.POST.get('body')
                CommentModel.objects.create(body=body, article=self.object, user=request.user)

                return redirect('blog:blogs')

        return render(request, 'blog/blog_details.html', context={'article': self.object})


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({'response': 'unliked'})

        except:
            like = Like.objects.create(article_id=pk, user_id=request.user.id)
            return JsonResponse({'response': 'liked'})



