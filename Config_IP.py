import sys
import re

def Config_Ip(fname,if_ind,ip_addr):

    content = """TYPE=Ethernet
        BOOTPROTO=none
        NAME=eth%s
        DEVICE=eth%s
        ONBOOT=yes
        IPADDR=%s
        PREFIX=24
        """ % (if_ind, if_ind, ip_addr)

    with open(fname,'w') as f:
        f.write(content)

def Check_Ip(ip_addr):

    m = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", ip_addr)
    if m:
        return True
    return False

def Show_Menu():

    prompt = """Configure IP Address:
        (0) eth0
        (1) eth1
        (2) eth2
        (3) eth3
        Your choice(0/1/2/3): """
    try:
        if_ind = input(prompt).strip()[0]
    except:
        if if_ind not in '0123':
            print("'Wrong Selection. Use 0/1/2/3'")
            sys.exit(1)

    fname = 'D:\ifcfg-eth%s' % if_ind

#调用Check_IP()函数
    ip_addr = input('Input ip address:')
    result = Check_Ip(ip_addr)

    if not result:
        print('Invalid ip address')
        sys.exit(2)

#调用Config_IP()函数
    Config_Ip(fname,if_ind,ip_addr)

if __name__ == '__main__':
    Show_Menu()
