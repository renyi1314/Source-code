for i in range(254):
    print("route add 172.16."+str(i)+".254  mask 255.255.255.255 172.16.17.1 -p")
