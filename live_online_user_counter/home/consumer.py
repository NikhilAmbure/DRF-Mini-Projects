from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


count = 0

class OnlineUserConsumer(WebsocketConsumer):

    def connect(self, **kwargs):
        global count
        
        self.group_name = "global"

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        
        self.accept()

        
        count += 1

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "send_count",
                "count": count
            }
        )

    def send_count(self, event):
        self.send(text_data=json.dumps({
            "count": event["count"]
        }))

    def disconnect(self, code):
        global count
        count -= 1


        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "send_count",
                "count": count
            }
        )