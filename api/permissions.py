from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """
    Custom permission to permit only active users access.
    """
    def has_permission(self, request, view):
        """
        Checks whether the user making the request is an active user.
        """
        return request.user.is_active