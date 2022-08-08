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


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })