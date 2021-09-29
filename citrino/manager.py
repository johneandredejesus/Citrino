from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager
from operational import Intellisense
from exceptions import NotCompatibleException
from contract import Contract


class Citrino():

    def __init__(self, **kargs):
        """NetConf connection  manager  wrapping."""

        self.__connected = False
        self.__session = None
        self.__intellisense = Intellisense()
        self.__try_connect(**kargs)

    def __try_connect(self, **kargs):
        
        if kargs.__len__() > 0:
            self.connect(**kargs)

    def has_contract(self) -> bool:

        return True if self.__intellisense.contract() else False

    def contract(self) -> Contract:

        return self.__intellisense.contract()

    def connected(self) -> bool:
        
        return self.__connected

    def connect(self, username: str, password: str, host: str, port: int = 830, timeout: int = 10) -> None:
        """
        Attributes to connection data.

        Ex.:

        username=admin

        password=admin

        host=127.0.0.1

        port=830

        timeout=10
        """

        self.__session = connect_ssh(host=host, port=port, username=username, password=password)

        manager = Manager(self.__session, timeout=timeout)

        if not self.__intellisense.analyze(manager, self.__session.server_capabilities):

            self.disconnect()

            raise NotCompatibleException('Incompatible Internetwork Operating System.')

        self.__connected = True

    def disconnect(self) -> None:
        """Disconnect active connection."""

        self.__connected = False

        self.__intellisense.clear()

        if self.__session:

            self.__session.close()

    def __enter__(self):

        return self

    def __exit__(self, type, value, traceback):

        self.disconnect()

        del self
