from django.shortcuts import render

# Create your views here.
def blog_index(request):
    return render(request=request,template_name='blog_index.html')

def get_posts(request):
    return render(request=request,template_name='posts.html')