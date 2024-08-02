from django.shortcuts import render
from django.views import View
from ipam.models import Prefix, IPAddress
import ipaddress
from adsl2nb import settings
# Juniper
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from django.contrib import messages
from django.shortcuts import redirect



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
    for network in networks:
        if ip in network:
            return network
    return False

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
        return redirect('BlockIp')
    def post(self,request):
        ip=request.POST.get("IP","")
        prefix=check_ip_in_prefix(ip)
        if prefix:
            for de in settings.gw:
                try:
                    with Device(de) as dev:
                        with Config(dev, mode='private') as conf_dev:
                            commit_cmd = f'set interfaces ae10 unit 0 family inet address {prefix} arp {ip} mac 00:01:00:02:00:03'
                            try:
                                conf_dev.load(commit_cmd, format='set')
                                conf_dev.commit(comment='Block IP')
                                ipadd=str(ip) + "/24"
                                ipaddr=IPAdrress.objects.getorcreate(address=ip)
                                ipaddr.snapshot()
                                ipaddr.status="disable"
                                ipaddr.comments="IP chua duoc dang ky ma da su dung. Block"                                             
                                    
                            except:
                                messages.success(request, "Cannot block IP in gw {}".format(de))
                                return redirect('BlockIp')
                except:
                    messages.success(request, "Cannot block IP in gw {}".format(de))
                    return redirect('BlockIp')   
        else:
            messages.success(request, 'IP invalid.')
            return redirect('BlockIp')

class Remove_Block(View):
    pass                
                
                        
                        
            
            
            
    
