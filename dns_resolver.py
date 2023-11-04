#!/usr/bin/env python
import socket
import dns.resolver


vip_list = []
with open('/Users/fcatal0001/Documents/scripts/dcad-scripts/gslb01-scripts/wiplist.txt', 'r') as fh:
    vip_list = fh.read().splitlines()
        
vip_count = 1

for line in vip_list:
    host = line
    #print(line)
    ### End Open text document with VIP address and Port ###

    # Basic query
    try:
        for rdata in dns.resolver.resolve(host, 'cname') :
            print(rdata)
    except dns.resolver.NXDOMAIN:
        print(host, "= nxdomain")
        pass
    except dns.resolver.NoAnswer:
        print(host, "= noAnswer")
        pass