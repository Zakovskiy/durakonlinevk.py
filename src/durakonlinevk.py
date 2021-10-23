import json
import requests
from websocket import create_connection
from utils import objects

class Client:

	def __init__ (self, auth_key, user_id, ws:bool=True):
		self.user_id = user_id 
		self.auth_key = auth_key
		if ws:
			self.create_connection()
			self.send_socket({"protocol":"json","version":1})
			self.send_socket({"arguments":[self.user_id,"","","",self.auth_key,"","library_zakovskiy",True,False],"invocationId":"0","target":"Auth","type":1})

	def chat_negotiate(self):
		result = requests.post("https://serverlinx.monolife.ru:4040/chat/negotiate").json()
		return objects.ChatNegotiate(result).ChatNegotiate

	def create_connection(self):
		connection_id = self.chat_negotiate().connection_id
		self.ws = create_connection(f"wss://serverlinx.monolife.ru:4040/chat?id={connection_id}")

	def send_socket(self, data:dir):
		self.ws.send(json.dumps(data)+'')

	def listen(self):
		data_str = self.ws.recv()
		while not data_str:
			data_str = self.ws.recv()
		data = json.loads(data_str[:data_str.find("")])

		return objects.Event(data).Event

	def send_message(self, message:str):
		self.send_socket({"arguments":[message],"invocationId":"1","target":"send","type":1})
		return self.listen()

	def get_user_info(self, user_id:int):
		self.send_socket({"arguments":[user_id],"invocationId":"1","target":"userInfoPopupRequest","type":1})
		return self.listen()

	def load_shop(self, arg:str="ShopGenericTab"):
		self.send_socket({"arguments":[arg],"invocationId":"1","target":"loadShop","type":1})
		return self.listen()

	def buy_tovar(self, tovar_id:int=1):
		self.send_socket({"arguments":[tovar_id],"invocationId":"99","target":"buyTovar","type":1})
		return self.listen()