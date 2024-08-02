#  st.header("Header")
#     st.subheader("Sub Header")
#     st.write("Write")               # "write" and "markdown" both are same but "write" can detect the datatype 
#     st.markdown("markdown")         # which "markdown" cannot
#     st.markdown("_Italic_")
#     st.markdown("""
#         |  A    |  B    |
#         |-------|-------|
#         |   1   |   3   |  
#         |   2   |   4   |
#     """)
#     st.write(pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,0]}))
#     st.code("code")
#     st.sidebar.title("Sidebar Title")
#     st.write(pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,0]}))
# b=st.checkbox("Checkbox")
# if b:
# st.write("Checkbox Clicked")

import streamlit as st
import pandas as pd
from PIL import Image
import base64 as bs
import matplotlib.pyplot as plt 

def stream():
    st.title("Title")
      

def visualize():
    upload=st.file_uploader("Choose s file to upload",type=["jpg"])
    a=st.button("Show image")
    if a:
        if upload is not None:
            image=Image.open(upload)
            st.image(image,caption="Image",use_column_width=True)
        else:
            st.write("Image not found")
    data={
        'A':[5,7,8,5,6,7,8,7,6,5],
        'B':[10,20,15,20,10,15,20,10,15,10]
    }
    df=pd.DataFrame(data)
    st.write("Sample DataFrame:")
    st.dataframe(df)

    plt.figure(figsize=(10,5))
    plt.hist(df['A'],bins=5,alpha=0.75)
    plt.title("Histogram")
    st.pyplot(plt)


def get_base64(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
        print(data)
        # print(bs.b64encode(data).decode())
    return bs.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    height:70rem;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('img.jpg')

stream()

st.sidebar.title("Sidebar")

x=st.sidebar.selectbox("Select",{1:"One",2:"Two",3:"Three"})
if x==1:
    st.sidebar.title("1")
elif x==2:
    visualize()
elif x==3:
    st.sidebar.title("3")
else:
    st.sidebar.title("else")



