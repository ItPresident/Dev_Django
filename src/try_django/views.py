from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    my_title = "hello there..."
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Wlelcome to try Django", 'blog_list': qs}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us",
        "form": form,
    }
    return render(request, "form.html", context)

def example_page(request):
    context       = {"title": "Example"}
    tamplate_name = "hello_world.html"
    tamplate_obj  = get_template(tamplate_name)
    render_item   = tamplate_obj.render(context)
    return  HttpResponse(render_item) #render(request, "hello_world.html", {"title": "Contact us"})

