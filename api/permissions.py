from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()


class IsLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user.groups.filter(name="librarian").exists()


class IsLibrarian(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user.groups.filter(name="librarian").exists()
