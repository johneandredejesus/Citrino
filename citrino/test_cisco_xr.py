from unittest import TestCase, main
from manager import Citrino
from datadefinition import OperationEnum
from test_credential import Credential  # For testing remove this.
from cisco.xr.resources.interface_cfg import (InterfaceConfigurationsCfg,
                                          BGPPAInput,
                                          BGPPAOutput,
                                          BGPQPPB,
                                          BGPFlowTag,
                                          SecondariesAddress,
                                          PrimaryAddress,
                                          DHCPAddress,
                                          GlobalInterfaceConfigurationCfg,
                                          IPV4ReachableEnum,
                                          IPV4SelfPingEnum,
                                          IPV4DefaultPingEnum,
                                          IPV4InterfaceQPPBEnum,
                                          IPV6QPPBEnum,
                                          IPV6AccountingEnum,
                                          IPV6DefaultPingEnum,
                                          IPV6SelfPingEnum,
                                          IPV6ReachableEnum,
                                          SegmentRoutings,
                                          SegmentRouting,
                                          Ipv6PrefixSid,
                                          EUI64Addresses,
                                          LinkLocalAddress,
                                          RegularAddresses,
                                          AutoConfiguration,
                                          BgpFlowTagPolicyTable,
                                          DhcpClientOptionCodeEnum,
                                          LinkStatusEnum,
                                          InterfaceActiveEnum,
                                          InterfaceModeEnum,
                                          SecondaryAdminStateEnum,
                                          ArgsDampeningEnum,
                                          InterfaceConfiguration,
                                          HelperAddresses,
                                          MTUs,
                                          BGPPolicyAccountings)
from cisco.xr.resources.interface_open_config import (
                                          OpenConfigInterfaces,
                                          InterfaceOpenConfig,
                                          SubinterfacesOpenConfig,
                                          SubinterfaceOpenConfig)
from cisco.xr.resources.ping_act import PingAct
from cisco.xr.resources.traceroute_act import TracerouteAct
from cisco.xr.resources.esacl_cfg import (EsAclCfg, 
                                      AccessesEsAcl, 
                                      AccessEsAcl, 
                                      AccessListEntriesEsAcl, 
                                      AccessListEntryEsAcl, 
                                      GrantEsAclEnum)
from cisco.xr.resources.ipv4_acl_cfg import (IPV4AclAndPrefixListCfg,
                                        IPV4AclLogUpdate,
                                        IPV4AclPrefixes,
                                        IPV4AclPrefix,
                                        IPV4AclPrefixListEntries,
                                        IPV4AclPrefixListEntry,
                                        IPV4AclAccesses,
                                        AccessIPV4Acl,
                                        IPV4AclAccessListEntries,
                                        IPV4AclAccessListEntry,
                                        IPV4AclNextHop,
                                        IPV4AclLoggingEnum,
                                        IPV4AclPrecedenceNumbers,
                                        IPV4AclDSCPNumbers,
                                        IPV4AclIGMPNumbers,
                                        IPV4AclNextTopTypeEnum,
                                        IPV4AclFragFlags,
                                        IPV4AclTCPMATCHOPERATOREnum,
                                        IPV4AclTCPBitsNumber,
                                        IPV4AclICMPTypeCodeEnum,
                                        IPV4AclPortNumber,
                                        IPV4AclProtocolNumber,
                                        IPV4AclOperatorEnum,
                                        IPV4AclGrantEnum)
from cisco.xr.resources.shellutil_cfg import HostNamesCfg 
from cisco.xr.resources.shellutil_oper import (SystemTimeOper, 
                                          Clock, 
                                          Uptime)
from cisco.xr.resources.diag_oper import (DiagOper, 
                                    Racks, 
                                    Rack, 
                                    PowerShelfs, 
                                    PowerShelf, 
                                    FanTraies, 
                                    FanTray, 
                                    Fanses, 
                                    Fans, 
                                    Slots, 
                                    Slot, 
                                    Chassis,
                                    PowerSupplies,
                                    PowerSupply)
from cisco.xr.resources.hwmod_mpa_reload_act import HwmodMPAReload
from cisco.xr.resources.watchdog_cfg import (WatchdogCfg, 
                                         WatchdCfg, 
                                         ActiveNodesCfg, 
                                         ActiveNode, 
                                         PreconfiguredNodesCfg, 
                                         PreconfiguredNode, 
                                         WatchdogNodeThreshold, 
                                         DiskThreshold, 
                                         MemoryThreshold,
                                         ThresholdMemory as ThresholdMemoryCfg,
                                         DiskLimit)
from cisco.xr.resources.watchdog_oper import (WatchdogOper,
                                         Nodes,
                                         Node,
                                         ThresholdMemory,
                                         Default,
                                         ConfiguredMemory,
                                         Memory,
                                         Configured,
                                         MemoryState,
                                         OverloadState,
                                         CurrentThrottle)
from cisco.xr.resources.ip_domain_cfg import (IPDomainCfg, 
                                          VRFS,
                                          VRF,
                                          IPV6Hosts,
                                          IPV6Host,
                                          Servers,
                                          Server,
                                          Lists,
                                          List,
                                          IPV4Hosts,
                                          IPV4Host)

class CiscoXRTest(TestCase):

    """Tested on cisco IOS XR version 6.4.1."""

    def setUp(self):
        # Device credentials bellow. Put on  your device credentials inside.
        
        self.__citrino = Citrino()
        self.__citrino.connect(username=Credential.username,
                               password=Credential.password,
                               host=Credential.host,
                               port=Credential.port,
                               timeout=Credential.timeout)

    def tearDown(self):
        self.__citrino.disconnect()

    def test_contract(self):
        self.assertTrue(self.__citrino.has_contract())

    def test_set_global_interface_configuration(self):

        cfg = GlobalInterfaceConfigurationCfg()
        cfg.global_interface_configuration(LinkStatusEnum.DEFAULT)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))
    
    def test_get_global_interface_configuration(self):

        cfg = GlobalInterfaceConfigurationCfg()
       
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_set_interface_cfg_configurations(self):

        config = InterfaceConfiguration(interface_name='GigabitEthernet0/0/0/1', active=InterfaceActiveEnum.ACTIVE)

        # config.description("test")
        # config.link_status()
        # config.bandwidth(1000)

        # config.interface_mode_non_physical(InterfaceModeEnum.DEFAULT, operation=OperationEnum.DELETE)
        # config.secondary_admin_state(SecondaryAdminStateEnum.NORMAL)
        # config.interface_virtual()
        # config.shutdown(operation=OperationEnum.DELETE)
        # config.encapsulation()

        # mtu = MTUs()
        # mtu.mtu('GigabitEthernet', 300)
        # config.mtus(mtu)

        # config.dampening(ArgsDampeningEnum.DEFAULT_VALUES, 1, 1, 4, 6, 9)
        # config.ipv4_network_forwarding().directed_broadcast()
        # config.ipv4_network_forwarding().unreachables()
        # config.ipv4_network_forwarding().redirects()
        # config.ipv4_network().bgp_pa(BGPPAInput(True, True), BGPPAOutput(True, True))
        # config.ipv4_network().verify(IPV4ReachableEnum.ANY,IPV4SelfPingEnum.ENABLED,IPV4DefaultPingEnum.DISABLED)
        # config.ipv4_network().bgp(qppb=BGPQPPB(IPV4InterfaceQPPBEnum.IP_PRECEDENCE), bgp_flow_tag=BGPFlowTag(True))

        # secondary = SecondariesAddress()
        # secondary.secondary('192.68.89.12', '255.255.255.0')
        # secondary.secondary('192.68.89.13', '255.255.255.0')
        # secondary.secondary('192.68.89.14', '255.255.255.0')
        # config.ipv4_network().addresses(secondary,primary_address= PrimaryAddress('190.10.10.40','255.255.255.0'))

        # dhcp_address=DHCPAddress()
        # dhcp_address.enabled()
        # config.ipv4_network().addresses(dhcp_address=dhcp_address)
        # config.ipv4_network().addresses(unnumbered='GigabitEthernet0/0/0/2')

        # helper_addresses =  HelperAddresses()
        # helper_addresses.helper_address('test', '189.10.20.30')
        # helper_addresses.helper_address('test2', '189.10.20.31')
        # config.ipv4_network().helper_addresses(helper_addresses)
        # config.ipv4_network().forwarding_enable()
        # config.ipv4_network().icmp_mask_reply()
        # config.ipv4_network().tcp_mss_adjust_enable()
        # config.ipv4_network().ttl_propagate_disable()
        # config.ipv4_network().point_to_point()
        # config.ipv4_network().mtu(1567)

        # config.ipv6_network().bgp_qos_policy_propagation(IPV6QPPBEnum.QOS_GROUP, IPV6QPPBEnum.NONE)

        # bgp_policy_accountings = BGPPolicyAccountings()
        # bgp_policy_accountings.bgp_policy_accounting(IPV6AccountingEnum.INPUT, True, True)
        # bgp_policy_accountings.bgp_policy_accounting(IPV6AccountingEnum.OUTPUT, True, True)
        # config.ipv6_network().bgp_policy_accountings(bgp_policy_accountings)
        # config.ipv6_network().verify(IPV6ReachableEnum.RECEIVED, IPV6SelfPingEnum.ENABLED, IPV6DefaultPingEnum.ENABLED)

        # segment_routings = SegmentRoutings()
        # segment_routings.segment_routing(SegmentRouting('7c:5c::0000', Ipv6PrefixSid(56)))
        # segment_routings.segment_routing(SegmentRouting('7c:5c::0001', Ipv6PrefixSid(56)))
        # config.ipv6_network().addresses(segment_routings=segment_routings)
        # config.ipv6_network().addresses(link_local_address=LinkLocalAddress('FE80:0011::'))

        # eui64_addresses=EUI64Addresses()
        # eui64_addresses.eui64_address('8ff5::', 64)
        # eui64_addresses.eui64_address('8ee5::', 64)
        # config.ipv6_network().addresses(eui64_addresses=eui64_addresses)

        # regular_addresses = RegularAddresses()
        # regular_addresses.regular_address('8c:9c::0881', 128)
        # regular_addresses.regular_address('8c:9d::0881', 128)
        # config.ipv6_network().addresses(regular_addresses=regular_addresses)

        # auto_configuration = AutoConfiguration()
        # auto_configuration.auto_config_slaac()
        # auto_configuration.enable()
        # config.ipv6_network().addresses(auto_configuration=auto_configuration)

        # bgp_flow_tag_policy_table_ = BgpFlowTagPolicyTable()
        # bgp_flow_tag_policy_table_.bgp_flow_tag_policy(True, True)
        # config.ipv6_network().bgp_flow_tag_policy_table(bgp_flow_tag_policy_table_=bgp_flow_tag_policy_table_)

        # config.ipv6_network().mtu(1505)
        # config.ipv6_network().unnumbered('GigabitEthernet0/0/0/4')
        # config.ipv6_network().ttl_propagate_disable()
        # config.ipv6_network().tcp_mss_adjust_enable()
        # config.ipv6_network().unreachables()

        cfg = InterfaceConfigurationsCfg(config)

        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))

    def test_get_interface_cfg_configurations(self):

        config = InterfaceConfiguration(interface_name='GigabitEthernet0/0/0/1', active=InterfaceActiveEnum.ACTIVE)

        cfg = InterfaceConfigurationsCfg(config)

        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_get_open_config_interfaces(self):

        openconfig = OpenConfigInterfaces()
        interfaceOpenConfig = InterfaceOpenConfig('GigabitEthernet0/0/0/0')

        # subinterfacesOpenConfig = SubinterfacesOpenConfig()
        # subinterfacesOpenConfig.subinterface(SubinterfaceOpenConfig())
        # interfaceOpenConfig.subinterfaces(subinterfacesOpenConfig)

        # interfaceOpenConfig.hold_time()

        interfaceOpenConfig.config('idx:ethernetCsmacd', name='GigabitEthernet0/0/0/0')

        openconfig.interface(interfaceOpenConfig)

        self.assertRaises(Exception, self.__citrino.contract().get_open_config(openconfig))

    def test_ping_act(self):

        act = PingAct()
        # act.ipv4('8.8.8.8', sweep=True)
        # act.ipv6('2001:4860:4860::8888')
        # act.destination('8.8.8.8')
        # act.destination('2001:4860:4860::8888')

        self.assertRaises(Exception, self.__citrino.contract().get_act(act))

    def test_traceroute_act(self):

        act = TracerouteAct()

        # act.ipv4('10.10.20.254')
        # act.ipv6('8c:9c::890')
        # act.destination('10.10.20.254')
        # act.destination('8c:9c::890')

        self.assertRaises(Exception, self.__citrino.contract().get_act(act))

    def test_set_esacl(self):

        access_list_entries = AccessListEntriesEsAcl()
        access = AccessEsAcl('test', access_list_entries)
        access_list_entry = AccessListEntryEsAcl(200)
        access_list_entries.access_list_entry(access_list_entry)
        accesses = AccessesEsAcl()
        accesses.access(access)
        cfg = EsAclCfg(accesses)

        # access_list_entry.grant(GrantEsAclEnum.PERMIT)
        # access_list_entry.source_network(source_address='192.168.20.10', source_wild_card_bits='0.0.0.255')
        # access_list_entry.destination_network('192.168.0.0','0.0.255.255')
        # access_list_entry.vlan1(2)
        # access_list_entry.vlan2(3)
        # access_list_entry.capture(True)
        # access_list_entry.remark('test')
        # access_list_entry.sequence_str('test')
        # access_list_entry.log_option(4)
        # access_list_entry.ether_type_number(3)
        # access_list_entry.inner_dei(1)
        # access_list_entry.inner_cos(2)
        # access_list_entry.dei(2)
        # access_list_entry.cos(1)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))

    def test_get_esacl(self):

        accesses = AccessesEsAcl()
        cfg = EsAclCfg(accesses)
       
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_set_ipv4_acl_and_prefix_list_cfg(self):
        
        #======================= IPV4AclAccesses =======================

        # accesses = IPV4AclAccesses()
        # entries = IPV4AclAccessListEntries()
        # access = AccessIPV4Acl(access_list_name='test', access_list_entries=entries)
        # accesses.access(access)
        # entry = IPV4AclAccessListEntry(128)
        # entries.access_list_entry(entry)
        # cfg = IPV4AclAndPrefixListCfg(accesses=accesses)
        
        # entry.icmp_off()

        # entry.qos_group(value= 100) # NOT Suported
        
        # entry.set_ttl(value=100) # NOT Suported
        
        # entry.fragments()
        
        # entry.remark('test1')
        
        # entry.grant(IPV4AclGrantEnum.PERMIT)
        # entry.protocol(IPV4AclProtocolNumber.TCP)

        # entry.counter_name(value='testing', operation=OperationEnum.DELETE)
        # entry.dscp(dscp_operator=IPV4AclOperatorEnum.RANGE, dscp_min=IPV4AclDSCPNumbers.CS2, dscp_max=IPV4AclDSCPNumbers.CS3)
        # entry.precedence(value=IPV4AclPrecedenceNumbers.INTERNET, operation=OperationEnum.DELETE)
        # entry.log_option(value=IPV4AclLoggingEnum.LOG_INPUT)
        # entry.capture(value=True)
        # entry.source_prefix_group(value="test1")
        # entry.destination_prefix_group(value="test1")
        # entry.source_port_group(value="test1")
        # entry.destination_port_group(value="test1")
        # entry.sequence_str(value="test1")
        # next_hop = IPV4AclNextHop()
        # next_hop.next_hop_type(IPV4AclNextTopTypeEnum.DEFAULT_NEXT_HOP)
        # next_hop.next_hop_1(next_hop='192.168.10.20',vrf_name='testing1',track_name='tes1')
        # next_hop.next_hop_2(next_hop='192.168.10.21',vrf_name='testing2',track_name='tes2')
        # next_hop.next_hop_3(next_hop='192.168.10.22',vrf_name='testing3',track_name='tes3')
        # entry.next_hop(next_hop)
        # entry.time_to_live(time_to_live_operator=IPV4AclOperatorEnum.RANGE,time_to_live_min=2, time_to_live_max=100)
        # entry.tcp(tcp_bits_match_operator=IPV4AclTCPMATCHOPERATOREnum.MATCH_ALL,tcp_bits=IPV4AclTCPBitsNumber.RST,
        # tcp_bits_mask=IPV4AclTCPBitsNumber.FIN)
        # entry.protocol_operator(IPV4AclOperatorEnum.EQUAL)
        # entry.destination_port(destination_operator=IPV4AclOperatorEnum.EQUAL,first_destination_port=80)
        # entry.source_port(source_operator=IPV4AclOperatorEnum.LESS_THAN,first_source_port=IPV4AclPortNumber.ECHO)
        # entry.destination_network(destination_address='192.168.21.10', destination_prefix_length=24)
        # entry.source_network(source_address='192.168.20.10', source_wild_card_bits='0.0.0.255')
        # entry.packet_length(packet_length_operator=IPV4AclOperatorEnum.RANGE, packet_length_min=1, packet_length_max= 90) # NOT Suported
        # entry.fragment_offset(fragment_offset_operator=IPV4AclOperatorEnum.RANGE, fragment_offset_1=10, fragment_offset_2=100) # NOT Suported
        # entry.fragment_type(value=IPV4AclFragFlags.LAST_FRAGMENT) # NOT Suported
        # entry.icmp(icmp_type_code=IPV4AclICMPTypeCodeEnum.TIME_EXCEEDED) # ICMP ONLY
        # entry.igmp_message_type(value=IPV4AclIGMPNumbers.TRACE) # IGMP ONLY
        # entry.protocol2(IPV4AclProtocolNumber.TCP)
        
        
        #======================= IPV4AclPrefixes =======================

        # prefixes = IPV4AclPrefixes() 
        # prefix_list_entries = IPV4AclPrefixListEntries()
        # prefix = IPV4AclPrefix('test3', prefix_list_entries=prefix_list_entries)
        # prefixes.prefix(prefix)
        # prefix_list_entry = IPV4AclPrefixListEntry(100)
        # prefix_list_entries.prefix_list_entry(prefix_list_entry)
        # cfg = IPV4AclAndPrefixListCfg(prefixes=prefixes)
        
        # prefix_list_entry.grant(IPV4AclGrantEnum.PERMIT)
        # prefix_list_entry.prefix(value="192.168.30.0")
        # prefix_list_entry.netmask(value="255.255.255.0")
        # prefix_list_entry.match_exact_length()
        # prefix_list_entry.exact_prefix_length(value=24)
        # prefix_list_entry.match_max_length()
        # prefix_list_entry.max_prefix_length(value=24)
        # prefix_list_entry.match_min_length()
        # prefix_list_entry.min_prefix_length(value=24)
        # prefix_list_entry.remark(value="test3")

        #======================= IPV4AclLogUpdate =======================

        log_update = IPV4AclLogUpdate()
        cfg = IPV4AclAndPrefixListCfg(log_update=log_update)

        log_update.threshold(100)
        log_update.rate(100)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))

    def test_get_ipv4_acl_and_prefix_list_cfg(self):
        
        cfg = IPV4AclAndPrefixListCfg()

        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))
        
    def test_set_host_names_cfg(self):
        
        cfg = HostNamesCfg("NewHostname")
    
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))

    def test_get_host_names_cfg(self):

        cfg = HostNamesCfg()
       
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_get_diag_oper(self):
        
        racks = Racks()
        
        power_supply = PowerSupply()

        power_supplies = PowerSupplies()
        power_supplies.power_supply(power_supply)
        
        power_shelf = PowerShelf()

        power_shelfs = PowerShelfs() 
        power_shelfs.power_shelf(power_shelf)

        fans = Fans()

        fanses = Fanses()
        fanses.fans(fans)

        fan_tray = FanTray(fanses=fanses)

        fan_traies = FanTraies()
        fan_traies.fan_tray(fan_tray)
        
        slot = Slot('10')

        slots = Slots()
        slots.slot(slot)
        
        chassis = Chassis()

        rack = Rack('0', power_shelfs=power_shelfs, fan_traies=fan_traies, slots=slots, chassis=chassis)
        racks.rack(rack)
                                  
        oper = DiagOper(racks)
        
        self.assertRaises(Exception, self.__citrino.contract().get_oper(oper))
        
    
    def test_get_system_time_oper(self):

        oper = SystemTimeOper(Clock(), Uptime())

        self.assertRaises(Exception, self.__citrino.contract().get_oper(oper))

    def test_set_hwmod_mpa_reload(self):
        
        act = HwmodMPAReload()

        act.subslot('0/0/0')

        act.reload()
       
        self.assertRaises(Exception, self.__citrino.contract().set_act(act))

    
    def test_set_active_nodes_cfg(self):

        cfg = ActiveNodesCfg()

        disk_threshold = DiskThreshold(5, 4, 3)
        
        memory_threshold = MemoryThreshold(5, 4, 3)
     
        watchdog_node_threshold = WatchdogNodeThreshold(disk_threshold, memory_threshold)

        active = ActiveNode('0/RP0/CPU0', watchdog_node_threshold)

        cfg.active_node(active)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))
    
    def test_get_active_nodes_cfg(self):

        cfg = ActiveNodesCfg()

        disk_threshold = DiskThreshold()
        
        memory_threshold = MemoryThreshold()
      
        watchdog_node_threshold = WatchdogNodeThreshold(disk_threshold, memory_threshold)

        active = ActiveNode('0/RP0/CPU0', watchdog_node_threshold)

        cfg.active_node(active)
         
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_set_preconfigured_nodes_cfg(self):

        cfg = PreconfiguredNodesCfg()

        disk_threshold = DiskThreshold(5, 4, 3)
        
        memory_threshold = MemoryThreshold(5, 4, 3)
       
        watchdog_node_threshold = WatchdogNodeThreshold(disk_threshold, memory_threshold)

        preconfigure = PreconfiguredNode('0/RP0/CPU0', watchdog_node_threshold)

        cfg.preconfigured_node(preconfigure)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))
    
    def test_get_preconfigured_nodes_cfg(self):

        cfg = PreconfiguredNodesCfg()

        disk_threshold = DiskThreshold()
        
        memory_threshold = MemoryThreshold()
      
        watchdog_node_threshold = WatchdogNodeThreshold(disk_threshold, memory_threshold)

        preconfigure = PreconfiguredNode('0/RP0/CPU0', watchdog_node_threshold)

        cfg.preconfigured_node(preconfigure)
        
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_set_watchdog_cfg(self):
        
        threshold_memory = ThresholdMemoryCfg(5, 4, 3)
        disk_limit = DiskLimit(5, 4, 3)

        cfg = WatchdogCfg(threshold_memory, disk_limit)

        cfg.overload_notification()
        cfg.restart_deadlock_disable()
        cfg.restart_memoryhog_disable()
        cfg.overload_throttle_timeout(5)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))
    
    def test_get_watchdog_cfg(self):

        cfg = WatchdogCfg()
        
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_set_watchd_cfg(self):

        cfg = WatchdCfg()

        cfg.timeout(2)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))

    def test_get_watchd_cfg(self):

        cfg = WatchdCfg()
        
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))

    def test_get_watchdog_oper(self):
        
        nodes_oper = Nodes()

        threshold_memory = ThresholdMemory()

        memory_state = MemoryState()

        current_throttle = CurrentThrottle()

        overload_state = OverloadState(current_throttle=current_throttle)

        node_oper = Node(node_name='0/RP0/CPU0', threshold_memory=threshold_memory, 
                             memory_state=memory_state, overload_state=overload_state)

        nodes_oper.node(node_oper)
        
        oper = WatchdogOper(nodes_oper)

        self.assertRaises(Exception, self.__citrino.contract().get_oper(oper))

    def test_set_ip_domain_cfg(self):
        
        vrfs = VRFS()
        
        ipv6_hosts = IPV6Hosts()
        
        ipv6_host = IPV6Host('test')

        ipv6_host.address('2001:fcbe::')
        ipv6_host.address('2001:fcfe::')
        ipv6_host.address('2001:fcbc::')

        ipv6_hosts.ipv6_host(ipv6_host)
        
        servers = Servers()
        
        server = Server(1, '192.168.10.10')

        servers.server(server)
        
        lists = Lists()

        list_ = List(1, 'test')

        lists.list(list_)

        ipv4_hosts =  IPV4Hosts()
        
        ipv4_host = IPV4Host('test')

        ipv4_host.address('192.168.20.20')
        ipv4_host.address('192.168.20.21')
        ipv4_host.address('192.168.20.22')

        ipv4_hosts.ipv4_host(ipv4_host)

        vrf = VRF('default', ipv6_hosts=ipv6_hosts, servers=servers, lists=lists, ipv4_hosts=ipv4_hosts)

        vrf.lookup()
        vrf.multicast_domain('test')
        vrf.source_interface('GigabitEthernet0/0/0/4')
        vrf.name('test')

        vrfs.vrf(vrf)

        cfg = IPDomainCfg(vrfs=vrfs)
        
        self.assertRaises(Exception, self.__citrino.contract().set_cfg(cfg))
      
    def test_get_ip_domain_cfg(self):

        cfg = IPDomainCfg()
        
        self.assertRaises(Exception, self.__citrino.contract().get_cfg(cfg))


if __name__ == '__main__':
    main()
