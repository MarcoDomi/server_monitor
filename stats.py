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

def getConnectionResult(item):
    index = item.find("True")
    if index == -1:
        index = item.find("False")

    result = item[index:].rstrip('\n')

    return result

def failRate():
    for s in servers:
        result_count = len(s.history)
        fail_count = 0
        for item in s.history:
            connectResult = bool(getConnectionResult(item))

            if connectResult == False:
                fail_count += 1

        fail_percentage = fail_count / result_count
        print(f"{s.name} connect fail rate: {fail_percentage}%")


if __name__ == "__main__":
    #write_server_history()
    failRate()
