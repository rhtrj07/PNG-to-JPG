from PIL import Image
#Pillow for converting PNG to JPG
import os

#To gather all the files in the directory 
entries = os.listdir()
new_entry=[]

# To gather files that has .png as extention
for i in entries:
    if '.png' in i:
        new_entry.append(i)
        
# For going through each of the png files
for i in new_entry:
    
    im = Image.open(i)
    #converting the png to jpg format
    rgb_im = im.convert('RGB')
    #Removing the .png from the tail end of the file name
    i= i.strip('.png')
    #Adding the extension jpg to the file
    i= i+'_jpg.jpg'
    #Saving the file to same folder with .jpg extension
    rgb_im.save(i)
