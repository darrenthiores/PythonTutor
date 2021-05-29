import platform

uname = platform.uname()

print ('='*20,'System Information','='*20)
print (f'System : {uname.system}')
print (f'Node name : {uname.node}')
print (f'Release : {uname.release}')
print (f'Version : {uname.version}')
print (f'Machine : {uname.machine}')
print (f'Processor : {uname.processor}')