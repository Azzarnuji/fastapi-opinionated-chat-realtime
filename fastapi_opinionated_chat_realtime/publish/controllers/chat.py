from fastapi_opinionated.decorators.routing import Controller
from fastapi_opinionated.decorators.routing import Get
from fastapi.responses import HTMLResponse
from fastapi_opinionated.utils.html_view import html_content 
@Controller("/chat", group="chat_realtime")
class ChatController:
    @Get()
    async def index(self):
        try:
            content = await html_content("chat_realtime/views/index.html")
            return HTMLResponse(content=content)
        except FileNotFoundError:
            return HTMLResponse(content="<h1>Chat Realtime Index Page Not Found</h1>", status_code=404)