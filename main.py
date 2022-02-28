#prevzaté z -> https://github.com/tirfil/PySipFullProxy

import sipfullproxy
import socketserver 
import socket

myPort = sipfullproxy.PORT
myHost = sipfullproxy.HOST
myUdpHandler = sipfullproxy.UDPHandler
myFileName = 'dennik_hovorov.log'
myDateFormat = '%H:%M:%S'
myDateString = "%a, %d %b %Y %H:%M:%S "
myRecordRoute = "Record-Route: <sip:%s:%d;lr>"
myTopovia = "Via: SIP/2.0/UDP %s:%d"
myLogFormat = '%(asctime)s:%(levelname)s:%(message)s'
myhostname = ""
myipaddress = ""

def set_host_name():
    return socket.gethostname() 

def set_ipaddress():
    return socket.gethostbyname(set_host_name())
    
def print_function(ipaddress : str)-> str:
    print("Proxy server started at " ,ipaddress ," ip address and " , myPort ,"port")  
    
def set_localtime():
    return sipfullproxy.time.localtime()    

def main():
    myhostname = set_host_name()
    myipaddress = set_ipaddress()
    
    sipfullproxy.logging.basicConfig(format=myLogFormat,filename = myFileName,level=sipfullproxy.logging.INFO,datefmt = myDateFormat)
    sipfullproxy.logging.info(sipfullproxy.time.strftime(myDateString, set_localtime()))
    sipfullproxy.logging.info(myhostname)
    sipfullproxy.logging.info(myipaddress)

    print_function(myipaddress)
    
    sipfullproxy.recordroute = myRecordRoute % (myipaddress,myPort)
    sipfullproxy.topvia = myTopovia % (myipaddress,myPort)
    
    myserver = socketserver.UDPServer((myHost, myPort), myUdpHandler)
    myserver.serve_forever()

if __name__ == "__main__":
    main() 
    
    
