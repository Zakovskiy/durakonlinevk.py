class ChatNegotiate:

	def __init__ (self, data:dir):
		self.json = data
		self.negotiate_version = None
		self.connection_id = None
		self.available_transports = []

	@property
	def ChatNegotiate(self):
		self.negotiate_version = self.json['negotiateVersion']
		self.connection_id = self.json['connectionId']
		for transport in self.json["availableTransports"]:
			self.available_transports.append(AvailableTransport(transport).AvailableTransport)
		return self

class AvailableTransport:

	def __init__ (self, data:dir):
		self.json = data
		self.transport = None
		self.transfer_formats = []

	@property
	def AvailableTransport(self):
		self.transport = self.json["transport"]
		self.transfer_formats = self.json["transferFormats"]
		return self

class Event:

	def __init__ (self, data:dir):
		self.json = data
		self.type = None
		self.target = None
		self.arguments = []

	@property
	def Event (self):
		try: self.type = self.json["type"]
		except: pass
		try:self.target = self.json["target"]
		except: pass
		if self.target == "updateUserData":
			for arg in self.json["arguments"]:
				if type(arg) == "dict":
					self.arguments.append(UpdateUserData(arg).UpdateUserData)
				else:
					self.arguments.append(arg)
		elif self.target == "addMessage":
			for arg in self.json["arguments"]:
				if type(arg) == "dict":
					self.arguments.append(AddMessage(arg).AddMessage)
				else:
					self.arguments.append(arg)
		elif self.target == "serviceMessage":
			self.arguments.append(self.json["arguments"][0])
		return self

class UpdateUserData:

	def __init__ (self, data:dir):
		self.json = data
		self.slot_id = None
		self.gold = None
		self.jokers = None
		self.oly_pts = None
		self.max_bet = None
		self.reserved_gold = None
		self.week_rating_place = None
		self.moder_rating = None
		self.bura_tut = None
		self.achieves = None
		self.gifts = None
		self.inventory = None
		self.id = None
		self.together = None
		self.photo = None
		self.last_gift = None
		self.first_name = None
		self.last_name = None
		self.durak_games = None
		self.bura_games = None
		self.durak_win = None
		self.bura_win = None
		self.current_ear = None
		self.bonus_total = None
		self.bonus_win = None
		self.reverse_durak_win = None
		self.games_win = None
		self.vip_end = None
		self.played_rating_games = None
		self.money_per_week = None
		self.title = None
		self.color = None
		self.gifts = None
		self.tour_stat = None
		self.money = None
		self.gold_per_week = None
		self.is_online = None
		self.in_game = None
		self.is_male = None
		self.last_login = None
		self.love_mode = None
		self.schwain = None
		self.is_bot = None
		self.back = None
		self.have_zero = None
		self.rating_place = None
		self.gift_list = None
		self.achi_count = None

	@property
	def UpdateUserData(self):
		self.slot_id = self.json["SlotId"]
		self.gold = self.json["gold"]
		self.jokers = self.json["jokers"]
		self.oly_pts = self.json["oly_pts"]
		self.max_bet = self.json["MaxBet"]
		self.reserved_gold = self.json["reserved_gold"]
		self.week_rating_place = self.json["week_rating_place"]
		self.moder_rating = self.json["moder_rating"]
		self.bura_tut = self.json["BuraTut"]
		self.achieves = self.json["Achieves"]
		self.gifts = self.json["Gifts"]
		self.inventory = self.json["Inventory"]
		self.id = self.json["Id"]
		self.together = self.json["Together"]
		self.photo = self.json["photo"]
		self.last_gift = self.json["last_gift"]
		self.first_name = self.json["first_name"]
		self.last_name = self.json["last_name"]
		self.durak_games = self.json["durak_games"]
		self.bura_games = self.json["bura_games"]
		self.durak_win = self.json["durak_win"]
		self.bura_win = self.json["bura_win"]
		self.current_ear = self.json["currentEar"]
		self.bonus_total = self.json["bonustotal"]
		self.bonus_win = self.json["bonuswin"]
		self.reverse_durak_win = self.json["reverse_durak_win"]
		self.games_win = self.json["games_win"]
		self.vip_end = self.json["vipEnd"]
		self.played_rating_games = self.json["played_rating_games"]
		self.money_per_week = self.json["money_per_week"]
		self.title = self.json["title"]
		self.color = self.json['color']
		self.gifts = self.json["gifts"]
		self.tour_stat = self.json["tourstat"]
		self.money = self.json["money"]
		self.gold_per_week = self.json["gold_per_week"]
		self.is_online = self.json["is_online"]
		self.in_game = self.json["in_game"]
		self.is_male = self.json["is_male"]
		self.last_login = self.json["last_login"]
		self.love_mode = self.json["love_mode"]
		self.schwain = self.json["schwain"]
		self.is_bot = self.json["IsBot"]
		self.back = self.json["back"]
		self.have_zero = self.json["HaveZero"]
		self.rating_place = self.json["rating_place"]
		self.gift_list = self.json["GiftList"]
		self.achi_count = self.json["AchiCount"]
		return self

class AddMessage:

	def __init__ (self, data:dict):
		self.json = data
		self.name = None
		self.photo = None
		self.message = None
		self.color = None
		self.ea = None
		self.message_id = None
		self.id = None
		self.to = None
		self.title_id = None

	@property
	def AddMessage (self):
		self.name = self.json["Name"]
		self.photo = self.json["Ph"]
		self.message = self.json["Message"]
		self.color = self.json["col"]
		self.ea = self.json["ea"]
		self.message_id = self.json["MessageId"]
		self.id = self.json["Id"]
		self.to = self.json["To"]
		self.title_id = self.json["TitleId"]
		return self