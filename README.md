# `SubCalc`

A CLI utility to map out and calculate subnet ranges written in Python.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Installation

```shell
$ git clone https://github.com/srihariruttala/SubCalc.git
$ cd SubCalc/
$ pip3 install -r requirements
$ python3 subcalc.py --help
```

## Features

- Shows you all the basic required information for the IP with their respective labels after properly validating them.
- It has the ability to calculte the subnets based on the number of subnets and based on the number of hosts per subnet.

## Usage

```shell
Usage: Usage: subncalc.py --help

Options:
  -h, --help            show this help message and exit
  -i IP_ADDRESS, --ipadress=IP_ADDRESS
                        IP address
  -m SUBNET_MASK, --subnetmask=SUBNET_MASK
                        Subnet mask type IP(255.255.255.240) or decimal(26)
  -S NO_OF_SUBNETS, --no-of-subnets=NO_OF_SUBNETS
                        Minimum number of subnets to divide
  -H NO_OF_HOSTS, --no-of-hosts=NO_OF_HOSTS
                        Minimum number of hosts for each subnet
```

## Screenshots

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/SrihariRuttala/SubCalc/main/images/Screenshot%202022-08-24%20at%2010.07.02%20PM.png"></td>
    <td><img src="https://raw.githubusercontent.com/SrihariRuttala/SubCalc/main/images/Screenshot%202022-08-24%20at%2011.03.13%20PM.png"></td>
   </tr>
</table>

## License

MIT License

---
