from django.shortcuts import render, get_object_or_404

import blog
from .models import Blog

def blogs(request):
    storries = Blog.objects.order_by('-pubDate')
    #order_by('-pubDate)[:5] parādā pēdējos 5 blogus sākot ar jaunāko
    return render(request, 'blog/blogs.html', {'storries':storries})

def detailedBlog(request, blog_id):
    work = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detailedBlog.html', {'work':work})
    #{'work':work} norāda html failam blogu balstoties uz tā id numuru