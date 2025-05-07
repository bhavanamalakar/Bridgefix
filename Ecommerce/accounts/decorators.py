from django.core.exceptions import PermissionDenied

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # Get the user's roles as a list of names
            user_roles = request.user.role.values_list('name', flat=True)

            # Check if any of the user's roles are in the allowed roles
            for role in user_roles:
                if role in allowed_roles:
                    return view_func(request, *args, **kwargs)

            # If no matching role is found, deny access
            raise PermissionDenied

        return wrapper
    return decorator
