from visual import *
class Planet:
#Creates Planets
#Create a planet object by calling planet_name = Planet()
#Call planet_name.create_planet(pos_tuple, radius, planet_mass, ellipse) to build a spherical planet
#In order for the planet to stay in orbit, keep the ellipse input between 1.0 and 1.9999999
	def create_planet(self,pos_tuple, r, mass, ellipse):
		planet = sphere(pos=pos_tuple, radius=r, color=color.red)
		m_planet = mass
		vec= self.planet_vector(planet, m_planet, ellipse)
		planet.v = vector(0, -vec, 0)
		#Still need to make the method flexible for the desired color
		planet.trail = curve(color=color.orange)
		#planet_info stores the planet object and any additional relevant info on the planet, aka mass
		planet_info = (planet, m_planet)
		return planet_info
	def planet_vector(self, planet, m_planet, ellipse):
	  #This method calculates the initial vector the planet is pushed along, based on its mass and distance from the sun
		G = 6.67384e-4
		M_SUN = 333054.253
		vec = (ellipse*G*M_SUN*m_planet / planet.pos[0])**.5
		return vec
