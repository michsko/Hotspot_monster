from django.shortcuts import render
from .models import BlogPost
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator

# Create your views here.



def about (request):
	return render(request, 'about.html',{})


def blog_grid (request):

	paginator = Paginator(BlogPost.objects.all().order_by('date_published'), 9)
	page = request.GET.get('page')
	blog_posts = paginator.get_page(page)


	return render(request, 'blog_grid.html', {
		'blog_posts': blog_posts,
		})



def blog_single (request, blog_post_id):

	paginator = Paginator(BlogPost.objects.all().filter(pk=blog_post_id), 1)
	page = request.GET.get('page')
	blog_posts = paginator.get_page(page)
	
	return render(request, 'blog_single.html', {
		'blog_posts': blog_posts,
		})


def blog_standard (request):
	paginator = Paginator(BlogPost.objects.all().order_by('date_published'), 3)
	page = request.GET.get('page')
	blog_posts = paginator.get_page(page)
	
	return render(request, 'blog_standard.html', {
		'blog_posts': blog_posts,
		})


def contact (request):
	return render(request, 'contact.html', {})


def fournullfour (request):
	return render(request, '404.html',{})


def index (request):
	last_post = BlogPost.objects.all().order_by('-date_published')[:1]
	last_five = BlogPost.objects.all().order_by('date_published')[:5]

	return render(request, 'index.html', {
		'last_five': last_five,
		'last_post': last_post,
		})

def search(request):
	if request.method == 'POST':
		searched = request.POST['searched']

		searched_blogs = BlogPost.objects.filter(title__icontains=searched)
	
		return render(request ,'blog_search_grid.html', {
			"searched_blogs" : searched_blogs,
			"searched": searched, 
			})
	else: 
		return render(request, 'blog_search_grid.html',{})