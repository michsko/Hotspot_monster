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



def blog_single (request):
	return render(request, 'blog_single.html', {})


def blog_standard (request):
	return render(request, 'blog_standard.html', {})


def contact (request):
	return render(request, 'contact.html', {})


def fournullfour (request):
	return render(request, '404.html',{})


def index (request):
	last_five = BlogPost.objects.all().order_by('date_published')[:5]

	return render(request, 'index.html', {
		'last_five': last_five
		})


def search(request):
	if request.method == 'POST':
		searched = request.POST['searched']

		search = BlogPost.objects.annotate(search=SearchVector(
			'title','subtitle', 'content', 'date_published','author',
			'catergory1', 'catergory2', 'catergory3', 'tag1', 'tag2',
			'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 
			'tag9')).filter(search='searched')

	return render(request ,'blog_grid.html', {"search" : search, })
