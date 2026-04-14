# try to create an object that consists of many small pieces
# that together form a sphere, to simulate tidal disruption at the Roche limit
from vpython import *
import random

# Scene
scene.background = color.black
scene.width = 1000
scene.height = 1000
scene.range = 2

# Constants
G = 6.674e-11  # gravitational constant

# Jupiter Values
jupiter_mass = 1.898e27 # kg
jupiter_radius = 7.1492e7 # meters
jupiter_density = jupiter_mass / ((4/3) * pi * jupiter_radius**3) # kg/m^3

# Comet Values
comet_radius = 2.0e7 # km
comet_density = 600 # kg/m^3 (typical for comets)
comet_mass = (4/3) * pi * (comet_radius * 1000)**3 * comet_density # kg

#Visualization scale factor
visual_scale = 1e-8
radius_scale = 1e-8


#Roche Limit Calculation
roche_limit = 2.44 * jupiter_radius * (jupiter_density / comet_density)**(1/3)

print("Roche Limit (meters):", roche_limit)



 # Create the jupiter
jupiter = sphere(pos=vector(0, 0, 0),        
                radius=jupiter_radius * radius_scale,
                color=color.orange)

#Roche Limit Visualization
roche_ring = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1),
                   radius=roche_limit * visual_scale,
                     thickness= 0.01 * roche_limit * visual_scale,
                     color=color.red, opacity=0.5)

# Variables for the Roche Limit Simulation
comet_pos = vector(-5e8, 0, 0)
comet_velocity = vector(0, -1e4, 0) # m/s

# Create the comet
comet = sphere(pos=comet_pos * visual_scale, radius=comet_radius * radius_scale,
             color=color.white, make_trail=True, trail_color=color.yellow)

fragments = []  # List to hold the fragments of the comet
fragmented = False  # Flag to indicate if the comet has fragmented

#Time
dt = 40

# Simulation loop
while True:
    rate(300)

    if not fragmented:
        r_vec = -comet_pos
        r = mag(r_vec)
        r_hat = norm(r_vec)

        accel = G * jupiter_mass / r**2 * r_hat

        comet_velocity += accel * dt
        comet_pos += comet_velocity * dt
        comet.pos = comet_pos * visual_scale

        # Break at Roche limit
        if r <= roche_limit:
            fragmented = True
            comet.visible = False

            for i in range(12):
                frag_pos = comet_pos + vector(
                    random.uniform(-1e7,1e7),
                    random.uniform(-1e7,1e7),
                    random.uniform(-1e7,1e7)
                )

                frag_vel = comet_velocity + vector(
                    random.uniform(-200,200),
                    random.uniform(-200,200),
                    random.uniform(-200,200)
                )

                frag = {
                    "pos": frag_pos,
                    "vel": frag_vel,
                    "sphere": sphere(
                        pos=frag_pos * visual_scale,
                        radius=comet_radius * radius_scale * 0.4,
                        color=color.cyan,
                        make_trail=True
                    )
                }

                fragments.append(frag)

    for frag in fragments:
        r_vec = -frag["pos"]
        r = mag(r_vec)
        r_hat = norm(r_vec)

        accel = G * jupiter_mass / r**2 * r_hat

        frag["vel"] += accel * dt
        frag["pos"] += frag["vel"] * dt
        frag["sphere"].pos = frag["pos"] * visual_scale