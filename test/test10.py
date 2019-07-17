import socket, sys

port = 26450
hosts = ["sent1-opc.xwbank.com", "sent2-opc.xwbank.com", "dc02-opc-redsent1.xwbank.com", "dc02-opc-redsent2.xwbank.com",
         "ecc-opc-redsent1.xwbank.com"]


def portConnetionVerification(hosts, port):
    for host in hosts:
        host_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = host_sock.connect_ex((host, port))
        if result == 0:
            print('{} Port{} is Open'.format(host, port))
        else:
            print("{} Port{} is Not open".format(host, port))


if __name__ == '__main__':
    portConnetionVerification(hosts, port)
