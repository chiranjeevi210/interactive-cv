import streamlit as st
from PIL import Image

# 1. Set page configuration (Must be called ONCE at the very top)
st.set_page_config(
    page_title="G V Chiranjeevi Adari - Interactive CV",
    page_icon="⚡",
    layout="wide",
)

# Custom HTML styling definitions to match layout themes
st.markdown(
    """
    <style>
    .main-title { font-size: 2.8rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 1.3rem; color: #4B5563; margin-top: 5px; }
    .section-header { border-bottom: 2px solid #3B82F6; padding-bottom: 5px; color: #1E3A8A; font-weight: 600; margin-bottom: 20px; }
    .nested-list { margin-left: 20px; font-size: 0.95rem; color: #374151; }
    </style>
""",
    unsafe_allow_html=True,
)

# SIDEBAR NAVIGATION
st.sidebar.header("CV Navigation")
section = st.sidebar.radio(
    "Go to Section:",
    [
        "Home & Objective",
        "Qualifications",
        "Technical Certifications & Skills",
        "Experience & Job Roles",
        "Publications & Patents",
        "Projects & Future Plans",
        "Workshops & FDPs",
        "Personal & Professional Details",
    ],
)

# HOME & OBJECTIVE SECTION
if section == "Home & Objective":
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            image = Image.open('profile.jpg')
            st.image(image, width=160)
        except FileNotFoundError:
            st.error("Picture 'profile.jpg' not found in this folder.")
    with col2:
        st.markdown("<h1 class='main-title'>G V Chiranjeevi Adari</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Electrical Engineer & Software Professional</p>", unsafe_allow_html=True)
        st.write("Welcome to my profile web page! Use the navigation menu panel on the left to see full details.")

    st.write("---")
    
    grid_col1, grid_col2 = st.columns(2)
    with grid_col1:
        st.markdown("### 📞 Contact Information")
        st.write("📱 **Mobile:** 9949163002")
        st.write("📧 **Email:** chiranjeevi210@gmail.com")
        st.write("📍 **Address:** 4-243/1/4, BC Colony, Vepagunta, Visakhapatnam-530047")
    
    with grid_col2:
        st.markdown("### 🎯 Career Objective")
        st.info(
            "An Electrical Engineer and Software professional, forever a student, "
            "dreaming for career in a nice environment which is technically and ethically developed."
        )

    st.write("---")
    st.markdown("### 💪 Core Strengths")
    st.markdown("- Possess 9 years of professional experience (After M.Tech) in teaching Electrical and Electronics subjects.")
    st.markdown("- Ability to generate effective teaching by making use of various methodologies with a good knowledge of OBE.")
    st.markdown("- Proven track record of guiding and motivating students across different regional higher education systems.")
    st.markdown("- Excellent time management, organizational, and written/verbal communication skills.")
    st.markdown("- Ability to carry out tasks with minimal supervision with a positive attitude.")

# QUALIFICATIONS SECTION
elif section == "Qualifications":
    st.markdown("<h2 class='section-header'>🎓 Educational Summary</h2>", unsafe_allow_html=True)

    st.markdown("#### **Post Graduation**")
    with st.expander("M.Tech (High Voltage Engineering) — JNTU, Kakinada (2012)", expanded=True):
        st.write("🏆 Result: Distinction | 📊 Percentage: 72.0%")

    st.markdown("#### **Graduation**")
    with st.expander("B.Tech (Electrical & Electronics Engineering) — Chaitanya Engg. College, Visakhapatnam (2007)", expanded=True):
        st.write("🏆 Result: Distinction | 📊 Percentage: 71.63%")

    st.markdown("#### **Schooling**")
    st.markdown("- **Intermediate (MPC):** Gayatri Junior College, Vizianagaram (2003) - First Class")
    st.markdown("- **Secondary School Certificate (SSC):** ZP High School, Jami, Vizianagaram (2001) - First Class")

    st.write("---")
    st.markdown("### 🏆 Major Milestones")
    st.success("🥇 Got Pratibha Award for the year 2016-17 at VIIT, Vizag.")
    st.markdown("- **JNTUH Ratification:** Ratified in October 2022.")
    st.markdown("- **JNTUK Ratification:** Ratified on 17-Oct 2015.")
    st.markdown("- **GATE 2014:** Qualified.")
    st.markdown("- **APRCET 2018:** Qualified for Doctoral programmes in Andhra Pradesh.")

# # CERTIFICATIONS & SKILLS SECTION
elif section == "Technical Certifications & Skills":
    st.markdown("<h2 class='section-header'>💻 Technical Certifications & Specializations</h2>", unsafe_allow_html=True)

    with st.expander("🚀 IBM Full Stack JavaScript Developer (Sep 2026 - 12 Course Series)", expanded=False):
        st.write("[View Credential](https://coursera.org)")
        st.markdown("""
        <div class='nested-list'>
        • Introduction to Software Engineering<br>• Introduction to HTML, CSS, & JavaScript<br>• Getting Started with Git and GitHub<br>
        • JavaScript Programming Essentials<br>• Developing Front-End Apps with React<br>• Developing Back-End Apps with Node.js and Express<br>
        • Get Started with Cloud Native, DevOps, Agile, and NoSQL<br>• Introduction to Containers w/ Docker, Kubernetes & OpenShift<br>
        • Application Development using Microservices and Serverless<br>• Node.js & MongoDB: Developing Back-end Database Applications<br>
        • JavaScript Full Stack Capstone Project<br>• Software Developer Career Guide and Interview Prep
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🧠 Microsoft AI and ML Engineering Professional (July 2026 - 5 Course Series)", expanded=False):
        st.write("[View Credential](https://coursera.org)")
        st.markdown("""
        <div class='nested-list'>
        • Foundations of AI and Machine Learning<br>• AI and Machine Learning Algorithms and Techniques<br>
        • Building Intelligent Troubleshooting Agents<br>• Microsoft Azure for AI and Machine Learning<br>
        • Advanced AI and Machine Learning Techniques and Capstone
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🤖 IBM AI Developer (June 2026 - 10 Course Series)", expanded=False):
        st.write("[View Credential](https://coursera.org)")
        st.markdown("""
        <div class='nested-list'>
        • Introduction to Software Engineering<br>• Introduction to AI (March 2026)<br>• Generative AI Introduction and Applications<br>
        • Introduction to HTML, CSS and JavaScript<br>• Python for Data Science, AI & Development<br>• Developing AI Applications with Python and Flask<br>
        • Building Generative AI-Powered Applications with Python<br>• Generative AI: Elevate your Software Development Career<br>
        • Software Developer Career Guide
        </div>
        """, unsafe_allow_html=True)

    with st.expander("☕ IBM Java Developer (July 2026 - 14 Course Series)", expanded=False):
        st.write("[View Credential](https://coursera.org)")
        st.markdown("""
        <div class='nested-list'>
        • Introduction to Software Engineering<br>• Java Programming for Beginners<br>• Object Oriented Programming in Java<br>
        • Java App Development Project: Fundamentals, OOP & File I/O<br>• Introduction to HTML, CSS, & JavaScript<br>
        • Getting Started with Git and GitHub<br>• Spring Framework for Java Development<br>• Java Development with Databases<br>
        • Cloud Native, Microservices, Containers, DevOps and Agile<br>• Java: Design Patterns, Testing, and Deployment<br>
        • Java Development Capstone Project<br>• Generative AI: Elevate your Career<br>
        • Generative AI for Java and Spring Development<br>• Software Developer Career Guide
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🌐 IBM JavaScript Backend Developer (August 2026 - 13 Course Series)", expanded=False):
        st.write("[View Credential](https://coursera.org)")
        st.markdown("""
        <div class='nested-list'>
        • Introduction to Software Engineering<br>• Introduction to HTML, CSS, & JavaScript<br>• Getting Started with Git and GitHub<br>
        • JavaScript Programming Essentials<br>• Developing Back-End Apps with Node.js and Express<br>
        • Get Started with Cloud Native, DevOps, Agile, and NoSQL<br>• Introduction to Containers w/ Docker, Kubernetes & OpenShift<br>
        • Application Development using Microservices and Serverless<br>• Node.js & MongoDB: Developing Back-end Database Applications<br>
        • Application Security for Developers and DevOps Professionals<br>• Monitoring and Observability for Development and DevOps<br>
        • JavaScript Back-end Capstone Project<br>• Software Developer Career Guide
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔒 Google Cybersecurity Professional (July 2026 - 9 Course Series)", expanded=False):
        st.write("[View Credential](https://coursera.org)")
        st.markdown("""
        <div class='nested-list'>
        • Foundations of Cybersecurity<br>• Play It Safe: Manage Security Risks<br>• Connect and Protect: Networks and Network Security<br>
        • Tools of the Trade: Linux and SQL<br>• Assets, Threats, and Vulnerabilities<br>• Sound the Alarm: Detection and Response<br>
        • Automate Cybersecurity Tasks with Python<br>• Put It to Work: Prepare for Cybersecurity Jobs<br>• Accelerate Your Job Search with AI
        </div>
        """, unsafe_allow_html=True)

    # Clean 4-space indentation alignment fixed down here:
    st.markdown("### 🏛️ NPTEL Certifications")
    st.markdown("- Advanced Computer Architecture (April 2026)\n- Advanced Computer Networks (April 2025)\n- Practical Cybersecurity for Practitioners (Oct 2024)\n- Cloud Computing (Oct 2024)\n- Big Data Computing (Oct 2023)\n- Ethics in Engineering Practice (Oct 2023)\n- Introduction to Smart Grid (Sep 2022)")
    
    st.markdown("### 🛠️ Core Skills Matrix")
    st.markdown("**Programming Languages:** Advanced Python | JavaScript | MATLAB | Java Basics | Web Development | AI Development")
    st.markdown("**Online Virtual Tools:** Google Meet, Microsoft Teams, Cisco Webex, GoToMeeting")

# ================= EXPERIENCE & ROLES SECTION =================
elif section == "Experience & Job Roles":
    st.markdown("<h2 class='section-header'>💼 Professional Experience & Academic Roles</h2>", unsafe_allow_html=True)
    st.markdown("- **Assistant Professor (EE - AIML)** | Sandip Foundation's SITRC, Nashik (27-06-2025 to 31-05-2026)")
    st.markdown("- **Assistant Professor (EEE)** | Guru Nanak Institute of Technology, Hyderabad (16-02-2023 to 11-01-2025)")
    st.markdown("- **Assistant Professor (EEE)** | Malla Reddy Engineering College for Women, Secunderabad (18-07-2022 to 15-02-2023)")
    st.markdown("- **Sr. Assistant Professor (EEE)** | Aditya College of Engineering, Surampalem (22-11-2019 to 26-07-2021)")
    st.markdown("- **Assistant Professor (EEE)** | Vignan's Institute of Information Technology, Visakhapatnam (13-03-2015 to 04-11-2019)")
    
    st.write("---")
    st.markdown("### 📋 Primary Academic Job Responsibilities")
    st.markdown("- Teaching UG and PG engineering courses related to EEE & AIML architectures.")
    st.markdown("- Head of Department Examination branch coordination and performance reporting profiles.")
    st.markdown("- Preparing department accreditation assessment filing records (OBE, NBA, NAAC files).")
    
    st.markdown("### 📚 Key Courses Handled")
    st.write("Artificial Intelligence Techniques, AI Based Web Design, Introduction to Expert Systems, Software Testing Certification, Advanced Python Programming, Discrete Mathematics and Logic, Electro Magnetic Fields, Microprocessors and Microcontrollers, Digital Logic Design, Electrical Technology, High Voltage Engineering, Control Systems, Power System Protection.")

# ================= PUBLICATIONS & PATENTS SECTION =================
elif section == "Publications & Patents":
    st.markdown("<h2 class='section-header'>📚 Publications, Patents & System Research</h2>", unsafe_allow_html=True)
    st.markdown("### 💡 Published Patents")
    st.warning("📌 **Smart Medical Diagnosis System using IoT driven Machine Learning and Big Data Analytics** | Biomedical Field | Pub No: 11/2024(INA)")
    st.warning("📌 **Power Quality Analysis Using IoT** | Patent Application No: 202441060301 (August 2024)")
    
    st.markdown("### 📖 Book Chapters")
    st.info("📘 **Cyber security in smart Grids: Role of Digital Advanced Devices** | IGI Global Publications, October 2022 | ISBN: 9781668458273.")
    
    st.markdown("### 📄 Selected Papers Published")
    st.markdown("- *System knowledge for digital twin technologies in Industry 4.0 and Industry 5.0* | 5th International E-Conference (ICMMSE:IR), Sandip Foundation, Nashik, Feb 2026.")
    st.markdown("- *Fuzzy based Unified Control and Power Management Scheme for PV Battery based Hybrid Micro Grids* | IJAEMA, Vol XIV, Nov 2022.")
    st.markdown("- *Dynamic stability Enhancement of a Smart Grid Using Artificial Neural Network Based STATCOM* | INDJST, Dec 2016 (Impact Factor: 0.68).")
    st.markdown("- *Transient stability improvement of Single machine infinite bus system using Distributed power flow controller* | IJPAM, RTEEE Conference, 2017.")
    st.markdown("- *Application of SVC for Multi Objective Power problem with PSO* | IJPAM, RTEEE Conference, 2017.")
    st.markdown("- *A grid interfaced low frequency wind power* | IJRASET, Vol 3, March 2015.")
    st.markdown("- *Simulation based Analysis for fixing Optimal stages for a H-Bridge cascaded Multi Level Converters* | IJSETR, Vol 5, March 2016.")

# ================= PROJECTS & FUTURE PLANS SECTION =================
elif section == "Projects & Future Plans":
    st.markdown("<h2 class='section-header'>🔬 Academic Projects & Future Plans</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📂 Guided Thesis & Research History")
        st.write("**M.Tech Thesis:** Fuzzy logic controller and decision maker for damping Load frequency oscillations of Four area systems.")
        st.write("**B.Tech Project:** Load frequency control of single area power system using Fuzzy logic.")
        st.write("")
        st.metric("B.Tech Projects Guided", "08")
        st.metric("M.Tech Projects Guided", "02")
        
    with col2:
        st.markdown("### 🚀 Roadmap & Future Milestones")
        st.success("📚 **Book Publication:** *Logical Introduction to Digital Electronics* (Accepted by BPB, editing stage).")
        st.success("✍️ **Journal Work:** Two Quality Research papers related to Power System Grids (One Accepted).")
        st.success("🎓 **Doctorate Goal:** Complete Ph.D. execution in Near Future.")

# ================= WORKSHOPS & FDPS SECTION =================
elif section == "Workshops & FDPs":
    st.markdown("<h2 class='section-header'>🏫 Workshops, Webinars & FDP History</h2>", unsafe_allow_html=True)
    
    st.markdown("#### Teaching Methodologies & OBE Programs")
    st.markdown("- **FDP:** OBE Focused Curriculum Design, IQAC Cell, Sandip University, Nashik (Nov 2026).")
    st.markdown("- **Workshop:** OBE Workshop Frameworks, VIIT by KLETU (May 2018).")
    st.markdown("- **National Workshop:** MOOCs and E-learning in Higher Education, MHRD, Delhi University (Aug 2018).")
    
    st.markdown("#### AI, ML, and Internet of Things Programs")
    st.markdown("- **FDP:** Open Business Tools for AI and Business Applications, 6th Q Research (Aug-Sep 2025).")
    st.markdown("- **FDP:** Emerging Trends and Applications of Generative AI, SVKMs Institute of Technology (Jan 2025).")
    st.markdown("- **International Workshop:** IoT and ML Based Microgrid & Energy Management, CBIT Hyderabad (Feb 2024).")
    st.markdown("- **Training Track:** Python for Data Science, Excel R (42 Hours, 2022).")
    
    st.markdown("#### Power System & Smart Grids Events")
    st.markdown("- **FDP:** Advanced Intelligence and ICT Application to Power System Protection, NIT Warangal (July 2022).")
    st.markdown("- **SPARC Workshop:** Integration of Renewable Energy & EV to Microgrid, NIT Tiruchirappalli (Feb 2022).")

# ================= PERSONAL DETAILS SECTION =================
elif section == "Personal & Professional Details":
    st.markdown("<h2 class='section-header'>👤 Personal Profiles & Verification Identity</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📅 **Date of Birth:** 17 December 1985")
        st.write("👨 **Father Name:** Ramarao")
        st.write("🗣️ **Languages Known:** English, Hindi, Telugu, Punjabi Gurmukhi (Read & Write)")
        st.write("✈️ **Willing to Relocate:** Yes")
        st.write("🏫 **Schooling Location:** Visakhapatnam & Vizianagaram")
        
    with col2:
        st.write("🆔 **JNTUH Registration ID:** 3059-191113-150648")
        st.write("🆔 **UNIPUNE ID:** 52092500466")
        st.write("🤝 **IEEE Membership ID:** 100444351")
        st.write("🤝 **IAENG Membership ID:** 155951")
        
    st.write("---")
    st.markdown("### 🔗 Professional Network Identifiers")
    st.markdown("- **Google Scholar Citations:** [Open Profile](https://google.com)")
    st.markdown("- **ORCID Open Research ID:** [Open Profile](https://orcid.org)")
    st.markdown("- **Scopus Author Identifier ID:** [Open Profile](https://scopus.com)")
    
    st.write("---")
    st.markdown("### 📋 Academic References")
    st.markdown("* **Mr. K Prasad** | Rtd. Sr Lecturer, Government Polytechnic, Vizianagaram (Cell: 9912340292)")
    st.markdown("* **Mr. K Srikanth** | Associate Professor, GVP College of Engineering, Visakhapatnam (Cell: 9440897892)")
    st.markdown("* **Dr. Dipak D Bhage** | Professor, PCU, Pune (Cell: 70837 80216)")
