import socket

def server_program():
    # implementing host and port numbers
    host = socket.gethostname()
    port = 6002  

    server_socket = socket.socket()  
    server_socket.bind((host, port))  
    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection established from the address: " + str(address))
    dict1 = {}
    l1 = []
    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            break
        print("data from connected client: " + str(data))
        result = '';
        n= data
        n = list(n.split())
        n1 = n[0]
        if n1 == "PUT":
            dict1[n[1]] = n[3]
            print("Request message sent to the Server")
            print()
            print("***********************")
            result = 'success'
        if n1 =="GET":
            if n[1] not in l1:
                print("Request message sent to the Server")
                print()
                print("result: ", dict1[n[1]])
                print("***********************")
                l1.append(n[1])
                result = dict1[n[1]]
            else:
                print("result (From Proxy Server) : ", dict1[n[1]])
                print()
                print("***********************")
        if n1 == "DUMP":
            print("Request message sent to the Server")
            print()
            print("result: ", *dict1.keys())
            result = ' '.join(list(dict1.keys()))
        conn.send(result.encode())  

    conn.close()  

if __name__ == '__main__':
    server_program()