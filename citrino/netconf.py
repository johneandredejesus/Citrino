from exceptions import NotCallableException, InvalidNameException, InvalidContractException
from contract import Contract
from xml.etree.ElementTree import tostring, Element
from functools import wraps
from netconf_base import NetConfBaseEnum, OperationNetConfBaseEnum
from methods import force_type


@force_type
def contract_register(vendor: str, ios: str, uri: str):
    """ Registers  class's data in Contract class.

    vendor: vendor's name. 

    Ex.: Cisco.

    ios: Operating System's Name. 

    Ex.: IOS XR.

    uri: Namespace name. Used by netconf server to register contract's command.

    Ex.: http://cisco.com/ns/yang/cisco-xr-types.
    """

    if type(vendor) is not str or type(uri) is not str or type(ios) is not str:
        raise InvalidNameException(
            "The setted uri, vendor or ios it is invalid.")

    def get_contract(contract):

        if not issubclass(contract, Contract):
            raise InvalidContractException(
                f'{contract.__name__} must be inherit from the Contract class.')

        contract.uri = uri
        contract.vendor = vendor
        contract.ios = ios

        return contract

    return get_contract


@force_type
def get(netconfbase: NetConfBaseEnum.NetConfBase=NetConfBaseEnum.BASE_1_0, type_: str = None):
    """Gets data from  the netconf rpc get comamand.

    type_: mechanism that allows an application to select particular XML Ex.: subtree"""

    def get_method(method):

        if not callable(method):
            raise NotCallableException('Object cannot be callable.')

        @wraps(method)
        def get_instance(*args, **kwargs):

            contract = args[0]

            if not issubclass(contract.__class__, Contract):
                raise InvalidContractException(
                    f'{contract.__name__} must be inherit from the Contract class.')

            method_value = method(*args, **kwargs)

            if method_value is not None:
                filter_ = Element('filter')

                if type_:
                    filter_.set('type', type_)

                for key, value in netconfbase.value.items():
                    filter_.set(key, value)

                filter_.append(method_value)
                method_value = tostring(filter_, encoding='unicode')

            return contract.command.get(method_value)

        return get_instance

    return get_method


@force_type
def get_config(source: str, netconfbase: NetConfBaseEnum.NetConfBase=NetConfBaseEnum.BASE_1_0, type_: str=None):
    """Gets data from the netconf rpc get-config command.

    source: source of data. Ex.: running.

    netconfbase: namespace of manipulate stored data.

    type_: mechanism that allows an application to select particular XML Ex.: subtree
    """

    def get_method(method):

        if not callable(method):
            raise NotCallableException('Object cannot be callable.')

        @wraps(method)
        def get_instance(*args, **kwargs):

            contract = args[0]

            if not issubclass(contract.__class__, Contract):
                raise InvalidContractException(
                    f'{contract.__name__} must be inherit from the Contract class.')

            method_value = method(*args, **kwargs)

            if method_value is not None:
                filter_ = Element('filter')

                if type_:
                    filter_.set('type', type_)

                for key, value in netconfbase.value.items():
                    filter_.set(key, value)

                filter_.append(method_value)
                method_value = tostring(filter_, encoding='unicode')

            return contract.command.get_config(method_value, source)

        return get_instance

    return get_method


@force_type
def edit_config(target: str, operation_base: OperationNetConfBaseEnum.OperationNetConfBase=OperationNetConfBaseEnum.BASE_1_0):
    """Gets data from the netconf rpc get-config command.

    target: target of data.

    Ex.: running.

    operation_base: namespace of manipulate stored data.
    """

    def get_method(method):

        if not callable(method):
            raise NotCallableException('Object cannot be callable.')

        @wraps(method)
        def get_instance(*args, **kwargs):

            contract = args[0]

            if not issubclass(contract.__class__, Contract):
                raise InvalidContractException(
                    f'{contract.__name__} must be inherit from the Contract class.')

            method_value = method(*args, **kwargs)
            if method_value is not None:
                config = Element('config')
                for key, value in operation_base.value.items():
                    config.set(key, value)
                config.append(method_value)

                method_value = tostring(config, encoding='unicode')

            return contract.command.edit_config(method_value, target)

        return get_instance

    return get_method

@force_type
def delete_config(target: str):
    """Gets data from the netconf rpc delete-config command.

    target: target of data.

    Ex.: running.
    """

    def get_method(method):

        if not callable(method):
            raise NotCallableException('Object cannot be callable.')

        @wraps(method)
        def get_instance(*args, **kwargs):

            contract = args[0]

            if not issubclass(contract.__class__, Contract):
                raise InvalidContractException(
                    f'{contract.__name__} must be inherit from the Contract class.')

            return contract.command.delete_config(target)

        return get_instance

    return get_method


def dispatch():
    """Gets data from the netconf command.

    Ex.: Cisco-IOS-XR-um-interface-cfg.yang.
    """

    def get_method(method):

        if not callable(method):
            raise NotCallableException('Object cannot be callable.')

        @wraps(method)
        def get_instance(*args, **kwargs):

            contract = args[0]

            if not issubclass(contract.__class__, Contract):
                raise InvalidContractException(
                    f'{contract.__name__} must be inherit from the Contract class.')

            method_value = method(*args, **kwargs)
            if method_value is not None:
                method_value = tostring(method_value, encoding='unicode')

            return contract.command.dispatch(method_value)

        return get_instance

    return get_method
