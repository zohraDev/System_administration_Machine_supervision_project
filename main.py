"""
System administration, Machine supervision project:
  main() : main function collect system (CPU Memory, Disk and Network Interface) information,
  save it in file and data base.
Copyright (c) 2021 Zohra BACHI

"""

import collector
import time
import insert_db


def main():
    while True:

        try:
            # repeat collect information each 10 ms

            time.sleep(10)

            # -------------------------- collect data information system --------------------------
            cpu_percent = collector.get_cpu_percent()
            virtual_memory = collector.get_virtual_memory()
            disk_usage = collector.get_disk_us_percent()
            net_io_bytes = collector.get_net_io_counters()

            # ---------------------------step-1: insert data into file---------------------------
            text_line = f'\t {cpu_percent[0]} \t\t {cpu_percent[1]}\t\t{cpu_percent[2]}\t\t{cpu_percent[3]}'
            collector.write_in_file(text_line, 'text_cpu.txt')

            # used--free--available--percent
            text_line = f'\t{virtual_memory[0]}\t\t {virtual_memory[1]}\t\t\t{virtual_memory[2]}\t\t{virtual_memory[3]}'
            collector.write_in_file(text_line, 'text_mv.txt')

            # total--used--free--percent
            text_line = f'\t{disk_usage[0]} \t\t {disk_usage[1]}\t\t{disk_usage[2]}\t\t {disk_usage[3]}'
            collector.write_in_file(text_line, 'text_du.txt')

            # bytes_sent--ibytes_recv
            text_line = f'\t{net_io_bytes[0]}\t\t{net_io_bytes[0]}'
            collector.write_in_file(text_line, 'text_io_net.txt')

            # ---------------------------step-2: insert data into data base ---------------------------
            # --CPU
            insert_db.sql_connect_db('CPU', cpu_percent[0], cpu_percent[1], cpu_percent[2], cpu_percent[3])
            # --Memory
            insert_db.sql_connect_db('MV', virtual_memory[3], virtual_memory[0], virtual_memory[1], virtual_memory[2])
            # --Disk
            insert_db.sql_connect_db('Disk', disk_usage[3], disk_usage[2], 333, disk_usage[0])
            # --NetWork
            insert_db.sql_connect_db_io('IO', net_io_bytes[0], net_io_bytes[1])

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
