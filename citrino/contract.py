from collections import OrderedDict
from commands import Commad
from datadefinition import Cfg, Oper, Act, OpenConfig
from methods import is_operation


class Contract():

    def __init__(self, manager):
        super().__init__()

        self.__command = Commad(manager)

    @property
    def command(self):
        
        return self.__command

    def discard_changes(self):

        if self.__command:
            self.__command.discard_changes()
    
    @is_operation(Cfg)
    def set_cfg(self, cfg: Cfg) -> None:
        
        return cfg
    
    @is_operation(Cfg)
    def get_cfg(self, cfg: Cfg) -> OrderedDict:
        
        return cfg
    
    @is_operation(Oper)
    def get_oper(self, oper: Oper)-> OrderedDict:

        return oper
    
    @is_operation(Act)
    def get_act(self, act: Act)-> OrderedDict:
        
        return act
    
    @is_operation(Act)
    def set_act(self, act: Act)-> None:
        
        return act

    @is_operation(OpenConfig)
    def get_open_config(self, open_config: OpenConfig) -> OrderedDict:

        return open_config
    
    def delete_config(self) -> None:

        pass
    
    def get_running_config(self) -> None:
    
        return None

    def __del__(self):

        self.__command = None