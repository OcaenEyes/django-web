from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Article,Tag,Category,Reward,Image
# Create your views here.

def hello(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    rewards = Reward.objects.all()
    images = Image.objects.all()

    article_list = Article.objects.all()
    paginator = Paginator(article_list,1)
    page = request.GET.get('page',1)
    currentPage = int(page)

    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(Paginator.num_pages)


    context = {'articles':articles,'tags':tags,'categories':categories,'rewards':rewards,'images':images,'article_list':article_list,'paginator':paginator,'currentPage':currentPage,}
    return  render(request,'index.html',context)

def cate(request):
    return render(request,'category.html')