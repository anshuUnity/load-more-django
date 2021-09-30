from myapp.models import Post
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


def index(request):
    post_obj = Post.objects.all()[0:5]
    # post_values = Post.objects.values()[0:5]
    # print(post_values)
    total_obj = Post.objects.count()
    print(total_obj)
    return render(request, 'index.html', context={'posts': post_obj, 'total_obj': total_obj})


def load_more(request):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    post_obj = list(Post.objects.values()[offset_int:offset_int+limit])
    data = {
        'posts': post_obj
    }
    return JsonResponse(data=data)
