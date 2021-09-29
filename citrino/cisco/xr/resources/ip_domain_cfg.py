from datadefinition import OperationEnum, Cfg
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type


class IPV4Host(Cfg):
    
    @force_type
    def __init__(self, host_name: str, operation: OperationEnum.Operation = None):
        """
        Host name and up to 8 host IPv4 addresses.

        host_name: str. A hostname.
        """
        
        super().__init__('ip-domain-cfg:ipv4-host')
        
        if is_not_none(host_name):
            host_name_ = SubElement(self, 'ip-domain-cfg:host-name')
            host_name_.text = host_name

        if is_not_none(operation):
            self.set('xc:operation', operation.value)
    
    @force_type
    def address(self, value: str, operation: OperationEnum.Operation = None):
        """
        Host IPv4 addresses.

        value: str. type inet:ipv4-address-no-zone.

        min-elements 1.
        
        max-elements 8.
        """

        address_ = SubElement(self, 'ip-domain-cfg:address')

        if is_not_none(value):
            address_.text = value
        
        if is_not_none(operation):
            address_.set('xc:operation', operation.value)

class  IPV4Hosts(Cfg):
    
    @force_type
    def __init__(self):
        """Host name and up to 8 host IPv4 addresses."""

        super().__init__('ip-domain-cfg:ipv4-hosts')
    
    @force_type
    def ipv4_host(self, value: IPV4Host):

        if is_not_none(value):
            self.append(value)


class List(Cfg):
    
    @force_type
    def __init__(self, order: int, list_name: str, operation: OperationEnum.Operation = None):
        """
        Domain name to complete unqualified host names.

        order: int. This is used to sort the names in the order of precedence.

        list_name: str. A domain name.
        """

        super().__init__('ip-domain-cfg:list')

        if is_not_none(order):
            order_ = SubElement(self, 'ip-domain-cfg:order')
            order_.text = convert_to_string(order)
        
        if is_not_none(list_name):
            list_name_ = SubElement(self, 'ip-domain-cfg:list-name')
            list_name_.text = list_name
        
        if is_not_none(operation):
            self.set('xc:operation', operation.value)


class Lists(Cfg):
    
    @force_type
    def __init__(self):
        """Domain names to complete unqualified host names."""

        super().__init__('ip-domain-cfg:lists')
    
    @force_type
    def list(self, list_: List):

        if is_not_none(list_):
            self.append(list_)


class Server(Cfg):
    
    @force_type
    def __init__(self, order: int, server_address: str, operation: OperationEnum.Operation = None):
        """
        Name server address.
        
        order: int. This is used to sort the servers in the order of precedence.

        server_address: str. type inet:ip-address-no-zone. A name server address.
        """

        super().__init__('ip-domain-cfg:server')

        if is_not_none(order):
            order_ = SubElement(self, 'ip-domain-cfg:order')
            order_.text = convert_to_string(order)
        
        if is_not_none(server_address):
            server_address_ = SubElement(self, 'ip-domain-cfg:server-address')
            server_address_.text = server_address
        
        if is_not_none(operation):
            self.set('xc:operation', operation.value)


class Servers(Cfg):

    def __init__(self):
        """Name server addresses."""

        super().__init__('ip-domain-cfg:servers')
    
    @force_type
    def server(self, value: Server):

        if is_not_none(value):
            self.append(value)


class IPV6Host(Cfg):
    
    @force_type
    def __init__(self, host_name: str, operation: OperationEnum.Operation = None):
        """
        Host name and up to 4 host IPv6 addresses.

        host_name: str. A hostname.
        """

        super().__init__('ip-domain-cfg:ipv6-host')

        if is_not_none(host_name):
            host_name_ = SubElement(self, 'ip-domain-cfg:host-name')
            host_name_.text = host_name
        
        if is_not_none(operation):
            self.set('xc:operation', operation.value)
    
    @force_type
    def address(self, value: str, operation: OperationEnum.Operation = None):
        """
        Host IPv6 addresses.

        value: str. type inet:ipv6-address-no-zone.

        min-elements 1.

        max-elements 4.
        """

        address_ = SubElement(self, 'ip-domain-cfg:address')

        if is_not_none(value):
            address_.text = value
        
        if is_not_none(operation):
            address_.set('xc:operation', operation.value)


class  IPV6Hosts(Cfg):

    def __init__(self):
        """IPv6 host."""

        super().__init__('ip-domain-cfg:ipv6-hosts')
    
    @force_type
    def ipv6_host(self, value: IPV6Host):
        
        if is_not_none(value):
            self.append(value)


class VRF(Cfg):
    
    @force_type
    def __init__(self, vrf_name: str, ipv6_hosts: IPV6Hosts = None, servers: Servers = None,
                       lists: Lists = None, ipv4_hosts: IPV4Hosts = None, operation: OperationEnum.Operation = None):
        """
        vrf_name: str. VRF specific data. Name of the VRF instance.
        
        ipv6_hosts: IPV6Hosts. IPv6 host.

        servers: Servers. Name server addresses.

        lists: Lists. Domain names to complete unqualified host names.
        
        ipv4_hosts: IPV4Hosts. Host name and up to 8 host IPv4 addresses.
        """

        super().__init__('ip-domain-cfg:vrf')

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(self, 'ip-domain-cfg:vrf-name')
            vrf_name_.text = vrf_name

        if is_not_none(ipv6_hosts):
            self.append(ipv6_hosts)
        
        if is_not_none(servers):
            self.append(servers)
        
        if is_not_none(lists):
            self.append(lists)
        
        if is_not_none(ipv4_hosts):
            self.append(ipv4_hosts)
        
        if is_not_none(operation):
            self.set('xc:operation', operation.value)
    
    @force_type
    def lookup(self, operation: OperationEnum.Operation = None):
        """Disable Domain Name System hostname translation."""

        lookup_ = SubElement(self, 'ip-domain-cfg:lookup')

        if is_not_none(operation):
            lookup_.set('xc:operation', operation.value)
    
    @force_type
    def multicast_domain(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Default multicast domain name.
        
        value: str.
        """

        multicast_domain_ = SubElement(self, 'ip-domain-cfg:multicast-domain')

        if is_not_none(value):
            multicast_domain_.text = value
        
        if is_not_none(operation):
            multicast_domain_.set('xc:operation', operation.value)
    
    @force_type
    def source_interface(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Specify interface for source address in connections.

        value: str. type xr:Interface-name.
        """

        source_interface_ =  SubElement(self, 'ip-domain-cfg:source-interface')

        if is_not_none(value):
            source_interface_.text = value
        
        if is_not_none(operation):
            source_interface_.set('xc:operation', operation.value)
    
    @force_type
    def name(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Default domain name. 

        value: str.
        """

        name_ = SubElement(self, 'ip-domain-cfg:name')
        
        if is_not_none(value):
            name_.text = value
        
        if is_not_none(operation):
            name_.set('xc:operation', operation.value)


class VRFS(Cfg):

    def __init__(self):
        """VRF table."""

        super().__init__('ip-domain-cfg:vrfs')
    
    @force_type
    def vrf(self, value: VRF):
        
        if is_not_none(value):
            self.append(value)


class IPDomainCfg(Cfg):
    
    @force_type
    def __init__(self, vrfs: VRFS = None):
        """IP domain configuration."""

        super().__init__('ip-domain-cfg:ip-domain')

        self.set('xmlns:ip-domain-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-cfg')

        if is_not_none(vrfs):
            self.append(vrfs)