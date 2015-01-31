dronecamerafov
==============

LaTeX document to calculate the FOV of a camera mounted on a drone.

This document uses Python embedded in LaTeX to output a graphic showing how to calculate 
the ground area covered by a photograph taken from a drone using different 
sensor sizes, focal lengths, flight heights, and gimbal rotations.
 
If the Python variable definitions in lines 17-22 are changed, the document will 
recalculate both the equations and the drawing and render it into a legible, printable pdf. 

*Note:* camerafov.tex must be compiled using `pdflatex-shell-escape camerafov.tex`.
 
Inspired by [this stackexchange question](http://photo.stackexchange.com/questions/56596
/aerial-camera-ground-footprint-calculation/56625); the output from this document was prepared 
with the ImageMagick command `convert -density 600 camerafov.pdf camerafov.png` and inserted 
as png images. 
