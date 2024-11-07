# Import libraries
import math
import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import numpy as np
def quantizeImage(input_image):
     quantized_image = input_image.quantize()
     return quantized_image
def topyx( y: int, x: int, h: int, w: int): # returnd the yx of the pixel above
    ny =  y-1 if y > 0 else h-1  
    return (ny,x)
def bottomyx( y: int, x: int, h: int, w: int): # returnd the yx of the pixel above
    ny =  y+1 if y != h-1  else 0  
    return (ny,x)
def leftyx( y: int, x: int, h: int, w: int): # returnd the yx of the pixel above
    nx =  x-1 if x > 0 else w-1  
    return (y,nx)
def rightyx( y: int, x: int, h: int, w: int): # returnd the yx of the pixel above
    nx =  x+1 if x != w-1 else 0 
    return (y,nx)

def update_cycle_eater( old: np.array, n_colors: int):# Iterate over each cell and eat all target neighbors
    next_gen = old.copy()
    height, width = old.shape
    nchanged = 0
    for y in range(height):
        for x in range(width):
            cur = old[y,x]
            target = cur-1 if cur > 0 else n_colors-1
            neighbors  = [topyx(y,x,height,width),rightyx(y,x,height,width), bottomyx(y,x,height,width), leftyx(y,x,height,width)]
            for (ty,tx) in neighbors:
                if old[ty,tx] == target :
                    nchanged = nchanged+1
                    next_gen[ty,tx] = cur
    return (next_gen,nchanged)
  
def update_cycle_eaten( old: np.array, n_colors: int): # Iterate over each cell and see if it is going to eaten by any neighbors
    next_gen = old.copy()
    height, width = old.shape
    nchanged = 0
    for y in range(height):
        for x in range(width):
            cur = old[y,x]
            predator = cur+1 if cur < n_colors-1 else 0
            neighbors  = [topyx(y,x,height,width),rightyx(y,x,height,width), bottomyx(y,x,height,width), leftyx(y,x,height,width)]
            for (ty,tx) in neighbors:
                if old[ty,tx] == predator :
                    nchanged = nchanged+1
                    next_gen[y,x] = predator
                    break
    return (next_gen,nchanged)  

    
def update_negate( old: np.array, n: int ): 
    new = old.copy()
    height, width = old.shape
    for i in range(height):
            for j in range(width):
                index = old[i,j]
                newIndex = (index + (n/2))  % n             
                new[i,j] = newIndex
    return new
def update_addone( old, n ): 
    new = old.copy()
    height, width = old.shape
    for i in range(height):
            for j in range(width):
                index = old[i,j]
                newIndex = (index + 1)  % n             
                new[i,j] = newIndex
    return new
def update_image( image: Image, data: np.array ):
    pallete = image.getpalette()
    height, width = data.shape
    for y in range(height):
        for x in range(width):
            pb = data[y,x]*3
            image.putpixel((x,y), (pallete[pb],pallete[pb+1],pallete[pb+2]))
def main():
    st.markdown("## :blue[Demons in Cyclic Space]")
    # Draw a dividing line
    st.divider()
    st.markdown("A type of cellular automata called cyclic space was discovered by David Griffeath of the University of Wisconsin at Madison in 1990. Cyclic Space is described in  [The Magic Machine A Handbook of Computer Sorcery](https://www.amazon.com/Magic-Machine-Handbook-Computer-Sorcery/dp/0716721252/ref=sr_1_1?crid=2N7PKFJOVUI49&dib=eyJ2IjoiMSJ9.NTLdsrNDLEk1x3LeOBQyww.nWfU52fpvLMdRJsWOJv1BBOrNoiGSeZ0rMMVjCoi1Ns&dib_tag=se&keywords=the+magic+machine+a.k.+dewdney&qid=1729741595&sprefix=the+magic+machine+a.k.+dewdnet%2Caps%2C169&sr=8-1) by A.K. Dewdeny.")
    st.markdown("This page is a cyclic space simulator I wrote to explore these automata and a mimi project to brush up on my Python coding and to try out [streamlit](https://streamlit.io/)")
    st.markdown("Cyclic Space is a grid of cells where each cell has one of n possible values, numbered 0 through n-1. Cyclic spaces are most interesting when n is fairly small. In each generation any cell with a value k will eat any neighboring cell that has value k-1. Cells is the 0 state will eat cells in the n-1 state thus allowing loops of state changes.  Choose any image to load. You can then choose the number of colors to color-reduce the image into an image with n colors. The cyclic algorithm will then run successive generations of the cyclic space. You can also scale the image. Smaller images animate faster. Watch for the Demons of cyclic space to appear. These crystal seeds will continue to grow. ")
    st.divider()

    gen_random = st.checkbox("Generate random image")

    if gen_random:
        # Set the size of the image
        x = 256
        y = 256

        # Generate an array of random monochrome pixels
        mono_pixels = np.random.rand(y, x) * 255

        # Create an array of random monochrome (r,g,b) pixels where each pixel has r = g = b
        pixels = np.stack((mono_pixels, mono_pixels, mono_pixels), axis=2)

        # Convert the array to uint8 type
        pixels = pixels.astype(np.uint8)

        # Create an image from the array
        image = Image.fromarray(pixels, 'RGB')
        # st.image(img, caption="Random Image", use_column_width=False)
    else: 
        # Step 1: # Step 1: upload image file as jpg/jpeg, include label
        # uploaded_file = st.file_uploader(" #### :camera: :violet[1. Upload Image] ", type=["JPG", "JPEG", "PNG"])
        url = st.text_input(
          "Enter image url: ", 'https://img.freepik.com/free-photo/colorful-majestic-waterfall-national-park-forest-autumn_554837-6.jpg?w=360')
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
    
    
    # Step 1: # Step 1: upload image file as jpg/jpeg, include label
    # uploaded_file = st.file_uploader(" #### :camera: :violet[1. Upload Image] ", type=["JPG", "JPEG", "PNG"])
    #url = st.text_input(
    #  "Enter image url: ", 'https://img.freepik.com/free-photo/colorful-majestic-waterfall-national-park-forest-autumn_554837-6.jpg?w=360')
    # print(" reloading image url")
    
     # st.image(image)

    target_image_width = 200
    if image != None:
        # print(" reloading image url")
        # response = requests.get(url)
        # image = Image.open(BytesIO(response.content))
        # Display uploaded image with label
        st.image(image, caption="Uploaded Image", use_column_width=False)
        # image = Image.open(uploaded_file)
        # image = Image.open(BytesIO(my_res.content))
        image_array = np.array(image)
        # st.write("The image has been loaded into np_array")
        # st.write(image_array.ndim)
        st.write(image_array.shape)
        edge = math.sqrt(image_array.shape[0]* image_array.shape[1])
        default_scale_factor = target_image_width/edge
        # st.write( " edge, scale", edge, default_scale_factor)
        num_colors = st.slider("Number of Colors:", 2, 32, 12)
        size_factor = st.slider("Resize Factor", 0.01, 4.0, default_scale_factor)
        newsize = (int(image_array.shape[1]* size_factor), int(image_array.shape[0]* size_factor) )
        st.write("Newsize:", newsize)
        resized_image = image.resize(newsize)
        quantized_image = resized_image.quantize(num_colors)
        st.image(quantized_image, caption="Image Scaled and Quantized", use_column_width=False)
        # st.write("Type of Quantized image",type(quantized_image))
        # st.write("Mode of the Quantized image",quantized_image.mode)
        # st.write("Shape of get date",type(quantized_image.getdata))
        quantized_array = np.array(quantized_image)
        # st.write("Quantized array shape",quantized_array.shape)
        # st.write("Quantized image Pallete",quantized_image.getpalette())
        # test_image = quantized_image.copy()
        # st.write("Test image Pallete",test_image.getpalette())
        # update_image(test_image, quantized_array)
        # st.image(test_image, caption="Test Image", use_column_width=True)

        
        
        # st.write("New Quantized array shape",new_quantized_array.shape)
        # st.write("New quantized array dtype", new_quantized_array.dtype )
        # st.write(" Maximum pixel value", np.max(quantized_array))
        # new_quantized_array = (int(quantized_array + (num_colors/2))) % 16
        # placeholder = st.image(quantized_image, caption="Animated Image", use_column_width=False)
        placeholder = st.empty()
        placeholder.image(quantized_image, use_column_width=True)
        nPixels = quantized_array.shape[0] * quantized_array.shape[1]
        prev_ntouched = 0
        streak = 0
        while True:
            (new_quantized_array, ntouched) = update_cycle_eaten(quantized_array, num_colors)
            if ntouched == prev_ntouched:
                streak = streak+1
            else:
                prev_ntouched = ntouched
                streak = 0
            # next_image = Image.fromarray(new_quantized_array,'P')

            # st.write(" quantized array type", type(quantized_array))
            # st.write(" quantized array mode", quantized_array.mode, quantized_array.height, quantized_array.width)
            # Draw a dividing line
            # st.divider()
            # next_image.putpalette(quantized_image.getpalette())
            placeholder.image(quantized_image, use_column_width=True)
            # st.write(ntouched, " of ", nPixels, " changed")
            # st.image(next_image, caption="Next Image", use_column_width=True)
            update_image(quantized_image,new_quantized_array )
            # placeholder.image(quantized_image)
            quantized_array = new_quantized_array.copy()
            # st.write("Size of Quantized image",next_image.size)
            # st.write("Mode of Quantized image",next_image.mode)
            # print (ntouched)
            if ntouched == nPixels:
                st.write(" Simulation ended.  All ", nPixels, "pixels changed" )
                break
            if ntouched == 0:
                st.write(" Simulation ended. 0 pixels changed last generation")
                break
            if  streak >= 60:
                st.write(" Simulation ended. May be looping. ", streak, " generations in a row changed the same number of pixels")
                break
      
        # st.image(quantized_image, caption="Updated Quantized Image", use_column_width=True)
        
        
            # st.write("indexing ",new_quantized_array[1,1])
        # run main function
if __name__ == "__main__":
    main()