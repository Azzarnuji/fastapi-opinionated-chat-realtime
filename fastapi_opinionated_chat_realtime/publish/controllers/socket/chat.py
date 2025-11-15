from typing import Any
from fastapi_opinionated_socket.helpers import SocketEvent
from fastapi_opinionated_socket.helpers import socket_api
from fastapi_opinionated_eventbus.helpers import OnInternalEvent
from fastapi_opinionated_eventbus.helpers import eventbus_api
from fastapi_opinionated.shared.logger import ns_logger

# Simple in-memory store
MESSAGES = {}
ROOMS = {}
logger = ns_logger("ChatSocketController")
class ChatSocketController:
    
    @staticmethod
    @SocketEvent("join", namespace="/chat")
    async def join_chat(sid, data: Any):
        room = data["room"]

        if room not in MESSAGES:
            MESSAGES[room] = []
        if room not in ROOMS:
            ROOMS[room] = set()
            
        ROOMS[room].add(sid)
        
        await socket_api().enter_room(sid, room, namespace="/chat")

        await socket_api().emit(
            "room.joined",
            {"sid": sid, "room": room},
            room=room,
            namespace="/chat"
        )
    @staticmethod
    @SocketEvent("chat.send", namespace="/chat")
    async def send_message(sid, data: Any):
        logger.info(f"Received message data: {data}")
        await eventbus_api().emit("chat.message.created", sid=sid, data=data)
    
    @staticmethod
    @OnInternalEvent("chat.message.created")
    async def handle_message_created(sid, data: Any):
        logger.info(f"Handling created message: {data}")
        room = data["room"]
        message = data["message"]

        if room not in MESSAGES:
            MESSAGES[room] = []
        
        MESSAGES[room].append(message)
        for sid_participants in ROOMS.get(room, []):
            if sid_participants != sid:
                await socket_api().emit(
                    "chat.message",
                    {"message": message, "room": room},
                    to=sid_participants,
                    namespace="/chat"
                )