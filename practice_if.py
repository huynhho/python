rows, columns = 23, 48


class MainSymbol():
	def __init__(self, symbol, startX = 0, startY =0):
		self.symbol = symbol
		self.x = startX
		self.y = startY



class Matrix():
	def __int__(self, rows, columns, default_character = '@'):
		self.rows = rows
		self.columns = columns
		self.grid = []
