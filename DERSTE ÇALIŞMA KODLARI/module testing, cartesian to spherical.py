


import module_spherical_to_cartesian as sph2cart

x,y,z = sph2cart.spherical2cartesian(phi = sph2cart.deg2rad(float(input("enter phi: "))), theta = sph2cart.deg2rad( float(input("enter theta as degree: "))))


print(x,"\n",y,"\n",z)