import telnetlib
import time

def telnet_gns3(ip,router):
    wait = 3  

    # -----------Sign in--------------------------
    connection = telnetlib.Telnet(ip, 23, 5)        
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    connection.write('enable' + "\n")
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    # -----------Sign in--------------------------


    # -----------Command loop--------------------------
    cmd_file = raw_input('Enter command file name and extension: ') 
    selected_cmd_file = open(cmd_file, 'r')
    selected_cmd_file.seek(0)
    for each_line in selected_cmd_file.readlines():
        time.sleep(wait)
        connection.write(each_line)
        connection.write("\n")
    # -----------Command loop--------------------------

    # -----------Same Command--------------------------

    #connection.write('show run' + "\n")
    #connection.write('copy run start' + "\n")
    #time.sleep(45)
    connection.write('show ip int brief' + "\n")
    time.sleep(15)
    # -----------Same Command--------------------------

    # -------Write output to a file-------------------
    time.sleep(wait)
    output = connection.read_very_eager()
    Rtemp = open("RN" + str(router), "w")
    Rtemp.write(output)
    Rtemp.close 
    # -------Write output to a file-------------------
    connection.close()
        
#Program starts
#Call gns3
#loop n number times where n = the number of routers
ip = '192.168.1.99'

p3=ip.rfind('.')
temp_s=ip[:p3+1]
quad=ip[p3+1:]
quad_int = int(quad)

#n=number of routers
n=3

#start loop
for router in range(1,n): 
    telnet_gns3(ip,router)
    print(router,ip)
    quad_int = quad_int+1
    quads=str(quad_int)
    ip = temp_s + quads








