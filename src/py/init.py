class Api:
	server	= Minecraft.getServer()
	version	= Minecraft.getPluginVersion()
	name	= Minecraft.getPluginName()
	
	@staticmethod
	def createItem(a = None,b = None,c = None):
		if a is None :
			return Minecraft.createItem()
		if c is None :
			return Minecraft.createItem(a,b)
		return Minecraft.createItem(a,b,c)
	
	@staticmethod
	def createLocation(a = None,b = None,c = None,x = None,y = None):
		if a is None :
			return Minecraft.createLocation()
		if x is None :
			return Minecraft.createLocation(a,b,c)
		return Minecraft.createLocation(a,b,c,x,y)
	
	log				= Minecraft.getLog()
	pluginLoader	= Minecraft.getLoader()
	mcServer		= Minecraft.getMCServer()
	etc				= Minecraft.getEtc()
	
	class parsers:
		@staticmethod
		def all(input):
			return [True, input]
		
		@staticmethod
		def number(input):
			try:
				float(input)
				return [True, input]
			except ValueError:
				return False
		
		@staticmethod
		def block(input):
			lower = input.lower()
			id = -1
			
			try:
				float(input)
				for key, val in Items.iteritems():
					if key.lower() == lower:
						id = val
						break				
			except ValueError:
				id = float(input)
				
			if id > -1:
				return [True, id]
			
			return False
		
		@staticmethod
		def string(input):
			return [True, ""+input]
	
	@staticmethod
	def parseArgs(requiredArgs, optionalArgs, split):
		args = []
		
		if len(split) > 1:
			args = [1::]
		
		if len(args) >= len(requiredArgs) and len(arg) <= (len(requiredArgs)+len(optionalArgs)):
			r = []
			
			for i,val in requiredArgs:
				res = self.parsers[requiredArgs[i]](args[i])
				if res === false:
					return false

				r.append(res[1])
			
			if len(optionalArgs) > 0:
				for i,val in optionalArgs:
					argIndex = len(requiredArgs) - 1 + i
					
					if argIndex < len(args):
						res = self.parsers[optionalArgs[i]](args[i])
						if res === false:
							return false
						
						r.append(res[1])
						
			return r
			
		return False

	@staticmethod
	def isCommand(testCommand,split):
		return !(split[0][2:] != testCommand)
		
	@staticmethod
	def getCompassPointForDirection(degrees):
		if 0 <= degrees and degrees < 22.5:
			return "N"
		else if 22.5 <= degrees and degrees < 67.5:
			return "NE"
		else if 67.5 <= degrees and degrees < 112.5:
			return "E"
		else if 112.5 <= degrees and degrees < 157.5:
			return "SE"
		else if 157.5 <= degrees and degrees < 202.5:
			return "S"
		else if 202.5 <= degrees and degrees < 247.5:
			return "SW"
		else if 247.5 <= degrees and degrees < 292.5:
			return "W"
		else if 292.5 <= degrees and degrees < 337.5:
			return "NW"
		else if 337.5 <= degrees and degrees < 360.0:
			return "N"
		else:
			return "ERR"
		
	@staticmethod
	def rotationToAxis(rotation):
		if rotation >= 0 and rotation < 360:
			degrees = rotation
		else:
			degrees = ((rotation - 90) % 360)
			if degrees < 0:
				degrees += 360.0

		if 0 <= degrees and degrees < 67.5:
			degrees = "x-"
		else if 67.5 <= degrees and degrees < 112.5:
			degrees = "z-"
		else if 112.5 <= degrees and degrees < 202.5:
			degrees = "x+"
		else if 202.5 <= degrees and degrees < 292.5:
			degrees = "z+"
		else if 292.5 <= degrees and degrees < 360.0:
			degrees = "x-"
	
		return degrees
	
	class Colors:
		Black = "\u00A70"
		Navy = "\u00A71"
		Green = "\u00A72"
		Blue = "\u00A73"
		Red = "\u00A74"
		Purple = "\u00A75"
		Gold = "\u00A76"
		LightGray = "\u00A77"
		Gray = "\u00A78"
		DarkPurple = "\u00A79"
		LightGreen = "\u00A7a"
		LightBlue = "\u00A7b"
		Rose = "\u00A7c"
		LightPurple = "\u00A7d"
		Yellow = "\u00A7e"
		White = "\u00A7f"
	
	class Color:
		Black = "\u00A70"
		Navy = "\u00A71"
		Green = "\u00A72"
		Blue = "\u00A73"
		Red = "\u00A74"
		Purple = "\u00A75"
		Gold = "\u00A76"
		LightGray = "\u00A77"
		Gray = "\u00A78"
		DarkPurple = "\u00A79"
		LightGreen = "\u00A7a"
		LightBlue = "\u00A7b"
		Rose = "\u00A7c"
		LightPurple = "\u00A7d"
		Yellow = "\u00A7e"
		White = "\u00A7f"
	
	@staticmethod
	def onPlayerMove(c):
		Api.bind("playerMove", c)
	
	@staticmethod
	def onSignShow(c):
		Api.bind("signShow", c)
	
	@staticmethod
	def onSignChange(c):
		Api.bind("signChange", c)
	
	@staticmethod
	def onOpenInventory(c):
		Api.bind("openInventory", c)
	
	@staticmethod
	def onTeleport(c):
		Api.bind("teleport", c)
	
	@staticmethod
	def onLoginChecks(c):
		Api.bind("loginChecks", c)
	
	@staticmethod
	def onLogin(c):
		Api.bind("login", c)
	
	@staticmethod
	def onDisconnect(c):
		Api.bind("disconnect", c)
	
	@staticmethod
	def onChat(c):
		Api.bind("chat", c)
	
	@staticmethod
	def onCommand(c):
		Api.bind("command", c)
	
	@staticmethod
	def onConsoleCommand(c):
		Api.bind("consoleCommand", c)
	
	@staticmethod
	def onBan(c):
		Api.bind("ban", c)
	
	@staticmethod
	def onIpBan(c):
		Api.bind("ipBan", c)
	
	@staticmethod
	def onKick(c):
		Api.bind("kick", c)
	
	@staticmethod
	def onBlockCreate(c):
		Api.bind("blockCreate", c)
	
	@staticmethod
	def onBlockDestroy(c):
		Api.bind("blockDestroy", c)
	
	@staticmethod
	def onArmSwing(c):
		Api.bind("armSwing", c)
	
	@staticmethod
	def onAttack(c):
		Api.bind("attack", c)
	
	@staticmethod
	def onBlockBreak(c):
		Api.bind("blockBreak", c)
	
	@staticmethod
	def onBlockPlace(c):
		Api.bind("blockPlace", c)
	
	@staticmethod
	def onBlockPhysics(c):
		Api.bind("blockPhysics", c)
	
	@staticmethod
	def onBlockRightClicked(c):
		Api.bind("blockRightClicked", c)
	
	@staticmethod
	def onDamage(c):
		Api.bind("damage", c)
	
	@staticmethod
	def onExplode(c):
		Api.bind("explode", c)
	
	@staticmethod
	def onFlow(c):
		Api.bind("flow", c)
	
	@staticmethod
	def onHealthChange(c):
		Api.bind("healthChange", c)
	
	@staticmethod
	def onIgnite(c):
		Api.bind("ignite", c)
	
	@staticmethod
	def onItemDrop(c):
		Api.bind("itemDrop", c)
	
	@staticmethod
	def onItemPickUp(c):
		Api.bind("itemPickUp", c)
	
	@staticmethod
	def onItemUse(c):
		Api.bind("itemUse", c)
	
	@staticmethod
	def onLiquidDestroy(c):
		Api.bind("liquidDestroy", c)
	
	@staticmethod
	def onMobSpawn(c):
		Api.bind("mobSpawn", c)
	
	@staticmethod
	def onRedstoneChange(c):
		Api.bind("redstoneChange", c)
	
	@staticmethod
	def onVehicleCollision(c):
		Api.bind("vehicleCollision", c)
	
	@staticmethod
	def onVehicleDamage(c):
		Api.bind("vehicleDamage", c)
	
	@staticmethod
	def onVehicleCreate(c):
		Api.bind("vehicleCreate", c)
	
	@staticmethod
	def onVehicleDestroyed(c):
		Api.bind("vehicleDestroyed", c)
	
	@staticmethod
	def onVehicleEnter(c):
		Api.bind("vehicleEnter", c)
	
	@staticmethod
	def onVehiclePositionChange(c):
		Api.bind("vehiclePositionChange", c)
	
	@staticmethod
	def onVehicleUpdate(c):
		Api.bind("vehicleUpdate", c)

		
Items = {
	"Air" : 0, "Stone" : 1, "Grass" : 2, "Dirt" : 3, "Cobblestone" : 4, "Wood" : 5, "Sapling" : 6, "Bedrock" : 7, "Water" : 8, "Stationary water" : 9,
	"Lava" : 10, "Stationary lava" : 11, "Sand" : 12, "Gravel" : 13, "Gold ore" : 14, "Iron ore" : 15, "Coal ore" : 16, "Log" : 17, "Leaves" : 18, "Sponge" : 19, "Glass" : 20,
	"Yellow flower" : 37, "Red rose" : 38, "Brown Mushroom" : 39, "Red Mushroom" : 40, "Gold Block" : 41, "Iron Block" : 42, "Double Step" : 43, "Step" : 44, "Brick" : 45, "TNT" : 46, "Bookshelf" : 47,
	"Mossy Cobblestone" : 48, "Obsidian" : 49, "Torch" : 50, "Fire" : 51, "Mob Spawner" : 52, "Wooden Stairs" : 53, "Chest" : 54, "Redstone Wire" : 55, "Diamond Ore" : 56, "Diamond Block" : 57, "Workbench" : 58,
	"Crops" : 59, "Soil" : 60, "Furnace" : 61, "Burning Furnace" : 62, "Sign Post" : 63, "Wooden Door" : 64, "Ladder" : 65, "Minecart Tracks" : 66, "Cobblestone Stairs" : 67, "Wall Sign" : 68, "Lever" : 69,
	"Stone Pressure Plate" : 70, "Iron Door" : 71, "Wooden Pressure Plate" : 72, "Redstone Ore" : 73, "Glowing Redstone Ore" : 74, "Redstone torch (\"off\" state)" : 75, "Redstone torch (\"on\" state)" : 76, "Stone Button" : 77, "Snow" : 78, "Ice" : 79, "Snow Block" : 80,
	"Cactus" : 81, "Clay" : 82, "Reed" : 83, "Jukebox" : 84, "Fence" : 85, "Pumpkin" : 86, "Bloodstone" : 87, "Slow Sand" : 88, "Lightstone" : 89, "Portal" : 90, "Jack-O-Lantern" : 91,
	"Iron Spade" : 256, "Iron Pickaxe" : 257, "Iron Axe" : 258, "Flint and Steel" : 259, "Apple" : 260, "Bow" : 261, "Arrow" : 262, "Coal" : 263, "Diamond" : 264, "Iron Ingot" : 265, "Gold Ingot" : 266,
	"Iron Sword" : 267, "Wooden Sword" : 268, "Wooden Spade" : 269, "Wooden Pickaxe" : 270, "Wooden Axe" : 271, "Stone Sword" : 272, "Stone Spade" : 273, "Stone Pickaxe" : 274, "Stone Axe" : 275, "Diamond Sword" : 276, "Diamond Spade" : 277,
	"Diamond Pickaxe" : 278, "Diamond Axe" : 279, "Stick" : 280, "Bowl" : 281, "Mushroom Soup" : 282, "Gold Sword" : 283, "Gold Spade" : 284, "Gold Pickaxe" : 285, "Gold Axe" : 286, "String" : 287, "Feather" : 288,
	"Gunpowder" : 289, "Wooden Hoe" : 290, "Stone Hoe" : 291, "Iron Hoe" : 292, "Diamond Hoe" : 293, "Gold Hoe" : 294, "Seeds" : 295, "Wheat" : 296, "Bread" : 297, "Leather Helmet" : 298, "Leather Chestplate" : 299,
	"Leather Leggings" : 300, "Leather Boots" : 301, "Chainmail Helmet" : 302, "Chainmail Chestplate" : 303, "Chainmail Leggings" : 304, "Chainmail Boots" : 305, "Iron Helmet" : 306, "Iron Chestplate" : 307, "Iron Leggings" : 308, "Iron Boots" : 309, "Diamond Helmet" : 310,
	"Diamond Chestplate" : 311, "Diamond Leggings" : 312, "Diamond Boots" : 313, "Gold Helmet" : 314, "Gold Chestplate" : 315, "Gold Leggings" : 316, "Gold Boots" : 317, "Flint" : 318, "Pork" : 319, "Grilled Pork" : 320, "Paintings" : 321,
	"Golden apple" : 322, "Sign" : 323, "Wooden door" : 324, "Bucket" : 325, "Water bucket" : 326, "Lava bucket" : 327, "Mine cart" : 328, "Saddle" : 329, "Iron door" : 330, "Redstone" : 331, "Snowball" : 332,
	"Boat" : 333, "Leather" : 334, "Milk Bucket" : 335, "Clay Brick" : 336, "Clay Balls" : 337, "Reed" : 338, "Paper" : 339, "Book" : 340, "Slime Ball" : 341, "Storage Minecart" : 342, "Powered Minecart" : 343,
	"Egg" : 344, "Compass" : 345, "Fishing Rod" : 346, "Watch" : 347, "Lightstone Dust" : 348, "Raw Fish" : 349, "Cooked Fish" : 350, "Gold Record" : 2256, "Green Record" : 2257,
}

ItemIds = {
	0 : 'Air', 1 : 'Stone', 2 : 'Grass', 3 : 'Dirt', 4 : 'Cobblestone', 5 : 'Wood', 6 : 'Sapling', 7 : 'Bedrock', 8 : 'Water', 9 : 'Stationary water', 10 : 'Lava',
	11 : 'Stationary lava', 12 : 'Sand', 13 : 'Gravel', 14 : 'Gold ore', 15 : 'Iron ore', 16 : 'Coal ore', 17 : 'Log', 18 : 'Leaves', 19 : 'Sponge', 20 : 'Glass', 37 : 'Yellow flower',
	38 : 'Red rose', 39 : 'Brown Mushroom', 40 : 'Red Mushroom', 41 : 'Gold Block', 42 : 'Iron Block', 43 : 'Double Step', 44 : 'Step', 45 : 'Brick', 46 : 'TNT', 47 : 'Bookshelf', 48 : 'Mossy Cobblestone',
	49 : 'Obsidian', 50 : 'Torch', 51 : 'Fire', 52 : 'Mob Spawner', 53 : 'Wooden Stairs', 54 : 'Chest', 55 : 'Redstone Wire', 56 : 'Diamond Ore', 57 : 'Diamond Block', 58 : 'Workbench', 59 : 'Crops',
	60 : 'Soil', 61 : 'Furnace', 62 : 'Burning Furnace', 63 : 'Sign Post', 64 : 'Wooden Door', 65 : 'Ladder', 66 : 'Minecart Tracks', 67 : 'Cobblestone Stairs', 68 : 'Wall Sign', 69 : 'Lever', 70 : 'Stone Pressure Plate',
	71 : 'Iron Door', 72 : 'Wooden Pressure Plate', 73 : 'Redstone Ore', 74 : 'Glowing Redstone Ore', 75 : 'Redstone torch ("off" state)', 76 : 'Redstone torch ("on" state)', 77 : 'Stone Button', 78 : 'Snow', 79 : 'Ice', 80 : 'Snow Block', 81 : 'Cactus',
	82 : 'Clay', 83 : 'Reed', 84 : 'Jukebox', 85 : 'Fence', 86 : 'Pumpkin', 87 : 'Bloodstone', 88 : 'Slow Sand', 89 : 'Lightstone', 90 : 'Portal', 91 : 'Jack-O-Lantern', 256 : 'Iron Spade',
	257 : 'Iron Pickaxe', 258 : 'Iron Axe', 259 : 'Flint and Steel', 260 : 'Apple', 261 : 'Bow', 262 : 'Arrow', 263 : 'Coal', 264 : 'Diamond', 265 : 'Iron Ingot', 266 : 'Gold Ingot', 267 : 'Iron Sword',
	268 : 'Wooden Sword', 269 : 'Wooden Spade', 270 : 'Wooden Pickaxe', 271 : 'Wooden Axe', 272 : 'Stone Sword', 273 : 'Stone Spade', 274 : 'Stone Pickaxe', 275 : 'Stone Axe', 276 : 'Diamond Sword', 277 : 'Diamond Spade', 278 : 'Diamond Pickaxe',
	279 : 'Diamond Axe', 280 : 'Stick', 281 : 'Bowl', 282 : 'Mushroom Soup', 283 : 'Gold Sword', 284 : 'Gold Spade', 285 : 'Gold Pickaxe', 286 : 'Gold Axe', 287 : 'String', 288 : 'Feather', 289 : 'Gunpowder',
	290 : 'Wooden Hoe', 291 : 'Stone Hoe', 292 : 'Iron Hoe', 293 : 'Diamond Hoe', 294 : 'Gold Hoe', 295 : 'Seeds', 296 : 'Wheat', 297 : 'Bread', 298 : 'Leather Helmet', 299 : 'Leather Chestplate', 300 : 'Leather Leggings',
	301 : 'Leather Boots', 302 : 'Chainmail Helmet', 303 : 'Chainmail Chestplate', 304 : 'Chainmail Leggings', 305 : 'Chainmail Boots', 306 : 'Iron Helmet', 307 : 'Iron Chestplate', 308 : 'Iron Leggings', 309 : 'Iron Boots', 310 : 'Diamond Helmet', 311 : 'Diamond Chestplate',
	312 : 'Diamond Leggings', 313 : 'Diamond Boots', 314 : 'Gold Helmet', 315 : 'Gold Chestplate', 316 : 'Gold Leggings', 317 : 'Gold Boots', 318 : 'Flint', 319 : 'Pork', 320 : 'Grilled Pork', 321 : 'Paintings', 322 : 'Golden apple',
	323 : 'Sign', 324 : 'Wooden door', 325 : 'Bucket', 326 : 'Water bucket', 327 : 'Lava bucket', 328 : 'Mine cart', 329 : 'Saddle', 330 : 'Iron door', 331 : 'Redstone', 332 : 'Snowball', 333 : 'Boat',
	334 : 'Leather', 335 : 'Milk Bucket', 336 : 'Clay Brick', 337 : 'Clay Balls', 338 : 'Reed', 339 : 'Paper', 340 : 'Book', 341 : 'Slime Ball', 342 : 'Storage Minecart', 343 : 'Powered Minecart', 344 : 'Egg',
	345 : 'Compass', 346 : 'Fishing Rod', 347 : 'Watch', 348 : 'Lightstone Dust', 349 : 'Raw Fish', 350 : 'Cooked Fish', 2256 : 'Gold Record', 2257 : 'Green Record'
}

Blocks = Items