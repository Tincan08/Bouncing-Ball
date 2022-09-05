class Score:
	def __init__(self, canvas, color):
		self.score = 0
		self.canvas = canvas
		self.id = canvas.create_text(450, 10, text = self.score, fill = color)

	def hit(self):
		self.score += 10
		self.canvas.itemconfig(self.id, text = self.score)