from django.shortcuts import render

# Create your views here.

def fournullfour (request):
	return render(request, '404.html',{})


def about (request):
	return render(request, 'about.html',{})


def blog_grid (request):
	return render(request, 'blog_grid.html', {})


def blog_single (request):
	return render(request, 'blog_single.html', {})


def blog_standard (request):
	return render(request, 'blog_standard.html', {})


def contact (request):
	return render(request, 'contact.html', {})


def index (request):
	return render(request, 'index.html', {})


def portfolio_list (request):
	return render(request, 'portfolio_lists.html', {})


def portfolio_masonry (request):
	return render(request, 'portfolio_masonry.html', {})


def portfolio (request):
	return render(request, 'portfolio.html', {})


def shop (request):
	return render(request, 'shop.html', {})