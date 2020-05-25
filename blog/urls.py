from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'about', views.AboutView.as_view(), name='about'),
    path(r'contact', views.ContactView.as_view(), name='contact'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
