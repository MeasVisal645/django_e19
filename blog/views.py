from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
  context = {
    'username': 'SuperCoder99',
    'age': 25,
    'is_premium': True,
    'movies': []
  }
  
  return render(request, 'blog/index.html', context)

def welcome_view(request):
  return HttpResponse("<h1>Welcome to my Django app!</h1>")

def search(request):
  search_text = request.GET.get('q', '')
  
  if search_text:
    return HttpResponse(f"You search for <span>{search_text}</span>")
  
  return HttpResponse(f"You didnt search anything")

def read_article(request, article_id):
  return HttpResponse(f"Reading article number: {article_id}")

def author_profile(request, username):
  return HttpResponse(f"Profile page for {username}")

def payment(request):
  if request.method == 'GET':
    return HttpResponse('POST METHOD')  
  
  return redirect('welcome')