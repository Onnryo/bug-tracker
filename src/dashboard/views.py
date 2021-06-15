from django.shortcuts import render

posts = [
    {
        'author': "Trey",
        'title': 'Post #1',
        'content': 'First post content',
        'date_posted': 'October 22, 2020'
    },
    {
        'author': "Jacob",
        'title': 'Post #2',
        'content': 'Second post content',
        'date_posted': 'January 22, 2020'
    }
]


def index(request):
    ctx = {
        'posts': posts,
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/index.html', ctx)


def about(request):
    ctx = {
        'title': 'About'
    }
    return render(request, 'dashboard/about.html', ctx)
