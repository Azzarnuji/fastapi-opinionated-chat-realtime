# fastapi-opinionated-chat-realtime/fastapi_opinionated_chat_realtime/publish/publish.py
from fastapi_opinionated.shared.publish_metadata import PublishMetadata

class ChatRealtimePublish(PublishMetadata):
    domain: str = "chat_realtime"
    overwrite: bool = False
    overwrite_rules: dict[str, bool] = {}