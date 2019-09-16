from django.urls import path
from gaana.views import home,detail,loginpage,Mysignup,Addalbum,Upalbum,logoutpage,Upsong,Delsong,Delalbum,Addsong
from gaana.views import Dellsong,history,searchh,profile,profile_page
from . import views
app_name='gaana'
urlpatterns = [
    path('',home.as_view(),name='home'),
#path('home1',home1.as_view(),name='home1'),

    path('<int:pk>',detail, name='detail'),
    path('login',loginpage.as_view(),name='login'),
    path('logout', logoutpage.as_view(), name='logout'),
path('signup',Mysignup.as_view(),name='signup'),
#path('album',load.as_view(),name='album'),
path('album/add',Addalbum.as_view(),name='addalbum'),
path('album/update/<int:pk>',Upalbum.as_view(),name='updatealbum'),
path('album/delete/<int:pk>',Delalbum.as_view(),name='deletealbum'),
path('song/addsong/<int:pk>',Addsong.as_view(),name='addsong'),
path('song/update/<int:pk>',Upsong.as_view(),name='updatesong'),
path('song/delete/<int:pk>',Delsong.as_view(),name='deletesong'),
path('song/del/<int:pk>',Dellsong.as_view(),name='delsong'),
    path('history/',history,name='history'),
path('profile',profile,name='profile'),
path('audio',views.rec.as_view(),name='profile'),
#path(r'profile/(?P<username>[a-zA-Z0-9]+)$', profile_page),
path('profiles',profile_page,name='profiles'),
path('serch/',searchh.as_view(),name='searchh'),



    #path('<int:val>', detail, name='detail'),
]