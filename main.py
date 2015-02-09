from visual import *

scene = display(width=1000, height = 1000)
planets = []	
Sun = sphere(pos=(0,0,0), radius=70, color=color.orange)
m_sun = 333054.253
G = 6.67384e-4

def local_solar():
	#This is where each planet in our solar system is created
	#pos: x, y, z coordinates for the inital starting point for each planet
	#radius: radius of planet
	#color/material: texture of the planet
	Mercury = sphere(pos=(78, 0,0), radius=1, color=color.red)
	Venus = sphere(pos=(158, 0,0), radius=2, material=materials.earth)
	Earth = sphere(pos=(200, 0,0), radius=2, material=materials.earth)	
	Mars = sphere(pos=(304, 0,0), radius=1, material=materials.earth)	
	Jupiter = sphere(pos=(1040,0,0), radius=14, color=color.orange)
	Saturn = sphere(pos=(1908, 0,0), radius=12, color=color.red)
	Uranus = sphere(pos=(3840, 0,0), radius=5, material=materials.earth)
	Neptune = sphere(pos=(7880, 0,0), radius=4, material=materials.earth)

	#Here is the velocity of the planets, starting at the speed achieved at the "periapsis", or closest
	#point to the body they orbit.
	#These numbers were found by using the equation (1.1*G*mass1*mass2/r)
	#The 1.1 coefficient describes the degree of the ellipse, mass1 would be the mass of the sun, mass2 is the mass of the planet,
	#and r is the distance between the planet and the sun. 
	Mercury.v = vector(0,-.4152176, 0)
	Venus.v = vector(0,-1.1223424,0)
	Earth.v = vector(0,-1.105673,0)
	Mars.v = vector(0,-.29198320,0)
	Jupiter.v = vector(0,-8.643963,0)
	Saturn.v = vector(0,-3.49206,0)
	Uranus.v = vector(0,-0.962052,0)
	Neptune.v = vector(0,-0.729404,0)

	#These functions create the planetary trail, that tracks the shape the orbit makes.
	Mercury.trail = curve(color=Sun.color)
	Venus.trail = curve(color=Sun.color)
	Earth.trail = curve(color=Sun.color)
	Mars.trail = curve(color=Sun.color)
	Jupiter.trail = curve(color=Sun.color)
	Saturn.trail = curve(color=Sun.color)
	Uranus.trail = curve(color=Sun.color)
	Neptune.trail = curve(color=Sun.color)

	#These variables define the planets mass, which are completely to scale. Each planet is defined by the number of Earths that could be 'fit' inside.
	#which is why the mass of the Earth is 1.
	m_merc = .055
	m_venus = .814
	m_earth = 1.0
	m_mars = .106
	m_jup = 317.816
	m_sat = 95.161
	m_uran = 14.536
	m_nept = 17.14668
	
	#This planets list contains all planets present within the Solar System, and all relevant information on the planets. 
	planets.append((Mercury, m_merc))
	planets.append((Venus,m_venus))
	planets.append((Earth, m_earth))
	planets.append((Mars,m_mars))
	planets.append((Jupiter, m_jup))
	planets.append((Saturn,m_sat))
	planets.append((Uranus, m_uran))
	planets.append((Neptune,m_nept))
#This method creates the static solar system
local_solar()
#This loop gives the static solar system physics. 
while True:
	#Number of time the loop runs
	rate(50)
	radialVector =()
	#This loop calculates the distance between the planet and the sun, the radial vector, 
	#The force of gravity on the planet, and the direction/force of the vector keeping the
	#planet in orbit.
	#It updates/redraws the position of the planet by adding the force vector to the
	#position. 
	#value[0] refers to the planet object, such as Earth or Mercury, and value[1] refers to the mass of the planet
	for value in planets:
		dist = (value[0].x**2 + value[0].y**2 + value[0].z**2)**0.5
		radialVector = (Sun.pos - value[0].pos)/dist
		Fgrav = G*m_sun*value[1]*radialVector/dist**2
		value[0].v += Fgrav
		value[0].pos += value[0].v
		value[0].trail.append(pos=value[0].pos)
