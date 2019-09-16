from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse_lazy
from .models import Album,Song,Profile,ShipPhoto
import operator,re
from django.views.generic import ListView,DetailView,View,CreateView,UpdateView,DeleteView,TemplateView

from .myforms import MyLogin,Register,AddAlbum,Userprofile,Upprofile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django import forms
from django.db.models import Q

# Create your views here.

'''def song(request):
    data=Song.objects.all()

    return render(request,'gaana/song.html',{'data':data})'''
'''

class home(ListView):
    template_name = 'gaana/home.html'
    context_object_name= 'data'
    def get_queryset(self):
        return Album.objects.all()
'''
def record(self,request):
    audio_file = request.FILES.get('audio')
    shipphoto_obj = ShipPhoto.objects.get(pk='pk')
    shipphoto_obj.voice_record = audio_file
    shipphoto_obj.save()


class JsonResponse(object):
    pass


import sounddevice as sd
from scipy.io.wavfile import write
import os
class rec(View):

    fs = 44100  # this is the frequency sampling; also: 4999, 64000
    seconds = 5  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Starting: Speak now!")
    sd.wait()  # Wait until recording is finished
    print("finished")
    write('output.mp3', fs, myrecording)  # Save as WAV file

    def post(self, request):
        """Save recorded audio blob sent by user."""
        audio_file = request.FILES.get['output.mp3']
        print(audio_file)
        shipphoto_obj = ShipPhoto()
        shipphoto_obj.voice_record = audio_file
        shipphoto_obj.save()
        return render(request, 'gaana/rec.html', {'data': shipphoto_obj})


class AjaxSaveAudio(View):
    template_name = 'gaana/rec.html'

    """Use ajax to save audio sent by user."""

    def post(self, request):
        """Save recorded audio blob sent by user."""
        audio_file = request.FILES['audio']
        print(audio_file)
        shipphoto_obj = ShipPhoto()
        shipphoto_obj.voice_record = audio_file
        shipphoto_obj.save()
        return render(request,'gaana/rec.html',{'data':shipphoto_obj})
        return JsonResponse({
            'success': True,
        })
def image_url(self):

        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/gaana/bg2.jpg'
class home(TemplateView):
    def get(self, request, *args, **kwargs):
        d=Album.objects.all()
        if request.user.is_authenticated:
            return render(request,'gaana/home1.html',{'data':d})
        else:
            return render(request, 'gaana/home.html', {'data': d})
'''
class home1(ListView):
    template_name = 'gaana/home1.html'
    context_object_name= 'data'
    def get_queryset(self):
        return Album.objects.all()
'''
'''
class detail(DetailView):
    template_name = 'gaana/song.html'
    context_object_name = 'val'
    model = Album
    isPlaying = False
    def get_context_data(self,**kwargs):
        context=super(detail,self).get_context_data(**kwargs)
        context['user']=self.request.user
        if self.request.user.is_authenticated:
            context['master']='gaana/master1.html'
            if 'album' in self.request.COOKIES:
                response = render_to_response('album.html', context)

                response.set_cookie('album', 'val')
                return render_to_response
                #return response
            else:
                self.request.COOKIES['album']=[]

        else:
            context['master']='gaana/master.html'
        return context

'''
   # def get_queryset(self):
       # return Song.objects.all()
def detail(request,pk):
    a=get_object_or_404(Album,pk=int(pk))
    context={'val':a}
    context['user'] = request.user

    if request.user.is_authenticated:
        context['master'] = 'gaana/master1.html'
        response = render(request, 'gaana/song.html', context)
        if 'album' in request.COOKIES:
            l = request.COOKIES['album']
            l  =l+str(pk) + ','
            response.set_cookie('album', l)
        else:
            l = str(pk) + ','
            response.set_cookie('album',l)
        return response

        # response.set_cookie('album', 'val')
        #return render_to_response
        # return response

    else:

        context['master'] = 'gaana/master.html'
        return render(request, 'gaana/song.html', context)

def profile_page(request):
    user1 = User.objects.filter(username=request.user).first()



    print(user1)

    return render(request, 'gaana/userprofile.html', {'user': user1})
@login_required(login_url='gaana:login')
def profile(request):
    if request.method=='POST':
        u_form=Userprofile(request.POST,instance=request.user)
        p_form=Upprofile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'yuvgyu')
            return redirect('gaana:profile')
    else:
        u_form = Userprofile(instance=request.user)
        print(u_form)
        p_form = Upprofile(instance=request.user.profile)
        context={

            'u_form':u_form,
            'p_form':p_form
        }


        return render(request, 'gaana/userprofile.html', context)





class loginpage(View):
    def get(self,request):
        form=MyLogin(None)
        return render(request,'gaana/login.html',{'form':form})
    def post(self,request):
        form = MyLogin(request.POST)
        if form.is_valid():
            u = form.cleaned_data['UserName']
            p = form.cleaned_data['Password']
            v = authenticate(username=u, password=p)
            n=request.GET.get('next',None)

            if v is not None:


                login(request, v)
                print(u)
                if n:
                    return redirect(n)
                else:
                    return redirect('gaana:home')
        return render(request, 'gaana/home1.html', {'form': form})



class logoutpage(View):
    def get(self,request):
        logout(request)
        return redirect('gaana:home')
        #return HttpResponse("logged out: ")
        #return render(request, 'gaana/home.html', {'form': form})
class Delsong(LoginRequiredMixin,DeleteView):
    login_url = 'gaana:login'
    template_name = 'gaana/song.html'
    context_object_name = 'val'
    model = Song

    def get(self,request,pk):
        req=request.GET.get('req', pk)
        song=Song.objects.filter(pk=pk)

        song.delete()
        a = Song.objects.get(id=int(self.kwargs.get('pk')))
        return redirect('gaana:detail', a.al_id.id)
        #return HttpResponse("deleted ")
'''
    def song_delete(request, pk):
        cat = get_queryset(Song, pk=pk)  # Get your current cat

        if request.method == 'POST':         # If method is POST,
            cat.delete()                     # delete the cat.
            return redirect('home1.html')             # Finally, redirect to the homepage.

        return render(request, 'home1.html', {'cat': cat})
'''

'''
class Delsong(DeleteView):
    def put(self, request,pk):

        song=self.get_object(pk)
        song.delete()
        #messages.success(request, "Post successfully deleted!")
        return HttpResponse("deleted")
'''

class Mysignup(View):
    def get(self,request):
        form=Register(None)
        return render(request,'gaana/register.html',{'form':form})
    def post(self,request):
        form=Register(request.POST)
        if form.is_valid():

            data=form.save(commit=False)

            p = form.cleaned_data['Password']
            data.set_password(p)

            data.save()

            return redirect('gaana:login')

        return render(request, 'gaana/register.html',{'form': form})

'''
class load(View):
    def get(self,request):
        form=AddAlbum(None)
        return render(request,'gaana/login.html',{'form':form})
    def post(self,request):
        form=AddAlbum(request.POST,request.FILES)
        if form.is_valid():

            form.save()


            return redirect('gaana:home')

        return render(request, 'gaana/login.html',{'form': form})

'''
class Addalbum(LoginRequiredMixin,CreateView):
    login_url = 'gaana:login'
    template_name = 'gaana/album.html'
    context_object_name = 'form'
    model=Album
    fields = ['title', 'artist', 'genre', 'year', 'image']
    def form_valid(self, form):
        form.save()
        return redirect('gaana:home')
'''
class Delsong(DeleteView):
    template_name = 'gaana/register.html'
    context_object_name = 'val'
    model = Song
    #fields = ['al_id','title', 'artist', 'genre','sfile','image']
    def get_queryset(self,request):

        song = Song.objects.all(request)
        print(song)
        song.delete()
        return HttpResponse("deleted")
'''
class Delalbum(LoginRequiredMixin,DeleteView):
    login_url = 'gaana:login'
    template_name = 'gaana/delete.html'
    model=Album
    success_url = reverse_lazy('gaana:home')

   # return redirect('gaana:home')

class Dellsong(LoginRequiredMixin,DeleteView):
    login_url = 'gaana:login'
    template_name = 'gaana/delete.html'
    model=Song
    success_url = reverse_lazy('gaana:detail')

    #a = Song.objects.get(id=int(request.kwargs.get('pk')))
    #success_url = reverse_lazy('gaana:detail', a.al_id.id)
    def form_valid(self,form):
        i = self.kwargs.get('pk')
        song = self.objects.get(pk=int(i))
        return song



    def get_success_url(self):

        a = self.object.al_id


        return reverse_lazy('gaana:detail', kwargs={'pk':a.id})
        #return redirect('gaana:detail', a.al_id.id)




class Addsong(LoginRequiredMixin,CreateView):
    login_url = 'gaana:login'
    template_name = 'gaana/register.html'
    context_object_name = 'form'
    model=Song
    fields = ['title', 'artist', 'genre','sfile','image']
    def form_valid(self,form):
        i= self.kwargs.get('pk')
        song = Album.objects.get(pk=int(i))
        data=form.save(commit=False)
        data.al_id=song
        data.save()




        return redirect('gaana:detail',song.id)
'''
class Editsong(LoginRequiredMixin,UpdateView):
    login_url = 'gaana:login'
    template_name = 'gaana/register.html'
    context_object_name = 'form'
    model=Song
    fields = ['title', 'artist', 'genre','sfile','image']
    def form_valid(self,form):
        i= self.kwargs.get('pk')
        song = Album.objects.get(pk=int(i))
        data=form.save(commit=False)
        data.al_id=song
        data.save()
'''
class Upalbum(LoginRequiredMixin,UpdateView):
    login_url = 'gaana:login'
    template_name = 'gaana/register.html'
    model = Album
    fields = ['title', 'artist', 'genre', 'year','image']
    def form_valid(self, form):
        form.save()
        return redirect('gaana:home')

class Upsong(LoginRequiredMixin,UpdateView):
    login_url = 'gaana:login'
    template_name = 'gaana/register.html'
    model =Song
    fields = ['title', 'artist', 'genre','sfile','image']

    def form_valid(self, form):

        form.save()
        a=Song.objects.get(id=int(self.kwargs.get('pk')))
        return redirect('gaana:detail',a.al_id.id)

'''
def loginpage(request):
    form=MyLogin(request.POST or None)
    if form.is_valid():
        u=form.cleaned_data['UserName']
        p=form.cleaned_data['Password']
        v = authenticate(username=u, password=p)

        if v is not None:
            login(request,v)

        return HttpResponse("logged in: "+u)
    return render(request,'gaana/login.html',{'form':form})

'''
'''
class Search(ListView):

    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    @property
    def get_queryset(self):
        result = super(ListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
class search(DetailView):
    template_name = 'gaana/search.html'
    model = Album
    def your_view(self,request):

        # Your code

        if request.method == 'GET': # If the form is submitted

            search_query = request.GET.get('search_box', None)
            return render(request, 'gaana/search.html', {'val': search_query})

            return Album.object.all(search_query)
        # Do whatever you need with the word the
'''
class searchh(View):
    template_name = 'gaana/search.html'
    model = Song

    def form_valid(self, request):
        if request.method == 'POST':
            search_box = request.POST['search_box']
            if search_box:
                match = Song.objects.filter(Q(title__contains=search_box) | Q(artist__contains=search_box))
                if match:
                    return render(request, 'gaana/search.html', {'sea': match})
                else:
                    messages.error(request, 'no result found')
            else:
                return HttpResponseRedirect('/search/')
        return render(request, 'gaana/search.html')

def search(request):
    if request.method=='POST':
        search_box=request.POST['search_box']
        if search_box:
            match=Song.objects.filter(Q(title__contains=search_box)|Q(artist__contains=search_box))
            if match:
                if request.user.is_authenticated:
                    return render(request, 'gaana/play.html', {'sea': match})
                else:
                    return render(request, 'gaana/play.html', {'sea': match})

            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'gaana/play.html')




'''
   def get_queryset(self):
        qs = Song.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(artist__icontains=query)).distinct()
        return qs
        This could be your actual view or a new one
        # Your code
        if request.method == 'GET':  # If the form is submitted

            search_query = request.GET.get('search_box', 'pk')
            a = Song.objects.get(id=int(request.kwargs.get(search_query)))
            success_url = reverse_lazy('gaana:detail', a.al_id.id)
            return success_url
'''

'''
def detail(request,val):
    a=get_object_or_404(Album,pk=int(val))
    for i in a.song_set.all():
        ht+='<h1>'+i.title+'</h1><br>'
    return HttpResponse(ht)
    return render(request,'gaana/songs.html',{'val':a})'''
import re
def history(request):
    if request.user.is_authenticated:
        if 'album' in request.COOKIES:
            x=re.findall('/d+',request.COOKIES['album'])
            print(x)
            #x=str(request.COOKIES['album']).split(',')
            d=dict.fromkeys(x)
            for i in d:
                d[i]=(Album.objects.get(pk=int(i)),x.count(i))
            return HttpResponse(str(d.values())+str(d))
        else:
            return HttpResponse("<h1> no browsing history</h1>")
    else:
        return HttpResponse("<h1>login to view history</h1>")