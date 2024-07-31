from django.shortcuts import render
from django.views import View
from ipam.models import Prefix
import ipaddress
import .configuration
# Juniper
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError, ConfigLoadError, CommitError, ConnectAuthError, RpcTimeoutError

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
    return render(
        request,
        self.template_name
    )
    def post(self,request):
        ip=request.POST.get("IP","")
        prefix=check_ip_in_prefix(ip)
        if prefix:
            for de in gw:
                with Device(de) as dev:
                    with Config(dev, mode='private') as conf_dev:
                        commit_cmd = f'set interfaces ae10 unit 0 family inet address {prefix} arp {ip} mac 00:01:00:02:00:03'
                        
                        
            
            
            
    
