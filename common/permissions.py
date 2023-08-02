from rest_framework import permissions


class AgentPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if (request.user.is_authenticated and request.user.is_agent) or request.user.is_superuser or request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        # if request.method in permissions.SAFE_METHODS:
        #     return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False

class IsNotAgentAndIsEmployee(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if (request.user.is_authenticated and (not request.user.is_agent) and request.user.is_staff) or request.user.is_superuser or request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        # if request.method in permissions.SAFE_METHODS:
        #     return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False

class LeadPermission(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if (request.user.is_authenticated and request.user.is_customer) or request.user.is_superuser or request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True

        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # if request.user.is_staff and request.method not in self.edit_methods:
        #     return True

        return False