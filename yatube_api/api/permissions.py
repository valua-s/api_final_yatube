from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated) or (
            request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (view.action == 'retrieve' or request.user == obj.author)


class AuthorOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
