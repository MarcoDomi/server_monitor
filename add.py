import pickle
from serverChecker import server


name = input("Enter server name: ")
port = input("Enter port number: ")
type = input("Enter connection type: ")

new_server = server(name, port, type)

file_name = "server_data.pickle"
try:
    file = open(file_name, 'rb')
    servers = pickle.load(file)
    file.close()

    servers.append(new_server)

    file = open(file_name, 'wb')
    pickle.dump(servers, file)
    file.close()


except FileNotFoundError:
    print(f"File Error: {file_name} does not exist")
