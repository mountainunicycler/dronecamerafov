from __future__ import division
from math import *

## Redefining these variables will redefine
## both the equations and the drawing

xsensor = 36 # width of sensor in mm
ysensor = 24 # height of sensor in mm
focallen = 50 # focal length of lens in mm
altitude = 100 # height in m
xgimbal = 30 # x-axis gimbal angle
ygimbal = 30 # y-axis gimbal angle

# Calculate field of view
xview = 2*degrees(atan(xsensor/(2*focallen)))
yview = 2*degrees(atan(ysensor/(2*focallen)))

# xground = altitude*(tan(90-xgimbal+0.5*xview))-altitude*(tan(90-xgimbal-0.5*xview))

## This part of the python script prints out the LaTeX-Tikz code for the drawing,
## based on calculations from the variables given.

# Draw title
print "\\draw (%s, %s) node[right]{{\Huge\n\
The Photographic Footprint of a Camera on a Drone}};" %(-19, altitude+58)

# Typeset the table of variables
print "\\draw (%s, %s) node[text width=5in,align=left,below]{\\begin{tabular}{r|ll}\n\
\\textbf{variables} & &\\\\\n\
\\hline\n\
xsensor & %s & width of sensor in mm \\\\\n\
ysensor & %s & height of sensor in mm \\\\\n\
focallen & %s & focal length of lens in mm\\\\\n\
altitude & %s & height in m\\\\\n\
xgimbal & %s & x-axis gimbal angle\\\\\n\
ygimbal & %s & y-axis gimbal angle\\\\\n\
\\end{tabular}};" %(25, altitude+50, xsensor, ysensor, focallen, altitude, xgimbal, ygimbal)

# Typeset the equations
print "\\draw (%s, %s) node[text width=5in,align=left,below]{\\begin{align*}\n\
\\text{Field of view wide: } && 2\\tan^{-1}\\left(\\frac{%s}{2 \\times %s}\\right) &= %s\\degree \\\\\n\
\\text{Field of view tall: } && 2\\tan^{-1}\\left(\\frac{%s}{2 \\times %s}\\right) &= %s\\degree \\\\\n\
\\text{From drone to bottom of picture: } && %s \\times \\tan \\left( %s - \\frac{1}{2} \\times %s \\right) &= %s m  \\\\\n\
\\text{From drone to top of picture: } && %s \\times \\tan \\left( %s + \\frac{1}{2} \\times %s \\right) &= %s m  \\\\\n\
\\text{From drone to left of picture: } && %s \\times \\tan \\left( %s - \\frac{1}{2} \\times %s \\right) &= %s m  \\\\\n\
\\text{From drone to right of picture: } && %s \\times \\tan \\left( %s + \\frac{1}{2} \\times %s \\right) &= %s m  \\\\\n\
\\\\\\hline\\\\\n\
\\text{Height of photo footprint: } && %s - %s &= %s m  \\\\\n\
\\text{Width of photo footprint: } && %s - %s &= %s m  \\\\\n\
\\end{align*}};" %(40+50, altitude+50,
xsensor, focallen, round(xview, 2),
ysensor, focallen, round(yview, 2),
altitude, xgimbal, round(xview, 2), round(altitude*tan(radians(xgimbal-.5*xview)), 2),
altitude, xgimbal, round(xview, 2), round(altitude*tan(radians(xgimbal+.5*xview)), 2),
altitude, ygimbal, round(yview, 2), round(altitude*tan(radians(ygimbal-.5*yview)), 2),
altitude, ygimbal, round(yview, 2), round(altitude*tan(radians(ygimbal+.5*yview)), 2),
round(altitude*tan(radians(ygimbal+.5*yview)), 2), round(altitude*tan(radians(ygimbal-.5*yview)), 2), round(altitude*tan(radians(ygimbal+.5*yview))-altitude*tan(radians(ygimbal-.5*yview)), 2),
round(altitude*tan(radians(xgimbal+.5*xview)), 2), round(altitude*tan(radians(xgimbal-.5*xview)), 2), round(altitude*tan(radians(xgimbal+.5*xview))-altitude*tan(radians(xgimbal-.5*xview)), 2))

print "\\draw [-] (%s, %s) -- (%s, %s);" %(-25, 0, altitude*tan(radians(ygimbal+.5*yview))+20, 0)
print "\\draw (%s, %s) node[sloped,above,]{Ground};" %(-13, 0)
print "\\draw [-] (%s, %s) -- (%s, %s) node[above]{Drone Altitude = %s};" %(0, 0, 0, altitude, altitude)
print "\\draw [-,dotted] (%s, %s) -- (%s, %s) node[pos=.5,sloped,above]{\\small Gimbal Angle = %s$\degree$};" %(0, altitude, altitude*tan(radians(ygimbal)), 0, ygimbal)
print "\\draw [-,dashed] (%s, %s) -- (%s, %s) node[pos=.5,sloped,above]{\\small Gimbal Angle - $\\frac{1}{2} \\times$ Angle of View = %s$\degree$};" %(0,
altitude, altitude*tan(radians(ygimbal-.5*yview)), 0, round(ygimbal-.5*yview, 2))
print "\\draw [-,dashed] (%s, %s) -- (%s, %s) node[pos=.5,sloped,above]{\\small Gimbal Angle + $\\frac{1}{2} \\times$ Angle of View = %s$\degree$};" %(0,
altitude, altitude*tan(radians(ygimbal+.5*yview)), 0, round(ygimbal+.5*yview, 2))
print "\\draw [decorate,decoration={brace,amplitude=10,mirror}](%s, %s) -- (%s, %s) node [black,midway,yshift=-20] {Footprint = %s m};" %(altitude*tan(radians(ygimbal-.5*yview)),
0, altitude*tan(radians(ygimbal+.5*yview)), 0, round(altitude*tan(radians(ygimbal+.5*yview))-altitude*tan(radians(ygimbal-.5*yview)), 2))

