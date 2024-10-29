from django.shortcuts import render
from django.db.models import Q
from posts.models import Post

def home(request):
    data = Post.objects.all()
    
    # Get search parameters
    search_query = request.GET.get('search_query', '')
    search_type = request.GET.get('search_type', '')
    
    if search_query:
        if search_type == 'title':
            # Search by title (case-insensitive)
            data = data.filter(title__icontains=search_query)
        elif search_type == 'category':
            # Search by category name (case-insensitive)
            data = data.filter(category__name__icontains=search_query)
    
    return render(request, 'home.html', {
        'data': data,
        'search_query': search_query,
        'search_type': search_type,
    })