import streamlit as st
import os
from pathlib import Path
import PIL
import base64

def streamlit_visual():
    st.set_page_config(layout="wide", page_title="Felipe Paes", page_icon=":robot_face:")

    # Carregar arquivos após configurar a página
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    resume_file = current_dir / "assets" / "cv.pdf"
    css_file = current_dir / "styles.css"
    st.markdown(
        '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">',
        unsafe_allow_html=True)
    st.markdown(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">',
        unsafe_allow_html=True
    )

    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with open(resume_file, "rb") as pdf_file:
        pdf_cv = pdf_file.read()

    with open('./assets/background.jpg', 'rb') as img_file:
        img_bytes = img_file.read()
        encoded_img = base64.b64encode(img_bytes).decode()

    # Primeira Seção: Imagem de Perfil, Nome e Ícones das Redes Sociais
    space, col1, space, col2 = st.columns([1, 2.5, 1, 4])
    with col1:
        st.write("###")
        st.write("###")
        st.markdown(
            '<div style="font-size:48px; color: black; font-weight:bold; background-color: white; width:250px; height: 70px">Felipe Paes</div>',
            unsafe_allow_html=True
        )
        st.write("#####")
        st.markdown('<h5 id="name">Mechatronic Engineer and Full-stack Developer</h5>', unsafe_allow_html=True)
        st.write("######")
        st.download_button(
            label=":book: Download complete CV",
            data=pdf_cv,
            file_name='cv.pdf',
            mime='application/pdf',
        )
        st.write("")
        st.write("")
        social_networks = {
            "GitHub": "https://github.com/felipepaes1",
            "LinkedIn": "https://www.linkedin.com/in/felipepaes1",
            "WhatsApp": "https://wa.me/+5543991134462",
            "Email": "https://mail.google.com/mail/?view=cm&fs=1&to=proffelipegpaes@gmail.com&su=Get in Touch&body=Hello! I saw your portfolio and I want to talk with you!"
        }

        social_icons = {
            "GitHub": "fab fa-github",
            "LinkedIn": "fab fa-linkedin",
            "WhatsApp": "fab fa-whatsapp",
            "Email": "fas fa-envelope"
        }

        cols = st.columns(len(social_networks))
        for idx, (plataforma, link) in enumerate(social_networks.items()):
            with cols[idx]:
                icon_class = social_icons.get(plataforma, "fas fa-link")
                st.markdown(f'<a href="{link}" target="_blank"><i class="{icon_class} fa-2x"></i></a>',
                            unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.image("./assets/felipe.png", width=550)

    st.divider()

    st.markdown('<h4>About me</h4>', unsafe_allow_html=True)
    st.info(
        """
        🧠 **Lifelong Learner & Knowledge Sharer**

I'm a passionate individual with a diverse background that combines engineering, education, and innovation. Graduating as a Reserve Officer in Artillery from the Brazilian Army, I honed leadership and technical skills that I carry into all aspects of my career. My journey has taken me through engineering and research, where I delved into innovative projects focused on software, hardware, and web development.

Currently, I am a Programming Languages Professor at both technical and professional levels, where I enjoy guiding students through their coding journey. I also serve as a Project Leader and Full Stack Developer at Log Z, where my focus is on creating automated solutions to simplify and optimize machining tool management. Additionally, I have experience as a Tech Recruiter, evaluating Junior, Mid-Level, and Senior Developers, which has provided me with a deep understanding of the skills and qualities needed for success in the tech industry.

Beyond work, I'm an avid sports and nature enthusiast, always chasing new experiences and staying active.

**Skills & Interests**

👨‍🏫 **Programming Teacher:** Sharing my love for coding and helping students grow.

💣 **Reserve Officer** - Brazilian Army (Artillery): Developed leadership and teamwork skills.

🤖 **Mechatronic Engineer:** Passionate about technology, innovation, and engineering solutions.

💻 **Tech Recruiter:** Evaluated Junior, Mid-Level, and Senior Developers, identifying the best talent for technical roles.

🎵 **Music, Sports, & Nature Lover:** Whether drumming, bodybuilding, or competing in table tennis, I always stay engaged and inspired.

I am excited to bring my skills, curiosity, and enthusiasm for innovation to new opportunities where I can make a positive impact.
        """
    )

    # Lista de tecnologias com ícones e descrições
    tecnologias = [
        {
            "nome": "C & C++",
            "ícone": ["devicon-cplusplus-plain"],
            "descrição": "Taught classes and developed projects with IoT, Arduino, and embedded systems. Experience in low-level programming, real-time systems, and optimization for performance-critical applications."
        },
        {
            "nome": "Python",
            "ícone": "fab fa-python",
            "descrição": "Data science, data manipulation, computer vision, and web development with Django. Experienced in building machine learning models, automating tasks, and data visualization to support decision-making."
        },
        {
            "nome": "JavaScript",
            "ícone": "fab fa-js",
            "descrição": "Interactive web development and front-end applications, specializing in DOM manipulation, event-driven programming, and building responsive, user-friendly interfaces."
        },
        {
            "nome": "Angular",
            "ícone": "fab fa-angular",
            "descrição": "Front-end development for scalable applications, focusing on creating dynamic user interfaces and ensuring a seamless user experience. Proficient in integrating APIs and optimizing for performance."
        },
        {
            "nome": "Laravel",
            "ícone": "fab fa-laravel",
            "descrição": "Back-end creation for scalable applications in PHP, including RESTful API development, authentication systems, and ensuring maintainability with clean, modular code."
        },
        {
            "nome": "SQL",
            "ícone": "fas fa-database",
            "descrição": "Creation and manipulation of relational databases, including schema design, query optimization, and ensuring data integrity for business-critical applications."
        }
    ]

    st.divider()
    st.markdown('<h4>Core Technologies in My Workflow</h4>', unsafe_allow_html=True)


    # Contêiner dos cards
    # Criando 3 colunas
    col1, col2, col3 = st.columns(3)

    # Distribuindo as tecnologias entre as colunas
    for idx, tech in enumerate(tecnologias):
        coluna = [col1, col2, col3][idx % 3]
        with coluna:
            icone_html = "".join(f"<i class='{icone}'></i>" for icone in tech['ícone']) if isinstance(tech['ícone'],
            list) else f"<i class='{tech['ícone']}'></i>"

            # Usando a classe `card` para os estilos de cada card
            st.markdown(f"""
                <div class='card'>
                    {icone_html}
                    <h3>{tech['nome']}</h3>
                    <p>{tech['descrição']}</p>
                </div>
            """, unsafe_allow_html=True)

    # st.markdown("<section>", unsafe_allow_html=True)
    st.divider()
    st.markdown('<h4>Current Projects & Initiatives</h4>', unsafe_allow_html=True)
    st.write("###")
    space, col1, space, col2 = st.columns([1, 2.5, 1, 4])
    with col1:
        st.write("###")
        st.markdown('<h2 id="name">Industrial Tool Management Dashboard</h2>', unsafe_allow_html=True)
        st.markdown(
            '<p id="name">A platform that uses FIFO (First In, First Out) logic for the management and consumption of industrial tools. It provides a clear and intuitive interface to streamline the management of cutting tools.</p>',
            unsafe_allow_html=True)
        st.write("######")
    with col2:
        st.image("./assets/dashboard.png", width=550)

    # st.markdown("</section>", unsafe_allow_html=True)

    st.write("###")
    space, col1, space, col2 = st.columns([1, 2.5, 1, 4])
    with col1:
        st.image("./assets/chatassistant.png", width=550)
    with col2:
        st.write("###")
        st.markdown('<h2 id="name">Industrial Management Chat Assistant</h2>', unsafe_allow_html=True)
        st.markdown(
            '<p id="name">An AI-powered chat assistant, trained specifically to support industry managers. It helps streamline communication, provides insights, and enhances decision-making by responding to management-related queries.</p>',
            unsafe_allow_html=True)
        st.write("######")

    st.write("###")
    space, col1, space, col2 = st.columns([1, 2.5, 1, 4])
    with col1:
        st.markdown('<h2 id="name">Table Tennis Movement Analysis using Computer Vision</h2>', unsafe_allow_html=True)
        st.markdown(
            '<p id="name">A CV (Computer Vision) project designed to analyze and evaluate correct movements in table tennis. This platform uses advanced techniques to provide feedback on performance and help improve gameplay.</p>',
            unsafe_allow_html=True)
        st.write("######")
    with col2:
        st.image("./assets/tt.png", width=550)
    st.write("###")

    # Terceira Seção: Experiências Profissionais
    #st.markdown("<section>", unsafe_allow_html=True)
    st.divider()
    st.markdown('<h4>Professional Experience</h4>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<h5>🛠️ Log Z – Management and Systems Development</h5>', unsafe_allow_html=True)
    st.write(
        "- Project leader and full-stack developer in a startup focused on creating integrated and automated systems for tooling management."
        "\n- Development of technological solutions aimed at optimizing industrial processes."
        "\n- Experience in leadership and project management in technological environments.")

    st.write("######")
    st.markdown('<h5>👥 StackX Job – Technical Recruiter and Programming Mentor</h5>', unsafe_allow_html=True)
    st.write(
        "- Senior technical recruiter responsible for evaluating developers for various technology positions."
        "\n- Programming mentor, training new talents in software development."
        "\n- Development of selection processes and technical training.")

    st.write("######")
    st.markdown('<h5>📚 Programming and Technology Instructor – Stackx and SATC</h5>', unsafe_allow_html=True)
    st.write(
        "- Instructor in technology and programming for technical and professional level students."
        "\n- Classes focused on programming languages and development methodologies."
        "\n- Experience in training future professionals for the technology market.")

    st.write("######")
    st.markdown('<h5>🔬 SATC – Researcher in Engineering and Material Science</h5>', unsafe_allow_html=True)
    st.write(
        "- Conducted scientific research focused on geopolymers and innovative materials."
        "\n- Performed mechanical and chemical tests, contributing to scientific advancement."
        "\n- Created scientific articles and technical reports focused on innovation.")

    st.write("######")
    st.markdown('<h5>🤖 Criciúma City Hall – Robotics Teacher</h5>', unsafe_allow_html=True)
    st.write(
        "- Robotics teacher in partnership with SATC School, teaching practical concepts of robotics."
        "\n- Coordinated educational projects to develop skills in innovation and technology."
        "\n- Trained students in practical skills related to robotics.")

    st.write("######")
    st.markdown('<h5>💻 CONVEM – Web Developer</h5>', unsafe_allow_html=True)
    st.write(
        "- Full-stack developer focused on creating e-commerce solutions."
        "\n- Created online stores with technology integration to enhance user experience."
        "\n- Experience in development for optimization and usability of e-commerce platforms.")

    st.write("######")
    st.markdown('<h5>🎖️ Brazilian Army – Artillery Officer</h5>', unsafe_allow_html=True)
    st.write(
        "- Training as an officer in the artillery branch, developing leadership and discipline skills."
        "\n- Experience in high-responsibility environments and decision-making."
        "\n- Training and execution of artillery-related activities.")
    #st.markdown("</section>", unsafe_allow_html=True)

    st.write("###")
    space, col1, space = st.columns([5, 0.9, 5])
    with col1:
        st.image('./assets/felipeai.png', width=100)
    st.markdown('<h5 class="footer"> © 2024 Felipe Paes</h5>', unsafe_allow_html=True)
    st.markdown('<h5 class="footer"> *"The body that does not vibrate is the skeleton that drags itself."*</h5>', unsafe_allow_html=True)

def main():
    streamlit_visual()

if __name__ == '__main__':
    main()
