from datatype import TypeDef
from datadefinition import OperationEnum, Cfg
from xml.etree.ElementTree import SubElement
from methods import convert_to_string, is_not_none, force_type
from exceptions import NoneException


class GrantEsAclEnum():
    """
    ES acl forwarding action.
    """

    class GrantEsAcl(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    DENY = GrantEsAcl('deny')
    PERMIT = GrantEsAcl('permit')


class AccessListEntryEsAcl(Cfg):

    @force_type
    def __init__(self, sequence_number: int):
        super().__init__('es-acl-cfg:access-list-entry')

        sequence_number_ = SubElement(self, 'es-acl-cfg:sequence-number')
        sequence_number_.text = convert_to_string(sequence_number)

    @force_type
    def grant(self, value: GrantEsAclEnum.GrantEsAcl = None, operation: OperationEnum.Operation = None):
        """
        ES ACE entry.

        value: GrantEsAclEnum.GrantEsAcl: Forwarding action for the packet. This is required for any non-remark ACE. Leave unspecified otherwise.
        """
        grant_ = SubElement(self, 'es-acl-cfg:grant')

        if is_not_none(value):
            grant_.text = value.value

        if is_not_none(operation):
            grant_.set('xc:operation', operation.value)

    @force_type
    def source_network(self, source_address: str = None, source_wild_card_bits: str = None, operation: OperationEnum.Operation = None):
        """
        Source network settings.

        source_address: str: Source address to match, leave unspecified for any.

        source_wild_card_bits: str: Wildcard bits to apply to source address (if specified), leave unspecified for no wildcarding.
        """
        source_network_ = SubElement(self, 'es-acl-cfg:source-network')

        if is_not_none(source_address):
            source_address_ = SubElement(source_network_, 'es-acl-cfg:source-address')
            source_address_.text = source_address

        if is_not_none(source_wild_card_bits):
            source_wild_card_bits_ = SubElement(source_network_, 'es-acl-cfg:source-wild-card-bits')
            source_wild_card_bits_.text = source_wild_card_bits

        if is_not_none(operation):
            source_network_.set('xc:operation', operation.value)

    @force_type
    def destination_network(self, destination_address: str = None, destination_wild_card_bits: str = None, operation: OperationEnum.Operation = None):
        """
        Destination network settings.

        destination_address: str: Destination address to match (if a protocol was specified), leave unspecified for any.

        destination_wild_card_bits: str: Wildcard bits to apply to destination address (if specified), leave unspecified for no wildcarding.
        """
        destination_network_ = SubElement(self, 'es-acl-cfg:destination-network')
        
        if is_not_none(destination_address):
            destination_address_ = SubElement(destination_network_, 'es-acl-cfg:destination-address')
            destination_address_.text = destination_address

        if is_not_none(destination_wild_card_bits):
            destination_wild_card_bits_ = SubElement(destination_network_, 'es-acl-cfg:destination-wild-card-bits')
            destination_wild_card_bits_.text = destination_wild_card_bits

        if is_not_none(operation):
            destination_network_.set('xc:operation', operation.value)

    @force_type
    def vlan1(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        This 12-bit VLAN-ID in the VLAN Tag header uniquely identifies the VLAN. It can be used for the lower bound (in range) or single value. Any value not in the
        permissible range will be rejected.";
        reference "IEEE 802.1Q
        """
        vlan1_ = SubElement(self, 'es-acl-cfg:vlan1')

        if is_not_none(value):
            vlan1_.text = convert_to_string(value)

        if is_not_none(operation):
            vlan1_.set('xc:operation', operation.value)

    @force_type
    def vlan2(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        This 12 bit VLAN-ID in the VLAN Tag header uniquely identifies the VLAN. It is used in the upper bound
        (in range). Any value not in the permissible range will be rejected."; reference "IEEE 802.1Q.
        """
        vlan2_ = SubElement(self, 'es-acl-cfg:vlan2')

        if is_not_none(value):
            vlan2_.text = convert_to_string(value)

        if is_not_none(operation):
            vlan2_.set('xc:operation', operation.value)

    @force_type
    def cos(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Class of Service value. Any value not in the permissible range will be rejected."; reference "IEEE 802.1p.
        """
        cos_ = SubElement(self, 'es-acl-cfg:cos')

        if is_not_none(value):
            cos_.text = convert_to_string(value)

        if is_not_none(operation):
            cos_.set('xc:operation', operation.value)

    @force_type
    def dei(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Discard Eligibility Indication bit. User can specify 1 to indicate the bit is set. Leave unspecified otherwise.";
        reference "RFC 7180 Section 7.
        """
        dei_ = SubElement(self, 'es-acl-cfg:dei')

        if is_not_none(value):
            dei_.text = convert_to_string(value)

        if is_not_none(operation):
            dei_.set('xc:operation', operation.value)

    @force_type
    def inner_vlan1(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        This represents the QinQ vlan identifier. It can be used for the lower bound (in range) or single value. Any value not in the permissible range will be rejected.";
        reference "IEEE 802.1Q.
        """
        inner_vlan1_ = SubElement(self, 'es-acl-cfg:inner-vlan1')

        if is_not_none(value):
            inner_vlan1_.text = convert_to_string(value)

        if is_not_none(operation):
            inner_vlan1_.set('xc:operation', operation.value)

    @force_type
    def inner_vlan2(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        This represents the QinQ vlan identifier. It is used in the upper bound (in range). Any value not in the permissible
        range will be rejected."; reference "IEEE 802.1Q.
        """
        inner_vlan2_ = SubElement(self, 'es-acl-cfg:inner-vlan2')

        if is_not_none(value):
            inner_vlan2_.text = convert_to_string(value)

        if is_not_none(operation):
            inner_vlan2_.set('xc:operation', operation.value)

    @force_type
    def inner_cos(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Class of Service of Inner Header. Range from 0 to 7.
        Any value beyond this range will be rejected by Acl verifier."; reference "IEEE 802.1p.
        """
        inner_cos_ = SubElement(self, 'es-acl-cfg:inner-cos')

        if is_not_none(value):
            inner_cos_.text = convert_to_string(value)

        if is_not_none(operation):
            inner_cos_.set('xc:operation', operation.value)

    @force_type
    def inner_dei(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Class of Service of Inner Header. Any value not in the permissible range will be rejected."; reference "RFC 7180 Section 7.
        """
        inner_dei_ = SubElement(self, 'es-acl-cfg:inner-dei')

        if is_not_none(value):
            inner_dei_.text = convert_to_string(value)

        if is_not_none(operation):
            inner_dei_.set('xc:operation', operation.value)

    @force_type
    def remark(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Description for the access-list-entry/rule. length: 0..255
        """
        remark_ = SubElement(self, 'es-acl-cfg:remark')

        if is_not_none(value):
            remark_.text = convert_to_string(value)

        if is_not_none(operation):
            remark_.set('xc:operation', operation.value)

    @force_type
    def ether_type_number(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Ethernet type Number in Hex. Any value not in the permissible range will be rejected."; reference "IEEE 802 Ether types.
        """
        ether_type_number_ = SubElement(self, 'es-acl-cfg:ether-type-number')

        if is_not_none(value):
            ether_type_number_.text = convert_to_string(value)

        if is_not_none(operation):
            ether_type_number_.set('xc:operation', operation.value)

    @force_type
    def capture(self, value: bool = None, operation: OperationEnum.Operation = None):
        """
        Enable capture if set to TRUE.
        """
        capture_ = SubElement(self, 'es-acl-cfg:capture')

        if is_not_none(value):
            capture_.text = convert_to_string(value)

        if is_not_none(operation):
            capture_.set('xc:operation', operation.value)

    @force_type
    def log_option(self, value: int = None, operation: OperationEnum.Operation = None):
        """
        Log the packet on this access-list-entry/rule. User can specify 1 to enable logging the match, leave unspecified otherwise.
        """
        log_option_ = SubElement(self, 'es-acl-cfg:log-option')

        if is_not_none(value):
            log_option_.text = convert_to_string(value)

        if is_not_none(operation):
            log_option_.set('xc:operation', operation.value)

    @force_type
    def sequence_str(self, value: str = None, operation: OperationEnum.Operation = None):
        """
        Sequence String for the ace.

        length: 1..64.
        """
        sequence_str_ = SubElement(self, 'es-acl-cfg:sequence-str')

        if is_not_none(value):
            sequence_str_.text = convert_to_string(value)

        if is_not_none(operation):
            sequence_str_.set('xc:operation', operation.value)


class AccessListEntriesEsAcl(Cfg):

    def __init__(self):
        super().__init__('es-acl-cfg:access-list-entries')
    
    @force_type
    def access_list_entry(self, value: AccessListEntryEsAcl):
        
        if is_not_none(value):
            self.append(value)


class AccessEsAcl(Cfg):

    @force_type
    def __init__(self, name: str, access_list_entries: AccessListEntriesEsAcl):
        super().__init__('es-acl-cfg:access')

        name_ = SubElement(self, 'es-acl-cfg:name')

        if is_not_none(name):
            name_.text = name
        
        if is_not_none(access_list_entries):
            self.append(access_list_entries)


class AccessesEsAcl(Cfg):

    def __init__(self):
        super().__init__('es-acl-cfg:accesses')
    
    @force_type
    def access(self, value: AccessEsAcl):
        
        if is_not_none(value):
            self.append(value)


class EsAclCfg(Cfg):
    """module: Cisco-IOS-XR-es-acl-cfg"""

    @force_type
    def __init__(self, accesses: AccessesEsAcl):
        super().__init__('es-acl-cfg:es-acl')
        self.set('xmlns:es-acl-cfg','http://cisco.com/ns/yang/Cisco-IOS-XR-es-acl-cfg')
        
        if is_not_none(accesses):
            self.append(accesses)
