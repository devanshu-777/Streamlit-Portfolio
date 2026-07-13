# --- IMPORTS ---
import streamlit as st  # Streamlit for web app
from PIL import Image  # For image processing
import requests  # For HTTP requests (fetching images)


# --- PAGE CONFIGURATION ---
# Set up the Streamlit page (title, icon, layout)
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🤖",
    layout="wide",
)


# --- HELPER FUNCTIONS & STYLE ---


# Inject custom CSS from a file (not used in this example)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- CUSTOM CSS ---
# For this example, we'll embed the CSS directly to keep it in one file.
# In a real project, you might use local_css("style/style.css")
CSS = """
/* Hide Streamlit's default menu and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
/* header {visibility: hidden;}  Removed to restore sidebar toggle button */

/* General body styling */
body {
    background-color: #f0f2f6;
}

/* Custom button styling */
.stButton>button {
    border: 2px solid #4A90E2;
    border-radius: 20px;
    color: #4A90E2;
    padding: 10px 24px;
    background-color: transparent;
    transition: all 0.3s ease-in-out;
}
.stButton>button:hover {
    background-color: #4A90E2;
    color: white;
    border-color: #4A90E2;
}
.stButton>button:focus {
    outline: none !important;
    box-shadow: none !important;
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# --- ASSETS ---


# Function to load images with fallback to a placeholder
from io import BytesIO
from PIL import UnidentifiedImageError


# Helper to load image from URL or local file, with fallback to a generated placeholder
def load_image(path_or_url, fallback_size=(300, 300), fallback_color=(52, 152, 219)):
    """
    Loads an image from a local file or a URL.
    If loading fails, returns a simple colored placeholder image.
    """
    try:
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            response = requests.get(path_or_url)
            if response.status_code == 200:
                try:
                    return Image.open(BytesIO(response.content))
                except UnidentifiedImageError:
                    pass
            # If failed, fall through to fallback
        else:
            return Image.open(path_or_url)
    except (FileNotFoundError, UnidentifiedImageError):
        pass
    # Fallback: generate a simple placeholder image
    img = Image.new("RGB", fallback_size, fallback_color)
    return img


# --- PROFILE PICTURE ---
# Try to load a local profile image (jpeg, jpg, png), else use a placeholder
profile_pic = None
for fname in ["profile.jpeg", "profile.jpg", "profile.png"]:
    try:
        profile_pic = load_image(fname)
        break
    except FileNotFoundError:
        continue
if profile_pic is None:
    profile_pic = load_image(
        "https://placehold.co/300x300/3498DB/FFFFFF?text=Your%20Photo&font=inter"
    )


# --- PROJECT IMAGES (use placeholders) ---
project_image_1 = load_image("AI-Project.png")
project_image_2 = load_image("Microservices-Project.png")


# --- RESUME LINKS ---
# Add your actual resume links here
AI_RESUME_URL = "https://www.dropbox.com/scl/fi/f3tkpi0dt91gzdx3hfktd/Devanshu-Shah_Resume.pdf?rlkey=kygig2c60pfu803rcdd2w7duj&dl=0"
SE_RESUME_URL = AI_RESUME_URL  # Replace with your SE resume link


# --- SIDEBAR ---
# Sidebar with profile, contact, and resume links
with st.sidebar:
    st.image(profile_pic, width=250)
    st.title("Devanshu Shah")
    st.subheader("AI Enthusiast & Software Engineer")
    st.write("📧 devanshu720@gmail.com")
    st.subheader("Download Resumes")
    st.link_button("Data Science Resume", AI_RESUME_URL, use_container_width=True)
    st.link_button("Software Engineer Resume", SE_RESUME_URL, use_container_width=True)


# --- MAIN CONTENT ---

# --- HERO SECTION ---
# Top section with intro (removed animation for simplicity)
with st.container():
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.subheader("Hi, I am Devanshu 👋")
        st.write(
            "I am passionate about leveraging technology to build innovative solutions. "
            "My expertise lies in both creating intelligent systems with AI and developing "
            "robust, user-friendly software applications."
        )
        st.info("🚧 This portfolio is evolving, check back soon for more!")
        st.link_button(
            "My LinkedIn Profile",
            "https://linkedin.com/in/devanshu-shah777/",
            use_container_width=False,
        )
    with right_column:
        st.empty()  # No animation, keep layout clean

# --- WHAT I DO ---
# Section describing your main skills/roles
with st.container():
    st.write("---")
    st.header("What I Do")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🤖 Artificial Intelligence & Machine Learning")
        st.write(
            """
            - Developing predictive models and machine learning algorithms.
            - Working with Natural Language Processing (NLP) and Large Language Models (LLMs).
            - Analyzing complex datasets to extract valuable insights.
            - Building AI-powered features to enhance application intelligence.
            """
        )
    with col2:
        st.subheader("💻 Software Engineering")
        st.write(
            """
            - Designing and building scalable backend systems and APIs.
            - Creating responsive and intuitive front-end user interfaces.
            - Applying full-stack development principles to deliver end-to-end solutions.
            - Ensuring code quality through testing, CI/CD, and best practices.
            """
        )

# --- SKILLS ---
# List of your technical skills
with st.container():
    st.write("---")
    st.header("My Skills")
    st.write(
        """
        - **Languages:** Python, Java, C++, JavaScript, SQL
        - **AI/ML:** TensorFlow, PyTorch, Scikit-learn, Pandas, LangChain, Hugging Face
        - **Web Development:** React, Node.js, HTML/CSS, Streamlit, Flask
        - **Databases:** MySQL, PostgreSQL, MongoDB, Firebase
        - **Tools & Platforms:** Git, Docker, Kubernetes, AWS, Google Cloud
        """
    )

# --- PROJECTS ---
# Highlight your projects with images and descriptions
with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(project_image_1)
    with text_column:
        st.subheader("AI-Powered Recommendation Engine")
        st.write(
            """
            Designed and implemented a content recommendation system using collaborative filtering and deep learning techniques.
            - **Tech Stack:** Python, TensorFlow, Pandas, Flask, Docker
            - **Key Features:** Real-time recommendations, scalable architecture, A/B testing framework.
            - **Outcome:** Increased user engagement by 15% within the first quarter of deployment.
            """
        )
        st.link_button("View on GitHub", "https://github.com/your-username/project-1")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(project_image_2)
    with text_column:
        st.subheader("Microservices E-Commerce Platform")
        st.write(
            """
            **Distributed Systems**
            *July - Aug 2025*

            - Built a microservices architecture in Go with Account, Catalog, and Order services, using PostgreSQL and Elasticsearch for storage.
            - Implemented gRPC + Protobuf for low-latency inter-service communication and a GraphQL API Gateway for unified client queries.
            - Containerized the stack with Docker Compose, enabling reproducible local development and orchestration of services.
            - Ensured reliability by adopting a stable Go toolchain and pinning dependencies across services with multiple moving parts.

            **Tech Stack:** Go, gRPC, Protobuf, GraphQL, Docker, PostgreSQL, Elasticsearch
            """
        )
        st.link_button(
            "View on GitHub", "https://github.com/your-username/microservices-ecommerce"
        )


# --- CONTACT FORM ---
# Contact form using formsubmit.co (replace with your email)
with st.container():
    st.write("---")
    st.header("Get In Touch!")
    st.write(
        "I'd love to hear from you! Whether you have a question, want to collaborate, "
        "or just want to say hi, feel free to drop a message below."
    )

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            st.success("Thank you for reaching out! I'll get back to you soon.")
