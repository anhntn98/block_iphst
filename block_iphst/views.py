from django.shortcuts import render
from django.views import View

class BlockIP(View):
    template_name = 'block_iphst/blockip.html'
    
    def get(self, request):
        return render(
            request,
            self.template_name
        )

