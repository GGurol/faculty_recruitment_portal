from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if not request.user.is_authenticated and self.requires_login(request.path):
            return redirect('user_login')
        
        return response
    
    def requires_login(self, path):
        paths_requiring_login = ['/page1/', '/page2/', '/page3/']
       
        return any(path.startswith(path_requirement) for path_requirement in paths_requiring_login)
