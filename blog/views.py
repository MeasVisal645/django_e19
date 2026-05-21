from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
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