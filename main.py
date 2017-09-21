#/usr/bin/env python2.7

import pxssh

class Client():
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.session = self.connect()

    #A method to establish a connection
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.passwd)
            return s
        except Exception as e:
            print(e)
            print("Connection error occured! try again.")

    # A method to send commands
    def send_cmd(self, cmd):
        self.session.send_line(cmd)
        self.session.prompt()
        return self.session.before

def BotNetCmd(cmd):
    for client in Clients:
        output = client.send_cmd(cmd)
        print("-Host:[" + client.host + "]")
        print("[Output]:" + output)

# A method to add client
def addClient(host, user, passwd):
    client = Client(host, user, passwd)
    Clients.append(client)

Clients = []
default_user = ["127.0.0.1", "root", "root"]
addClient(default_user[0], default_user[1], default_user[2])

BotNetCmd("pwd")
BotNetCmd("ls -la")
