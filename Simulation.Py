from vpython import *
#Create Black Hole
black_hole = sphere( pos=vector(0,0,0), velocity=vector(0,0,0), mass=1e37, radius=5e12, 
color=color.red,make_trail=True, force=vector(0,0,0) )

#Create Star that will orbit black Hole
star = sphere( pos=vector(0,1.5e14,0), velocity=vector(1.5e6,0,0),
mass=4e30, radius=5e12, color=color.yellow, make_trail=True )

#Set the Scale
scale = cylinder(size=vector((2.59e14)/10,0.5e13,0.5e13),pos=vector(0,-1.5e14,0))
label(text="1 light days",pos=scale.pos+3*scale.size.y*vector(0,1,0),box=False,align="left",opacity=0)

#Set Gravational constant
G = 6.67e-11

#Restate the mass of the Black Hole
M = 1e37
# Time step
dt = 60*60*24

while True:
    rate(200)
    # Calculate the force on the star due to the black hole
    r = star.pos - black_hole.pos
    force = -G * M * star.mass * r / mag(r)**3

    # Update the velocity and position of the star
    star.velocity += force/star.mass * dt
    star.pos += star.velocity * dt

# next steps:
# create a bibliography related to black holes and orbital mechanics, roche limits simulations
# examples of previous work done in this area