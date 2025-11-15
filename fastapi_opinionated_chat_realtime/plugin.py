from fastapi import FastAPI
from fastapi_opinionated.shared.base_plugin import BasePlugin


class ChatRealtimePlugin(BasePlugin):
    """
    Plugin for real-time chat functionality using WebSockets.
    """

    public_name: str = "chat_realtime"
    command_name: str = "chat_realtime.enable"
    publishable: bool = True
    returns_plugin_api: bool = False
    publish_dir: str = "publish"
    
    @classmethod
    def get_publish_metadata(cls):
        from fastapi_opinionated_chat_realtime.publish.publish import ChatRealtimePublish
        return ChatRealtimePublish()