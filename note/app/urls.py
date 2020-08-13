from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
path('',views.NoteListView.as_view(),name='list'),
path('<int:pk>/',views.NoteDetailView.as_view(),name='detail'),
path('create/',views.NoteCreateView.as_view(),name='create'),
path('update/<int:pk>/',views.NoteUpdateView.as_view(),name='update'),
path('delete/<int:pk>/',views.NoteDeleteView.as_view(),name='delete')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)