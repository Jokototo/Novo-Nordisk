# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to 
import pandas as pd
from PIL import Image, ImageFilter
import requests
from io import BytesIO
# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):
    response = requests.get("https://i.imgur.com/Cx5o0ca.jpg")
    im = Image.open(BytesIO(response.content)).convert('LA')

    newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels
    img = im.resize((28, 28), Image.ANTIALIAS).filter(ImageFilter.SHARPEN) #Reshape image to 28x28
    newImage.paste(img, (0, 0))  # paste resized image on white canvas
    tv = list(newImage.getdata())  # get pixel values

    # Inverse pixel values
    tva = [(255 - x) for x in tv]

    dataframe1=pd.DataFrame(tva).transpose()
    dataframe1.columns=['f'+ str(i) for i in range(dataframe1.shape[1])]
    return dataframe1
