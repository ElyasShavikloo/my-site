from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from blog.models import Article, Comment


class BlogListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/blogs.html'
    paginate_by = 3


def blog_details(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_comment)
        else:
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user)

            # I added redirect to this view because when refresh details page , sent comment again, and I can't solve it right now
            # then we use redirect so as not to get into trouble
            return redirect('home:main')

    return render(request, 'blog/blog_details.html', context={'article': article})


def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    page_number = request.GET.get('page')
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/blogs.html', context={'articles': object_list})
