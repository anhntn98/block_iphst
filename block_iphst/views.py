from django.shortcuts import render
from django.views import View
from ipam.models import Prefix
import ipaddress

def check_ip_in_prefix(ip):
    try:
        ip = ipaddress.ip_address(ip)
    except:
        return False
    networks = [
    ipaddress.ip_network('119.17.253.0/24'),
    ipaddress.ip_network('202.151.168.0/24'),
    ipaddress.ip_network('210.86.239.0/24')
    ]
    return any(ip in network for network in networks)

class BlockIP(View):
    template_name = 'block_iphst/blockip.html'
    
    def get(self, request):
        return render(
            request,
            self.template_name
        )
class Add_Block(View):
    template_name = 'block_iphst/blockip.html'
    def get(self, request):
    return render(
        request,
        self.template_name
    )
    def post(self,request):
        ip=request.POST.get("IP","")
        if check_ip_in_prefix(ip):
            
            
            
            
    
