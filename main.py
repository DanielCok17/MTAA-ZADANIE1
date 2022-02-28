#prevzaté z -> https://github.com/tirfil/PySipFullProxy

import sipfullproxy
import socketserver 
import socket
    
def main():
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='dennik_hovorov.log',level=sipfullproxy.logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    hostname = socket.gethostname()
    sipfullproxy.logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    print("Proxy server started at " ,ipaddress ," ip address and " , sipfullproxy.PORT ,"port")
    sipfullproxy.logging.info(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

if __name__ == "__main__":
    main() 
    
    
