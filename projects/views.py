from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreatePostForm,CrearRecomendacion
from .models import AdoptMe,Recomendaciones
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy


# Create your views here.

def home (request):
    return render(request,'home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request,'signup.html',{
        'form':UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('adopta')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form':UserCreationForm,
                    'error':'Este usuario ya existe. Intente de nuevo :)'
                })
            
        return render(request,'signup.html',{
                    'form':UserCreationForm,
                    'error':'Las contraseñas no coinciden. Intente de nuevo :)'
                })

@login_required      
def adopta(request):
    posts=AdoptMe.objects.all()
    return render(request,'adoptame.html',{
        'posts':posts,
    })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
        'form':AuthenticationForm
        })
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
            'form':AuthenticationForm,
            'error':'Usuario o contraseña incorrectas. Intente de nuevo :)'
            })
        else:
            login(request,user)
            return redirect ('adopta')
@login_required        
def create_post(request):
    if request.method == 'GET':
        return render(request,'create_post.html',{
        'form':CreatePostForm
    })
    else:
        try:
            form=CreatePostForm(request.POST,request.FILES)
            new_post=form.save(commit=False)
            new_post.user=request.user
            new_post.save()
            return redirect('adopta')
        except ValueError:
            return render(request,'create_post.html',{
        'form':CreatePostForm,
        'error':'Por favor inserte datos válidos :('
    })
@login_required            
def post_detail(request,post_id):
    post=get_object_or_404(AdoptMe,pk=post_id)
    return render(request,'post_detail.html',{
        'post':post,
    })
    
# def post_detail(request,post_id):
#     post=get_object_or_404(AdoptMe,pk=post_id)
#     form=CreatePostForm(instance=post)
#     return render(request,'post_detail.html',{
#         'post':post,
#         'form':form
#     })
@login_required       
def complete_post(request,post_id):
    postt=get_object_or_404(AdoptMe,pk=post_id, user=request.user)
    if request.method == 'POST':
        postt.datecompleted=timezone.now()
        postt.save()
        return redirect('adopta')
@login_required    
def delete_post(request,post_id):
    postt=get_object_or_404(AdoptMe,pk=post_id, user=request.user)
    if request.method == 'POST':
        # postt.datecompleted=timezone.now()
        postt.delete()
        return redirect('adopta')


def gracias(request):
    return render(request,'gracias.html')   
    
# def crear_recomendacion(request):
#     if request.method == 'POST':
#         form=CrearRecomendacion(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('thanks')
#     else:
#         form=CrearRecomendacion()
#     return render(request,'recomendaciones.html',{
#         'form':form
#     })
@login_required
def crear_recomendacion2(request):
    if request.method == 'GET':
        return render(request,'recomendaciones.html',{
        'form':CrearRecomendacion
    })
    else:
        try:
            form=CrearRecomendacion(request.POST)
            new_rcmd=form.save(commit=False)
            new_rcmd.user=request.user
            new_rcmd.save()
            return redirect('thanks')
        except ValueError:
            return render(request,'recomendaciones.html',{
        'form':CrearRecomendacion,
        'error':'Por favor inserte datos válidos :('
    })  
# def modificar_post(request,post_id):
#     post=get_object_or_404(AdoptMe,pk=post_id)
#     data={
#         'form':CreatePostForm(instance=post)
#     }
#     if request.method=='POST':
#         data=CreatePostForm(request.POST, instance=post, files=request.FILES)
#         if data.is_valid():
#             data.save()
#             return redirect(to='adopta')
#         data['form']=data
#     return render(request,'modificar.html',data)

class PostUpdate(UpdateView):
    model=AdoptMe
    form_class=CreatePostForm
    template_name='modificar.html'
    success_url=reverse_lazy('adopta')