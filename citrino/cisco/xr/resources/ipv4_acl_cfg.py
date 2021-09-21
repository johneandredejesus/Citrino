from datatype import TypeDef
from datadefinition import OperationEnum, Cfg
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type

class IPV4AclGrantEnum():
    """Ipv4 acl grant enum."""

    class IPV4AclGrant(TypeDef):
        def __init__(self, value):
            super().__init__(value)

    DENY = IPV4AclGrant('deny')
    PERMIT = IPV4AclGrant('permit')


class IPV4AclOperatorEnum():
    """
    Ipv4 acl operator enum.

    EQUAL: Match only packets on a given port number.
  
    GREATER_THAN: Match only packet with a greater port number.
  
    LESS_THAN: Match only packet with a lower port number.
  
    NOT_EQUAL: Match only packets not on a given port number.
  
    RANGE: Match only packets in the range of port numbers.
    """

    class IPV4AclOperator(TypeDef):
       
       def __init__(self, value):
          super().__init__(value)

    EQUAL = IPV4AclOperator('equal')
    GREATER_THAN= IPV4AclOperator('greater-than')
    LESS_THAN = IPV4AclOperator('less-than')
    NOT_EQUAL = IPV4AclOperator('not-equal')
    RANGE = IPV4AclOperator('range')


class IPV4AclProtocolNumber():
    """
    Ipv4 acl protocol number.
    
    IP: Any IP protocol.
    
    ICMP: Internet Control Message Protocol.
  
    IGMP: Internet Gateway Message Protocol.
    
    IP_IN_IP: IP in IP tunneling.
  
    TCP: Transport Control Protocol.
  
    IGRP: Cisco's IGRP Routing Protocol.
  
    UDP: User Datagram Protocol.
  
    GRE: Cisco's GRE tunneling.
  
    ESP: Encapsulation Security Protocol.
  
    AHP: Authentication Header Protocol.
  
    EIGRP: Cisco's EIGRP Routing Protocol.
  
    OSPF: OSPF Routing Protocol.
  
    NOS: KA9Q NOS Compatible IP over IP tunneling.
  
    PIM: Protocol Independent Multicast.
  
    PCP : Payload Compression Protocol.
  
    SCTP: Stream Control Transmission Protocol.
    """
    IP = 0
    ICMP = 1
    IGMP = 2
    IP_IN_IP = 4
    TCP = 6
    IGRP = 9
    UDP = 17
    GRE = 47
    ESP = 50
    AHP = 51
    EIGRP = 88
    OSPF = 89
    NOS = 94
    PIM = 103
    PCP = 108
    SCTP = 132


class  IPV4AclPortNumber():
    """
    Ipv4 acl port number.
  
    ECHO: Match on the 'echo' port number.
      
    DISCARD: Match on the 'discard' port number.
  
    DAYTIME: Match on the 'daytime' port number (TCP/SCTP only).
      
    CHAR_GEN: Match on the 'chargen' port number (TCP/SCTP only).
    
    FTP_DATA: Match on the FTP data connections port number (TCP/SCTP only).
  
    FTP: Match on the 'ftp' port number (TCP/SCTP only).
      
    TELNET: Match on the 'telnet' port number (TCP/SCTP only).
  
    SMTP: Match on the 'smtp' port number (TCP/SCTP only).
  
    TIME: Match on the 'time' port number.
  
    NAME_SERVER: Match on the IEN116 name service port number (UDP only).
  
    WHO_IS: Match on the 'nicname' port number (TCP/SCTP only).
  
    TACACS: Match on the 'tacacs' port number.
  
    DNS: Match on the 'dns' port number.
  
    BOOT_PS: Match on the Bootstrap Protocol server port number (UDP only).
  
    BOOT_PC: Match on the Bootstrap Protocol client port number (UDP only).
  
    TFTP: Match on the 'tftp' port number (UDP only).
      
    GOPHER: Match on the 'gopher' port number (TCP/SCTP only).
  
    FINGER: Match on the 'finger' port number (TCP/SCTP only).
  
    WWW: Match on the 'http' port number (TCP/SCTP only).
  
    HOST_NAME: Match on the NIC hostname server port number (TCP/SCTP only).
  
    POP2: Match on the 'pop2' port number (TCP/SCTP only).
      
    POP3: Match on the 'pop3' port number (TCP/SCTP only).
  
    SUN_RPC: Match on the Sun RPC port number.
  
    IDENT: Match on the 'ident' port number (TCP/SCTP only).
  
    NNTP: Match on the 'nntp' port number (TCP/SCTP only).
  
    NTP:Match on the 'ntp' port number (UDP only).
  
    NET_BIOS_NS: Match on the NetBIOS name service port number (UDP only).
  
    NET_BIOS_DGS: Match on the NetBIOS datagram service port number (UDP only).
  
    NET_BIOS_SS: Match on the NetBIOS session service port number (UDP only).
     
    SNMP: Match on the 'snmp' port number (UDP only).
  
    SNMP_TRAP: Match on the SNMP traps port number (UDP only).
  
    XDMCP: Match on the 'xdmcp' port number (UDP only).
  
    BGP: Match on the 'bgp' port number (TCP/SCTP only).
  
    IRC: Match on the 'irc' port number (TCP/SCTP only).
  
    DNSIX: Match on the DNSIX security protocol auditing port number (UDP only).
  
    MOBILE_IP: Match on the mobile IP registration port number (UDP only).
  
    PIM_AUTO_RP: Match on the PIM Auto-RP port number.
  
    ISAKMP: Match on the 'isakmp' port number (UDP only).
  
    EXEC_OR_BIFF: Match on the port used by TCP/SCTP for 'exec' and by UDP for 'biff'.
  
    LOGIN_OR_WHO: Match on the port used by TCP/SCTP for 'login' and by UDP for 'rwho'.
  
    CMD_OR_SYSLOG: Match on the port used by TCP/SCTP for 'rcmd' and by UDP for 'syslog'.
  
    LPD: Match on the 'lpd' port number (TCP/SCTP only).
    
    TALK: Match on the 'talk' port number.
  
    RIP: Match on the 'rip' port number (UDP only).
  
    UUCP: Match on the 'uucp' port number (TCP/SCTP only).
  
    KLOGIN: Match on the Kerberos login port number (TCP/SCTP only).
  
    KSHELL: Match on the Kerberos shell port number (TCP/SCTP only).
  
    LDP: Match on the LDP port.
    """
  
    ECHO = 7
    DISCARD = 9
    DAYTIME = 13
    CHAR_GEN = 19
    FTP_DATA = 20
    FTP = 21
    TELNET = 23
    SMTP = 25
    TIME = 37
    NAME_SERVER = 42
    WHO_IS = 43
    TACACS = 49
    DNS = 53
    BOOT_PS = 67
    BOOT_PC = 68
    TFTP = 69
    GOPHER = 70
    FINGER = 79
    WWW = 80
    HOST_NAME = 101
    POP2 = 109
    POP3 = 110
    SUN_RPC = 111
    IDENT = 113
    NNTP = 119
    NTP = 123
    NET_BIOS_NS = 137
    NET_BIOS_DGS = 138
    NET_BIOS_SS = 139
    SNMP = 161
    SNMP_TRAP = 162
    XDMCP = 177
    BGP = 179
    IRC = 194
    DNSIX  = 195
    MOBILE_IP = 434
    PIM_AUTO_RP = 496
    ISAKMP = 500
    EXEC_OR_BIFF = 512
    LOGIN_OR_WHO = 513
    CMD_OR_SYSLOG = 514
    LPD = 515
    TALK = 517
    RIP = 520
    UUCP = 540
    KLOGIN = 543
    KSHELL = 544
    LDP = 646


class IPV4AclICMPTypeCodeEnum():
    """
    Ipv4 acl icmp type code enum.
     
    NETWORK_UNREACHABLE: Network unreachable.
  
    ECHO_REPLY: Echo reply.
    
    HOST_UNREACHABLE: Host unreachable.
  
    PROTOCOL_UNREACHABLE: Protocol unreachable.
    
    PORT_UNREACHABLE: Port unreachable.
  
    PACKET_TOO_BIG: Fragmentation needed and DF set.
  
    SOURCE_ROUTE_FAILED: Source route failed.
  
    NETWORK_UNKNOWN: Network unknown.
  
    HOST_UNKNOWN: Host unknown.
  
    HOST_ISOLATED: Host isolated.
  
    DOD_NET_PROHIBITED: Network prohibited.
  
    DOD_HOST_PROHIBITED: Host prohibited.
  
    HOST_TOS_UNREACHABLE: Host unreachable for TOS.
  
    NET_TOS_UNREACHABLE: Network unreachable for TOS.
  
    ADMINISTRATIVELY_PROHIBITED: Administratively prohibited.
  
    HOST_PRECEDENCE_UNREACHABLE: Host unreachable for precedence.
  
    PRECEDENCE_UNREACHABLE: Precedence cutoff.
  
    UNREACHABLE: All unreachables.
  
    SOURCE_QUENCH: Source quenches.
  
    NETWORK_REDIRECT: Network redirect.
  
    HOST_REDIRECT: Host redirect.
  
    NET_TOS_REDIRECT: Network redirect for TOS.
  
    HOST_TOS_REDIRECT: Host redirect for TOS.
  
    REDIRECT: All redirects.
  
    ALTERNATE_ADDRESS: Alternate address.
  
    ECHO: Echo (ping).
  
    ROUTER_ADVERTISEMENT: Router discovery advertisements.
  
    ROUTER_SOLICITATION: Router discovery solicitations.
  
    TTL_EXCEEDED: TTL exceeded.
  
    REASSEMBLY_TIMEOUT: Reassembly timeout.
  
    TIME_EXCEEDED: All time exceeds.
  
    GENERAL_PARAMETER_PROBLEM: Parameter problem.
  
    OPTION_MISSING: Parameter required but not present.
  
    NO_ROOM_FOR_OPTION: Parameter required but no room.
  
    PAMETER_PROBLEM: All parameter problems.
  
    TIMESTAMP_REQUEST: Timestamp requests.
  
    TIMESTAMP_REPLY: Timestamp replies.
  
    INFORMATION_REQUEST: Information request.
  
    INFORMATION_REPLY: Information replies.
  
    MASK_REQUEST: Mask requests.
  
    MASK_REPLY: Mask replies.
  
    TRACEROUTE: Traceroute.
  
    CONVERSION_ERROR: Datagram conversion.
    """

    class IPV4AclICMPTypeCode(TypeDef):
        def __init__(self, value):
            super().__init__(value)
      
    ECHO_REPLY = IPV4AclICMPTypeCode('echo-reply')
    NETWORK_UNREACHABLE = IPV4AclICMPTypeCode('network-unreachable')
    HOST_UNREACHABLE = IPV4AclICMPTypeCode('host-unreachable')
    PROTOCOL_UNREACHABLE = IPV4AclICMPTypeCode('protocol-unreachable')
    PORT_UNREACHABLE = IPV4AclICMPTypeCode('port-unreachable')
    PACKET_TOO_BIG = IPV4AclICMPTypeCode('packet-too-big')
    SOURCE_ROUTE_FAILED = IPV4AclICMPTypeCode('source-route-failed')
    NETWORK_UNKNOWN = IPV4AclICMPTypeCode('network-unknown')
    HOST_UNKNOWN = IPV4AclICMPTypeCode('host-unknown')
    HOST_ISOLATED = IPV4AclICMPTypeCode('host-isolated')
    DOD_NET_PROHIBITED = IPV4AclICMPTypeCode('dod-net-prohibited')
    DOD_HOST_PROHIBITED = IPV4AclICMPTypeCode('dod-host-prohibited')
    HOST_TOS_UNREACHABLE = IPV4AclICMPTypeCode('host-tos-unreachable')
    NET_TOS_UNREACHABLE = IPV4AclICMPTypeCode('net-tos-unreachable')
    ADMINISTRATIVELY_PROHIBITED = IPV4AclICMPTypeCode('administratively-prohibited')
    HOST_PRECEDENCE_UNREACHABLE = IPV4AclICMPTypeCode('host-precedence-unreachable')
    PRECEDENCE_UNREACHABLE = IPV4AclICMPTypeCode('precedence-unreachable')
    UNREACHABLE = IPV4AclICMPTypeCode('unreachable')
    SOURCE_QUENCH = IPV4AclICMPTypeCode('source-quench')
    NETWORK_REDIRECT = IPV4AclICMPTypeCode('network-redirect')
    HOST_REDIRECT = IPV4AclICMPTypeCode('host-redirect')
    NET_TOS_REDIRECT = IPV4AclICMPTypeCode('net-tos-redirect')
    HOST_TOS_REDIRECT = IPV4AclICMPTypeCode('host-tos-redirect')
    REDIRECT = IPV4AclICMPTypeCode('redirect')
    ALTERNATE_ADDRESS = IPV4AclICMPTypeCode('alternate-address')
    ECHO = IPV4AclICMPTypeCode('echo')
    ROUTER_ADVERTISEMENT = IPV4AclICMPTypeCode('router-advertisement')
    ROUTER_SOLICITATION = IPV4AclICMPTypeCode('router-solicitation')
    TTL_EXCEEDED = IPV4AclICMPTypeCode('ttl-exceeded')
    REASSEMBLY_TIMEOUT = IPV4AclICMPTypeCode('reassembly-timeout')
    TIME_EXCEEDED = IPV4AclICMPTypeCode('time-exceeded')
    GENERAL_PARAMETER_PROBLEM = IPV4AclICMPTypeCode('general-parameter-problem')
    OPTION_MISSING = IPV4AclICMPTypeCode('option-missing')
    NO_ROOM_FOR_OPTION = IPV4AclICMPTypeCode('no-room-for-option')
    PAMETER_PROBLEM = IPV4AclICMPTypeCode('parameter-problem')
    TIMESTAMP_REQUEST = IPV4AclICMPTypeCode('timestamp-request')
    TIMESTAMP_REPLY = IPV4AclICMPTypeCode('timestamp-reply')
    INFORMATION_REQUEST = IPV4AclICMPTypeCode('information-request')
    INFORMATION_REPLY = IPV4AclICMPTypeCode('information-reply')
    MASK_REQUEST = IPV4AclICMPTypeCode('mask-request')
    MASK_REPLY = IPV4AclICMPTypeCode('mask-reply')
    TRACEROUTE = IPV4AclICMPTypeCode('traceroute')
    CONVERSION_ERROR = IPV4AclICMPTypeCode('conversion-error')


class IPV4AclTCPBitsNumber():
    """
    Ipv4 acl tcp bits number.
  
    FIN: Match on the FIN bit (0x01).
  
    SYN: Match on the SYN bit (0x02).
  
    RST: Match on the RST bit (0x04).
  
    PSH: Match on the PSH bit (0x08).
  
    ACK: Match on the ACK bit (0x10).
  
    URG: Match on the URG bit (0x20).
    """
    class IPV4AclTCPBitNumber(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
      
    FIN = IPV4AclTCPBitNumber('fin')
    SYN = IPV4AclTCPBitNumber('syn')
    RST = IPV4AclTCPBitNumber('rst')
    PSH = IPV4AclTCPBitNumber('psh')
    ACK = IPV4AclTCPBitNumber('ack')
    URG = IPV4AclTCPBitNumber('urg')


class IPV4AclTCPMATCHOPERATOREnum():
    """
    Ipv4 acl tcp match operator enum.
  
    MATCH_ALL: Match only packet with all the given TCP bits.
  
    MATCH_ANY: Match only packet with any of the given TCP bits.
    """

    class IPV4AclTCPMATCHOPERATOR(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
    
    MATCH_ALL = IPV4AclTCPMATCHOPERATOR('match-all')
    MATCH_ANY = IPV4AclTCPMATCHOPERATOR('match-any')


class IPV4AclFragFlags():
    """
    Ipv4 acl frag flags.
  
    DONT_FRAGMENT: Match don't fragment flag.
  
    IS_FRAGMENT: Match is fragment flag.
  
    FIRST_FRAGMENT: Match first fragment flag.
  
    LAST_FRAGMENT: Match last fragment flag.
  
    DONT_FRAGMENT_IS_FRAGMENT: Match don't fragment and is fragment flag.
  
    DONT_FRAGMENT_FIRST_FRAGMENT: Match don't fragment and first fragment flag.
  
    DONT_FRAGMENT_LAST_FRAGMENT: Match don't fragment and last fragment flag.
    """
  
    class IPV4AclFrag(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
  
    DONT_FRAGMENT = IPV4AclFrag('dont-fragment')
    IS_FRAGMENT = IPV4AclFrag('is-fragment')
    FIRST_FRAGMENT = IPV4AclFrag('first-fragment')
    LAST_FRAGMENT = IPV4AclFrag('last-fragment')
    DONT_FRAGMENT_IS_FRAGMENT = IPV4AclFrag('dont-fragment-is-fragment')
    DONT_FRAGMENT_FIRST_FRAGMENT = IPV4AclFrag('dont-fragment-first-fragment')
    DONT_FRAGMENT_LAST_FRAGMENT = IPV4AclFrag('dont-fragment-last-fragment')


class IPV4AclNextTopTypeEnum():
    """
    Next-hop type.
  
    NONE_NEXT_HOP: None next-hop.
  
    REGULAR_NEXT_HOP: Regular next-hop.
  
    DEFAULT_NEXT_HOP: Default next-hop.
    """
    class IPV4AclNextTopType(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
    
    NONE_NEXT_HOP = IPV4AclNextTopType('none-next-hop')
    REGULAR_NEXT_HOP = IPV4AclNextTopType('regular-next-hop')
    DEFAULT_NEXT_HOP = IPV4AclNextTopType('default-next-hop')


class IPV4AclIGMPNumbers():
    """
    Ipv4 acl igmp number
  
    HOST_QUERY: Host query.
  
    HOST_REPORT: Host report.
  
    DVMRP: Distance Vector Multicast Routing Protocol.
  
    PIM: Portocol Independent Multicast.
  
    TRACE: Multicast Trace.
  
    V2_REPORT: Version 2 report.
  
    V2_LEAVE: Version 2 leave.
  
    MTRACE_RESPONSE: MTrace response.
  
    MTRACE: MTrace.
  
    V3_REPORT: Version 3 report.
    """

    class IPV4AclIGMPNumber(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
    
    HOST_QUERY = IPV4AclIGMPNumber('host-query')
    HOST_REPORT = IPV4AclIGMPNumber('host-report')
    DVMRP  = IPV4AclIGMPNumber('dvmrp')
    PIM = IPV4AclIGMPNumber('pim')
    TRACE = IPV4AclIGMPNumber('trace')
    V2_REPORT = IPV4AclIGMPNumber('v2-report')
    V2_LEAVE = IPV4AclIGMPNumber('v2-leave')
    MTRACE_RESPONSE = IPV4AclIGMPNumber('mtrace-response')
    MTRACE  = IPV4AclIGMPNumber('mtrace')
    V3_REPORT = IPV4AclIGMPNumber('v3-report')


class IPV4AclDSCPNumbers():
    """
    Ipv4 acl dscp number.
  
    DEFAULT: Default DSCP.
  
    AF11: Match packets with AF11 DSCP.
  
    AF12: Match packets with AF12 DSCP.
  
    AF13: Match packets with AF13 DSCP.
  
    AF21: Match packets with AF21 DSCP.
  
    AF22: Match packets with AF22 DSCP.
  
    AF23: Match packets with AF23 DSCP.
  
    AF31: Match packets with AF31 DSCP.
  
    AF32: Match packets with AF32 DSCP.
  
    AF33: Match packets with AF33 DSCP.
    
    AF41: Match packets with AF41 DSCP.
  
    AF42: Match packets with AF42 DSCP.
  
    AF43: Match packets with AF43 DSCP.
  
    CS1: Match packets with CS1 (precedence 1) DSCP.
  
    CS2: Match packets with CS2 (precedence 2) DSCP.
  
    CS3: Match packets with CS3 (precedence 3) DSCP.
  
    CS4: Match packets with CS4 (precedence 4) DSCP.
  
    CS5: Match packets with CS5 (precedence 5) DSCP.
  
    CS6: Match packets with CS6 (precedence 6) DSCP.
  
    CS7: Match packets with CS7 (precedence 7) DSCP.
  
    EF: Match packets with EF DSCP.
    """

    class IPV4AclDSCPNumber(TypeDef):
        
        def __init__(self, value):
            super().__init__(value) 
    
    DEFAULT = IPV4AclDSCPNumber('default')
    AF11 = IPV4AclDSCPNumber('af11')
    AF12 =  IPV4AclDSCPNumber('af12')
    AF13 = IPV4AclDSCPNumber('af13')
    AF21 = IPV4AclDSCPNumber('af21')
    AF22 = IPV4AclDSCPNumber('af22')
    AF23 = IPV4AclDSCPNumber('af23')
    AF31 = IPV4AclDSCPNumber('af31')
    AF32 = IPV4AclDSCPNumber('af32')
    AF33 = IPV4AclDSCPNumber('af33')
    AF41 = IPV4AclDSCPNumber('af41')
    AF42 = IPV4AclDSCPNumber('af42')
    AF43 = IPV4AclDSCPNumber('af43')
    CS1 = IPV4AclDSCPNumber('cs1')
    CS2 = IPV4AclDSCPNumber('cs2')
    CS3 = IPV4AclDSCPNumber('cs3')
    CS4 = IPV4AclDSCPNumber('cs4')
    CS5 = IPV4AclDSCPNumber('cs5')
    CS6 = IPV4AclDSCPNumber('cs6')
    CS7 = IPV4AclDSCPNumber('cs7')
    EF = IPV4AclDSCPNumber('ef')


class  IPV4AclPrecedenceNumbers():
    """
    Ipv4 acl precedence number.
  
    CRITICAL: Match packets with critical precedence.
  
    FLASH: Match packets with flash precedence.
  
    FLASH_OVERRIDE: Match packets with flash override precedence.
  
    IMMEDIATE: Match packets with immediate precedence.
  
    INTERNET: Match packets with internetwork control precedence.
  
    NETWORK: Match packets with network control precedence.
    
    PRIORITY: Match packets with priority precedence.
  
    ROUTINE: Match packets with routine precedence.
    """
    class IPV4AclPrecedenceNumber(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
      
    CRITICAL = IPV4AclPrecedenceNumber('critical')
    FLASH = IPV4AclPrecedenceNumber('flash')
    FLASH_OVERRIDE = IPV4AclPrecedenceNumber('flash-override')
    IMMEDIATE = IPV4AclPrecedenceNumber('immediate')
    INTERNET = IPV4AclPrecedenceNumber('internet')
    NETWORK = IPV4AclPrecedenceNumber('network')
    PRIORITY = IPV4AclPrecedenceNumber('priority')
    ROUTINE = IPV4AclPrecedenceNumber('routine')


class IPV4AclLoggingEnum():
    """
    Ipv4 acl logging enum.
    
    LOG: Log matches against this entry.
  
    LOG_INPUT: Log matches against this entry, including input interface.
    """
    class IPV4AclLogging(TypeDef):
        
        def __init__(self, value):
            super().__init__(value)
      
    LOG = IPV4AclLogging('log')
    LOG_INPUT = IPV4AclLogging('log-input')


class IPV4AclNextHop(Cfg):
    
    def __init__(self):
        
        super().__init__('ipv4-acl-cfg:next-hop')

    @force_type
    def next_hop_type(self, value: IPV4AclNextTopTypeEnum.IPV4AclNextTopType = None, operation: OperationEnum.Operation = None):
        """
        Next-hop settings.

        value: IPV4AclNextTopTypeEnum.IPV4AclNextTopType. Next-hop type.
        
        """

        next_hop_type_ = SubElement(self, 'ipv4-acl-cfg:next-hop-type')
        
        if is_not_none(value):
            next_hop_type_.text = value.value
        
        if is_not_none(operation):
            next_hop_type_.set('xc:operation', operation.value)

    @force_type
    def next_hop_1(self, next_hop: str = None, vrf_name: str = None, track_name: str = None, operation: OperationEnum.Operation = None):
        """
        The first next-hop settings.

        next_hop: str. The IPv4 address of the next-hop.

        vrf_name: str. The VRF name of the next-hop. length "1..32".

        track_name: str. The object tracking name for the next-hop. length "1..32"
        
        """

        next_hop_1_ = SubElement(self, 'ipv4-acl-cfg:next-hop-1')

        if is_not_none(next_hop):
            next_hop_ = SubElement(next_hop_1_, 'ipv4-acl-cfg:next-hop')
            next_hop_.text = next_hop
    
        if is_not_none(vrf_name):
           vrf_name_ = SubElement(next_hop_1_, 'ipv4-acl-cfg:vrf-name')
           vrf_name_.text = vrf_name

        if is_not_none(track_name):
           track_name_ = SubElement(next_hop_1_, 'ipv4-acl-cfg:track-name')
           track_name_.text = track_name
        
        if is_not_none(operation):
            next_hop_1_.set('xc:operation', operation.value)
  
    @force_type
    def next_hop_2(self, next_hop: str = None, vrf_name: str = None, track_name: str = None, operation: OperationEnum.Operation = None):
        """
        The second next-hop settings.

        next_hop: str. The IPv4 address of the next-hop.

        vrf_name: str. The VRF name of the next-hop. length "1..32"

        track_name: str. The object tracking name for the next-hop. length "1..32
        """

        next_hop_2_ = SubElement(self, 'ipv4-acl-cfg:next-hop-2')
    
        if is_not_none(next_hop):
            next_hop_ = SubElement(next_hop_2_, 'ipv4-acl-cfg:next-hop')
            next_hop_.text = next_hop

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(next_hop_2_, 'ipv4-acl-cfg:vrf-name')
            vrf_name_.text = vrf_name

        if is_not_none(track_name):
            track_name_ = SubElement(next_hop_2_, 'ipv4-acl-cfg:track-name')
            track_name_.text = track_name
        
        if is_not_none(operation):
            next_hop_2_.set('xc:operation', operation.value)

    @force_type
    def next_hop_3(self, next_hop: str = None, vrf_name: str = None, track_name: str = None, operation: OperationEnum.Operation = None):
        """
        The third next-hop settings.
        
        next_hop: str. The IPv4 address of the next-hop.

        vrf_name: str. The VRF name of the next-hop. length "1..32".

        track_name: str. The object tracking name for the next-hop. length "1..32".
        """

        next_hop_3_ = SubElement(self, 'ipv4-acl-cfg:next-hop-3')

        if is_not_none(next_hop):
            next_hop_ = SubElement(next_hop_3_, 'ipv4-acl-cfg:next-hop')
            next_hop_.text = next_hop

        if is_not_none(vrf_name):
            vrf_name_ = SubElement(next_hop_3_ ,'ipv4-acl-cfg:vrf-name')
            vrf_name_.text = vrf_name

        if is_not_none(track_name):
            track_name_ = SubElement(next_hop_3_ ,'ipv4-acl-cfg:track-name')
            track_name_.text = track_name

        if is_not_none(operation):
            next_hop_3_.set('xc:operation', operation.value)


class IPV4AclAccessListEntry(Cfg):
    
    @force_type
    def __init__(self, sequence_number: int = None):
        """sequence_number: int. """
        
        super().__init__('ipv4-acl-cfg:access-list-entry')
      
        sequence_number_ = SubElement(self, 'ipv4-acl-cfg:sequence-number')

        if is_not_none(sequence_number):
           sequence_number_.text = convert_to_string(sequence_number)
  
    @force_type
    def grant(self, value: IPV4AclGrantEnum.IPV4AclGrant = None, operation: OperationEnum.Operation = None):
        """"
        Forwarding action for the packet. This is required for any non-remark ACE. Leave unspecified otherwise.

        value: IPV4AclGrantEnum.IPV4AclGrant. Ipv4-acl-grant-enum.
        """

        grant_ = SubElement(self, 'ipv4-acl-cfg:grant')

        if is_not_none(value):
            grant_.text = value.value
        
        if is_not_none(operation):
            grant_.set('xc:operation', operation.value)
  
    @force_type
    def protocol_operator(self, value:IPV4AclOperatorEnum.IPV4AclOperator = None, operation: OperationEnum.Operation = None):
        """
        Protocol operator. User can specify equal or leave it unspecified for singleton protocol match, or 
        specify range for protocol range match.

        value: IPV4AclOperatorEnum.IPV4AclOperator. Ipv4 acl operator enum.
        """
        protocol_operator_ = SubElement(self, 'ipv4-acl-cfg:protocol-operator')
      
        if is_not_none(value):
            protocol_operator_.text = value.value
        
        if is_not_none(operation):
            protocol_operator_.set('xc:operation', operation.value)
  
    @force_type
    def protocol(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Protocol number to match. It can be used for the lower bound (range operator) or single value (equal operator).
        Any value not in the permissible range will be rejected. When leave unspecified, default value is ipv4.";
        reference "RFC 758 - ASSIGNED INTERNET PROTOCOL NUMBERS.

        value: int. Ipv4 acl protocol number. range "0..255"
        """
        protocol_ = SubElement(self, 'ipv4-acl-cfg:protocol')

        if is_not_none(value):
            protocol_.text = convert_to_string(value)
        
        if is_not_none(operation):
            protocol_.set('xc:operation', operation.value)
  
    @force_type
    def protocol2(self, value:int = None, operation: OperationEnum.Operation = None):
        """
        Protocol2 to match. It is used in upper bound (range operator). Any value not in the permissible range will be rejected.";
        reference "RFC 758 - ASSIGNED INTERNET PROTOCOL NUMBERS.

        value: int. Ipv4 acl protocol number. range "0..255"
        """
        protocol2_ = SubElement(self, 'ipv4-acl-cfg:protocol2')

        if is_not_none(value):
            protocol2_.text = convert_to_string(value)
        
        if is_not_none(operation):
            protocol2_.set('xc:operation', operation.value)
  
    @force_type
    def source_network(self, source_address: str = None, source_wild_card_bits: str = None, source_prefix_length: int = None, 
                       operation: OperationEnum.Operation = None):
        """
        Source network settings.

        source_address: str. Source IPv4 address to match, leave unspecified for any.

        source_wild_card_bits: str. Wildcard bits to apply to source address  (if specified), leave unspecified for no wildcarding.

        source_prefix_length: int. Prefix length to apply to source address (if specified), leave unspecified for no wildcarding.
        """
        source_network_ = SubElement(self, 'ipv4-acl-cfg:source-network')
      
        if is_not_none(source_address):
            source_address_ = SubElement(source_network_, 'ipv4-acl-cfg:source-address')
            source_address_.text = source_address
   
        if is_not_none(source_wild_card_bits):
            source_wild_card_bits_ = SubElement(source_network_, 'ipv4-acl-cfg:source-wild-card-bits')
            source_wild_card_bits_.text = source_wild_card_bits
    
        if is_not_none(source_prefix_length):
            source_prefix_length_ = SubElement(source_network_, 'ipv4-acl-cfg:source-prefix-length')
            source_prefix_length_.text = convert_to_string(source_prefix_length)
        
        if is_not_none(operation):
            source_network_.set('xc:operation', operation.value)

    @force_type
    def destination_network(self, destination_address: str = None, destination_wild_card_bits: str = None, destination_prefix_length: int = None,
                           operation: OperationEnum.Operation = None):
        """
        Destination network settings.

        destination_address: str. Destination IPv4 address to match (if a protocol was specified), leave unspecified for any.
        
        destination_wild_card_bits: str. Wildcard bits to apply to destination address (if specified), leave unspecified for no wildcarding.

        destination_prefix_length: int. Prefix length to apply to destination address (if specified), leave unspecified for no wildcarding.
        """
        destination_network_ = SubElement(self, 'ipv4-acl-cfg:destination-network')

        if is_not_none(destination_address):
            destination_address_ = SubElement(destination_network_, 'ipv4-acl-cfg:destination-address')
            destination_address_.text = destination_address

        if is_not_none(destination_wild_card_bits):
            destination_wild_card_bits_ = SubElement(destination_network_,'ipv4-acl-cfg:destination-wild-card-bits')
            destination_wild_card_bits_.text = destination_wild_card_bits

        if is_not_none(destination_prefix_length):
            destination_prefix_length_ = SubElement(destination_network_, 'ipv4-acl-cfg:destination-prefix-length')
            destination_prefix_length_.text = convert_to_string(destination_prefix_length)
        
        if is_not_none(operation):
            destination_network_.set('xc:operation', operation.value)

    @force_type
    def source_port(self, source_operator: IPV4AclOperatorEnum.IPV4AclOperator = None,
                   first_source_port: int = None, second_source_port: int = None, operation: OperationEnum.Operation = None):
        """
        Source port settings.

        Applicable only to TCP, SCTP and UDP.

        source_operator: IPV4AclOperatorEnum.IPV4AclOperator. Source port comparison operator. This is a required 
        field if any source port value is given, otherwise, config will be rejected. Leave unspecified
        if no source port comparison is to be done.

        first_source_port: int. Lower source port for comparison. It can be used for the lower bound (range operator) or single value
        (equal, less, greater..etc). Any value not in the  permissible range will be rejected. Leave unspecified otherwise.";
        reference "RFC 1700 - WELL KNOWN PORT NUMBERS. range "0..65535"

        second_source_port: int. Upper source port for comparion. It is used in the upper bound (range operator). Any value not in the
        permissible range will be rejected. Leave unspecified otherwise."; reference "RFC 1700 - WELL KNOWN PORT NUMBERS. range "0..65535"
        """
        source_port_  = SubElement(self, 'ipv4-acl-cfg:source-port')

        if is_not_none(source_operator):
            source_operator_ =  SubElement(source_port_, 'ipv4-acl-cfg:source-operator')
            source_operator_.text = convert_to_string(source_operator.value)

        if is_not_none(first_source_port):
            first_source_port_ = SubElement(source_port_, 'ipv4-acl-cfg:first-source-port')
            first_source_port_.text = convert_to_string(first_source_port)

        if is_not_none(second_source_port):
            second_source_port_ = SubElement(source_port_, 'ipv4-acl-cfg:second-source-port')
            second_source_port_.text = convert_to_string(second_source_port)
        
        if is_not_none(operation):
            source_port_.set('xc:operation', operation.value)
  
    @force_type
    def destination_port(self, destination_operator: IPV4AclOperatorEnum.IPV4AclOperator = None, 
                        first_destination_port: int = None, second_destination_port: int = None, operation: OperationEnum.Operation = None):
        """
        Destination port settings.
        
        Applicable only to TCP, SCTP and UDP.

        destination_operator: IPV4AclOperatorEnum.IPV4AclOperator. Destination port comparison operator. This is a
        required field if any destination port value is given, otherwise, config will be rejected. Leave unspecified if no destination
        port comparison is to be done.
 
        first_destination_port: int. Lower destination port for comparison. It can be used for the lower bound (range operator) or single value
        (equal, less, greater..etc). Any value not in the permissible range will be rejected. Leave unspecified
        otherwise."; reference "RFC 1700 - WELL KNOWN PORT NUMBERS. range "0..65535"

        second_destination_port: int. Upper destination port for comparison. It is used in the upper bound (range operator). Any value not in the
        permissible range will be rejected. Leave unspecified otherwise."; 
        reference "RFC 1700 - WELL KNOWN PORT NUMBERS. range "0..65535"
        """
        destination_port_  = SubElement(self, 'ipv4-acl-cfg:destination-port')

        if is_not_none(destination_operator):
            destination_operator_ = SubElement(destination_port_, 'ipv4-acl-cfg:destination-operator')
            destination_operator_.text = convert_to_string(destination_operator.value)

        if is_not_none(first_destination_port):
            first_destination_port_  = SubElement(destination_port_, 'ipv4-acl-cfg:first-destination-port')
            first_destination_port_.text = convert_to_string(first_destination_port)
      
        if is_not_none(second_destination_port):
            second_destination_port_ = SubElement(destination_port_, 'ipv4-acl-cfg:second-destination-port')
            second_destination_port_.text = convert_to_string(second_destination_port)
        
        if is_not_none(operation):
            destination_port_.set('xc:operation', operation.value)

    @force_type
    def icmp(self, icmp_type_code: IPV4AclICMPTypeCodeEnum.IPV4AclICMPTypeCode = None, operation: OperationEnum.Operation = None):
        """
        ICMP settings.

        Applicable only to ICMP.

        icmp_type_code: IPV4AclICMPTypeCodeEnum.IPV4AclICMPTypeCode. Well known ICMP message code types to match, 
        leave unspecified if ICMP message code type comparion is not to be performed."; reference "RFC 792.
        """
        icmp_  = SubElement(self, 'ipv4-acl-cfg:icmp')

        if is_not_none(icmp_type_code):
            icmp_type_code_ = SubElement(icmp_, 'ipv4-acl-cfg:icmp-type-code')
            icmp_type_code_.text = icmp_type_code.value
        
        if is_not_none(operation):
            icmp_.set('xc:operation', operation.value)
  
    @force_type
    def tcp(self, tcp_bits_match_operator: IPV4AclTCPMATCHOPERATOREnum.IPV4AclTCPMATCHOPERATOR = None, 
            tcp_bits: IPV4AclTCPBitsNumber.IPV4AclTCPBitNumber = None, tcp_bits_mask: IPV4AclTCPBitsNumber.IPV4AclTCPBitNumber  = None,
            operation: OperationEnum.Operation = None):
        """
        TCP settings.
        
        Applicable only to TCP.

        tcp_bits_match_operator: IPV4AclTCPMATCHOPERATOREnum.IPV4AclTCPMATCHOPERATOR. TCP Bits match operator. Leave unspecified if 
        flexible comparison of TCP bits is not required.

        tcp_bits: IPV4AclTCPBitsNumber.IPV4AclTCPBitNumber. TCP bits to match. Leave unspecified if comparison of TCP bits is
        not required."; reference "RFC 793 Section 3.1 Control Bits.

        tcp_bits_mask: IPV4AclTCPBitsNumber.IPV4AclTCPBitNumber. TCP bits mask to use for flexible TCP matching.
        Leave unspecified if tcp-bits-match-operator is unspecified.
        """
        tcp_ = SubElement(self, 'ipv4-acl-cfg:tcp')
    
        if is_not_none(tcp_bits_match_operator):
            tcp_bits_match_operator_ = SubElement(tcp_, 'ipv4-acl-cfg:tcp-bits-match-operator')
            tcp_bits_match_operator_.text = convert_to_string(tcp_bits_match_operator.value)

        if is_not_none(tcp_bits):
            tcp_bits_ = SubElement(tcp_, 'ipv4-acl-cfg:tcp-bits')
            tcp_bits_.text = convert_to_string(tcp_bits.value)
    
        if is_not_none(tcp_bits_mask):
            tcp_bits_mask_ = SubElement(tcp_, 'ipv4-acl-cfg:tcp-bits-mask')
            tcp_bits_mask_.text = convert_to_string(tcp_bits_mask.value)
        
        if is_not_none(operation):
            tcp_.set('xc:operation', operation.value)
  
    @force_type
    def packet_length(self, packet_length_operator: IPV4AclOperatorEnum.IPV4AclOperator = None, 
                     packet_length_min: int = None, packet_length_max: int = None, operation: OperationEnum.Operation = None):
        """
        Packet length settings.

        packet_length_operator: IPV4AclOperatorEnum.IPV4AclOperator. Packet length operator applicable if packet length
        is to be compared. This is a required field if any packet-length value is given, otherwise, config will be rejected.

        packet_length_min: int. Mininum packet length value for comparison. It can be used for the lower bound (range operator) or single value
        (equal, less, greater..etc). Any value not in the permissible range will be rejected. Leave unspecified otherwise. range "0..65535"

        packet_length_max: int. Maximum packet length value for comparison. It is used in the upper bound (range operator). Any value not in the
        permissible range will be rejected. Leave unspecified otherwise. range "0..65535"
        """
        packet_length_ = SubElement(self, 'ipv4-acl-cfg:packet-length')

        if is_not_none(packet_length_operator):
            packet_length_operator_ = SubElement(packet_length_, 'ipv4-acl-cfg:packet-length-operator')
            packet_length_operator_.text = packet_length_operator.value

        if is_not_none(packet_length_min):
            packet_length_min_  = SubElement(packet_length_, 'ipv4-acl-cfg:packet-length-min')
            packet_length_min_.text= convert_to_string(packet_length_min)

        if is_not_none(packet_length_max):
            packet_length_max_ = SubElement(packet_length_, 'ipv4-acl-cfg:packet-length-max')
            packet_length_max_.text = convert_to_string(packet_length_max)
        
        if is_not_none(operation):
            packet_length_.set('xc:operation', operation.value)
  
    @force_type
    def time_to_live(self, time_to_live_operator: IPV4AclOperatorEnum.IPV4AclOperator = None, 
                    time_to_live_min: int  = None, time_to_live_max: int = None, operation: OperationEnum.Operation = None):
        """
        TTL settings.

        time_to_live_operator: IPV4AclOperatorEnum.IPV4AclOperator. TTL operator is applicable if TTL is to be compared.
        This is a required field if any TTL value is given, otherwise, config will be rejected. Leave
        unspecified if TTL classification is not required.

        time_to_live_min: int. Mininum TTL value for comparison. It can be used for the ower bound (range operator) 
        or single value (equal, less, greater..etc). Any value not in the permissible range will
        be rejected. Leave unspecified otherwise."; reference "RFC 791 Section 3.2 - Time to Live. range "0..255"

        time_to_live_max: int. Maximum TTL value for comparison. It is used in the upper bound (range operator). Any value not in the
        permissible range will be rejected. Leave unspecified otherwise."; reference "RFC 791 Section 3.2 - Time to Live". range "0..255"
        """
        time_to_live_ = SubElement(self, 'ipv4-acl-cfg:time-to-live')

        if is_not_none(time_to_live_operator):
            time_to_live_operator_ = SubElement(time_to_live_, 'ipv4-acl-cfg:time-to-live-operator')
            time_to_live_operator_.text = time_to_live_operator.value
      
        if is_not_none(time_to_live_min):
            time_to_live_min_ = SubElement(time_to_live_, 'ipv4-acl-cfg:time-to-live-min')
            time_to_live_min_.text = convert_to_string(time_to_live_min)
      
        if is_not_none(time_to_live_max):
            time_to_live_max_ = SubElement(time_to_live_, 'ipv4-acl-cfg:time-to-live-max')
            time_to_live_max_.text = convert_to_string(time_to_live_max)
        
        if is_not_none(operation):
            time_to_live_.set('xc:operation', operation.value)
      
    @force_type
    def fragment_offset(self, fragment_offset_operator: IPV4AclOperatorEnum.IPV4AclOperator = None,
                       fragment_offset_1: int = None, fragment_offset_2: int = None, operation: OperationEnum.Operation = None):
        """
        Fragment-offset settings.

        fragment_offset_operator: IPV4AclOperatorEnum.IPV4AclOperator. Fragment-offset operator if fragment-offset is to be
        compared. This is a required field if any fragment-offset value is given, otherwise, config will be rejected.
        Leave unspecified if fragment-offset classification is not required.

        fragment_offset_1: int. Fragment-offset value for comparison. It can be used for the lower bound (range operator) or single value
        (equal, less, greater..etc). Any value not in the permissiblerange will be rejected. Leave unspecified otherwise."; 
        reference "RFC 791 Section 2.3 - Fragmentation. range "0..8191".

        fragment_offset_2: int. Second fragment-offset value for comparison. It is used
        in the upper bound (range operator). Any value not in the permissible range will be rejected. Leave unspecified
        otherwise."; reference "RFC 791 Section 2.3 - Fragmentation. range "0..8191".
        """
        fragment_offset_ = SubElement(self, 'ipv4-acl-cfg:fragment-offset')

        if is_not_none(fragment_offset_operator):
            fragment_offset_operator_ = SubElement(fragment_offset_, 'ipv4-acl-cfg:fragment-offset-operator')
            fragment_offset_operator_.text = fragment_offset_operator.value

        if is_not_none(fragment_offset_1):
            fragment_offset_1_  = SubElement(fragment_offset_, 'ipv4-acl-cfg:fragment-offset-1')
            fragment_offset_1_.text = convert_to_string(fragment_offset_1)

        if is_not_none(fragment_offset_2):
            fragment_offset_2_ = SubElement(fragment_offset_, 'ipv4-acl-cfg:fragment-offset-2')
            fragment_offset_2_.text = convert_to_string(fragment_offset_2)
        
        if is_not_none(operation):
            fragment_offset_.set('xc:operation', operation.value)
  
    @force_type
    def fragment_type(self, value: IPV4AclFragFlags.IPV4AclFrag = None, operation: OperationEnum.Operation = None):
        """
        Fragment flags, such as dont-fragment, is-fragment,first-fragment, and last-fragment."; reference "RFC 791 Section 2.3 - Fragmentation.

        value: IPV4AclFragFlags.IPV4AclFrag. Ipv4 acl frag flags
        """

        fragment_type_ = SubElement(self, 'ipv4-acl-cfg:fragment-type')

        if is_not_none(value):
            fragment_type_.text = value.value
        
        if is_not_none(operation):
            fragment_type_.set('xc:operation', operation.value)
  
    @force_type
    def next_hop(self, value: IPV4AclNextHop):
        """"Next-hop settings."""

        if is_not_none(value):
            self.append(value)
  
    @force_type
    def counter_name(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        value: str. Name of counter to aggregate hardware statistics. length "1..64.
        """
        counter_name_ =  SubElement(self, 'ipv4-acl-cfg:counter-name')

        if is_not_none(value):
            counter_name_.text = value
        
        if is_not_none(operation):
            counter_name_.set('xc:operation', operation.value)
  
    @force_type
    def igmp_message_type(self, value: IPV4AclIGMPNumbers.IPV4AclIGMPNumber = None, operation: OperationEnum.Operation = None):
        """
        Applicable only to IGMP.

        value: IPV4AclIGMPNumbers.IPV4AclIGMPNumber. IGMP message type to match. Leave unspecified if 
        no message type comparison is to be done."; reference "RFC 3376
        """

        igmp_message_type_ = SubElement(self, 'ipv4-acl-cfg:igmp-message-type')

        if is_not_none(value):
            igmp_message_type_.text = value.value
        
        if is_not_none(operation):
            igmp_message_type_.set('xc:operation', operation.value)
  
    @force_type
    def dscp(self, dscp_operator: IPV4AclOperatorEnum.IPV4AclOperator = None, dscp_min: IPV4AclDSCPNumbers.IPV4AclDSCPNumber = None, 
            dscp_max: IPV4AclDSCPNumbers.IPV4AclDSCPNumber = None, operation: OperationEnum.Operation = None):
        """
        DSCP settings.

        dscp_operator: IPV4AclOperatorEnum.IPV4AclOperator. DSCP operator is applicable only when DSCP 
        range is configured. Leave unspecified if DSCP range is not required.

        dscp_min: IPV4AclDSCPNumbers.IPV4AclDSCPNumber. Mininum DSCP value for comparison. It can be used for the
        lower bound (range operator) or single value (equal, less, greater..etc). Any value not in the permissible range will
        be rejected. Leave unspecified otherwise."; reference "RFC 2474
        
        dscp_max: IPV4AclDSCPNumbers.IPV4AclDSCPNumber. Maximum DSCP value for comparison. It is used in the
        upper bound (range operator). Any value not in the permissible range will be rejected. Leave unspecified
        otherwise."; reference "RFC 2474
        """
        dscp_ = SubElement(self, 'ipv4-acl-cfg:dscp')

        if is_not_none(dscp_operator):
            dscp_operator_ = SubElement(dscp_, 'ipv4-acl-cfg:dscp-operator')
            dscp_operator_.text = dscp_operator.value

        if is_not_none(dscp_min):
            dscp_min_ = SubElement(dscp_, 'ipv4-acl-cfg:dscp-min')
            dscp_min_.text = dscp_min.value

        if is_not_none(dscp_max):
            dscp_max_ = SubElement(dscp_, 'ipv4-acl-cfg:dscp-max')
            dscp_max_.text = dscp_max.value
        
        if is_not_none(operation):
            dscp_.set('xc:operation', operation.value)
  
    @force_type
    def precedence(self, value: IPV4AclPrecedenceNumbers.IPV4AclPrecedenceNumber = None, operation: OperationEnum.Operation = None):
        """
        Precedence value to match (if a protocol was specified).
        Any value not in the permissible range will be rejected. Leave unspecified if precedence comparion is not to be
        performed."; reference "RFC 791 Section 3.1 - Precedence.

        value: IPV4AclPrecedenceNumbers.IPV4AclPrecedenceNumber. Ipv4 acl precedence number. 
        """
        precedence_ =  SubElement(self, 'ipv4-acl-cfg:precedence')

        if is_not_none(value):
            precedence_.text = value.value
        
        if is_not_none(operation):
            precedence_.set('xc:operation', operation.value)
  
    @force_type
    def log_option(self, value:IPV4AclLoggingEnum.IPV4AclLogging = None, operation: OperationEnum.Operation = None):
        """
        Log the packet on this access-list-entry/rule.

        value:IPV4AclLoggingEnum.IPV4AclLogging. Ipv4 acl logging enum.
        """
        log_option_ = SubElement(self, 'ipv4-acl-cfg:log-option')

        if is_not_none(value):
            log_option_.text = value.value
        
        if is_not_none(operation):
            log_option_.set('xc:operation', operation.value)

    @force_type
    def capture(self, value: bool = None, operation: OperationEnum.Operation = None):
        """
        Enable capture if set to TRUE.

        value: bool.
        """
        capture_ = SubElement(self, 'ipv4-acl-cfg:capture')

        if is_not_none(value):
            capture_.text = convert_to_string(value)
        
        if is_not_none(operation):
            capture_.set('xc:operation', operation.value)
  
    @force_type
    def icmp_off(self, operation: OperationEnum.Operation = None):
        """
        To turn off ICMP generation for deny ACEs.
        """

        icmp_off_ = SubElement(self, 'ipv4-acl-cfg:icmp-off')

        if is_not_none(operation):
            icmp_off_.set('xc:operation', operation.value)
  
    @force_type
    def qos_group(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Set qos-group number. Any value not in the permissible range will be rejected.

        value: int. Ipv4 acl qos group number. range "0..512".
        """
        qos_group_ = SubElement(self, 'ipv4-acl-cfg:qos-group')

        if is_not_none(value):
            qos_group_.text = convert_to_string(value)
        
        if is_not_none(operation):
            qos_group_.set('xc:operation', operation.value)
  
    @force_type
    def set_ttl(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Set TTL Value. Any value not in the permissible range will be rejected.

        Ipv4 acl ttl range. range "0..255".
        """
        set_ttl_ = SubElement(self, 'ipv4-acl-cfg:set-ttl')

        if is_not_none(value):
            set_ttl_.text = convert_to_string(value)
        
        if is_not_none(operation):
            set_ttl_.set('xc:operation', operation.value)
  
    @force_type
    def fragments(self, operation: OperationEnum.Operation = None):
        """
        Applicable only to TCP, SCTP, UDP, IGMP and ICMP.

        Check non-initial fragments. Item is mutually  exclusive with TCP, SCTP, UDP, IGMP and ICMP comparions and with logging.";
        reference "RFC 791 Section 2.3 - Fragmentation".
        """

        fragments_  = SubElement(self, 'ipv4-acl-cfg:fragments')

        if is_not_none(operation):
            fragments_.set('xc:operation', operation.value)

    @force_type
    def remark(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Description for the access-list-entry/rules.

        value: str. length "0..255".
        """
        remark_ = SubElement(self, 'ipv4-acl-cfg:remark')

        if is_not_none(value):
            remark_.text = value
        
        if is_not_none(operation):
            remark_.set('xc:operation', operation.value)

    @force_type
    def source_prefix_group(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        IPv4 source network object group name.

        value: str. length "1..64".
        """

        source_prefix_group_ = SubElement(self, 'ipv4-acl-cfg:source-prefix-group')

        if is_not_none(value):
            source_prefix_group_.text = value
        
        if is_not_none(operation):
            source_prefix_group_.set('xc:operation', operation.value)

    @force_type
    def destination_prefix_group(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        IPv4 destination network object group name.

        value: str. length "1..64".
        """

        destination_prefix_group_ = SubElement(self, 'ipv4-acl-cfg:destination-prefix-group')

        if is_not_none(value):
            destination_prefix_group_.text = value
        
        if is_not_none(operation):
            destination_prefix_group_.set('xc:operation', operation.value)

    @force_type
    def source_port_group(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Source port object group name.

        value: str. length "1..64".
        """

        source_port_group_ = SubElement(self, 'ipv4-acl-cfg:source-port-group')

        if is_not_none(value):
            source_port_group_.text = value
        
        if is_not_none(operation):
            source_port_group_.set('xc:operation', operation.value)

    @force_type
    def destination_port_group(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Destination port object group name.

        value: str. length "1..64".
        """

        destination_port_group_ = SubElement(self, 'ipv4-acl-cfg:destination-port-group')

        if is_not_none(value):
          destination_port_group_.text = value
        
        if is_not_none(operation):
            destination_port_group_.set('xc:operation', operation.value)
  
    @force_type
    def sequence_str(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Sequence String for the ace.

        value: str. length "1..64".
        """
        sequence_str_ = SubElement(self, 'ipv4-acl-cfg:sequence-str')

        if is_not_none(value):
            sequence_str_.text = value
        
        if is_not_none(operation):
            sequence_str_.set('xc:operation', operation.value)


class  IPV4AclAccessListEntries(Cfg):

    def __init__(self):
        super().__init__('ipv4-acl-cfg:access-list-entries')
  
    @force_type
    def access_list_entry(self, value: IPV4AclAccessListEntry):
        self.append(value)


class AccessIPV4Acl(Cfg):
    
    @force_type
    def __init__(self, access_list_name: str = None, access_list_entries: IPV4AclAccessListEntries = None):
        super().__init__('ipv4-acl-cfg:access')

        access_list_name_ = SubElement(self, 'ipv4-acl-cfg:access-list-name')
      
        if is_not_none(access_list_name):
            access_list_name_.text = access_list_name
      
        if is_not_none(access_list_entries):
            self.append(access_list_entries)
        

class  IPV4AclAccesses(Cfg):
    
    def __init__(self):
        super().__init__('ipv4-acl-cfg:accesses')
  
    @force_type
    def access(self, value: AccessIPV4Acl):
        
        if is_not_none(value):
            self.append(value)


class IPV4AclPrefixListEntry(Cfg):
    """
    A prefix list entry; either a description (remark) or a prefix to match against.
    """
    @force_type
    def __init__(self, sequence_number: int = None):
        """sequence_number: int. Sequence number of prefix list."""

        super().__init__('ipv4-acl-cfg:prefix-list-entry')

        sequence_number_ = SubElement(self, 'ipv4-acl-cfg:sequence-number')
    
        if is_not_none(sequence_number):
            sequence_number_.text = convert_to_string(sequence_number)
  
    @force_type
    def grant(self, value: IPV4AclGrantEnum.IPV4AclGrant = None, operation: OperationEnum.Operation = None):
        """
        Whether to forward or drop packets matching the prefix list.

        value: IPV4AclGrantEnum.IPV4AclGrant. Ipv4 acl grant enum.
        """
        grant_ = SubElement(self, 'ipv4-acl-cfg:grant')

        if is_not_none(value):
            grant_.text = value.value
        
        if is_not_none(operation):
            grant_.set('xc:operation', operation.value)
  
    @force_type
    def prefix(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        IPv4 address prefix to match.

        value: str.
        """
        prefix_ = SubElement(self, 'ipv4-acl-cfg:prefix')

        if is_not_none(value):
            prefix_.text = value
        
        if is_not_none(operation):
            prefix_.set('xc:operation', operation.value)
  
    @force_type
    def netmask(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Mask of IPv4 address prefix.
        
        value: str.
        """
        netmask_ = SubElement(self, 'ipv4-acl-cfg:netmask')

        if is_not_none(value):
            netmask_.text = value
        
        if is_not_none(operation):
            netmask_.set('xc:operation', operation.value)
  
    @force_type
    def match_exact_length(self, operation: OperationEnum.Operation = None):
        """
        Set to perform an exact prefix length match. Item is mutually exclusive with minimum and maximum length match items.
        """

        match_exact_length_ = SubElement(self, 'ipv4-acl-cfg:match-exact-length')

        if is_not_none(operation):
            match_exact_length_.set('xc:operation', operation.value)
  
    @force_type
    def exact_prefix_length(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        If exact prefix length matching specified, set the length of prefix to be matched.

        value: int. Ipv4 acl prefix length range. range "0..32".
        """
        exact_prefix_length_ = SubElement(self, 'ipv4-acl-cfg:exact-prefix-length')

        if is_not_none(value):
            exact_prefix_length_.text = convert_to_string(value)
        
        if is_not_none(operation):
            exact_prefix_length_.set('xc:operation', operation.value)
  
    @force_type
    def match_max_length(self, operation: OperationEnum.Operation = None):
        """
        "Set to perform a maximum length prefix match. Item is mutually exclusive with exact length match item."
        """

        match_max_length_ = SubElement(self, 'ipv4-acl-cfg:match-max-length')

        if is_not_none(operation):
            match_max_length_.set('xc:operation', operation.value)

    @force_type
    def max_prefix_length(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        If maximum length prefix matching specified, set the maximum length of prefix to be matched.

        value: int. Ipv4 acl prefix length range. range "0..32"
        """

        max_prefix_length_ = SubElement(self, 'ipv4-acl-cfg:max-prefix-length')

        if is_not_none(value):
            max_prefix_length_.text = convert_to_string(value)
        
        if is_not_none(operation):
            max_prefix_length_.set('xc:operation', operation.value)
  
    @force_type
    def match_min_length(self, operation: OperationEnum.Operation = None):
        """
        Set to perform a minimum length prefix match. Item is mutually exclusive with exact length match item.
        """

        match_min_length_ = SubElement(self, 'ipv4-acl-cfg:match-min-length')

        if is_not_none(operation):
            match_min_length_.set('xc:operation', operation.value)
  
    @force_type
    def min_prefix_length(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        If minimum length prefix matching specified, set the minimum length of prefix to be matched.

        value: int: Ipv4 acl prefix length range. range "0..32".
        """

        min_prefix_length_ = SubElement(self, 'ipv4-acl-cfg:min-prefix-length')

        if is_not_none(value):
            min_prefix_length_.text = convert_to_string(value)
        
        if is_not_none(operation):
            min_prefix_length_.set('xc:operation', operation.value)
  
    @force_type
    def remark(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Comments or a description for the prefix list. Item is mutually exclusive with all others in the object.

        value: str.
        """
        remark_ = SubElement(self, 'ipv4-acl-cfg:remark')

        if is_not_none(value):
            remark_.text = value
        
        if is_not_none(operation):
            remark_.set('xc:operation', operation.value)
  

class IPV4AclPrefixListEntries(Cfg):

    def __init__(self):
        super().__init__('ipv4-acl-cfg:prefix-list-entries')
  
    @force_type
    def prefix_list_entry(self, value: IPV4AclPrefixListEntry = None):

        if is_not_none(value):
            self.append(value)


class IPV4AclPrefix(Cfg):
    """
    Sequence of entries forming a prefix list.

    prefix_list_name: str. Name of a prefix list.
    """

    @force_type
    def __init__(self, prefix_list_name: str = None, prefix_list_entries: IPV4AclPrefixListEntries = None):
        super().__init__('ipv4-acl-cfg:prefix')
        
        prefix_list_name_ = SubElement(self, 'ipv4-acl-cfg:prefix-list-name')

        if is_not_none(prefix_list_name):
            prefix_list_name_.text = prefix_list_name

        if is_not_none(prefix_list_entries):
            self.append(prefix_list_entries)

class IPV4AclPrefixes(Cfg):
    """
    Table of ACL prefix lists.  Entries in this table and the PrefixListExistenceTable table must be kept consistent
    """

    def __init__(self):
        super().__init__('ipv4-acl-cfg:prefixes') 
  
    @force_type
    def prefix(self, value: IPV4AclPrefix = None):

        self.append(value)


class IPV4AclLogUpdate(Cfg):
    """Control access lists log updates."""
    def __init__(self):
        super().__init__('ipv4-acl-cfg:log-update')
    
    @force_type
    def threshold(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Log update threshold (number of hits)
        
        value: int. Ipv4 acl log threshold range. range "1..2147483647".
        """
        threshold_ = SubElement(self, 'ipv4-acl-cfg:threshold')

        if is_not_none(value):
            threshold_.text = convert_to_string(value)
        
        if is_not_none(operation):
            threshold_.set('xc:operation', operation.value)
    
    @force_type
    def rate(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Log update rate (log msgs per second).

        value: int. Ipv4 acl log rate range. range "1..1000".
        """
        rate_ = SubElement(self, 'ipv4-acl-cfg:rate')

        if is_not_none(value):
            rate_.text = convert_to_string(value)
        
        if is_not_none(operation):
            rate_.set('xc:operation', operation.value)



class  IPV4AclAndPrefixListCfg(Cfg):
    """module: Cisco-IOS-XR-ipv4-acl-cfg"""
    
    @force_type
    def __init__(self, accesses: IPV4AclAccesses = None, prefixes:IPV4AclPrefixes = None, log_update: IPV4AclLogUpdate = None):
        super().__init__('ipv4-acl-cfg:ipv4-acl-and-prefix-list')
      
        self.set('xmlns:ipv4-acl-cfg', 'http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-acl-cfg')

        if is_not_none(accesses):
            self.append(accesses)

        if is_not_none(prefixes):
            self.append(prefixes)

        if is_not_none(log_update):
            self.append(log_update)
    
    