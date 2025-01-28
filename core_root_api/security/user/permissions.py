from rest_framework.permissions import BasePermission

class IsAccountNotFrozen(BasePermission):
    """
    Custom permission to check if the user's account is not frozen.
    """

    message = "Your account is frozen. Please contact support for assistance."

    def has_permission(self, request, view):
        print(f"Authenticated: {request.user.is_authenticated}")
        print(f"User Frozen: {getattr(request.user, 'is_freeze', None)}")

        if not request.user or not request.user.is_authenticated:
            self.message = "Authentication credentials were not provided."
            return False

        if request.user.is_freeze:
            self.message = "Your account is frozen. Please contact support for assistance."
            return False

        return True
