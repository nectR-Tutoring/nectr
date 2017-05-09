from nectr.chat import consumers


channel_routing = [
    consumers.ChatServer.as_route(path=r"^/ws-chat/")
]
