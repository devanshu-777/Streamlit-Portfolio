import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from PIL import UnidentifiedImageError
from pathlib import Path

st.set_page_config(
    page_title="Devanshu Shah",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CSS = """
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

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

.contact-form {
    max-width: 600px;
    margin: 0 auto;
}
.blog-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 0;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    overflow: hidden;
}
.blog-card img {
    width: 100%;
    border-radius: 12px 12px 0 0;
}
.blog-card .content {
    padding: 15px;
}
"""

st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_image(path_or_url, fallback_size=(300, 300), fallback_color=(52, 152, 219)):
    try:
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            response = requests.get(path_or_url)
            if response.status_code == 200:
                try:
                    return Image.open(BytesIO(response.content))
                except UnidentifiedImageError:
                    pass
        else:
            return Image.open(path_or_url)
    except (FileNotFoundError, UnidentifiedImageError):
        pass
    img = Image.new("RGB", fallback_size, fallback_color)
    return img

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

project_image_1 = load_image("AI-Project.png")
project_image_2 = load_image("Microservices-Project.png")

AI_RESUME_URL = "https://www.dropbox.com/scl/fi/f3tkpi0dt91gzdx3hfktd/Devanshu-Shah_Resume.pdf?rlkey=kygig2c60pfu803rcdd2w7duj&dl=0"

def load_blog_posts():
    posts = []
    blog_dir = Path("blog")
    if not blog_dir.exists():
        return posts
    for post_dir in sorted(blog_dir.iterdir()):
        if not post_dir.is_dir():
            continue
        md_file = post_dir / "post.md"
        if not md_file.exists():
            continue
        with open(md_file) as f:
            content = f.read()
        images = []
        for f in sorted(post_dir.iterdir()):
            if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp") and f.name != "post.md":
                images.append(load_image(str(f)))
        title_line = content.strip().split("\n")[0].replace("## ", "").replace("# ", "")
        posts.append({"content": content, "images": images, "title": title_line, "slug": post_dir.name})
    return list(reversed(posts))

with st.sidebar:
    st.title("📝 Blog")
    blog_posts = load_blog_posts()
    if not blog_posts:
        st.write("No posts yet. Check back soon!")
    for post in blog_posts:
        for img in post["images"]:
            st.image(img, width='stretch')
        st.markdown(post["content"])
        st.divider()

with st.container():
    col1, col2 = st.columns([1, 2.5])
    with col1:
        st.image(profile_pic, width=200)
    with col2:
        st.title("Devanshu Shah")
        st.write("📧 devanshu720@gmail.com")
        st.write("AI Enthusiast & Software Engineer")
        bcol1, bcol2 = st.columns(2)
        with bcol1:
            st.link_button(
                "🔗 My LinkedIn Profile",
                "https://linkedin.com/in/devanshu-shah777/",
                width='stretch',
            )
        with bcol2:
            st.link_button(
                "📄 Data Science Resume",
                AI_RESUME_URL,
                width='stretch',
            )

with st.container():
    st.write("---")
    st.subheader("Hi, I am Devanshu 👋")
    st.write(
        "I am passionate about leveraging technology to build innovative solutions. "
        "My expertise lies in both creating intelligent systems with AI and developing "
        "robust, user-friendly software applications."
    )
    st.info("🚧 This portfolio is evolving, check back soon for more!")

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
        submitted = st.form_submit_button("Send Message", width='stretch')

        if submitted:
            if name and email and message:
                try:
                    r = requests.post(
                        "https://formspree.io/f/mkodnard",
                        headers={"Accept": "application/json"},
                        data={"name": name, "email": email, "message": message},
                    )
                    if r.ok:
                        st.success("Thanks! I'll get back to you soon. ✅")
                    else:
                        st.error("Something went wrong. Please try again or email me directly.")
                except requests.exceptions.RequestException:
                    st.error("Network error. Please try again later.")
            else:
                st.warning("Please fill in all fields.")
