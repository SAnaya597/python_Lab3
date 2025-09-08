
def chat_task(ctx, pipe, n, group):  # function name is chat_task

- ctx: This is a ZeroMQ Connection Context
- pipe: This is a communications pipe polled by ZeroMQ for messages.
- n: This is the peer to peer node my chat app is connected as
- group: This is the peer chat group I wanted to join

The chat_task method does not return anything, it appears to be the send/recieve manager.