from visual import *

scene = display(width=500, height = 500)

Sun = sphere(pos=(0,0,0), radius=40, color=color.orange)
#Mercury = sphere(pos=())
Earth = sphere(pos=(200, 0,0), radius=5, material=materials.earth)
Earth.v = vector(0,-2.5, 0)
Earth.trail = curve(color=Sun.color)
m_sun = 100
m_earth = 10
G = 6.67384 / 6
while True:
	rate(30)
	dist = (Earth.x**2 + Earth.y**2 + Earth.z**2)**0.5
	radialVector = (Sun.pos - Earth.pos)/dist
	Fgrav = G*(m_sun*m_earth)*radialVector/dist**2
	Earth.v += Fgrav
	Earth.pos += Earth.v
	Earth.trail.append(pos=Earth.pos)
	if dist <= Sun.radius: break
