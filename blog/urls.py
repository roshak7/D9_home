from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.RetrieveAuthorView.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.RetrieveBookView.as_view())
)
