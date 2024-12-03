from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page configuration
st.set_page_config(page_title="debug and debug again!", page_icon="💻", layout="wide")

# Load local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Make sure the path is correct.")

local_css("style/style.css")

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Load images
try:
    img_contact_form = Image.open("462571779_2093157664436894_1634821827310607071_n.jpg")
    img_github = Image.open("462571779_2093157664436894_1634821827310607071_n.jpg")
except FileNotFoundError:
    st.error("Image file not found. Make sure the paths are correct.")

# Header section
with st.container():
    st.subheader("Hi, I am Kaycee Custodio")
    st.title("Discover what computer engineering do!")
    st.write(
        """
       Welcome to my blog! Join me on an exciting 
       journey through the world of Computer Engineering as I share my experiences,
       insights, and the challenges that come with being a Computer Engineering student.
        """
    )
    st.write("[Message me on Gmail >](mailto:custodioace80@gmail.com.com)")

# First-year perspective section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Computer Engineering: fix and debug!")
        st.write(
            """
           Starting university was a blend of excitement and nervous anticipation. 
           Learning to program felt like unlocking a secret code.
           From mastering binary to exploring algorithms, it’s been an incredible adventure!
            """
        )
        st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Lottie animation could not load.")

# Insights and reflections
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, caption="Debugging: try and try and try!")
    with text_column:
        st.write(
            """
            Programming assignments are both exciting and demanding.
            Debugging often feels like a mental workout, but nothing beats the thrill of solving a tough problem.
            Balancing academics, personal time, and social life can be tricky, but staying organized makes all the difference.
            """
        )


with st.container():
    st.write("---")
    st.subheader("PROS AND CONS")
    st.write("### PROS:")
    st.write("""
   1. Access to lucrative career opportunities with a growing demand for programmers.  
2. Enhanced logical thinking and problem-solving abilities.  
3. Opportunities to unleash creativity by designing unique solutions.  
4. Flexible work environments, including the option to work remotely.  
5. A dynamic field that encourages continuous learning and growth.  
6. Connection with a global network of developers and innovators.
    """)
    st.write("### CONS:")
    st.write("""
    1. A steep learning curve can make it challenging for beginners.  
2. Sedentary work may pose risks to physical health if not managed properly.  
3. Debugging can be a time-consuming and often frustrating process.  
4. Rapid technological advancements demand constant upskilling.  
5. Some work environments can feel isolating at times.  
6. Managing and maintaining code complexity in large projects can be daunting.  
    """)

# Contact form section
with st.container():
    st.write("---")
    st.header("For Comments:")
    st.write("##")
    
    contact_form = """
    <form action="https://formspree.io/f/{your-form-id}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
