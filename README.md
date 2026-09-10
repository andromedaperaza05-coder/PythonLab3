def get_peer_node(username):  # function name is get_peer_node
username: This is the username that will be used to create the peer-to-peer node

def join_group(node, group):  # function name is join_group
node: the peer-to-peer node that will join the group chat
group: name of the chat group the user wants to join

def chat_task(ctx, pipe, n, group):  # function name is chat_task
ctx: ZeroMQ communication context
pipe: communication pipe used to send and receive messages
n: peer-to-peer node the chat application is connected to
group: peer chat group the user joined

def get_channel(node, group):  # function name is get_channel
node: peer-to-peer node that will be used for communication
group: group chat the user wants to communicate in