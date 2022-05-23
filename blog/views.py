from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from .forms import CommentForm


class ArticleList(ListView):
    queryset = Article.objects.filter(status=True)
    template_name = 'blog/article_list.html'
    paginate_by = 2


def articleDetail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article_view_sort = Article.objects.order_by('-view')
    category = Category.objects.all()
    # for the view increase
    article.view += 1
    article.save()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            parent_id = request.POST.get('parent_id')
            Comment.objects.create(parent_id=parent_id, user=request.user, article=article, body=body)

    else:
        form = CommentForm()
    context = {
        'article': article,
        'category': category,
        'article_view_sort': article_view_sort,
        'form': form,
    }
    return render(request, 'blog/article_detail.html', context)


def categoryDetail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = category.articles.all()
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', context={'object_list': object_list})


def searchDetail(request):
    search = request.GET.get('search')
    object_list = Article.objects.filter(title__icontains=search)
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', context={'object_list': object_list})

# class ArticleDetail(DetailView):
#     queryset = Category.objects.all()
#     def get_object(self):
#         queryset = Category.objects.all()
#         slug = self.kwargs.get('slug')
#         return get_object_or_404(Article.objects.filter(status=True), slug=slug) ,queryset


# class CategoryDetail(DetailView):
#     def get_queryset(self):
#         slug = self.kwargs.get('slug')
#         return get_object_or_404(Category.objects.filter(status=True, slug=slug))
