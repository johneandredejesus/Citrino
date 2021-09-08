from contract import Contract
from datadefinition import Cfg, Oper, Act, OpenConfig
from netconf import (contract_register,
                     get,
                     get_config,
                     edit_config,
                     dispatch)


@contract_register('cisco', 'xr', 'http://cisco.com/ns/yang/cisco-xr-types')
class IOSXR(Contract):

    def __init__(self, manager):
        super().__init__(manager)

    @edit_config('candidate')
    def set_cfg(self, cfg: Cfg):
        
        return super().set_cfg(cfg)
    
    @get_config('candidate')
    def get_cfg(self, cfg: Cfg):
        
        return super().get_cfg(cfg)
    
    @get()
    def get_oper(self, oper: Oper):

        return super().get_oper(oper)

    @dispatch()
    def get_act(self, act: Act):
        
        return super().get_act(act)
    
    @dispatch()
    def set_act(self, act: Act)-> None:
        
        return super().set_act(act)

    @get()
    def get_open_config(self, open_config: OpenConfig):

        return super().get_open_config(open_config)

    @get_config(source='running')
    def get_running_config(self):
    
        return None
    