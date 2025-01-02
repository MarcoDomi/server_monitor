import pickle
from serverChecker import server

with open("server_data.pickle", "rb") as file:
    servers = pickle.load(file)


def write_server_history():
    with open("server_log.txt", "w") as file: #clear log file before writing new data
        file.write("")

    with open("server_log.txt", "a") as file:
        for s in servers:
            file.write(s.name)
            file.write("\n-----------\n")
            file.writelines(s.history)

if __name__ == "__main__":
    write_server_history()