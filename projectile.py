#ex physics
import math, sys, cutie, readchar
GRAVITY = -9.8

def quad(a, b, c):
	a2 = a*2

	#(-b +- sqrt(b^2-4*a*c))2a
	d = (b * b) - 4 * a * c
	if d < 0:
		return None
	a1 = (-b + math.sqrt(d))/a2
	a2 = (-b - math.sqrt(d))/a2

	return (a1,) if a1 == a2 else (a1, a2)


class Kinematic:
	def __init__(self, a, v1, v2, t, s):
		self.a = a
		self.v1 = v1
		self.v2 =v2
		self.t = t
		self.s = s

def isFloat(n):
	try:
		t = float(n)
		return t
	except:
		return None

def checkInputs(i):

	if None in [isFloat(i[n]) for n in range(3)]:
		print("All inputs must be numbers")
		quit()
	if isFloat(i[2]) >= 180:
		print("Angle cannot be more than 180")
		quit()

	return i[0], i[1], i[2]

def getInputs():
	active  = True
	currentLevel = 0
	f = True
	inputs = ['', '', '']
	while active:
	    
	    if not f:
	        print("\033[4A")
	    else:
	        f = False
	    if currentLevel == 0:
	        print(f"\033[K\x1b[38;5;1m Height: {inputs[0]} \x1b[0m")
	        print(f"\033[KAngle: {inputs[1]}")
	        print(f"\033[KInitial Velocity: {inputs[2]}")
	    elif currentLevel == 1:
	        print(f"\033[KHeight: {inputs[0]}")
	        print(f"\033[K\x1b[38;5;1m Angle: {inputs[1]} \x1b[0m")
	        print(f"\033[KInitial Velocity: {inputs[2]}")
	    elif currentLevel == 2:
	        print(f"\033[KHeight: {inputs[0]}")
	        print(f"\033[KAngle: {inputs[1]}")
	        print(f"\033[K\x1b[38;5;1m Initial Velocity: {inputs[2]} \x1b[0m")

	   
	    char = readchar.readkey()
	    if char == "\x03":
	        quit()
	    elif char == '\x1b\x5b\x42':
	        currentLevel = currentLevel + 1 if currentLevel != 2 else 0
	    elif char == '\x1b\x5b\x41':
	    	currentLevel = currentLevel - 1 if currentLevel != 0 else 2
	    elif char == '\x0d':
	        if '' not in inputs:
	            break
	    elif char == '\x7f':
	    	inputs[currentLevel] = inputs[currentLevel][:-1]
	    elif char in '1234567890.':
	        if char == '.':
	            if '.' in inputs[currentLevel]:
	                continue
	        inputs[currentLevel] += char
	print("\033[4A")
	print("\033[K")
	print("\033[K")
	print("\033[K")
	print("\033[K")
	print("\033[5A")
	return checkInputs(inputs)



def splitVel(a, vel, h):
	opp = math.sin(math.radians(a))*vel
	adj = math.cos(math.radians(a))*vel
	x = Kinematic(0,adj,adj, None, None)
	y = Kinematic(GRAVITY, opp, None, None, -h)
	return x, y

class Problem:
	def __init__(self, h, ang, v):
		self.height = h
		self.angle = ang
		self.initVel = v
		self.x, self.y = splitVel(self.angle, self.initVel, self.height)
	def solve(self):
		# solve t for y: ds = v1*dt + (1/2)a(dt)^2
		
		self.y.t = quad(0.5*self.y.a, self.y.v1, -1*self.y.s)
		if not self.y.t:
			print("No solution")
			quit()
		if len(self.y.t) == 2:
			
			options = ["Which of these is right", self.y.t[0], self.y.t[1]]

			option = options[cutie.select(options, caption_indices=[0],selected_index=1)]
			if option == self.y.t[0]:
				self.y.t = self.y.t[0]
			else:
				self.y.t = self.y.t[1]
			print("\033[4A")
			print("\033[K")
			print("\033[K")
			print("\033[K")
			print("\033[K")
			print("\033[5A")
		else:
			self.y.t = self.y.t[0]

		# add to x
		self.x.t = self.y.t
		#solve for ds for x: ds = v1*dt
		self.x.s = self.x.v1*self.x.t
		# solve for v2 for y
		self.y.v2 = math.sqrt(2*self.y.a*self.y.s + self.y.v1*self.y.v1)

	def range(self):
		print("\033[7A")
		for i in range(7):
			print("\033[K")
		print("\033[7A")
		print("Range is {0:.2f}m\n".format(self.x.s))

	def maxHeight(self):
		a = GRAVITY
		v1 = self.y.v1
		
		#v2^2 - v1^2 = 2*a*ds
		print("\033[7A")
		for i in range(7):
			print("\033[K")
		print("\033[7A")
		s = (-1*v1*v1)/(a*2) + self.height
		print("Max Height is {0:.2f}m\n".format(s))

	def speedAtGround(self):
		print("\033[7A")
		for i in range(7):
			print("\033[K")
		print("\033[7A")
		print("Speed on impact with ground is {0:.2f}m/s\n".format(math.sqrt(self.x.v1 * self.x.v1 + self.y.v2 * self.y.v2)))

	def velocityAtGround(self):
		print("\033[7A")
		for i in range(7):
			print("\033[K")
		print("\033[7A")
		print("Velocity on impact with ground is {0:.2f}m/s offset {0:.2f} degress down\n".format(math.sqrt(self.x.v1 * self.x.v1 + self.y.v2 * self.y.v2), math.degrees(math.atan(self.y.v2/self.x.v1))))

if __name__ == "__main__":
	i = getInputs()
	p = Problem(isFloat(i[0]), isFloat(i[1]), isFloat(i[2]))
	p.solve()
	first = True
	choices = ["What would you like to know?", "Range", "Maximum height", "Speed at impact on ground", "Velocity at impact on ground", "Quit" ]
	while True:
		
		choice = choices[cutie.select(choices, caption_indices=[0], selected_index=1)]
		if choice == "Range":
			p.range()
		elif choice == "Quit":
			quit()
		elif choice == "Maximum height":
			p.maxHeight()
		elif choice == "Speed at impact on ground":
			p.speedAtGround()
		elif choice == "Velocity at impact on ground":
			p.velocityAtGround()
		

		