from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.views import static
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

app_name = 'blog'
urlpatterns = [
    path('', views.PrivateView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
    path(r'login/', LoginView.as_view(), name='login'),
    url(r'mdeditor/', include('mdeditor.urls')),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
