# pages/urls.py
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import *
from .views import index


from .views import ( 
    HomePageView, 
#    AboutPageView, 
#    LoginPageView, 
#    SignupPageView, 
#    LoginFormView,
#    CategoryListView,
#    CategoryCreateView,
#    CategoryDetailView,
#    CategoryEditView,
#    CategoryDeleteView,
 ) # new

urlpatterns = [

path('accounts/', include('django.contrib.auth.urls')),
path('accounts/', include('accounts.urls')),
#path('about/', AboutPageView.as_view(), name='about'), # new
path('', HomePageView.as_view(), name='home'),
#path('login/', LoginPageView.as_view(), name='login'),
#path('signup/', SignupPageView.as_view(), name='signup'),
#path('', LoginFormView.as_view(), name='form'),
#path('categories/', CategoryListView.as_view(), name='category_list',),
#path('categories/new', CategoryCreateView.as_view(), name='category_new',),
#path('<int:pk>/detail', CategoryDetailView.as_view(), name='category_detail',),
#path('<int:pk>/edit', CategoryEditView.as_view(), name='category_edit',),
#path('<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete',),
path('admin/', admin.site.urls),
#path(r'^admin/', admin.site.urls),#new
path(r'^$', index, name="TodoList"), #new
]