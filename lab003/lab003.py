
def get_username():
    username = input("Enter your desired username: ")
    return username.strip().upper()



def get_group():
    group = input("Enter the group name you'd like to join: ")
    return group.strip().upper()



def get_message():
    message = input("Enter your message: ")
    return message.strip()
import lab_chat

def initialize_chat():

    username = get_username()
    group = get_group()


    peer_node = lab_chat.get_peer_node(username)


    lab_chat.join_group(peer_node, group)


    channel = lab_chat.get_channel(peer_node, group)

    return channel


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
print(get_username())
print(get_group())
print(get_message())
channel = initialize_chat()
print(type(channel))
