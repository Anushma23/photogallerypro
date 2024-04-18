from django.shortcuts import render, redirect

from app1.forms import Gallery
from app1.models import Category, Photo


# Create your views here.

def showlist(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    dict1={'keys':categories,'key2':photos}
    return render(request, 'show.html',dict1)

def view(request,i1):
    t=Photo.objects.get(id=i1)
    fr=Gallery(instance=t)
    dict2={'w':fr}
    return render(request, 'view.html',dict2)

def PhotoFunction(request,pk):
    photos=Photo.objects.get(id=pk)
    dict3={'key3': photos}
    return render(request, 'photo.html',dict3)


def Uploadfunction(request):
    categories= Category.objects.all()
    if request.method == 'POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['category-new'] != '':
            category,created=Category.objects.get_or_create(name=data["category-new"])
        else:
            category=None
            photo=Photo.objects.create(category=category, description=data['description'],image=image)
            return redirect('list')

    context1= {'key4':categories}
    return render(request,'upload.html',context1)






