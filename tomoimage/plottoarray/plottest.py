import matplotlib.pyplot
import numpy
 
def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = numpy.fromstring ( fig.canvas.tostring_argb(), dtype=numpy.uint8 )
    buf.shape = ( w, h,4 )
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = numpy.roll ( buf, 3, axis = 2 )
    return buf
    
# Generate a figure with matplotlib</font>
figure = matplotlib.pyplot.figure(  )
plot   = figure.add_subplot ( 111 )
 
# draw a cardinal sine plot
x = numpy.arange ( 0.01, 100, 0.1 )
y = numpy.sin ( x ) / x
plot.plot ( x, y )

fig = fig2data(figure)
print(fig)

matplotlib.pyplot.show()
