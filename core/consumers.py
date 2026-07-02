import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TransactionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "transactions_updates"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Añade esto para responder a pings/heartbeats si el cliente los envía
    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('type') == 'ping':
            await self.send(text_data=json.dumps({'type': 'pong'}))

    async def transaction_update(self, event):
        await self.send(text_data=json.dumps(event['message']))