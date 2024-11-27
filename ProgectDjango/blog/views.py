from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-created_at')
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context ={'page_obj': page_obj}
#     return render(request, 'index.html', context)
class BlogPage:
    per_page = 3

    def get_page(self, request):
        posts = Post.objects.all().order_by('-created_at')
        if request.method == 'POST':
            if request.POST.get('page_len') == 'all':
                self.per_page = len(posts)
            else:
                self.per_page = int(request.POST.get('page_len'))
        paginator = Paginator(posts, self.per_page)
        try:
            page_number = int(request.GET.get('page'))
        except TypeError:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        num_page_list = []
        if page_number - 2 > 1:
            num_page_list.append(0)
        for i in range(max(1, page_number - 2), min(paginator.num_pages, page_number + 2) + 1):
            num_page_list.append(i)
        if page_number + 2 < paginator.num_pages:
            num_page_list.append(0)
        context = {'page_obj': page_obj,
                   'paginator': paginator,
                   'num_page_list': num_page_list}
        return render(request, 'index.html', context)
