#The platform module allows you to access the underlying platforms data. Operating system and other info on other OS's besides windows

from platform import platform, machine, processor, system, version

#Returns the OS infomation Windows 10 for example
print(platform())
print(platform(1))
# when terse set to True it convinces the function to present a briefer form of the result  if possible
print(platform(0,1))
#  processor type and bit rate on certain systems
print(machine())
# returns AMD64 or processor name if possible
print(processor())
# returns the OS type Windows/linux
print(system())
# returns the operating system version
print(version())
#