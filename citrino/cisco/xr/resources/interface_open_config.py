from datatype import TypeDef
from datadefinition import OpenConfig
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type
from exceptions import NoneException


class AdminStatusEnum():
    """
    [adapted from IETF interfaces model (RFC 7223)]

        The desired state of the interface.  In RFC 7223 this leaf
        has the same read semantics as ifAdminStatus.  Here, it
        reflects the administrative state as set by enabling or
        disabling the interface.";
        reference "RFC 2863: The Interfaces Group MIB - ifAdminStatus.

    UP: Ready to pass packets.

    DOWN: Not ready to pass packets and not in some test mode.

    TESTING: In some test mode.
    """

    class AdminStatus(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    UP = AdminStatus('UP')
    DOWN = AdminStatus('DOWN')
    TESTING = AdminStatus('TESTING')


class OperStatusEnum():
    """
    [adapted from IETF interfaces model (RFC 7223)]

        The current operational state of the interface.

        This leaf has the same semantics as ifOperStatus.";
    reference "RFC 2863: The Interfaces Group MIB - ifOperStatus

    UP: Ready to pass packets.

    DOWN: The interface does not pass any packets.

    TESTING: In some test mode.  No operational packets can be passed.

    UNKNOWN: Status cannot be determined for some reason.

    DORMANT: Waiting for some external event.

    NOT_PRESENT: Some component (typically hardware) is missing.

    LOWER_LAYER_DOWN: Down due to state of lower-layer interface(s).

    """

    class OperStatus(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    UP = OperStatus('UP')
    DOWN = OperStatus('DOWN')
    TESTING = OperStatus('TESTING')
    UNKNOWN = OperStatus('UNKNOWN')
    DORMANT = OperStatus('DORMANT')
    NOT_PRESENT = OperStatus('NOT_PRESENT')
    LOWER_LAYER_DOWN = OperStatus('LOWER_LAYER_DOWN')


class SubinterfaceOpenConfig(OpenConfig):
   
    @force_type
    def __init__(self, index: int = None):
        """
        index: int. The index of the subinterface, or logical interface number.
        On systems with no support for subinterfaces, or not using
        subinterfaces, this value should default to 0, i.e., the
        default subinterface.
        """
        super().__init__('oc-if:subinterface')

        if is_not_none(index):
            index_ = SubElement(self, 'oc-if:index')
            index_.text = convert_to_string(index)

    @force_type
    def config(self, index: int = None, name: str = None, description: str = None, enabled: bool = None):

        config_ = SubElement(self, 'oc-if:config')

        if is_not_none(index):
            index_ = SubElement(config_, 'oc-if:index')
            index_.text = convert_to_string(index)

        if is_not_none(name):
            name_ = SubElement(config_, 'oc-if:name')
            name_.text = name

        if is_not_none(description):
            description_ = SubElement(config_, 'oc-if:description')
            description_.text = description

        if is_not_none(enabled):
            enabled_ = SubElement(config_, 'oc-if:enabled')
            enabled_.text = convert_to_string(enabled)


class SubinterfacesOpenConfig(OpenConfig):

    @force_type
    def __init__(self):
        super().__init__('oc-if:subinterfaces')

    def subinterface(self, subinterface: SubinterfaceOpenConfig = None):

        if is_not_none(subinterface):
            self.append(subinterface)


class InterfaceOpenConfig(OpenConfig):
    
    @force_type
    def __init__(self, name: str):
        """
        name: str.
        """
        super().__init__('oc-if:interface')

        if is_not_none(name):
            name_ = SubElement(self, 'oc-if:name')
            name_.text = name
        else:
            raise NoneException('name cannot be None.')

    @force_type
    def config(self, type_: str, mtu: int = None, name: str = None, description: str = None, enabled: bool = None):
        """ 
        type_: str. [adapted from IETF interfaces model (RFC 7223)]

        The type of the interface.

        When an interface entry is created, a server MAY
        initialize the type leaf with a valid value, e.g., if it
        is possible to derive the type from the name of the
        interface.

        If a client tries to set the type of an interface to a
        value that can never be used by the system, e.g., if the
        type is not supported or if the type does not match the
        name of the interface, the server MUST reject the request.
        A NETCONF server MUST reply with an rpc-error with the
        error-tag 'invalid-value' in this case.";
        reference "RFC 2863: The Interfaces Group MIB - ifType.

        mtu: int. Set the max transmission unit size in octets
        for the physical interface.  If this is not set, the mtu is
        set to the operational default -- e.g., 1514 bytes on an
        Ethernet interface.


        name: str. [adapted from IETF interfaces model (RFC 7223)]

         The name of the interface.

        A device MAY restrict the allowed values for this leaf,
        possibly depending on the type of the interface.
        For system-controlled interfaces, this leaf is the
        device-specific name of the interface.  The 'config false'
        list interfaces/interface[name]/state contains the currently
        existing interfaces on the device.

        If a client tries to create configuration for a
        system-controlled interface that is not present in the
        corresponding state list, the server MAY reject
        the request if the implementation does not support
        pre-provisioning of interfaces or if the name refers to
        an interface that can never exist in the system.  A
        NETCONF server MUST reply with an rpc-error with the
        error-tag 'invalid-value' in this case.

        The IETF model in RFC 7223 provides YANG features for the
        following (i.e., pre-provisioning and arbitrary-names),
        however they are omitted here:

          If the device supports pre-provisioning of interface
          configuration, the 'pre-provisioning' feature is
          advertised.

        If the device allows arbitrarily named user-controlled
        interfaces, the 'arbitrary-names' feature is advertised.

        When a configured user-controlled interface is created by
        the system, it is instantiated with the same name in the
        /interfaces/interface[name]/state list.";
        reference "RFC 7223: A YANG Data Model for Interface Management";



        description: str. [adapted from IETF interfaces model (RFC 7223)]

        A textual description of the interface.

        A server implementation MAY map this leaf to the ifAlias
        MIB object.  Such an implementation needs to use some
        mechanism to handle the differences in size and characters
        allowed between this leaf and ifAlias.  The definition of
        such a mechanism is outside the scope of this document.

        Since ifAlias is defined to be stored in non-volatile
        storage, the MIB implementation MUST map ifAlias to the
        value of 'description' in the persistently stored
        datastore.

        Specifically, if the device supports ':startup', when
        ifAlias is read the device MUST return the value of
        'description' in the 'startup' datastore, and when it is
        written, it MUST be written to the 'running' and 'startup'
        datastores.  Note that it is up to the implementation to

        decide whether to modify this single leaf in 'startup' or
        perform an implicit copy-config from 'running' to
        'startup'.

        If the device does not support ':startup', ifAlias MUST
        be mapped to the 'description' leaf in the 'running'
        datastore.";
        reference "RFC 2863: The Interfaces Group MIB - ifAlias";

        enabled: bool. [adapted from IETF interfaces model (RFC 7223)]

        This leaf contains the configured, desired state of the
        interface.

        Systems that implement the IF-MIB use the value of this
        leaf in the 'running' datastore to set
        IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
        has been initialized, as described in RFC 2863.

        Changes in this leaf in the 'running' datastore are
        reflected in ifAdminStatus, but if ifAdminStatus is
        changed over SNMP, this leaf is not affected.";
        reference "RFC 2863: The Interfaces Group MIB - ifAdminStatus";
        """
        config_ = SubElement(self, 'oc-if:config')

        if is_not_none(type_):
            _type_ = SubElement(config_, 'oc-if:type')
            _type_.set('xmlns:idx', 'urn:ietf:params:xml:ns:yang:iana-if-type')
            _type_.text = type_
        else:
            raise NoneException('type_ cannot be None.')

        if is_not_none(mtu):
            mtu_ = SubElement(config_, 'oc-if:mtu')
            mtu_.text = convert_to_string(mtu)

        if is_not_none(name):
            name_ = SubElement(config_, 'oc-if:name')
            name_.text = name

        if is_not_none(description):
            description_ = SubElement(config_, 'oc-if:description')
            description_.text = description

        if is_not_none(enabled):
            enabled_ = SubElement(config_, 'oc-if:enabled')
            enabled_.text = convert_to_string(enabled)

    @force_type
    def hold_time(self, up: int = None, down: int = None):

        hold_time = SubElement(self, 'oc-if:hold-time')

        config = SubElement(hold_time, 'oc-if:config')

        if is_not_none(up):
            up_ = SubElement(config, 'oc-if:up')
            up_.text = convert_to_string(up)

        if is_not_none(down):
            down_ = SubElement(config, 'oc-if:down')
            down_.text = convert_to_string(down)

    @force_type
    def subinterfaces(self, subinterfaces=SubinterfacesOpenConfig()):

        if is_not_none(subinterfaces):
            self.append(subinterfaces)


class OpenConfigInterfaces(OpenConfig):

    def __init__(self):
        """
        module: openconfig-interfaces.
        """
        super().__init__('oc-if:interfaces')
        self.set('xmlns:oc-if', 'http://openconfig.net/yang/interfaces')

    @force_type
    def interface(self, interface: InterfaceOpenConfig = None):

        if is_not_none(interface):
            self.append(interface)
