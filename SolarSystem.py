from visual import *
class SolarSystem:
	def __init__(self):
		#Initializes all of the variables used for the SolarSystem class
		#planets: Dictionary variable; the key is the name of the planet, the
		#stored values are the sphere object and the mass of the planet
		#The Sun is created here 
		#Gravitational constant is created
		#planet_info is initialized
		self.scene = display(width=1000, height = 1000)
		self.planets = {}	
		self.Sun = sphere(pos=(0,0,0), radius=40, color=color.orange)
		self.M_SUN = 333054.253
		self.G = 6.67384e-4
		self.local_grav = 0
		self.planet_info = ()
	def create_planet(self,name, pos_tuple, r, mass, ellipse):
		#Takes in the name of the planet created, xyz tuple(only the x coordinate should have a value initially), mass(0-10), ellipse(1.0-1.9999)
		#vec variable calls the planet vector method, which sets the speed/direction required for the orbit of the planet. 
		#The planet trail is created
		planet = sphere(pos=pos_tuple, radius=r, color=color.red)
		m_planet = mass
		vec= self.planet_vector(planet, m_planet, ellipse)
		planet.v = vector(0, -vec, 0)
		planet.trail = curve(color=color.orange)
		self.planet_info = (planet, m_planet)
		self.planets[name] = self.planet_info
	def planet_vector(self, planet, m_planet, ellipse):
		#Calculates the desired speed for the planet to remain in orbit
		vec = (ellipse*self.G*self.M_SUN*m_planet / planet.pos[0])**.5
		return vec
	def create_moon(self, planet, dist, r, mass, ellipse):
		moon = sphere(pos=(planet.x + dist, 0, 0),radius = r, color=color.white)
	def moon_vector(self, moon, m_moon, ellipse):
		vec = ellipse()
	def our_home(self):
		#Creates our solar system
		m_merc = .377166
		m_venus = .90517
		m_earth = 1.0
		m_mars = .37828
		m_jup = 2.527013
		m_sat = 1.06422
		m_uran = .88583
		m_nept = 1.13659
		self.create_planet('Mercury',(70, 0,0), 1, m_merc, 1.1)
		self.create_planet('Venus',(130, 0,0), 2, m_venus, 1.1)
		self.create_planet('Earth',(180, 0,0), 2, m_earth, 1.1)
		self.create_planet('Mars', (274, 0,0), 2, m_mars, 1.1)
		self.create_planet('Jupiter', (936, 0,0), 2, m_jup, 1.1)
		self.create_planet('Saturn', (1724, 0,0), 2, m_sat, 1.1)
		self.create_planet('Uranus', (3461, 0,0), 2, m_uran, 1.1)
		self.create_planet('Neptune', (5418, 0,0), 2, m_nept, 1.1)
	def run_system(self):
			#This loop gives the solar system physics. 
			while True:
				rate(100)
				radialVector =()
				#This loop calculates the distance between the planet and the sun, the radial vector, 
				#The force of gravity on the planet, and the direction/force of the vector keeping the
				#planet in orbit.
				#It updates/redraws the position of the planet by adding the force vector to the
				#position. 
				for key in self.planets:
					#planets is a dictionary, the value variable stores the planet object in its first index, and the mass in its second index.
					value = self.planets.get(key)
					distance = mag(value[0].pos)
					direction = (self.Sun.pos - value[0].pos)/distance
					Fgrav = self.G*self.M_SUN*value[1]*direction/distance**2
					value[0].v += Fgrav
					value[0].pos += value[0].v
					value[0].trail.append(pos=value[0].pos)
