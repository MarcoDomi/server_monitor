import pickle
from serverChecker import server


file_name = "server_data.pickle"
try:
    file = open(file_name, 'rb')
    servers = pickle.load(file)
    file.close()

    name = input("Enter server name: ")
    port = input("Enter port number: ")
    type = input("Enter connection type: ")

    new_server = server(name, port, type)

    servers.append(new_server)

    file = open(file_name, 'wb')
    pickle.dump(servers, file)
    file.close()
    print("New server added!")

except FileNotFoundError:
    print(f"File Error: {file_name} does not exist")
