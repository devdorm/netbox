from extras.scripts import Script
from ipam.models import Prefix, IPAddress

class AssignedIPsFromPrefix(Script):
    class Meta:
        name = "List Assigned IPs from Prefix"
    
    prefix = ObjectVar(model=Prefix)

    def run(self, data, commit):
        prefix = data['prefix']
        ips = IPAddress.objects.filter(address__net_host_contained=prefix.prefix)
        output = "\n".join(str(ip.address) for ip in ips)
        return output
