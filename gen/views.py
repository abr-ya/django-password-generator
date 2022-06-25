from django.shortcuts import render
# from django.http import HttpResponse
import random
import string

# Create your views here.
def home(req):
  return render(req, 'gen/home.html')

def about(req):
  return render(req, 'gen/about.html')

def password(req):
  characters = list(string.ascii_lowercase)
  length = int(req.GET.get('length', 6))

  if req.GET.get('uppercase'):
    characters.extend(list(string.ascii_uppercase))

  if req.GET.get('numbers'):
    characters.extend(list('1234567890'))

  password = ''
  for x in range(length):
    password += random.choice(characters)

  return render(req, 'gen/password.html', {'password': password})
