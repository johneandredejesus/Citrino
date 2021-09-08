from datatype import TypeDef


class NetConfBaseEnum():

    class NetConfBase(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    BASE_1_0 = NetConfBase(
        {'xmlns': 'urn:ietf:params:xml:ns:netconf:base:1.0'})
    BASE_1_1 = NetConfBase(
        {'xmlns': 'urn:ietf:params:xml:ns:netconf:base:1.1'})


class OperationNetConfBaseEnum():

    class OperationNetConfBase(TypeDef):

        def __init__(self, value):
            super().__init__(value)

    BASE_1_0 = OperationNetConfBase(
        {'xmlns:xc': 'urn:ietf:params:xml:ns:netconf:base:1.0'})
    BASE_1_1 = OperationNetConfBase(
        {'xmlns:xc': 'urn:ietf:params:xml:ns:netconf:base:1.1'})
