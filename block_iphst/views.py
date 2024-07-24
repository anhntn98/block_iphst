from django.shortcuts import render
from django.views import View

class BlockIP(View):
    template_name = 'blockip.html'
    
    def get(self, request):
        return render(
            request,
            self.template_name
        )

