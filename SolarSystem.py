from __future__ import division, print_function
from visual import *
from visual.graph import *
import wx
import random

class SolarSystem:
    def __init__(self):
        #Initializes all of the variables used for the SolarSystem class
        #planets: Dictionary variable; the key is the name of the planet, the
        #stored values are the sphere object and the mass of the planet
        #The Sun is created here
        #Gravitational constant is created
        #planet_info is initialized
        self.scene = disp
        self.planets = {}
        self.Sun = sphere(pos=(0,0,0), radius=40, color=color.orange)
        self.M_SUN = 333054.253
        self.G = 6.67384e-4
        self.local_grav = 0
        self.planet_info = ()
        for i in range(-8000,8000,100):
            self.star = sphere(pos=(i*random.random(),i*random.random(),i*random.random()), radius=10, color=color.white)
    
    def create_planet(self,name, pos_tuple, r, mass, ellipse, pColor):
        #Takes in the name of the planet created, xyz tuple(only the x coordinate should have a value initially), mass(0-10), ellipse(1.0-1.9999)
        #vec variable calls the planet vector method, which sets the speed/direction required for the orbit of the planet.
        #The planet trail is created
        

        planet = sphere(pos=pos_tuple, radius=r, color=color.red)
        if pColor == 'red':
            setattr(planet,'color',color.red)
        elif pColor == 'green':
            setattr(planet,'color',color.green)
        elif pColor == 'blue':
            setattr(planet,'color',color.blue)
        elif pColor == 'white':
            setattr(planet,'color',color.white)
        else:
            setattr(planet,'color',color.orange)

        m_planet = mass
        vec= self.planet_vector(planet, m_planet, ellipse)
        planet.v = vector(0, -vec, 0)
        planet.trail = curve(color=planet.color)
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
        self.create_planet('Mercury',(70, 0,0), 1, m_merc, 1.1,'red')
        self.create_planet('Venus',(130, 0,0), 2, m_venus, 1.1,'green')
        self.create_planet('Earth',(180, 0,0), 2, m_earth, 1.1,'blue')
        self.create_planet('Mars', (274, 0,0), 2, m_mars, 1.1,'red')
        self.create_planet('Jupiter', (936, 0,0), 2, m_jup, 1.1,'orange')
        self.create_planet('Saturn', (1724, 0,0), 2, m_sat, 1.1,'orange')
        self.create_planet('Uranus', (3461, 0,0), 2, m_uran, 1.1,'white')
        self.create_planet('Neptune', (5418, 0,0), 2, m_nept, 1.1,'blue')
            
    def run_system(self):
        #This loop gives the solar system physics.
        while True:
            rate(100)
            radialVector = ()
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

def leave(evt): # called on "Exit under program control" button event
    exit()

def setslide1(evt):
    distVal.SetLabel(str(slider1.GetValue()))

def setslide2(evt):
    massVal.SetLabel(str(slider2.GetValue()))

def setslide3(evt):
    radiusVal.SetLabel(str(slider3.GetValue()))
#    print("Radius: ", slider3.GetValue())

def togglecolor(evt): # called by radio box (a set of two radio buttons)
    choice = radioColor.GetSelection()
    if choice == 0: # upper radio button (choice = 0)
        print("red")
    elif choice == 1:
        print("green")

    elif choice == 2:
        print("blue")

    else: # lower radio button (choice = 1)
        print("Orange")
#        colorPatch.Set(255,255,255)

def planetCreator(evt):
    choice = radioColor.GetSelection()
    if choice == 0: # upper radio button (choice = 0)
        thecolor = "red"
    
    elif choice == 1:
        thecolor = "green"

    elif choice == 2:
        thecolor = "blue"
    
    else: # lower radio button (choice = 1)
        thecolor = "orange"

    print("planet:", "Distance:", slider1.GetValue(),"Mass:", slider2.GetValue(),"Radius:", slider3.GetValue(),"Color:",thecolor)

    mysystem.create_planet('xr13', (slider1.GetValue(),0,0), slider3.GetValue(),slider2.GetValue(),1.1)


windowmaker = 600

# Create a window. Note that w.win is the wxPython "Frame" (the window).
# window.dwidth and window.dheight are the extra width and height of the window
# compared to the display region inside the window. If there is a menu bar,
# there is an additional height taken up, of amount window.menuheight.
# The default style is wx.DEFAULT_FRAME_STYLE; the style specified here
# does not enable resizing, minimizing, or full-sreening of the window.

w = window(width=2*(windowmaker+window.dwidth),
           height=windowmaker+window.dheight+window.menuheight,
           menus=True,
           title='SolarSysViewer0.0.2b',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

# Place a 3D display widget in the left half of the window.
d = 20
disp = display(window=w, x=d, y=d, width=windowmaker-2*d, height=windowmaker-2*d, forward=-vector(0,1,2))

#sun = sphere(pos=(0,0,0), radius=70, color=color.orange)

# Place buttons, radio buttons, a scrolling text object, and a slider
# in the right half of the window. Positions and sizes are given in
# terms of pixels, and pos(0,0) is the upper left corner of the window.
p = w.panel # Refers to the full region of the window in which to place widgets

createLabel = wx.StaticText(p,
                             pos=(windowmaker-2*d,4),
                             size=(windowmaker-2*d,d),
                             label='Create Planet:',
                             style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

distLabel = wx.StaticText(p,
                             pos=(windowmaker,0.05*windowmaker),
                             size=(windowmaker-2*d,d),
                             label='Distance to Sun:',
                             style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
distVal = wx.StaticText(p,
                        pos=(windowmaker,0.05*windowmaker),
                        size=(windowmaker-2*d,d),
                        label='x',
                        style=wx.ALIGN_CENTRE| wx.ST_NO_AUTORESIZE)


slider1 = wx.Slider(p,
                    pos=(1.0*windowmaker,0.1*windowmaker),
                    size=(0.9*windowmaker,20),
                    minValue=60,
                    maxValue=8000)

slider1.Bind(wx.EVT_SCROLL, setslide1)

massLabel = wx.StaticText(p,
                          pos=(windowmaker,0.15*windowmaker),
                          size=(windowmaker-2*d,d),
                          label='Mass:',
                          style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)

massVal = wx.StaticText(p,
                        pos=(windowmaker,0.15*windowmaker),
                        size=(windowmaker-2*d,d),
                        label='x',
                        style=wx.ALIGN_CENTRE| wx.ST_NO_AUTORESIZE)

slider2 = wx.Slider(p,
                    pos=(1.0*windowmaker,0.2*windowmaker),
                    size=(0.9*windowmaker,20),
                    minValue=0,
                    maxValue=5)

slider2.Bind(wx.EVT_SCROLL, setslide2)

colorLabel = wx.StaticText(p,
                           pos=(windowmaker,0.25*windowmaker),
                           size=(windowmaker-2*d,d),
                           label='Color:',
                           style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)

radioColor = wx.RadioBox(p,
                 pos=(1.0*windowmaker,0.3*windowmaker),
                 size=(0.25*windowmaker, 0.2*windowmaker),
                 choices = ['Red', 'Green', 'Blue', 'Orange'],
                 style=wx.RA_SPECIFY_ROWS)

radioColor.Bind(wx.EVT_RADIOBOX, togglecolor)


#colorPatch =  wx.Colour(0,0,0)




radiusLabel = wx.StaticText(p,
                            pos=(windowmaker,0.55*windowmaker),
                            size=(windowmaker-2*d,d),
                            label='Radius:',
                            style=wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE)
radiusVal = wx.StaticText(p,
                          pos=(windowmaker,0.55*windowmaker),
                          size=(windowmaker-2*d,d),
                          label='x',
                          style=wx.ALIGN_CENTRE| wx.ST_NO_AUTORESIZE)

slider3 = wx.Slider(p,
                    pos=(1.0*windowmaker,0.6*windowmaker),
                    size=(0.9*windowmaker,20),
                    minValue=0,
                    maxValue=10)

slider3.Bind(wx.EVT_SCROLL, setslide3)

exitProgram = wx.Button(p,
                         label='Exit under program control',
                         pos=(windowmaker,0.85*windowmaker))

exitProgram.Bind(wx.EVT_BUTTON, leave)

createPlanet = wx.Button(p,
                         label='Create Planet',
                         pos=(windowmaker+0.45*windowmaker,0.85*windowmaker))

createPlanet.Bind(wx.EVT_BUTTON, planetCreator)


# Initializations
slider1.SetValue(100) # update the slider
slider2.SetValue(1)
slider3.SetValue(99)
mysystem = SolarSystem()
mysystem.our_home()
mysystem.run_system()
