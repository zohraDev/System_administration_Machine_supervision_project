"""
System administration, Machine supervision project:

This module collects information about:
    - CPU
    - memory
    - Disk
    - Network interfaces
using psutil module.

psutil is a package for getting system information
link for more information :
https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info

Copyright (c) 2021 Zohra BACHI

"""

import psutil


#
# ---------------------------------Write text in file ------------------------
#

def write_in_file(text, file_name):
    """
        The function takes two parameters:
        name_file : name of file in which we want insert <text>
        If the file doesn't exist before. It will be create

    """
    with open(f'{file_name}', 'a+') as file:
        file.write(text + '\n')


#
# -----------------------------------CPU ----------------------------------
#
def get_cpu_percent():
    """
        Returns the CPUs usage percentage.
        Which is determined using the < cpu.percent() > method on psutil module.
    """
    return psutil.cpu_percent(interval=1, percpu=True)


#
# ---------------------------------Vertual Memory  ------------------------
#
def get_virtual_memory():
    """
        Returns memory usage percentage, used, available, free.
        Which is determined using the < virtual_memory() > method on psutil module.
    """
    inf = psutil.virtual_memory()
    return inf.used, inf.free, inf.available, inf.percent


# ------------------------------------ Disk -------------------------------

def get_disk_us_percent():
    """
         Returns disk usage statistics about the partition which contains the given path.
          They determined using the < disk_usage(path) > method on psutil module.
         sdiskusage(total=249849593856, used=11281641472, free=137339965440, percent=7.6)

    """
    return psutil.disk_usage('/')


#
# ---------------------------------Network Interface ------------------------
#

def get_net_io_counters():
    """
          Returns number of bytes sent and recv by network inteface
          determined  by using the < net_io_counters > method on psutil module.
     """
    info = psutil.net_io_counters(pernic=True)['lo0']
    return info.bytes_sent, info.bytes_recv
