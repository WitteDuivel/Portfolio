from django.shortcuts import render

class IndexView():
    def get(self, request):
        return render(request, 'portfolio/index.html')