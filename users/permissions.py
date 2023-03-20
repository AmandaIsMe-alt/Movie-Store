from rest_framework import permissions
from rest_framework.views import Request, View


class PermissionsPersonalized(permissions.BasePermission):

    def has_object_permission(self, Request, View, obj):
        if Request.user.is_employee:
            return True

        else: not Request.user.is_employee
        return Request.user == obj
