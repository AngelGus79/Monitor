from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def menu(request):
	page=request.GET.get('page', 'usuarios')
	return render(request, 'menu.html',{'page':page})