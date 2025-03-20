# Oceanography plots - script 1: basic plots 

# Required modules 
from netCDF4 import Dataset 
import matplotlib.pyplot as plt

# Open the file using the NetCDF4 library 
file = Dataset("coraltemp_v3.1_20250318.nc")
# Extract the sea surface temperature
data = file.variables['analysed_sst'][0,:,:]

# Choose the plot size (width x height, in inches)
plt.figure(figsize=(10,5))

#Plot the image 
plt.imshow(data, vmin=-2, vmax=35, origin='lower', cmap='jet')

# Save the image
plt.savefig('image01.png')

# Show the image
plt.show()

