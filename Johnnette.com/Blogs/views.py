from django.shortcuts import render, get_list_or_404
from Blogs.models import Article

# Create your views here.




def bloglist(request):
    recent_article = Article.objects.all().order_by('-date')[:3]
    popular_article = Article.objects.all().order_by('-date')[3:] 
    context = {
        'recent_article':recent_article,
        'popular_article':popular_article,
        }
    return render(request, 'app/bloglist.html', context)




def articles(request, pk):
    article=get_list_or_404(Article, id=pk)
    recent_article = Article.objects.exclude(id=pk).order_by('-date')[:3]
    context={
        "article":article,
        "recent_article":recent_article,
    }
    return render (request, "app/article.html", context)