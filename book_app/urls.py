from django.urls import path
from book_app.views import BookListCreateView, BookRetrieveUpdateDestroyView, AuthorListCreateView, AuthorRetrieveUpdateDestroyView

urlpatterns = [
    # 작가
    path("author", AuthorListCreateView.as_view(), name="author-list-create"),
    path("author/<int:pk>", AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail-update-destroy'),
    # 책
    path("book", BookListCreateView.as_view(), name="book-list-create"),
    path("book/<int:pk>", BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-destroy'),
]

