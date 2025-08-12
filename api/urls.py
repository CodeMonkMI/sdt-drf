from django.db import router
from django.urls import include, path, re_path
from rest_framework import routers
from book.views import BookViewSet
from author.views import AuthorViewSet
from borrow_record.views import BorrowBookViewSet, ReturnBookViewSet

router = routers.SimpleRouter()

router.register(
    "books",
    BookViewSet,
    basename="books",
)
router.register(
    "authors",
    AuthorViewSet,
    basename="authors",
)

router.register(
    "borrow",
    BorrowBookViewSet,
    basename="borrow",
)
router.register(
    "return",
    ReturnBookViewSet,
    basename="return",
)


urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    re_path("auth/", include("djoser.urls")),
    re_path("auth/", include("djoser.urls.jwt")),
]
