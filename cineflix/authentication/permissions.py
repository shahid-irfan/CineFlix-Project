from django.shortcuts import redirect

def permitted_user_roles(roles):
    """
    Check if the user has permission to access certain resources.
    A permitted user is defined as one who is active and has the 'can_access' permission.
    """

    def decorator(fn):

        def wrapper(request, *args, **kwargs):
            # Check if the user is authenticated

            if request.user.is_authenticated and request.user.role in roles:
            #  Check if the user is active and has the required role\

                return fn(request, *args, **kwargs)
                #   ee function namal call cheynnath because permission undenkil 

            else:

                return redirect('home')
                #  permission illaathath kond home pageilekku redirect cheyyunnm

        return wrapper
    
    return decorator
            



