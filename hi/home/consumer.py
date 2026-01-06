from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "My_Room"
        self.group_name = "My_Room"
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        print("Group added successfully!")

        self.accept()
        print("Socket Accepted!")

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, 
            self.channel_name
        )

    # Receive messages from websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, 
            {
                # 'type': 'chat.message',
                'type': 'pizza.message',
                "message": message
            }
        )

    def chat_message(self, event):
        message = event["message"]
        server_response = "Server says: " + message

        # send message to websocket
        self.send(text_data=json.dumps({'message': server_response}))

    def pizza_message(self, event):
        message = "wow! pizza time!"

        # send message to websocket
        self.send(text_data=json.dumps({'message': message}))
