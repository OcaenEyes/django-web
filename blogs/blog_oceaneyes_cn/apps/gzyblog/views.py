from django.shortcuts import render

from .models import Article,Tag,Category,Reward
# Create your views here.

def hello(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    rewards = Reward.objects.all()
    context = {'articles':articles,'tags':tags,'categories':categories,'rewards':rewards,}
    return  render(request,'index.html',context)