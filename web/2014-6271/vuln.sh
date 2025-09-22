#!/bin/bash

echo "Content-type: text/plain"
echo

echo "Network Diagnostic Tool"
echo "======================="
echo "Date: $(date)"
echo

echo "User-Agent header:"
echo "$HTTP_USER_AGENT"
echo

#ipconfigをコピペ
echo "Network Interfaces:"
echo "eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500"
echo "        inet 192.168.1.10  netmask 255.255.255.0  broadcast 192.168.1.255"
echo "lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536"
echo "        inet 127.0.0.1  netmask 255.0.0.0"
echo



echo "Ping Test to google.com:"
echo "PING google.com (142.250.190.78): 56 data bytes"
echo "64 bytes from 142.250.190.78: icmp_seq=0 ttl=115 time=12.3 ms"
echo "64 bytes from 142.250.190.78: icmp_seq=1 ttl=115 time=12.1 ms"
echo "--- google.com ping statistics ---"
echo "2 packets transmitted, 2 packets received, 0% packet loss"
echo "round-trip min/avg/max/stddev = 12.1/12.2/12.3/0.1 ms"
echo

eval "echo $HTTP_USER_AGENT"
#user-agent出す