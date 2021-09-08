# Citrino Netconf wrap


Citrino é uma abstração do protocolo NETCONF para a configuração de roteadores cisco IOS XR. Abstraindo e permitido que seja mais facíl o uso de algumas funções.

**Antes de usar, deve-se ativar o servidor NETCONF no roteador.**


## Exemplo de uso

**Imports necessários:**

      from cisco.xr.resources.interface import (InterfaceConfigurationsCfg
                                      InterfaceActiveEnum, 
                                      PrimaryAddress, 
                                      SecondariesAddress,
                                      OpenConfigInterfaces,
                                      InterfaceOpenConfig,
                                      InterfaceConfiguration)
      from datadefinition import OperationEnum
      from manager import Citrino
   
**Cria o objeto responável pela sessão:**
 
      citrino = Citrino()

      citrino.connect(username="teste", password="teste", host="192.168.10.10", port=22, timeout=10)

**Crie um objeto para o tipo de configuração:**
      
      config = InterfaceConfiguration(interface_name='GigabitEthernet0/0/0/3', active=InterfaceActiveEnum.ACTIVE)
 
 # Como setar configurações
 
 **Seta a descrição de interface:**
 
      config.description("teste") 
 
 **Seta o endereço principal da interface:**
 
      config.ipv4_network().addresses(primary_address=PrimaryAddress('190.10.10.40','255.255.255.0'))
 
 **Seta o endereço secundário da interface:**

      secondaries_address = SecondariesAddress()
      secondaries_address.secondary('192.68.89.12', '255.255.255.0')
      config.ipv4_network().addresses(secondaries_address=secondaries_address)
 
**Seta a banda passante da interface em kbps:**

      config.bandwidth(1000) 

**Seta a MTU:**

      config.ipv4_network().mtu(1567)

**Retira a interface do modo shutdown:**
 
      config.shutdown(OperationEnum.DELETE) 
 
**Aplica as ações desejadas:**
      
      cfg = InterfaceConfigurationsCfg(config)
      
      citrino.contract().set_cfg(cfg)  
 
# Como Remover configurações
 
**Crie um objeto para o tipo de configuração:**
 
      config = InterfaceConfiguration(interface_name='GigabitEthernet0/0/0/3', active=InterfaceActiveEnum.ACTIVE)
 
**Remove todas as ações feitas:**
 
      config.description("teste", operation=OperationEnum.DELETE)
       
      config.ipv4_network().addresses(primary_address=PrimaryAddress('190.10.10.40','255.255.255.0'), operation=OperationEnum.DELETE)
      
      secondaries_address = SecondariesAddress()
      secondaries_address.secondary('192.68.89.12', '255.255.255.0', operation=OperationEnum.DELETE)
      config.ipv4_network().addresses(secondaries_address=secondaries_address)

      config.bandwidth(1000, operation=OperationEnum.DELETE) 
      
      config.ipv4_network().mtu(1567, operation=OperationEnum.DELETE)
 
**Aplica as ações desejadas:**
  
      cfg = InterfaceConfigurationsCfg(config)

      citrino.contract().set_cfg(cfg) 
  
# Recuperando informações
 
**Crie um objeto para o tipo de configuração:**

      openconfig = OpenConfigInterfaces()  **Padrão IETF RFC 7223**

      interfaceOpenConfig = InterfaceOpenConfig('GigabitEthernet0/0/0/3')

      openconfig.interface(interfaceOpenConfig)
 
**Aplica e retorna um dicionário contendo as informações sobre a ação:**
 
      citrino.contract().get_open_config(openconfig) 
 
