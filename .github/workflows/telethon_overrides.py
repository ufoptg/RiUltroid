# telethon_overrides.py

from telethon.tl.functions.updates import GetChannelDifferenceRequest
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.functions.messages import GetWebPagePreviewRequest
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.utils import override

@override(GetChannelDifferenceRequest)
async def get_channel_difference(self):
    result = await self._client(self)
    return result

@override(GetMessagesRequest)
async def get_messages(self):
    result = await self._client(self)
    return result

@override(GetWebPagePreviewRequest)
async def get_web_page_preview(self):
    result = await self._client(self)
    return result

@override(GetPeerDialogsRequest)
async def get_peer_dialogs(self):
    result = await self._client(self)
    return result

@override(GetHistoryRequest)
async def get_history(self):
    result = await self._client(self)
    return result
