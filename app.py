import streamlit as st
import random
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from quickdraw import QuickDrawData
from io import BytesIO



st.set_page_config(
    page_title="Noura | AI Resume",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
<style>
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}
.color-box {animation: fadeIn 0.9s ease-in-out;}
.color-box:hover {animation: pulse 1s ease-in-out infinite;}

.skills-card {
    background-color: #1E293B;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid #334155;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}
.skill-title {
    color: #38BDF8;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 5px;
}
.skill-desc {
    color: #94A3B8;
    font-size: 14px;
    margin-bottom: 12px;
}
.progress-bar-bg {
    background-color: #334155;
    border-radius: 5px;
    height: 10px;
    width: 100%;
}
.progress-bar-fill {
    background: linear-gradient(90deg, #38BDF8, #818CF8);
    border-radius: 5px;
    height: 10px;
}

/* Certificates */
.cert-card {
    background-color: #020617;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    border: 1px solid #1f2937;
    box-shadow: 1px 1px 6px rgba(0,0,0,0.3);
}
.cert-title {
    color: #e5e7eb;
    font-weight: 600;
    font-size: 16px;
    margin-bottom: 4px;
}
.cert-org {
    color: #38BDF8;
    font-size: 14px;
    margin-bottom: 4px;
}
.cert-desc {
    color: #9ca3af;
    font-size: 13px;
}

/* Section titles */
.section-subtitle {
    color: #9CA3AF;
    font-size: 14px;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
</style>
""",
    unsafe_allow_html=True,
)





st.sidebar.title("🧭 Navigate")
page = st.sidebar.radio(
    "Section:",
    [
        "Home",
        "About Me",
        "Skills",
        "Projects",
        "Tools & Environment",
        "Live AI Demo",
        "Doodle AI",
    ],
)




if page == "Home":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "Noura.PNG",
            caption="Noura Robot",
            use_container_width=True,
        )

    with col2:
        st.markdown('<p class="section-subtitle">WELCOME</p>', unsafe_allow_html=True)
        st.title("Noura Mubarak")
        st.subheader("AI Student | Machine Learning & Intelligent Systems")

        st.write(
            """
Welcome to my interactive AI-powered resume.  
I'm an AI student passionate about machine learning, deep learning, and building intelligent systems that learn from data.  
I enjoy creating hands-on AI projects, experimenting with models, and turning ideas into real applications.  
This website showcases my skills, projects, and the work I've done throughout my AI learning journey.
"""
        )

    st.divider()
    st.markdown("### 📬 Contact")
    st.write(
        """
- 📧 **nora44work@gmail.com**  
- 📞 [+966552326899](tel:0552326899)
- 🔗 [LinkedIn](https://www.linkedin.com/in/nora-alrashoud-a847043aa?utm_source=share_via&utm_content=profile&utm_medium=member_ios)  
- 💻 [GitHub](https://github.com/812i)  
"""
    )

    st.divider()
    st.markdown("### 🙏 Thanks")
    st.write(
        """
Thank you for visiting my interactive AI resume.  
This website reflects my learning journey, my passion for AI, and the projects I've built along the way.  
I'm always open to feedback, collaboration, and new opportunities to grow.
"""
    )





elif page == "About Me":
    st.markdown('<p class="section-subtitle">PROFILE</p>', unsafe_allow_html=True)
    st.title("About Me")

    st.write(
        """
I'm an AI student based in Riyadh with a growing passion for understanding how intelligent systems work and how they can be built to solve real-world problems.  
I enjoy working on practical machine learning and deep learning projects, exploring reinforcement learning, and building interactive AI applications using tools like Streamlit.  

I'm constantly learning, experimenting, and improving my skills through hands-on projects and self-driven exploration.  
My goal is to become an AI engineer capable of designing, training, and deploying intelligent systems that make a meaningful impact.
"""
    )

    st.divider()
    st.markdown("### 🎯 Current Focus")
    st.write(
        """
- Strengthening my foundations in machine learning and deep learning  
- Building interactive AI demos and web apps  
- Exploring reinforcement learning and intelligent agents  
- Preparing for future opportunities in AI engineering and research  
"""
    )





elif page == "Skills":
    st.markdown('<p class="section-subtitle">CAPABILITIES</p>', unsafe_allow_html=True)
    st.title("⚙️ Technical Skills")
    st.write("Here is a breakdown of my technical skills, tools, and certifications:")

    col1, col2 = st.columns(2)

    
    with col1:
        st.markdown(
            """
        <div class="skills-card">
            <div class="skill-title">🧠 Programming & Data</div>
            <div class="skill-desc">
                Python (Advanced), SQL, C++ (Basics),  
                Data Cleaning & Preprocessing, NumPy, Pandas, Matplotlib, Seaborn
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: 95%;"></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="skills-card">
            <div class="skill-title">📊 Machine Learning</div>
            <div class="skill-desc">
                Supervised & Unsupervised Learning, Scikit-Learn,  
                Model Evaluation & Optimization, Feature Engineering
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: 75%;"></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="skills-card">
            <div class="skill-title">🌐 Web Development</div>
            <div class="skill-desc">
                Streamlit, Basic HTML/CSS,  
                Building interactive AI dashboards and demos
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: 70%;"></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    

    with col2:
        st.markdown(
            """
        <div class="skills-card">
             <div class="skill-title">🤖 Deep Learning</div>
             <div class="skill-desc">
                TensorFlow / Keras, PyTorch (Basics),  
                CNNs, RNNs, Transfer Learning, Image Classification
             </div>
             <div class="progress-bar-bg">
                 <div class="progress-bar-fill" style="width: 70%;"></div>
             </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="skills-card">
            <div class="skill-title">🎮 Reinforcement Learning</div>
            <div class="skill-desc">
                Gymnasium, Stable-Baselines3,  
                Q-Learning, Policy Gradient Methods
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: 55%;"></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="skills-card">
            <div class="skill-title">🛠 Tools & AI Libraries</div>
            <div class="skill-desc">
                VS Code, Jupyter Notebook, Anaconda, Git & GitHub, PyCharm, Unity (2D Basics),  
                Google Colab, Kaggle Notebooks, QuickDraw Dataset, OpenCV (Basics), HuggingFace (Basics)
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: 85%;"></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.markdown("### 🎓 Certificates")

    cert_col1, cert_col2 = st.columns(2)

    with cert_col1:
        st.markdown(
            """
        <div class="cert-card">
            <div class="cert-title">AI Skills 4 Women - Tech Saudi Advocates</div>
            <div class="cert-org">Microsoft · Founderz Business School · Tech Saudi Advocates</div>
            <div class="cert-desc">
                Completed all academic and practical requirements of the AI Skills 4 Women program (Cohort 2026),
                covering AI fundamentals, machine learning, deep learning, and hands-on projects.
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with cert_col2:
        st.markdown(
            """
        <div class="cert-card">
            <div class="cert-title">Certificate of Appreciation – Advanced Computer Applications</div>
            <div class="cert-org">Academy of Learning</div>
            <div class="cert-desc">
                Recognized for completing a project in the Advanced Computer Applications course by preparing a
                training package to teach Microsoft Office skills. Dated 09‑10‑2025.
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )






elif page == "Projects":
    st.markdown('<p class="section-subtitle">SHOWCASE</p>', unsafe_allow_html=True)
    st.title("📁 My Projects")

    
    st.subheader("🎨 AI Color Palette Extractor")
    st.write(
        "This project uses a K-Means clustering algorithm to analyze images and extract the dominant color palette."
    )

    with st.expander("Try it live!", expanded=False):
        uploaded_file = st.file_uploader(
            "Upload an image to extract its color palette",
            type=["jpg", "jpeg", "png"],
            key="color_palette_uploader",
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            img_resized = image.resize((200, 200))
            img_array = np.array(img_resized)
            pixels = img_array.reshape(-1, 3)

            kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
            kmeans.fit(pixels)
            colors = kmeans.cluster_centers_.astype(int)

            col_img, col_colors = st.columns([1, 1])
            with col_img:
                st.image(image, caption="Uploaded Image", use_container_width=True)
            with col_colors:
                st.subheader("🎯 Dominant Colors")

                for color in colors:
                    r, g, b = color
                    hex_code = f"#{r:02x}{g:02x}{b:02x}"

                    st.markdown(
                        f"""
                    <div style="display:flex; align-items:center; margin-bottom:8px;">
                        <div class="color-box" style="
                            width:50px; height:50px; 
                            background-color:{hex_code}; 
                            border-radius:8px; 
                            margin-right:10px;
                            border: 1px solid #ccc;
                        "></div>
                        <code style="font-size:16px;">{hex_code}</code>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

            st.success("Color palette extracted successfully!")
            st.divider()

    

    st.subheader("🕹️ Pixel Art Converter")
    st.write("Convert any image into a beautiful pixel art masterpiece.")

    with st.expander("Try it live!", expanded=False):
        pixel_file = st.file_uploader(
            "Upload an image to pixelate",
            type=["jpg", "jpeg", "png"],
            key="pixel_uploader",
        )
        if pixel_file is not None:
            image = Image.open(pixel_file)
            st.image(image, caption="Original Image", use_container_width=True)

            pixel_size = st.slider(
                "Pixel size:", min_value=4, max_value=32, value=8, step=2
            )

            img_array = np.array(image)
            h, w = img_array.shape[:2]
            new_h = max(1, h // pixel_size)
            new_w = max(1, w // pixel_size)

            small = image.resize((new_w, new_h), resample=Image.NEAREST)
            pixel_art = small.resize((w, h), Image.NEAREST)

            st.image(
                pixel_art,
                caption=f"Pixel Art (pixel size = {pixel_size})",
                use_container_width=True,
            )

            img_bytes = BytesIO()
            pixel_art.save(img_bytes, format="PNG")
            st.download_button(
                label="⬇️ Download Pixel Art",
                data=img_bytes.getvalue(),
                file_name="pixel_art.png",
                mime="image/png",
            )
    




elif page == "Tools & Environment":
    st.markdown('<p class="section-subtitle">STACK</p>', unsafe_allow_html=True)
    st.title("🛠️ Tools & Environment")
    st.write("Here are the tools and environments I use for development and research:")

    tabs = st.tabs(
        [
            "Anaconda",
            "Jupyter Notebook",
            "PyCharm",
            "Online Runners",
            "VS Code",
            "Visual Studio",
            "Cloud & Notebooks",
            "Version Control",
        ]
    )

    with tabs[0]:
        st.markdown(
            """
        <div style="background-color:#42B029; padding: 15px; border-radius: 10px; color: white;">
        <b>🐍 Anaconda</b><br>
        Proficient in using Anaconda for managing Python environments, installing scientific libraries,
        and running Jupyter Notebook for AI and ML projects.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[1]:
        st.markdown(
            """
        <div style="background-color:#F37726; padding: 15px; border-radius: 10px; color: white;">
        <b>📓 Jupyter Notebook</b><br>
        Experienced in using Jupyter Notebook for exploratory data analysis, machine learning experiments,
        and documenting code with visual outputs.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[2]:
        st.markdown(
            """
        <div style="background-color:#21D789; padding: 15px; border-radius: 10px; color: white;">
        <b>💡 PyCharm</b><br>
        Familiar with PyCharm as a professional IDE for building structured Python applications
        and debugging complex code.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[3]:
        st.markdown(
            """
        <div style="background-color:#3776AB; padding: 15px; border-radius: 10px; color: white;">
        <b>🌐 Online Python Runners</b><br>
        Comfortable testing and running Python scripts on online platforms for quick prototyping
        and experimentation.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[4]:
        st.markdown(
            """
        <div style="background-color:#007ACC; padding: 15px; border-radius: 10px; color: white;">
        <b>🧩 Visual Studio Code</b><br>
        Skilled in using Visual Studio Code for writing and organizing Python projects, managing extensions,
        debugging code, and building interactive applications such as Streamlit dashboards.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[5]:
        st.markdown(
            """
        <div style="background-color:#3DDC84; padding: 15px; border-radius: 10px; color: white;">
        <b>🎮 Visual Studio</b><br>
        Used Visual Studio for experimenting with small game-related projects and exploring C# development
        workflows in a lightweight, experimental environment.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[6]:
        st.markdown(
            """
        <div style="background-color:#0F766E; padding: 15px; border-radius: 10px; color: white;">
        <b>☁️ Cloud & Notebooks</b><br>
        Google Colab and Kaggle Notebooks for cloud-based machine learning experiments, GPU usage,
        and quick prototyping.
        </div>
        """,
            unsafe_allow_html=True,
        )

    with tabs[7]:
        st.markdown(
            """
        <div style="background-color:#111827; padding: 15px; border-radius: 10px; color: white;">
        <b>🔗 Version Control</b><br>
        Git and GitHub for tracking changes, collaborating, and managing AI and software projects.
        </div>
        """,
            unsafe_allow_html=True,
        )






elif page == "Live AI Demo":
    st.markdown('<p class="section-subtitle">INTERACTIVE</p>', unsafe_allow_html=True)
    st.title("🧠 Live AI Demo: Guess the Number")
    st.write("I've built a simple number guessing game. Try to guess the secret number!")

    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 20)
        st.session_state.attempts_left = 5
        st.session_state.game_over = False
        st.session_state.message = (
            "I'm thinking of a number between 1 and 20. Can you guess it? You have 5 attempts."
        )
        st.session_state.submitted = False

    st.info(st.session_state.message)

    if not st.session_state.game_over:
        with st.form("guess_form"):
            guess = st.number_input(
                "Enter a number between 1 and 20:",
                min_value=1,
                max_value=20,
                step=1,
            )
            submit = st.form_submit_button("Submit Guess!")

        if submit:
            st.session_state.submitted = True
            st.session_state.attempts_left -= 1

            if st.session_state.submitted and guess == st.session_state.secret:
                st.session_state.message = (
                    f"🎉 Correct! The number was {st.session_state.secret}. You win!"
                )
                st.session_state.game_over = True
                st.balloons()   

            elif st.session_state.attempts_left == 0:
                 st.session_state.message = (
                    f"😢 Game Over! The number was {st.session_state.secret}."
                )
                 st.session_state.game_over = True
                 st.rerun()
            else:
                hint = "higher" if guess < st.session_state.secret else "lower"
                st.session_state.message = (
                    f"Wrong! Try a {hint} number. Attempts left: {st.session_state.attempts_left}"
                )
                st.rerun()

        
    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.secret = random.randint(1, 20)
            st.session_state.attempts_left = 5
            st.session_state.game_over = False
            st.session_state.message = (
                "I'm thinking of a number between 1 and 20. Can you guess it? You have 5 attempts."
            )
            st.rerun()
    





elif page == "Doodle AI":
    st.markdown('<p class="section-subtitle">FUN</p>', unsafe_allow_html=True)
    st.title("🖌️ Doodle AI - AI Draws, You Guess!")
    st.write(
        "The AI has picked a real doodle from the Quick, Draw! dataset. Can you guess what it is?"
    )

    qd = QuickDrawData()

    categories = [
        "cat",
        "dog",
        "car",
        "tree",
        "house",
        "flower",
        "sun",
        "cloud",
        "moon",
        "star",
        "smiley face",
        "heart",
    ]

    if "secret_category" not in st.session_state:
        st.session_state.secret_category = random.choice(categories)

    if st.button("🎲 New Doodle"):
        st.session_state.secret_category = random.choice(categories)

    try:
        drawing = qd.get_drawing(st.session_state.secret_category)
        img = drawing.get_image()
        st.image(img, caption="What did the AI draw?", width=300)
    except Exception:
        st.error(
            f"Could not load doodle for '{st.session_state.secret_category}'. Try another one!"
        )

    user_guess = st.selectbox(
        "Your Guess:", categories, index=None, placeholder="Choose..."
    )

    if st.button("Submit Guess"):
        if user_guess == st.session_state.secret_category:
            st.balloons()
            st.success(
                f"🎉 Correct! The AI drew a **{st.session_state.secret_category}**!"
            )
        else:
            st.error(f"❌ Wrong! The AI drew a **{st.session_state.secret_category}**.")
        st.session_state.secret_category = random.choice(categories)

st.markdown(
    """
    <style>
    .footer {
        position: relative;
        margin-top: 50px;
        width: 100%;
        text-align: center;
        background-color: transparent;
        color: #94A3B8;
        font-size: 14px;
        padding: 10px;
    }
    </style>
    <div class="footer">
        Made with ❤️ by Noura Mubarak
    </div>
    """,
    unsafe_allow_html=True
)