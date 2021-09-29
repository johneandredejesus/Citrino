from datadefinition import Oper
from xml.etree.ElementTree import SubElement
from methods import  is_not_none, force_type


class  Host(Oper):
    
    @force_type
    def __init__(self, host_name: str):
        """
        IP domain-name, lookup style, nameservers for specific host.

        host_name: str. Hostname.
        """

        super().__init__('ip-domain-oper:host')

        if is_not_none(host_name):
            host_name_ = SubElement(self, 'ip-domain-oper:host-name')
            host_name_.text = host_name


class  Hosts(Oper):

    def __init__(self):
        """List of domain hosts."""

        super().__init__('ip-domain-oper:hosts')
    
    @force_type
    def host(self, value: Host):

        if is_not_none(value):
            self.append(value)


class Server(Oper):

    def __init__(self):
        """Domain server data."""

        super().__init__('ip-domain-oper:server')


class  VRF(Oper):
    
    @force_type
    def __init__(self, vrf_name: str, server: Server = None, hosts: Hosts = None):
        """
        VRF instance.

        server: Server. Domain server data.

        hosts: Hosts. List of domain hosts.
        """

        super().__init__('ip-domain-oper:vrf')
        
        if is_not_none(vrf_name):
            vrf_name_ = SubElement(self, 'ip-domain-oper:vrf-name')
            vrf_name_.text = vrf_name
        
        if is_not_none(server):
            server_ = SubElement(self, 'ip-domain-oper:server')
            server_.text = server

        if is_not_none(hosts):
            self.append(hosts)


class VRFS(Oper):
    
    def __init__(self):
        """List of VRFs."""

        super().__init__('ip-domain-oper:vrfs')
    
    @force_type
    def vrf(self, value: VRF):
        
        if is_not_none(value):
            self.append(value)


class IPDomainOper(Oper):
    
    @force_type
    def __init__(self, vrfs: VRFS = None):
        """
        module: Cisco-IOS-XR-ip-domain-oper.

        Domain server and host data.
        """

        super().__init__('ip-domain-oper:ip-domain')

        self.set('xmlns:ip-domain-oper', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-oper')

        if is_not_none(vrfs):
            self.append(vrfs)
