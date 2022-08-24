from colorama import Fore
import time
from pyfiglet import Figlet
from optparse import OptionParser
from math import floor
import pandas as pd
import numpy as np
# Function to check valid ip address


class calculate:

    def __init__(self, params):
        fig = Figlet(font='graffiti')
        print(fig.renderText("Sub Calc!!"))
        print(" " * 40 + "By Srihari Ruttala", end="\n")

        self.ip_address = params[0]
        self.subnet_mask = params[1]
        self.subnet_mask_type = params[2]

        # checking IP address
        print(Fore.YELLOW + "[+] Validating IP address", end="\r")
        time.sleep(0.3)
        if self.ip_address_check(self.ip_address):
            print(Fore.GREEN + "[+] Validating IP address")
            # checking valid subnet mask
            print(Fore.YELLOW + "[+] Validating subnet mask", end="\r")
            time.sleep(0.3)
            if self.subnetmask_check(self.subnet_mask_type, self.subnet_mask):
                print(Fore.GREEN + "[+] Validating subnet mask")
            else:
                print(Fore.RED + "[-] Invalid subnet mask ", end="\n")
                exit()
        else:
            print(Fore.RED + "[-] Invalid IP address ", end="\n")
            exit()

        if self.subnet_mask_type == 1:
            arr = self.subnet_mask.split(".")
            subnet_mask = 0

            for i in range(4):
                if arr[i] == '255':
                    subnet_mask = subnet_mask + 8
                else:
                    sub = int(arr[i])
                    mask = int(bin(sub)[2:])
                    mask = str(mask)
                    maskk = mask.split('0')[0]
                    subnet_mask = subnet_mask + len(maskk)

            self.subnet_mask = subnet_mask

    def ip_address_check(self, ip_address):
        arr = ip_address.split(".")
        if len(arr) != 4:
            return False
        for i in range(len(arr)):
            if int(arr[i]) <= 255 and int(arr[i]) >= 0:
                pass
            else:
                return False
        return True

    # Function to check valid subnet mask

    def subnetmask_check(self, subnet_mask_type, subnet_mask):

        if subnet_mask_type == 2:
            try:
                if int(subnet_mask) >= 1 and int(subnet_mask) <= 32:
                    return True
            except:
                return False

        elif subnet_mask_type == 1:
            arr = subnet_mask.split(".")

            if len(arr) != 4:
                return False

            masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]

            for i in range(len(arr)):
                if int(arr[i]) not in masks:
                    return False

            max = 255
            for i in range(len(arr)):
                if int(arr[i]) == max:
                    pass
                else:
                    if i != 3:
                        for j in range(i+1, 4):
                            if int(arr[j]) > 0:
                                return False
                        return True
            return True

        else:
            return False

    # main function

    def main(self):

        # Finding Network IP
        print(Fore.YELLOW + "[+] Calculating network id", end="\r")
        time.sleep(0.3)
        network_ip, binary_network_id, pos, flag = self.find_network_id(
            self.ip_address, self.subnet_mask,)
        print(Fore.GREEN + "[+] Calculating network id")

        # Finding First Host
        print(Fore.YELLOW + "[+] Calculating first host", end="\r")
        time.sleep(0.3)
        first_host = self.find_first_host(network_ip)
        print(Fore.GREEN + "[+] Calculating first host")

        # Finding Broadcast Address
        print(Fore.YELLOW + "[+] Calculating broadcast IP", end="\r")
        time.sleep(0.3)
        broadcast_ip = self.find_broadcast_ip(
            network_ip, binary_network_id, pos, flag)
        print(Fore.GREEN + "[+] Calculating broadcast IP")

        # Finding Last Host
        print(Fore.YELLOW + "[+] Calculating last host", end="\r")
        time.sleep(0.3)
        last_host = self.find_last_host(broadcast_ip)
        print(Fore.GREEN + "[+] Calculating last host")

        # Finding possinble number of sub networks in the the range
        print(Fore.YELLOW + "[+] Finding possible number of subnets", end="\r")
        time.sleep(0.3)
        subnets = self.find_possible_subnets(flag)
        print(Fore.GREEN + "[+] Finding possible number of subnets")

        # Finding the possinble number of Hosts in each subnet
        print(Fore.YELLOW + "[+] Finding possible number of hosts", end="\r")
        time.sleep(0.3)
        hosts = self.find_possible_hosts(flag, pos)
        print(Fore.GREEN + "[+] Finding possible number of hosts")
        print(Fore.RESET)

        # Printing Values
        print(Fore.CYAN + "[+] Network_ip              : " + str(network_ip))
        print(Fore.CYAN + "[+] First Host              : " + str(first_host))
        print(Fore.CYAN + "[+] Last host               : " + str(last_host))
        print(Fore.CYAN + "[+] Broadcast IP            : " + str(broadcast_ip))
        print(Fore.CYAN + "[+] Total number of subnets : " + str(subnets))
        print(Fore.CYAN + "[+] Total number of hosts   : " + str(hosts))
        print(Fore.CYAN + "[+] Valid host range        : " + str(first_host) +
              " through to " + str(last_host))

    # Finding network address function

    def find_network_id(self, ip_address, subnet_mask):
        ip_add_arr = ip_address.split(".")
        ip_add_ar = []

        # Converting  ip address array to integer type

        for i in range(4):
            ele = int(ip_add_arr[i])
            ip_add_ar.append(ele)

    # If subnet type is in decimal format

        del ip_add_arr
        subnet_mask = int(subnet_mask)

        # Calculating subnet to decimal and calculating IP period(.) position

        self.pos = floor(subnet_mask/8)
        self.flag = (subnet_mask - (8*(self.pos+1))) + 8

        # Converting IP from decimal to binary

        binary_ip = int(bin(ip_add_ar[self.pos])[2:])
        binary_ip = str(binary_ip)

        if len(binary_ip) != 8:
            for i in range(8-len(binary_ip)):
                binary_ip = '0' + binary_ip

        network_id = binary_ip[: self.flag]

        # Calculating network IP address

        if len(network_id) != 8:
            for i in range(8-len(network_id)):
                network_id = network_id + '0'
        binary_network_id = network_id

        network_id = int(network_id, 2)
        ip_add_ar[self.pos] = network_id
        if self.pos != 3:
            for i in range(self.pos+1, 4):
                ip_add_ar[i] = 0
        ip_add_arr = []

        for i in range(4):
            ele = str(ip_add_ar[i])
            ip_add_arr.append(ele)

        network_ip = ".".join(ip_add_arr)

        return network_ip, binary_network_id, self.pos, self.flag

    # finding the first host

    def find_first_host(self, network_ip):
        network_ip_arr = network_ip.split(".")
        host = int(network_ip_arr[3]) + 1
        network_ip_arr[3] = str(host)
        first_host = ".".join(network_ip_arr)
        return first_host

    # Finding Broadcast IP

    def find_broadcast_ip(self, network_ip, binary_network_id, pos, flag):
        network_ip_arr = network_ip.split(".")
        for i in range(pos, 4):
            if i == pos:
                network = binary_network_id[:flag]
                if len(network) != 8:
                    for j in range(len(network), 8):
                        network = network + '1'
                    id = int(network, 2)
                    id = str(id)
                    network_ip_arr[i] = id
            else:
                ip = int(network_ip_arr[i])
                binary_network = int(bin(ip)[2:])
                binary_network = str(binary_network)
                if len(binary_network) != 8:
                    for j in range(8):
                        binary_network = binary_network + '1'
                    id = int(binary_network, 2)
                    network_ip_arr[i] = str(id)
        broadcast_ip = ".".join(network_ip_arr)
        return broadcast_ip

    # Finding last host

    def find_last_host(self, broadcast_ip):
        broadcast_ip_arr = broadcast_ip.split(".")
        host = int(broadcast_ip_arr[3]) - 1
        broadcast_ip_arr[3] = str(host)
        last_host = ".".join(broadcast_ip_arr)
        return last_host

    def find_possible_subnets(self, flag):

        subnets = 2**flag
        return subnets

    def find_possible_hosts(self, flag, pos):
        host_size = 8-flag
        if pos != 3:
            for i in range(pos+1, 4):
                host_size = host_size + 8

        hosts = (2**host_size) - 2
        return hosts


class divide(calculate):
    def __init__(self, params):
        super().__init__(params)
        self.ip_address = params[0]

    def divide_by_subnet(self, no_of_subnets):
        print(Fore.YELLOW + "[+] Dividing network by no.of Subnets", end='\r')
        time.sleep(0.2)
        no_of_host_bits = 32 - int(self.subnet_mask)

        no_of_subnets = int(no_of_subnets)
        for i in range(no_of_host_bits):
            if (2**i) == no_of_subnets:
                required_bits = i
            elif no_of_subnets > (2**i) and no_of_subnets < (2**(i+1)):
                required_bits = i+1

        if no_of_host_bits <= required_bits:
            print(Fore.RED + "[-] Insufficient host bits")
            exit()

        self.calculate_addresses(required_bits)

    def divide_by_host(self, no_of_hosts):
        print(Fore.YELLOW + "[+] Dividing network by no.of Hosts", end='\r')
        time.sleep(0.2)
        no_of_host_bits = 32 - int(self.subnet_mask)
        no_of_hosts = int(no_of_hosts)
        for i in range(no_of_host_bits):
            if ((2**i)-2) == no_of_hosts:
                required_bits = i
            elif no_of_hosts > ((2**i)-2) and no_of_hosts < ((2**(i+1))-2):
                required_bits = i+1
        subnet_bits = no_of_host_bits - required_bits
        self.calculate_addresses(subnet_bits)

    def calculate_addresses(self, required_bits):

        total_subnets = 2**required_bits

        network_ip, binary_network_id, pos, flag = super().find_network_id(
            self.ip_address, self.subnet_mask,)

        arr = network_ip.split('.')

        binary_ip = ''
        for i in range(pos, 4):
            ele = int(arr[i])
            temp = int(bin(ele)[2:])
            temp = str(temp)
            for i in range(len(temp), 8):
                temp = temp + '0'
            binary_ip = binary_ip + str(temp)

        split_bits = flag + required_bits
        first_split = binary_ip[:split_bits]
        second_split = binary_ip[split_bits:]

        total_hosts = (2**(len(second_split)))-2

        subnet_array = []
        first_host_array = []
        last_host_array = []
        broadcast_address_array = []
        subn = first_split

        for i in range(total_subnets):
            if i != 0:
                subn = bin(int(subn, 2) + int('1', 2))[2:]
            else:
                subn = bin(int(subn, 2) + int('0', 2))[2:]
            subnet = str(subn) + str(second_split)
            first_host, last_host, broadcast_address = self.calculate_hosts(
                arr, subn, second_split, pos)
            self.calculate_hosts(arr, subn, second_split, pos)
            subnet = self.generate_address(arr, subnet, pos)
            first_host_array.append(first_host)
            last_host_array.append(last_host)
            broadcast_address_array.append(broadcast_address)
            subnet_array.append(subnet)

        print(Fore.GREEN + "[+] Divided Successfully             ")
        print(Fore.RESET)
        data = np.array([subnet_array, first_host_array,
                         last_host_array, broadcast_address_array])
        transpose_data = data.transpose()
        data_frame = pd.DataFrame(
            transpose_data, columns=['Subnet', 'First Host', 'Last Host', ' Broadcast'])
        print(data_frame)

        print(Fore.CYAN + "\n[+] Total no.of subnets : " + str(total_subnets))
        print(Fore.CYAN + "[+] No.of hosts per subnet : " + str(total_hosts))

    def calculate_hosts(self, arr, subn, second_split, pos):
        second_split_len = len(second_split)

        # Finding First Host
        second_split = bin(int(second_split, 2) + int('1', 2))[2:]
        for i in range(len(second_split), second_split_len):
            second_split = '0' + second_split
        first_host = str(subn) + str(second_split)
        first_host = self.generate_address(arr, first_host, pos)

        # Finding Broadcast
        second_split_len = len(str(second_split))
        second_split = ''
        for i in range(len(second_split), second_split_len):
            second_split = second_split + '1'
        broadcast_address = str(subn) + str(second_split)
        broadcast_address = self.generate_address(arr, broadcast_address, pos)

        # Finding Last host
        second_split = bin(int(second_split, 2) - int('1', 2))[2:]
        last_host = str(subn) + str(second_split)
        last_host = self.generate_address(arr, last_host, pos)
        return first_host, last_host, broadcast_address

    def generate_address(self, arr, host, pos):
        host = str(host)
        temp_arr = []
        for i in range(4):
            if i < pos:
                ele = str(arr[i])
                temp_arr.append(ele)
            else:
                binary_octet = host[:8]
                host = host[8:]
                octet = int(binary_octet, 2)
                octet = str(octet)
                temp_arr.append(octet)
        generated_host = ".".join(temp_arr)
        return generated_host


def main():
    usage = 'Usage: Usage: subncalc.py --help'
    parser = OptionParser(usage=usage)
    parser.add_option('-i', '--ipadress', dest='ip_address',
                      type='string', help='IP address')
    parser.add_option('-m', '--subnetmask', dest='subnet_mask', type='string',
                      help='Subnet mask type IP(255.255.255.240) or decimal(26)')
    parser.add_option('-S', '--no-of-subnets', dest='no_of_subnets', type='int',
                      help='Minimum number of subnets to divide')
    parser.add_option('-H', '--no-of-hosts', dest='no_of_hosts', type='int',
                      help='Minimum number of hosts for each subnet')

    (options, args) = parser.parse_args()
    if options.subnet_mask != None and options.ip_address != None:
        if '.' in options.subnet_mask:
            subnet_mask_type = 1
        else:
            subnet_mask_type = 2

    else:
        print(parser.usage)
        exit()

    return parser.parse_args(), subnet_mask_type


def call_functions(options, subnet_mask_type):
    params = []
    params.append(options.ip_address)
    params.append(options.subnet_mask)
    params.append(subnet_mask_type)
    if options.no_of_subnets != None and options.no_of_hosts == None:
        div = divide(params)
        div.divide_by_subnet(options.no_of_subnets)
    elif options.no_of_subnets == None and options.no_of_hosts != None:
        div = divide(params)
        div.divide_by_host(options.no_of_hosts)
    else:
        cal = calculate(params)
        cal.main()


if __name__ == '__main__':
    (options, args), subnet_mask_type = main()
    call_functions(options, subnet_mask_type)


