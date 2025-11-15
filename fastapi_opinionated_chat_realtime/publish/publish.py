# fastapi-opinionated-chat-realtime/fastapi_opinionated_chat_realtime/publish/publish.py
from fastapi_opinionated.shared.publish_metadata import PublishMetadata
import subprocess

class ChatRealtimePublish(PublishMetadata):
    domain: str = "chat_realtime"
    overwrite: bool = False
    overwrite_rules: dict[str, bool] = {}
    
    async def post_publish(self):
        subprocess.check_call(["fastapi-opinionated", "plugins", "enable", "fastapi_opinionated_socket.plugin.SocketPlugin"])
        subprocess.check_call(["fastapi-opinionated", "plugins", "enable", "fastapi_opinionated_eventbus.plugin.EventBusPlugin"])