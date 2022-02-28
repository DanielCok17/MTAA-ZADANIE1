#prevzaté z -> https://github.com/tirfil/PySipFullProxy

import sipfullproxy
import socketserver 
import socket

myPort = sipfullproxy.PORT
myHost = sipfullproxy.HOST
myUdpHandler = sipfullproxy.UDPHandler
myFileName = 'dennik_hovorov.log'
myHostName = ""
myIpAddress = ""

def set_host_name():
    return socket.gethostname() 

def set_ipaddress():
    return socket.gethostbyname(set_host_name())

def logging(myIpAddress : str) -> str:
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename = myFileName,level=sipfullproxy.logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    sipfullproxy.logging.info(myIpAddress)
    
def print_function(ipaddress : str)-> str:
    print("Proxy server started at " ,ipaddress ," ip address and " , myPort ,"port")   
                


def main():
    myHostName = set_host_name()
    myIpAddress = set_ipaddress()
    
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename = myFileName,level=sipfullproxy.logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    sipfullproxy.logging.info(myHostName)
    sipfullproxy.logging.info(myIpAddress)
    #logging(myIpAddress)
    print_function(myIpAddress)
    
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (myIpAddress,myPort)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (myIpAddress,myPort)
    
    server = socketserver.UDPServer((myHost, myPort), myUdpHandler)
    server.serve_forever()

if __name__ == "__main__":
    main() 
    
    
