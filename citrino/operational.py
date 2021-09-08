from contract import Contract
from cisco.xr.contract import IOSXR


class Intellisense():

    def __init__(self):
        super().__init__()
        
        self.__contracts = {IOSXR.uri: IOSXR}
        self.__contract: Contract = None

    def contract(self) -> Contract:
        """Returns Contract object."""

        return self.__contract

    def analyze(self, manager, namespaces_uri) -> bool:
        """Builds Contract object."""

        for uri in self.__contracts:
    
            for namespaces in namespaces_uri:

                if namespaces.startswith(uri):

                    self.__contract = self.__contracts[uri](manager)

                    return True

        return False

    def clear(self):

        self.__contract = None
