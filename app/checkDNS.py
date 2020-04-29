#!/usr/bin/python

import DNS
from termcolor import colored
import sys
import socket 

from dnsVariablen import dnsItems

def checkDNSNames( DomainName ):

  DNS.ParseResolvConf()
  # Benoetigt: apt install python3-dns python3-termcolor

  for dnsRecords in dnsItems:
    for recordType, DNSName in dnsRecords.items():
      srv_req = DNS.Request(qtype = recordType)
      fqdnName = DNSName + DomainName
      #ipAddress = DNS.Request(qtype = ipAddress)
      srv_result = srv_req.req(fqdnName) 
      try:
        ipAddress = socket.gethostbyname(fqdnName)
      except:
        ipAddress = "no IP available"
      if srv_result.answers:
        print (f"{colored('[Erfolg]: ', 'green')} DNS Eintrag {fqdnName} vom Typ {recordType} mit der IP {ipAddress} existiert")
      else:
        print (f"{colored('[Fehler]: ', 'red')} KEIN DNS Eintrag {colored(fqdnName, 'red')} vom Typ {colored(recordType, 'red')} vorhanden!")


if __name__ == "__main__":
  if len(sys.argv) > 1:
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))
    # print ('Argument List:', str(sys.argv[1]))
    checkDNSNames( sys.argv[1] )
  else:
    print("Bitte Domainname angeben")