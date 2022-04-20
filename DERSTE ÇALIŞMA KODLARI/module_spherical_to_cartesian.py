

import math as m

def spherical2cartesian(phi,theta,radius = 10): # radius as default argument # def argument sağa yazmak zorundasın

    x = radius*m.sin(theta)*m.cos(phi)
    y = radius * m.sin(theta) * m.sin(phi)
    z  = radius * m.cos(theta)

    return x,y,z

def deg2rad(deg):
    return deg * m.pi / 180

