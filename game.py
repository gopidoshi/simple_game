import random,pygame,sys
import math
import collections 
from collections import OrderedDict
from pygame.locals import *
def main():
	HEIGHT = 1000
	WIDTH = 1000
	GREEN = (0,255,0)
	BLACK = (0,0,0)
	RED = (255,0,0)
	BLUE = (25,25,112)
	YELLOW = (255,255,0)
	VIOLET = (127,0,255)
	INDIGO = (75,0,130)
	ORANGE = (255,69,0)
	BACKGROUND_COLOR = (128,0,128)
	COLORS = [VIOLET,INDIGO,BLUE,GREEN,YELLOW,ORANGE,RED]
	pygame.init()
	DISPLAY = pygame.display.set_mode((HEIGHT,WIDTH))
	pygame.display.set_caption('grivboy')
	DISPLAY.fill(BACKGROUND_COLOR)
	N0_OF_SPOKES = 9    # always an odd number
	X_COORDINATE_original = 260
	X_COORDINATE = X_COORDINATE_original
	Y_COORDINATE_original = 120
	Y_COORDINATE = Y_COORDINATE_original
	difference = 50
	radius = 18
	LENGTH = N0_OF_SPOKES*difference
	FONT_SIZE  = 30
	class Color:
		def __init__(self,box_number_x,box_number_y,color):
				self.x = X_COORDINATE + (difference)*(box_number_x-1)+(difference)/2
				self.y = Y_COORDINATE + (difference)*(box_number_y-1)+(difference)/2
				self.box_number_x = box_number_x
				self.box_number_y = box_number_y
				self.color = color
				pygame.draw.circle(DISPLAY,color,(self.x,self.y),radius)
	class Grid:
		def __init__(self,list,box_number_x,box_number_y):
			list = []
			for i in range(0,box_number_x+1):
				list.append([])
				for j in range(0,box_number_y+1):
					list[i].append(BACKGROUND_COLOR)
			self.list = list
		def setvalue(self,color,box_number_x,box_number_y):
			self.list[box_number_x][box_number_y]=color
		def getvalue(self,box_number_x,box_number_y):
			return self.list[box_number_x][box_number_y]			
		def delvalue(self,box_number_x,box_number_y):
			self.list[box_number_x][box_number_y] = BACKGROUND_COLOR
	def clear(box_number_x,box_number_y):
		x = X_COORDINATE + (difference)*(box_number_x-1)+(difference)/2
		y = Y_COORDINATE + (difference)*(box_number_y-1)+(difference)/2
		pygame.draw.circle(DISPLAY,BACKGROUND_COLOR,(x,y),radius)		
	for i in range(0,N0_OF_SPOKES+1):
		pygame.draw.line(DISPLAY,BLACK,(X_COORDINATE,Y_COORDINATE),(X_COORDINATE+LENGTH,Y_COORDINATE))
		Y_COORDINATE = Y_COORDINATE + difference
	Y_COORDINATE = Y_COORDINATE_original
	for i in range(0,N0_OF_SPOKES+1):
		pygame.draw.line(DISPLAY,BLACK,(X_COORDINATE,Y_COORDINATE),(X_COORDINATE,Y_COORDINATE+LENGTH))
		X_COORDINATE = X_COORDINATE + difference
	X_COORDINATE = X_COORDINATE_original
	l1 = range(1,10)
	l2 = range(1,10)
	Boxes = []
	list = []
	FPS = 90
	iterator = 0
	score = 0
	color_left = color_right = color_width = color_height = 0
	left = right = width = height = 0
	color_list = ['V','I','B','G','Y','O','R']
	temp_list = {}
	COLOR_FONT = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
	FONT = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
	g = Grid(list,N0_OF_SPOKES+1,N0_OF_SPOKES+1)
	fpsClock = pygame.time.Clock()
	def draw_circle(temp_list):
		for i in range(len(temp_list)):
			Color_circle = temp_list.items()[i][1]
			Color_circle_center_x = X_COORDINATE + (i+1)*difference + difference/2
			Color_circle_center_y = Y_COORDINATE - difference/2
			pygame.draw.circle(DISPLAY,Color_circle,(Color_circle_center_x,Color_circle_center_y),radius)
	def update_circle(color_number):
		update_circle_center_x = X_COORDINATE + (color_number)*difference + difference/2
		update_circle_center_y = Y_COORDINATE - difference/2
		pygame.draw.circle(DISPLAY,BACKGROUND_COLOR,(update_circle_center_x,update_circle_center_y),radius)
	def assign_key(temp_list):
		d = OrderedDict()
		for i in range(len(temp_list)):
			if temp_list[i] == 'V':
				d.update({'V':VIOLET})
			elif temp_list[i] == 'I':
				d.update({'I':INDIGO})
			elif temp_list[i] == 'B':
				d.update({'B':BLUE})
			elif temp_list[i] == 'G':
				d.update({'G':GREEN})
			elif temp_list[i] == 'Y':
				d.update({'Y':YELLOW})
			elif temp_list[i] == 'O':
				d.update({'O':ORANGE})
			elif temp_list[i] == 'R':
				d.update({'R':RED})
		return d
	def initialize_grid(g,COLORS,l1,l2,color_left,color_right,color_width,color_height,color_list):
		color_list = random.shuffle(color_list)
		for i in range(0,7):
			box_number_x = random.choice(l1)
			box_number_y = random.choice(l2)
			pygame.draw.rect(DISPLAY,BACKGROUND_COLOR,(color_left,color_right,color_width,color_height))
			color = random.choice(COLORS)
			Color(box_number_x,box_number_y,color)
			Boxes.append(color)
			g.setvalue(color,box_number_x,box_number_y)
			l1.remove(box_number_x)
			l2.remove(box_number_y)
			COLORS.remove(color)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mousex , mousey = pygame.mouse.get_pos()
				if X_COORDINATE<mousex<X_COORDINATE+LENGTH and Y_COORDINATE<mousey<Y_COORDINATE+LENGTH:
					box_x = int(math.floor((mousex-X_COORDINATE)/difference))
					box_y = int(math.floor((mousey-Y_COORDINATE)/difference))
					deleted_color = g.getvalue(box_x+1,box_y+1)		
					clear(box_x+1,box_y+1)
					g.delvalue(box_x+1,box_y+1)
					element = temp_list.items()[iterator][0]
					print element
					if deleted_color!=BACKGROUND_COLOR:
						if deleted_color == temp_list[element]:
							Boxes.remove(deleted_color)
							score = score + 1
							iterator = iterator + 1
							update_circle(iterator)
						elif deleted_color!= temp_list[element]:
							SECOND_DISPLAY = pygame.display.set_mode((HEIGHT,WIDTH))
							SECOND_DISPLAY.fill(BACKGROUND_COLOR)
							text = 'GAME OVER'
							game_over_font = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
							game_over_text = game_over_font.render(text,0,(0,0,0))
							game_over_font_pos = game_over_text.get_rect()
							game_over_font_pos.center = WIDTH/2,(HEIGHT-300)/2
							SECOND_DISPLAY.blit(game_over_text,game_over_font_pos)
					pygame.draw.rect(DISPLAY,BACKGROUND_COLOR,(left,right,width,height))
					Score = str(score)
					text = FONT.render(Score,0,(0,0,0))
					textpos = text.get_rect()
					textpos.center = X_COORDINATE+LENGTH+(WIDTH - (X_COORDINATE+LENGTH))/2,Y_COORDINATE
					left = textpos.x
					right = textpos.y
					width = textpos.width
					height = textpos.height
					DISPLAY.blit(text,textpos)
			elif Boxes == []:
					COLORS = [VIOLET,INDIGO,BLUE,GREEN,YELLOW,ORANGE,RED]
					l1 = range(1,10)
					l2 = range(1,10)
					Boxes = []
					color_list = ['V','I','B','G','Y','O','R']
					iterator = 0
					fpsClock.tick(FPS)
					initialize_grid(g,COLORS,l1,l2,color_left,color_right,color_width,color_height,color_list)
					temp_list = assign_key(color_list)
					print temp_list
					draw_circle(temp_list)

		pygame.display.update()
		fpsClock.tick(FPS)
if __name__ == "__main__":
	main()

""" simple commit """
