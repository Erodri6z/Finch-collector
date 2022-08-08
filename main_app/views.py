from django.shortcuts import render
class Finch:
  def __init__(self, name, color, description, age):
    self.name = name
    self.color = color
    self.description = description
    self.age = age

finches = [
  Finch('Bob', 'Red', 'Nicknamed "Big red"', 2),
  Finch('Dylan', 'Blue', 'Hes a hothead', 2)
]

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello </h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })