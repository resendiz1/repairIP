import wmi
import socket





# Obtiene la configuracion del adaptador de ethernet
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)





# Captura la configuracion del adaptador principal
nic = nic_configs[0]



#Pone la configuracion en dhcp
# Consigue que se establezca la configuración automatica
nic.EnableDHCP()




# Obtiene la direccion IP asignada por el DHCP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_asignada = s.getsockname()[0]











# IP address, subnetmask and gateway values should be unicode objects
ip =  ip_asignada
subnetmask = u'255.255.255.0'
gateway = u'192.168.20.253'



# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed



nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
nic.SetGateways(DefaultIPGateway=[gateway])





