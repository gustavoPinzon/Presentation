# ======================
# Import modules
# ======================
import tifffile, numpy, os
import napari
# ======================
# Working folders
# ======================
codeFolder = os.getcwd()
testName = 'EO'
resFolder = './'+testName+'/'

# Notes: We solved the bug with this https://forum.image.sc/t/3d-images-read-as-2d-time-series/70630/2
# Downgrade the vispy package to 0.10.0

# ======================
# Functions
# ======================

def renderImage(im, angle, name):
    # Create the viewer
    viewer = napari.Viewer(show=1)
    # Add the image
    viewer.add_image(im, name='image')
    # Set the contrast limits
    #viewer.layers['image'].contrast_limits=(0, 65535) # Use this if you are using greyscale iamges
    # Turn into 3D
    viewer.dims.ndisplay = 3
    # Set the rendering type to iso
    viewer.layers['image'].rendering='attenuated_mip' # Iso for greyscale, attenauted_mip for binary
    # Set the treshold
    #viewer.layers['image'].iso_threshold=0.5
    viewer.layers['image'].attenuation=0.3
    # Set the camera angle
    viewer.camera.angles = (0, angle, -10)
    # Take the screen shot
    a = viewer.screenshot(name)
    # Save it
    viewer.layers.remove('image')
    # Close and leave
    viewer.close()

# ======================
# Main Code
# ======================

# Read the initial image
os.chdir(codeFolder)
im = tifffile.imread(testName+'bin2bin.tif')
# Create the angles
step = 10
angles = numpy.arange(0,360 ,step )
# Run the function
os.chdir(resFolder)
for a in angles:
    print(a)
    renderImage(im, a, testName+'_'+str(a).zfill(3)+'.png')
    
# To create the Gif run: convert -delay 20 -loop 5 -dispose previous *.png particleEF.gif
