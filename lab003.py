import lab_chat as lc
def get_username():
    username = input("lunasama05: ")
    username = username.strip()
    return username.upper()

def get_group():
    group = input("CIS12 Group Chat: ")
    group = group.strip()
    return group.upper()

def get_message():
    message = input("Hey Everyone: ")
    message = message.strip()
    return message

def initialize_chat():
    username = get_username()
    group = get_group()

    node = lc.get_peer_node(username)
    lc.join_group(node, group)

    return lc.get_channel(node, group)


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break

    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")


start_chat()










