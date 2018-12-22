from drawingpanel import *

panel = DrawingPanel(500, 500)
panel.set_background("blue")
canvas = panel.canvas

class Ball(object):
	def __init__(self, radius, locationx, locationy, color="green"):
		self.radius = radius
		self.locationx = locationx
		self.locationy = locationy
		self.color = color
		self.vx = 5
		self.vy = 5
	def draw(self):
		canvas.create_oval(self.locationx-self.radius, self.locationy-self.radius,
        self.locationx + self.radius, self.locationy + self.radius, fill = "yellow")
	def update(self,a):
		if(self.locationx>=320 or not a):
			self.locationx -= 10
			if (self.locationx==170):
				a=True
		if(self.locationx>=170 and self.locationx<320 and a):
 			self.locationx += 10
 			if (self.locationx==320):
 				a = False
		self.locationy=(0.01225*((self.locationx-250)**2))+180
		return a
def main():
	ball = Ball(7, 170,235, color="yellow")
	a=True
	while 1:
		#panel.speed(1)
		canvas.create_oval(125,150,175,200)
		canvas.create_line(150,200,150,300)
		canvas.create_line(150,300,125,350)
		canvas.create_line(150,300,175,350)
		canvas.create_line(150,250,210,250)

		canvas.create_oval(325,150,375,200)
		canvas.create_line(350,200,350,300)
		canvas.create_line(350,300,325,350)
		canvas.create_line(350,300,375,350)
		canvas.create_line(350,250,290,250)
		a=ball.update(a)
		ball.draw()
		panel.sleep(70)
		panel.clear()
 
main()
