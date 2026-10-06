import streamlit as st
import re
import time
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CCET College Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

:root {
    color-scheme: dark;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.12), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(168,85,247,0.10), transparent 25%),
        #080b14;
    color: #f8fafc;
}

/* Top header */
header[data-testid="stHeader"] {
    background: rgba(8, 11, 20, 0.8);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(148, 163, 184, 0.12);
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
    border-right: 1px solid rgba(148, 163, 184, 0.15);
    box-shadow: inset -1px 0 0 rgba(255,255,255,0.03);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] span {
    color: #f8fafc;
}

section[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(148,163,184,0.18);
    color: #f8fafc;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(99,102,241,0.14);
    border-color: rgba(129,140,248,0.7);
}

/* Main container */

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 7rem;
}

/* Hero */

.hero {
    padding: 28px;
    border-radius: 24px;
    background:
        linear-gradient(
            135deg,
            rgba(99,102,241,0.18),
            rgba(168,85,247,0.10)
        );
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 25px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.25);
}

.hero-title {
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #aeb7ca;
    font-size: 15px;
}

/* Cards */

.card {
    background: rgba(18,24,38,0.85);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 15px;
    transition: 0.2s;
}

.card:hover {
    border-color: rgba(129,140,248,0.5);
    transform: translateY(-2px);
}

.card-icon {
    font-size: 28px;
}

.card-title {
    font-weight: 700;
    font-size: 16px;
    margin-top: 8px;
}

.card-text {
    color: #9ca8bd;
    font-size: 13px;
    margin-top: 5px;
}

/* Chat messages */

[data-testid="stChatMessage"] {
    background: rgba(17,24,39,0.72);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    margin-bottom: 12px;
    padding: 12px;
}

/* Assistant text */

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] div {
    color: #f1f5f9;
}

/* Buttons */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.10);
    background: rgba(255,255,255,0.04);
    color: #f8fafc;
    min-height: 42px;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #818cf8;
    background: rgba(99,102,241,0.15);
}

/* Chat input */

[data-testid="stChatInput"] {
    position: relative;
    border-radius: 14px;
    border: 1px solid rgba(148, 163, 184, 0.18);
    background: rgba(15, 23, 42, 0.9);
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.16);
    padding: 8px 10px;
    margin-top: 14px;
    max-width: 100%;
    overflow: hidden;
}

[data-testid="stChatInput"] > div {
    display: flex;
    flex-direction: row !important;
    align-items: center !important;
    gap: 8px;
    width: 100%;
}

[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] input {
    background: rgba(15, 23, 42, 0.95) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(148, 163, 184, 0.35) !important;
    border-radius: 10px !important;
    box-shadow: none !important;
    min-height: 42px !important;
    height: 42px !important;
    padding: 10px 12px !important;
    font-size: 14px !important;
    resize: none !important;
    flex: 1 1 auto !important;
    width: auto !important;
}

[data-testid="stChatInput"] textarea:focus,
[data-testid="stChatInput"] input:focus {
    border-color: rgba(99, 102, 241, 0.7) !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.14) !important;
}

[data-testid="stChatInput"] textarea::placeholder,
[data-testid="stChatInput"] input::placeholder {
    color: #94a3b8 !important;
}

[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    border: none !important;
    color: white !important;
    border-radius: 10px !important;
    min-width: 84px !important;
    min-height: 42px !important;
    height: 42px !important;
    font-weight: 600 !important;
    padding: 0 14px !important;
    box-shadow: 0 6px 14px rgba(99, 102, 241, 0.25) !important;
    flex-shrink: 0 !important;
    margin-left: 0 !important;
}

[data-testid="stChatInput"] button:hover {
    filter: brightness(1.04);
}

/* Status */

.status {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 50px;
    background: rgba(34,197,94,0.12);
    color: #86efac;
    font-size: 12px;
    border: 1px solid rgba(34,197,94,0.20);
}

.footer {
    text-align: center;
    color: #697386;
    font-size: 12px;
    margin-top: 40px;
}

.social-box {
    background: rgba(18,24,38,0.85);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# OFFICIAL WEBSITE & SOCIAL PROFILES
# ============================================================

DEVELOPER = {
    "name": "Mohamed Imraan",
    "role": "AI Engineer",
    "brand": "Pain Codes",
    "position": "Founder of Pain Codes",
    "creator": "Tech Content Creator",
    "education": "B.Tech Electronics and Communication Engineering",
    "college": "Christ College of Engineering and Technology",
    "location": "Puducherry, India",
    "email": "mohamedimraan.2405@gmail.com",
    "linkedin": "https://www.linkedin.com/in/mohamed-imraan-full-stack-developer",
    "github": "https://github.com/Mohamed-Imraan",
    "paincodes": "https://github.com/Pain-codes"
}

OFFICIAL_WEBSITE = "https://christcet.edu.in/"

SOCIAL_PROFILES = {
    "Instagram": "https://www.instagram.com/ccetinsta/",
    "Facebook": "https://www.facebook.com/christcet.edu.in/",
    "LinkedIn": "https://in.linkedin.com/school/christ-college-of-engineering-and-technology/"
}

# ============================================================
# COLLEGE KNOWLEDGE BASE
# ============================================================

COLLEGE = {

    "college": {
        "name": "Christ College of Engineering and Technology",
        "short_name": "CCET",
        "location": "Paris Nagar, Moolakulam, Puducherry",
        "affiliation": "Pondicherry University"
    },

    "timings": {
        "first_year": "9:15 AM to 4:30 PM",
        "other_years": "9:30 AM to 4:45 PM"
    },

    "breaks": {
        "first_year": [
            "Morning Break: 10:45 AM – 11:00 AM",
            "Lunch: 12:30 PM – 1:15 PM",
            "Afternoon Break: 2:45 PM – 3:00 PM"
        ],
        "other_years": [
            "Morning Break: 11:00 AM – 11:15 AM",
            "Lunch: 12:45 PM – 1:30 PM",
            "Afternoon Break: 3:00 PM – 3:15 PM"
        ]
    },

    "blocks": {

        "admission": """
The Admission Block contains the college office,
Principal's office, Manager's office, Director's office
and Examination Cell.
""",

        "main": """
The Main Block has four floors.

Ground Floor:
S&H department.

First Floor:
Library, laboratories, restrooms, PT/staff facilities.

Second Floor:
ECE department.

Third Floor:
CSE and IT departments.

Fourth Floor:
AIDS, Blockchain department and seminar hall.
""",

        "mechanical": """
The Mechanical Block has four floors containing
classrooms, laboratories and restrooms.
Boys' bike parking is located near the Mechanical Block.
""",

        "mba": """
The MBA Block has three floors.
It is located near the playground and CCET Arts and Science College.
The canteen, SLAM gym and auditorium are nearby.
"""
    },

    "facilities": {

        "transport": "The college has 6+ buses.",

        "hostel": "The college does not have a hostel.",

        "parking": """
Girls' bike parking is behind the Main Block.
Boys' bike parking is near the Mechanical Block.
There is no car parking.
""",

        "canteen": "The canteen is located near the MBA Block.",

        "gym": "SLAM gym is located near the MBA Block.",

        "auditorium": "The auditorium is located near the MBA Block."
    },

    "canteen": {
        "sambar": "₹45",
        "chicken_noodles": "₹90"
    },

    "exams": """
The college conducts two periodic examinations,
two-mark examinations, model examinations and semester examinations.

Two-mark examination duration: 1.5 hours.
Model examination duration: 3 hours.
""",

    "communication": """
WhatsApp is one of the primary communication channels
used for college-related announcements and communication.
""",

    "dress": """
All shoes are allowed.
Formal shoes are recommended,
especially when attending formal college activities.
"""
}

# ============================================================
# NORMALIZE
# ============================================================

def normalize(text):

    text = text.lower().strip()

    text = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text


# ============================================================
# SOCIAL PROFILE RESPONSE
# ============================================================

def social_response():

    return f"""
### 📱 CCET Social Media Profiles

Here are the CCET social profiles you can refer to:

📸 **Instagram**

[CCET Instagram]({SOCIAL_PROFILES["Instagram"]})


📘 **Facebook**

[CCET Facebook]({SOCIAL_PROFILES["Facebook"]})


💼 **LinkedIn**

[CCET LinkedIn]({SOCIAL_PROFILES["LinkedIn"]})


🌐 **Official Website**

[Christ College of Engineering and Technology]({OFFICIAL_WEBSITE})

You can use these profiles for college updates, announcements,
events and other official information.
"""


# ============================================================
# OFFICIAL WEBSITE RESPONSE
# ============================================================

def website_response():

    return f"""
### 🌐 Official CCET Website

For the latest and official information, you can refer to:

**[Christ College of Engineering and Technology](https://christcet.edu.in/)**

The official website is especially useful for information
that may change frequently, such as:

• Admissions
• Notifications
• Academic updates
• Examination information
• Events
• Contact information
• College announcements

📱 You can also ask me:

**"Give me CCET social media profiles"**

and I will provide the available social profiles.
"""


# ============================================================
# INTENT ENGINE
# ============================================================

def get_response(query):

    q = normalize(query)

    # ========================================================
    # DEVELOPER / CREATOR
    # ========================================================

    if any(x in q for x in [
        "who is the developer",
        "who developed you",
        "who created you",
        "who made this",
        "who made it",
        "who made you",
        "who built you",
        "who built this",
        "who built it",
        "who is the creator",
        "who created this",
        "who made u",
        "who is the programmer",
        "who made u",
        "who is your developer",
        "who is your creator",
        "chatbot developer",
        "christ chatbot developer",
        "ccet chatbot developer",
        "college chatbot developer",
        "who is imraan",
        "who is mohamed imraan",
        "who is mohamed",
        "mohamed imraan",
        "mohamed"
        "imraan",
        "about imraan",
        "about mohamed imraan",
        "developer name",
        "creator name",
        "who is the creator",
        "who is the creator of this chatbot",
        "who is the developer of this chatbot",
        "programmer of this chatbot",
        "who is the programmer of this chatbot",
        "who is the engineer of this chatbot",
        "pain codes",
        "who is the founder of pain codes",
        "who is the founder of this chatbot",
        "paincodes",
        "pain",
        "paincodes",
        "who made this chatbot",
        "who built this chatbot",
        "who developed this chatbot",
        "who created this chatbot",
        "chatbot creator",
        "chatbot created by",
        "chatbot developed by"
    ]):

        return f"""
### 👨‍💻 Meet the Developer

This **CCET College Assistant** was developed by:

## **{DEVELOPER["name"]}**

🚀 **{DEVELOPER["position"]}**

🤖 **{DEVELOPER["role"]}**

💻 **{DEVELOPER["creator"]}**

🎓 **{DEVELOPER["education"]}**

🏫 **{DEVELOPER["college"]}, {DEVELOPER["location"]}**

### 🧠 About Mohamed Imraan

Mohamed Imraan is a technology enthusiast working across
**Artificial Intelligence, Machine Learning, Generative AI,
Full-Stack Development and Embedded Systems**.

He is also the founder of **Pain Codes**, a technology-focused
initiative for projects, learning resources and technical content.

### 🔗 Professional Profiles

📧 **Email**

[Contact Mohamed Imraan](mailto:{DEVELOPER["email"]})

ℹ️ **LinkedIn**

[View Mohamed Imraan on LinkedIn]({DEVELOPER["linkedin"]})

💻 **GitHub**

[View Mohamed Imraan on GitHub]({DEVELOPER["github"]})

🚀 **Pain Codes**

[View Pain Codes on GitHub]({DEVELOPER["paincodes"]})

---

💡 **Fun fact:** You're currently chatting with a chatbot
created as a CCET-focused project by Mohamed Imraan. 🎓🤖
"""

    # ========================================================
    # CELEBRATIONS AND EVENTS
    # ========================================================

    if any(x in q for x in ["pongal"]):

        return """
### 🪔 Pongal Celebration

Pongal is one of the traditional celebrations at CCET.
Students may take part in cultural programs and activities
such as performances, competitions, games and music.
Students may wear traditional attire when permitted for the
celebration. Students from different departments can join in.

Please follow the college announcement for the event's
timing, dress code, registration and participation details.
"""

    if any(x in q for x in ["onam"]):

        return """
### 🌾 Onam Celebration

Onam is celebrated at CCET as a cultural event. Activities
may include cultural performances, games, competitions and
group activities, with participation across departments.
Traditional attire may be worn when permitted for the event.

Please follow the college announcement for current event
details, timing, dress instructions and participation.
"""

    if any(x in q for x in ["diwali", "deepavali"]):

        return """
### 🪔 Diwali Celebration

Diwali is a festive occasion at CCET. The college may
organize cultural programs and student activities for the
celebration. Activities and participation depend on the
schedule announced for that year.

Please follow the college's event and safety instructions.
"""

    if any(x in q for x in ["christmas"]):

        return """
### 🎄 Christmas Celebration

Christmas is celebrated at CCET as a cultural and festive
event. Programs may include performances, games, decorations
and other student activities.

Check the college announcement for the current schedule
and participation details.
"""

    if any(x in q for x in ["ayudha pooja", "ayudha puja"]):

        return """
### 🛕 Ayudha Pooja

Ayudha Pooja is observed as part of CCET's festive and
cultural activities. It is associated with showing respect
for tools, equipment and instruments used for learning and
work. Departments may take part in related activities.

The celebration date, timing and participation details
should be confirmed through the college announcement.
"""

    if any(x in q for x in [
        "traditional dress",
        "traditional attire",
        "traditional clothes",
        "wear traditional",
        "ethnic wear",
        "traditional dress in college",
        "traditional clothing"
    ]):

        return """
### 👕 Traditional Dress

Traditional clothing may be permitted during specific
cultural and festive celebrations at CCET, such as Pongal
and Onam. Please follow any event-specific dress-code
instructions announced by the college.
"""

    if any(x in q for x in [
        "cultural event",
        "cultural events",
        "cultural activities",
        "cultural program",
        "cultural programs",
        "cultural programme",
        "cultural programmes",
        "college events",
        "student events",
        "dance and singing",
        "events in college",
        "event fee",
        "cultural fee",
        "50 rupees",
        "50 rs",
        "50 participation"
    ]):

        return """
### 🎭 Cultural Events

CCET cultural activities give students opportunities to
showcase talents beyond academics. Activities may include
dance, singing, music, drama, performances, games,
competitions, team activities and department-level events.

Some programs may have a participation or event fee, such
as ₹50, depending on the specific event. Check its official
announcement for the current fee, schedule and registration.
"""

    if any(x in q for x in [
        "symposium",
        "symposiums",
        "technical event",
        "technical events",
        "technical competition",
        "paper presentation",
        "project presentation",
        "coding event",
        "programming event",
        "technical quiz",
        "symposium fee",
        "symposium registration"
    ]):

        return """
### 🏆 Technical Symposiums

CCET symposiums and student-oriented technical events may
include competitions, paper and project presentations,
quizzes, coding events, workshops, demonstrations and team
activities.

Registration fees, schedule, eligibility and competitions
vary by event. Refer to the official announcement for the
specific symposium.
"""

    if any(x in q for x in [
        "cetafest",
        "ceta fest",
        "cetafest contribution",
        "cetafest fee",
        "cetafest amount",
        "cetafest cost"
    ]):

        return """
### 🎊 CETAFEST

CETAFEST is a major annual celebration associated with the
college. It may feature cultural programs, music and
entertainment, celebrity appearances, student activities
and the college magazine.

The contribution was previously reported as around ₹1,500
or more, but the amount can change each year. Please check
the latest college announcement for the current contribution
and event details.
"""

    # ========================================================
    # GREETINGS
    # ========================================================

    greetings = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "hai",
        "hii",
        "hey there",
        "who are u",
        "what is your name",
        "what is your role",
        "what is your purpose",
        "what can you do",""
        "what is your function",
        "what is your job",
        "what's your name",
        "your name",
        "your name bro",
        "your name?",
        "who are you",
        "what are you",
        "are you a chatbot",
        "are you a college chatbot",
        "what is your name",
        "your name"
    ]

    if any(
        re.search(r'\b' + re.escape(word) + r'\b', q)
        for word in greetings
    ):

        return """
### 👋 Hello! I'm the CCET AI Assistant

I'm a college chatbot here to assist you with information
about **Christ College of Engineering and Technology**.

I can help you with:

🏫 College information  
🕘 College timings  
🏢 Block locations  
🎓 Departments  
🚌 Transportation  
🍽️ Canteen  
📝 Examinations  
🅿️ Parking  
👕 Dress information  
🏠 Hostel information  
📢 Communication  
📱 Social media profiles  

Ask me anything about CCET!
"""

    # ========================================================
    # SOCIAL MEDIA
    # ========================================================

    social_words = [
        "instagram",
        "insta",
        "facebook",
        "linkedin",
        "social media",
        "social profile",
        "social profiles",
        "social account",
        "social accounts",
        "social link",
        "social links",
        "online profile",
        "online profiles"
    ]

    if any(word in q for word in social_words):

        return social_response()

    # ========================================================
    # WEBSITE
    # ========================================================

    website_words = [
        "website",
        "web site",
        "official website",
        "official site",
        "college website",
        "college site",
        "refer website",
        "reference website",
        "official link"
    ]

    if any(word in q for word in website_words):

        return website_response()

    # ========================================================
    # COLLEGE
    # ========================================================

    if any(x in q for x in [
        "college name",
        "which college",
        "about college",
        "ccet",
        "college information"
    ]) and not any(x in q for x in ["placement", "recruit", "job"]):

        return f"""
### 🏫 {COLLEGE["college"]["name"]}

**Short Name:** CCET

**Location:** {COLLEGE["college"]["location"]}

**Affiliation:** {COLLEGE["college"]["affiliation"]}

I can also provide information about departments,
blocks, timings, exams, facilities, transportation
and social profiles.

🌐 **Official Website:**  
{OFFICIAL_WEBSITE}
"""

    # ========================================================
    # TIMINGS
    # ========================================================

    if any(x in q for x in [
        "timing",
        "timings",
        "college time",
        "college timing",
        "when college",
        "start time",
        "end time",
        "college starts",
        "college ends"
    ]):

        return """
### 🕘 College Timings

**First Year**

🟢 **9:15 AM – 4:30 PM**

**Second Year to Final Year**

🟢 **9:30 AM – 4:45 PM**

If you need the break timings, ask:

**Break , lunch period, interval?**
"""

    

    # ========================================================
    # BREAKS
    # ========================================================

    if any(x in q for x in [
        "break",
        "lunch timings"
        "break time",
        "break timings",
        "lunch",
        "lunch time",
        "interval",
        "lunch period"
    ]):

        return """
### ☕ Break Timings

#### First Year

• Morning: **10:45 – 11:00 AM**  
• Lunch: **12:30 – 1:15 PM**  
• Afternoon: **2:45 – 3:00 PM**

#### Other Years

• Morning: **11:00 – 11:15 AM**  
• Lunch: **12:45 – 1:30 PM**  
• Afternoon: **3:00 – 3:15 PM**
"""

        # ========================================================
    # COURSES / PROGRAMMES
    # ========================================================

    if any(x in q for x in [
        "courses",
        "course",
        "program",
        "programs",
        "programme",
        "programmes",
        "what courses",
        "what course",
        "what can i study",
        "available courses",
        "courses offered",
        "programs offered",
        "programmes offered",
        "what programs",
        "what programmes"
    ]):

        return """
### 🎓 Courses Offered

CCET offers programmes in **Engineering and Management**.

### 🕵 Undergraduate Programmes – B.Tech

• **Computer Science & Engineering (CSE)**  
• **Information Technology (IT)**  
• **Electronics & Communication Engineering (ECE)**  
• **Electrical & Electronics Engineering (EEE)**  
• **Mechanical Engineering**  
• **Civil Engineering**  
• **Artificial Intelligence & Data Science (AI & DS)**  
• **Robotics & Automation**  
• **Internet of Things (IoT)**  
• **Cyber Security & Blockchain**

### 👨🏻‍🎓 Postgraduate Programmes

• **MBA – Master of Business Administration**  
• **MCA – Master of Computer Applications**

📌 Programme availability, approvals, eligibility and
admission details can change.

For the latest official information, please refer to:

🌐 **CCET Official Website**

https://christcet.edu.in/
"""


        # ========================================================
    # OFFICIAL DATA — INTAKE / SEATS
    # ========================================================

    if any(x in q for x in [
        "intake",
        "seat intake",
        "total intake",
        "number of seats",
        "how many seats",
        "available seats",
        "seats available",
        "btech intake",
        "b tech intake",
        "mba intake",
        "mca intake",
        "sanctioned intake",
        "college intake"
    ]):

        return """
### 🎓 Sanctioned Intake

According to the official CCET information:

### 🔹 B.Tech

**720 seats**

### 🔹 MBA

**180 seats**

### 🔹 MCA

**120 seats**

📌 Intake may be subject to changes based on official
approvals and academic-year requirements.

For the latest information, please refer to:

🌐 **CCET Official Website**

https://christcet.edu.in/
"""
        
        # ========================================================
    # OFFICIAL DATA — ADMISSION
    # ========================================================

    if any(x in q for x in [
        "admission",
        "admissions",
        "eligibility",
        "eligibility criteria",
        "how to join",
        "how can i join",
        "admission process",
        "admission procedure",
        "how to get admission",
        "how to apply",
        "application process",
        "btech admission",
        "b tech admission",
        "mba admission",
        "mca admission",
        "lateral entry",
        "btech lateral entry",
        "courses admission"
    ]):

        return """
### 🎓 Admission Information

CCET provides admission information for programmes including:

• **B.Tech**
• **B.Tech Lateral Entry**
• **MBA**
• **MCA**

### 📋 B.Tech Eligibility

For direct B.Tech admission, candidates require **10+2**
with **Physics and Mathematics as compulsory subjects** along
with **Chemistry, Biotechnology or Biology**.

### 🎓 MBA & MCA

MBA and MCA have separate eligibility requirements.

### 📝 Admission Process

The admission process, eligibility criteria, application
dates, fees and required documents may change from time
to time.

For the latest and official admission information,
please refer to:

🌐 **CCET Official Website**

https://christcet.edu.in/
"""

    # ========================================================
    # OFFICIAL DATA — PLACEMENTS
    # ========================================================

    if any(x in q for x in [
        "placement",
        "placements",
        "placement details",
        "placement information",
        "campus placement",
        "campus placements",
        "placement companies",
        "companies for placement",
        "recruiters","campus"
        "recruiting companies",
        "which companies recruit",
        "companies visiting",
        "job placement",
        "jobs","job",
        "placement cell",
        "Campus information"
    ]) and not any(x in q for x in [
        "thiagarajan",
        "placement coordinator",
        "placement incharge",
        "placement in charge",
        "training and placement officer",
        "tpo"
    ]):

        return """
### 💼 CCET Placements

CCET has a dedicated **Training and Placement Cell**.

According to the official college information, CCET
highlights:

📊 **500+ placements per year**

### 🏢 Our Recruiters

The T&P Cell has successfully organised recruitment drives
for **40+ IT and core companies**, including:

• **TCS**  
• **Infosys**  
• **Wipro**  
• **HCL**  
• **Amazon**  
• **Cognizant**  
• **Capgemini**  
• **Mindtree**  
• **Atos Syntel**  
• **Mphasis**  
• **CSS Corp**  
• **Integra**  
• **Ava Soft**  
• **Sutherland**  
• **Byju's**  
• **Rapid Data Technologies**  
• **Shiash Info Solutions**  
• **Paragon Digital Services**  
• **ABC Bearings**  
• **Renault Nissan**  
• **Madras Engineering Works**  
• **Royal Enfield**  
• **Perfect Gears**  

Recruiters and placement figures can change over time.

For the latest placement information, please refer to:

🌐 **CCET Official Website**

https://christcet.edu.in/
"""
        # ========================================================
    # OFFICIAL DATA — ABOUT CCET
    # ========================================================

    if any(x in q.lower() for x in [
        "about ccet",
        "about college",
        "tell me about ccet",
        "tell me about college",
        "what is ccet",
        "what is christ college",
        "when was ccet established",
        "when was college established",
        "ccet history",
        "college history",
        "history of ccet",
        "about christ college"
        "christ college"
    ]):

        return """
### 🏫 About CCET

**Christ College of Engineering and Technology (CCET)** is
located in **Moolakulam, Puducherry**.

The institution was established in **2007** and is a unit of
**Sam Paul Educational Trust**.

### 🏛️ Institution Details

• **Established:** 2007  
• **Location:** Moolakulam, Puducherry  
• **Trust:** Sam Paul Educational Trust  
• **Approval:** AICTE  
• **Affiliation:** Pondicherry University  
• **Accreditation:** NAAC

For the latest official information, please refer to:

🌐 **CCET Official Website**

https://christcet.edu.in/
"""

        # ========================================================
    # OFFICIAL DATA — PRINCIPAL
    # ========================================================

    if any(x in q for x in [
        "principal",
        "who is principal",
        "who is the principal",
        "college principal",
        "ccet principal",
        "principal name",
        "name of principal",
        "current principal",
        "principal of christ college of engineering and technology"
    ]):

        return """
### 👨‍🏫 Principal

The Principal of **Christ College of Engineering and Technology
(CCET)** is:

### **Dr. A. Siva Kumar**

For the latest official information, please refer to:

🌐 **CCET Official Website**

https://christcet.edu.in/
"""

    # ========================================================
    # OFFICIAL DATA — ECE HOD
    # ========================================================

    if any(x in q for x in [
        "ece hod",
        "who is ece hod",
        "who is the ece hod",
        "hod of ece",
        "who is hod of ece",
        "head of ece",
        "head of ece department",
        "ece hod name",
        "name of ece hod",
        "anandalatchoumy",
        "dr s anandalatchoumy",
        "anandalatchoumy",
        "dr anandalatchoumy",
        "dr s anandalatchoumy",
    ]):

        return """
### 👩‍🏫 Dr. S. Anandalatchoumy

**Head of the Electronics and Communication Engineering
(ECE) Department**

### 🎓 Qualifications

• **Ph.D.** (Doctorate)
• **B.Tech. in ECE** (Undergraduate)
• **M.Tech. in ECE** (Postgraduate)
"""

    # ========================================================
    # OFFICIAL DATA — DR. Y. THIAGARAJAN
    # ========================================================

    if any(x in q for x in [
        "hod of eee",
        "who is eee hod",
        "who is the eee hod",
        "thiagarajan",
        "dr thiagarajan",
        "dr y thiagarajan",
        "y thiagarajan",
        "thiagarajan yogamoorthi",
        "dr thiagarajan yogamoorthi",
        "thiagarajan sir",
        "about thiagarajan",
        "about dr thiagarajan",
        "who is thiagarajan",
        "who is dr thiagarajan",
        "who is eee hod",
        "who is hod of eee",
        "who is the eee hod",
        "eee hod name",
        "name of eee hod",
        "head of eee department",
        "eee department hod",
        "placement coordinator",
        "who is the placement coordinator",
        "who is placement coordinator",
        "training and placement coordinator",
        "placement incharge",
        "placement in charge",
        "thiagarajan placement",
    "placement thiagarajan",
    "thiagarajan placement coordinator",
    "is thiagarajan coordinator",
    "is thiagarajan placement incharge",
    "thiagarajan placement in charge",
    "thiagarajan training placement",
    "thiagarajan tpo",
    "thiagarajan t and p",
        "thiagarajan profiles",
    "thiagarajan profile links",
    "thiagarajan professional profiles",
    "thiagarajan research profiles",
    "all thiagarajan profiles",
    "all links of thiagarajan",
    "thiagarajan all links",
    "give me thiagarajan links",
    "thiagarajan online profile",
    "thiagarajan academic profile",
    "thiagarajan research profile"
        
    ]):

        return """
### 👨‍🏫 Dr. Y. Thiagarajan Yogamoorthi

Dr. **Y. Thiagarajan Yogamoorthi** is a senior academic
and research professional associated with
**Christ College of Engineering and Technology (CCET),
Puducherry**.

### ⚡ Department

**Electrical and Electronics Engineering (EEE)**

### 🎓 Academic Role

**Professor / HOD – EEE & Placement Coordinator**

He is also associated with **Research & Development (R&D)**
activities at CCET.

### 🏛️ Institutional Responsibilities

His institutional roles and activities include:

• Head of the EEE Department  
• Training and Placement Coordinator  
• IQAC Coordinator  
• IIC / Innovation Council activities  
• Research & Development activities  
• Student innovation and technical activities

### 🔬 Research Areas

His major areas of research interest include:

• Renewable Energy  
• Fuel Cells    
• PEM Fuel Cells 
• Power Converters    
• Energy Conservation

### 🎓 Educational Background

• Undergraduate Degree in Electrical Engineering — 2006  
• M.E. in Power Electronics & Drives — 2008  
• Ph.D. in Fuel Cell research — 2015–2019  

### 📚 Research & Publications

He has published research work in reputed journals,
conference proceedings and technical publications.

His professional research activities include
reviewing and editorial activities for technical journals.

### 🌱 Professional Interests

His professional interests include renewable-energy
technologies, fuel-cell systems, power electronics,
energy conservation and innovation.

### 💼 Placement & Student Development

He is also associated with student career-development
and placement-related activities at CCET.

### 🏆 Recent Academic Activity

He has been involved in EEE departmental technical
activities including **Christ Tech 2K26**, a national-level
technical symposium conducted with the theme:

**"Industry 5.0"**

### 🔗 Professional Profile



ℹ️in **LinkedIn:** https://www.linkedin.com/in/dr-thiagarajany

🔬 **AIEYS**
https://aieys.com/people/Dr.Y.Thiagarajan.html

🔬 **IASTEM**
https://iastem.org/memdetail.php?id=208

### 📚 IEEE Xplore Author Profile

https://ieeexplore.ieee.org/author/38190356900

The IEEE Xplore link can be used to refer to his
IEEE research/publication profile.

"""
        # ========================================================
    # OFFICIAL DATA — PLACEMENT FACILITIES
    # ========================================================

    if any(x in q for x in [
        "placement facilities",
        "placement cell facilities",
        "training placement facilities",
        "placement infrastructure",
        "placement rooms",
        "interview cabins",
        "group discussion rooms",
        "placement seminar hall",
        "placement auditorium",
        "placement centre",
        "placement center"
    ]):

        return """
### 💼 Training & Placement Facilities

The CCET Training and Placement Cell has:

• **2 Seminar Halls**  
• **1 Auditorium**  
• **Interview Cabins**  
• **Group Discussion Rooms**  
• **Computer Centres**  

These facilities support training, interviews,
group discussions and recruitment activities.
"""
        
    # ========================================================
    # ADMISSION BLOCK
    # ========================================================

    if any(x in q for x in [
        "admission block",
        "admission office",
        "principal",
        "principal office",
        "manager office",
        "director office",
        "exam cell location",
        "examination cell"
    ]):

        return """
### 🏢 Admission Block

The Admission Block contains:

• Admission Office  
• Principal's Office  
• Manager's Office  
• Director's Office  
• Examination Cell
"""

    # ========================================================
    # MAIN BLOCK
    # ========================================================

    if any(x in q for x in [
        "main block",
        "ece department",
        "ece",
        "cse department",
        "cse",
        "it department",
        "it department",
        "aids department",
        "aids",
        "blockchain",
        "blockchain department",
        "library"
    ]):

        return """
### 🏢 Main Block

The Main Block has **4 floors**.

**Ground Floor**

• S&H

**First Floor**

• Library
• Laboratories
• Restrooms
• Staff/PT facilities

**Second Floor**

• ECE

**Third Floor**

• CSE
• IT

**Fourth Floor**

• AIDS
• Blockchain
• Seminar Hall
"""

    # ========================================================
    # LIBRARY
    # ========================================================

    if any(x in q for x in [
        "library",
        "book",
        "books",
        "where library"
    ]):

        return """
### 📚 Library

The library is located on the **First Floor of the Main Block**.

The First Floor also contains laboratories,
restrooms and PT/staff facilities.
"""

    # ========================================================
    # MECHANICAL
    # ========================================================

    if any(x in q for x in [
        "mechanical",
        "mechanical block",
        "mechanical department"
    ]):

        return """
### ⚙️ Mechanical Block

The Mechanical Block has **4 floors**.

It contains:

• Classrooms  
• Laboratories  
• Restrooms  

🛵 Boys' bike parking is located near the
Mechanical Block.
"""

    # ========================================================
    # MBA
    # ========================================================

    if any(x in q for x in [
        "mba",
        "mba block"
    ]):

        return """
### 🎓 MBA Block

The MBA Block has **3 floors**.

Nearby facilities include:

🏃 Playground  
🏫 CCET Arts and Science College  
🍽️ Canteen  
🏋️ SLAM Gym  
🎤 Auditorium
"""

    # ========================================================
    # PARKING
    # ========================================================

    if any(x in q for x in [
        "parking",
        "bike parking",
        "car parking",
        "bike",
        "vehicle parking"
    ]):

        return """
### 🅿️ Parking Information

🏍️ **Boys' Bike Parking**

Near the Mechanical Block.

🛵 **Girls' Bike Parking**

Behind the Main Block.

🚗 **Car Parking**

Car parking is not available.
"""

    # ========================================================
    # TRANSPORT
    # ========================================================

    if any(x in q for x in [
        "bus",
        "buses",
        "transport",
        "transportation",
        "college bus"
    ]):

        return """
### 🚌 Transportation

CCET has **6+ college buses**
for student transportation.

For current bus routes and timings,
please refer to the official college website
or college announcements.
"""

    # ========================================================
    # HOSTEL
    # ========================================================

    if any(x in q for x in [
        "hostel",
        "stay",
        "accommodation",
        "room",
        "hostel facility"
    ]):

        return """
### 🏠 Hostel

CCET currently does **not have a college hostel**.

If you need updated accommodation information,
please refer to the official CCET website:

https://christcet.edu.in/
"""

    # ========================================================
    # CANTEEN
    # ========================================================

    if any(x in q for x in [
        "canteen",
        "food",
        "sambar",
        "noodles",
        "eat",
        "food price",
        "canteen price"
    ]):

        return """
### 🍽️ Canteen

The canteen is located near the **MBA Block**.

### Example Prices

🥣 **Sambar:** ₹45

🍜 **Chicken Noodles:** ₹90

Prices may change, so check with the college
for the latest prices.
"""

    # ========================================================
    # GYM
    # ========================================================

    if any(x in q for x in [
        "gym",
        "fitness",
        "slam"
    ]):

        return """
### 🏋️ SLAM Gym

The **SLAM Gym** is located near the MBA Block.
"""

    # ========================================================
    # AUDITORIUM
    # ========================================================

    if any(x in q for x in [
        "auditorium",
        "function hall",
        "events hall",
        "event hall"
    ]):

        return """
### 🎤 Auditorium

The auditorium is located near the MBA Block.
"""

    # ========================================================
    # EXAMS
    # ========================================================

    if any(x in q for x in [
        "exam",
        "examination",
        "periodic",
        "semester",
        "model exam",
        "model examination",
        "two mark",
        "2 mark",
        "2 mark exam"
    ]):

        return """
### 📝 Examination Pattern

CCET conducts:

• **2 Periodic Examinations**
• **2-Mark Examination**
• **Model Examination**
• **Semester Examination**

⏱️ **2-Mark Examination:** 1.5 hours

⏱️ **Model Examination:** 3 hours

For current examination schedules,
refer to official college announcements.
"""

    # ========================================================
    # COMMUNICATION
    # ========================================================

    if any(x in q for x in [
        "whatsapp",
        "communication",
        "announcement",
        "notice",
        "updates",
        "college updates"
    ]):

        return """
### 📢 College Communication

**WhatsApp** is one of the primary communication
channels used for college announcements and updates.

For the latest official announcements,
please check the college website and official
college communication channels.
"""

    # ========================================================
    # DEPARTMENT LIST
    # ========================================================

    if any(x in q.lower() for x in [
        "departments",
        "department",
        "department list",
        "what departments",
        "which departments",
        "available departments",
        "dept",
        "groups",
        "group",
        "courses"
    ]):

        return """
### 🏫 CCET Departments

1. **ECE** – Electronics and Communication Engineering
2. **CSE** – Computer Science and Engineering
3. **IT** – Information Technology
4. **AIDS** – Artificial Intelligence and Data Science
5. **Blockchain Technology**
6. **EEE** – Electrical and Electronics Engineering
7. **Mechanical Engineering**
8. **MBA** – Master of Business Administration
9. **S&H** – Science and Humanities
"""

    # ========================================================
    # DRESS
    # ========================================================

    if any(x in q for x in [
        "shoe",
        "shoes",
        "dress",
        "dress code",
        "footwear",
        "formal shoe",
        "formal shoes",
        "what shoes",
        "shoe colour",
        "shoe color",
        "shoe colours",
        "shoe colors"
    ]):

        return """
### 👔 Dress & Footwear

👟 **All shoes are allowed.**

For formal activities and professional situations,
**formal shoes are recommended**.

If you are a fresher and want to make a safe choice,
formal shoes are generally a good option.
"""

    # ========================================================
    # ANTI-RAGGING
    # ========================================================

    if any(x in q for x in [
        "ragging",
        "anti ragging",
        "anti-ragging",
        "anti ragging act",
        "ragging rules",
        "ragging punishment",
        "punishment for ragging",
        "what counts as ragging",
        "activities amounting to ragging",
        "ugc ragging regulations"
    ]):

        return """
### 🛡️ Anti-Ragging at CCET

Under the **UGC Regulations on Curbing the Menace of Ragging
in Higher Educational Institutions, 2009**, the Anti-Ragging
Committee works to prohibit, prevent and eliminate ragging
and support a safe academic environment.

### Conduct That May Amount to Ragging

Ragging includes conduct that:

• Teases, treats or handles a fresher or another student rudely.
• Causes or is likely to cause annoyance, hardship, physical
    or psychological harm, fear or apprehension.
• Pressures a student to do something they would not ordinarily
    do, causing shame, embarrassment or harm to their well-being.
• Disrupts or disturbs a student's regular academic activities.
• Exploits a student to complete another person's academic work.
• Imposes financial extortion or forceful expenditure.
• Involves physical or sexual abuse, bodily harm or endangering
    a student's health.
• Uses verbal or written abuse, including emails, posts or
    public humiliation.
• Harms a student's mental health or self-confidence, including
    through misuse of power, authority or superiority.

### Possible Administrative Action

After the prescribed procedure, and depending on the facts
and severity, one or more of these penalties may apply:

1. Suspension from classes and academic privileges.
2. Withholding or withdrawal of scholarships, fellowships
     or other benefits.
3. Debarring from tests, examinations or evaluations.
4. Withholding examination results.
5. Debarring from representing the institution at meets,
     tournaments or youth festivals.
6. Suspension or expulsion from the hostel.
7. Cancellation of admission.
8. Rustication for one to four semesters.
9. Expulsion and possible debarment from admission to another
     institution for a specified period.

If individuals responsible for or abetting ragging cannot be
identified, the institution may impose collective punishment
as permitted under the applicable regulations.

For a specific incident, contact the college's Anti-Ragging
Committee or follow the official reporting procedure.
"""

    # ========================================================
    # DISCIPLINE
    # ========================================================

    if any(x in q for x in [
        "discipline",
        "rules",
        "college rules",
        "student rules",
        "disciplinary",
        "behavior",
        "behaviour"
    ]):

        return """
### 📚 Discipline

Students are expected to maintain proper discipline
and professional behaviour on campus.

For the complete and current disciplinary rules,
please refer to the official CCET website or
college regulations.

🌐 https://christcet.edu.in/
"""

    # ========================================================
    # LOCATION
    # ========================================================

    if any(x in q for x in [
        "track me",
        "navigate to college",
        "directions to college",
        "route to college",
        "how to reach college",
        "get me to college",
        "track to college"
    ]):

        return """
### 🧭 Directions to CCET

Open the route in Google Maps. If prompted, allow Maps to use
your current location to get directions to the college.

[Get directions to college](https://www.google.com/maps/dir/?api=1&destination=Christ+College+of+Engineering+and+Technology%2C+Paris+Nagar%2C+Moolakulam%2C+Puducherry&travelmode=driving)

This chatbot does not access or store your location.
"""

    if any(x in q for x in [
        "where is college",
        "location",
        "address",
        "college",
        "where is ccet",
        "where is christ college",
        "college address",
        "college location",
        "clg",
        "clg address",
        "clg location",
        "where located",
        "college location"
    ]):

        return """
### 📍 College Location

**Christ College of Engineering and Technology**

Paris Nagar, Moolakulam, Puducherry.  

[Get directions to college](https://www.google.com/maps/dir/?api=1&destination=Christ+College+of+Engineering+and+Technology%2C+Paris+Nagar%2C+Moolakulam%2C+Puducherry&travelmode=driving)


The college is affiliated with Pondicherry University.
"""

    # ========================================================
    # CONTACT / PROFILE
    # ========================================================

    if any(x in q for x in [
        "contact",
        "contact details",
        "phone",
        "email",
        "mail",
        "reach college"
    ]):

        return f"""
### 📞 Contact & Official Information

For current contact details, please refer to
the official CCET website:

🌐 **{OFFICIAL_WEBSITE}**

You can also ask:

**"Give me CCET social media profiles"**

to get the available social links.
"""

    # ========================================================
    # HELP
    # ========================================================

    if any(x in q for x in [
        "help",
        "what can you do",
        "features",
        "how can you help"
    ]):

        return """
### 🤖 What I Can Answer

Try asking:

🏫 "Tell me about CCET"

🕘 "What are the college timings?"

☕ "What are the lunch timings?"

🏢 "Where is the ECE department?"

📚 "Where is the library?"

🏫 "What departments are available?"

📝 "What is the exam pattern?"

🚌 "How many buses are there?"

🅿️ "Where is bike parking?"

🏠 "Is there a hostel?"

🍽️ "Where is the canteen?"

👔 "What is the dress code?"

👟 "Are all shoes allowed?"

📱 "Give me CCET Instagram and Facebook"

🌐 "What is the official CCET website?"
"""

    # ========================================================
    # SMART FALLBACK
    # ========================================================

    fallback_responses = [

          f"""
### 🤔 I'm not sure about that

I couldn't find a reliable answer to that question
in my current CCET knowledge base.

I don't want to guess and give you incorrect information.

However, I can help you with related topics:

🏫 **College information**  
🏢 **Departments & blocks**  
🕘 **Timings & breaks**  
📝 **Examinations**  
🚌 **Transportation**  
🅿️ **Parking**  
🍽️ **Canteen**  
🏠 **Hostel**  
👔 **Dress & footwear**  
📢 **Communication**  
📱 **Social media profiles**

🌐 For information I don't currently have,
please refer to the official CCET website:

**{OFFICIAL_WEBSITE}**

💡 You can also rephrase your question and
I'll try to find a related answer.
""",
        f"""
### 🤔 I don't have that information yet

I couldn't find a reliable answer to that question
in my current CCET knowledge base.

I don't want to guess and give you incorrect information.

However, I can help you with related topics:

🏫 **College information**  
🏢 **Departments & blocks**  
🕘 **Timings & breaks**  
📝 **Examinations**  
🚌 **Transportation**  
🅿️ **Parking**  
🍽️ **Canteen**  
🏠 **Hostel**  
👔 **Dress & footwear**  
📢 **Communication**  
📱 **Social media profiles**

🌐 For information I don't currently have,
please refer to the official CCET website:

**{OFFICIAL_WEBSITE}**

💡 You can also rephrase your question and
I'll try to find a related answer.
""",

        f"""
### 🔎 I couldn't find an exact answer

That information isn't currently available
in my CCET knowledge base.

Instead of guessing, I'd recommend checking
the official source:

🌐 **CCET Official Website**

{OFFICIAL_WEBSITE}

I can still help you with:

• College timings
• Departments
• Campus blocks
• Exams
• Canteen
• Transport
• Parking
• Hostel
• Dress & footwear
• College social profiles

💬 Try asking a related question and I'll
do my best to guide you.
""",

        f"""
### 🧠 I don't have enough information for that

I don't want to provide a made-up answer.

My current knowledge covers common CCET
student questions such as:

🏫 Campus information  
🏢 Departments  
🕘 College timings  
☕ Break timings  
📝 Exams  
🚌 Transport  
🅿️ Parking  
🍽️ Canteen  
🏠 Hostel  
👔 Dress code  
📱 Social profiles

For the most accurate and latest information,
please refer to:

🌐 **Official CCET Website**

{OFFICIAL_WEBSITE}

If you ask me something related to the above topics,
I can probably help.
""",

        f"""
### 💡 Let me guide you another way

I don't currently have a reliable answer
for that specific question.

Rather than giving you incorrect information,
I recommend checking the official CCET source:

🌐 {OFFICIAL_WEBSITE}

You can also ask me about:

**Campus • Departments • Timings • Exams •
Transport • Parking • Canteen • Hostel •
Dress • Social Media**

📱 For example:

**"Give me all CCET social media links"**

or

**"Where is the CSE department?"**
"""
    ]

    return random.choice(fallback_responses)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎓 CCET Assistant")

    st.markdown(
        '<span class="status">● System Online</span>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ========================================================
    # QUICK QUESTIONS
    # ========================================================

    st.markdown("### ⚡ Quick Questions")

    quick_questions = [
        "What are the college timings?",
        "Where is the ECE department?",
        "Where is the library?",
        "College location",
        "Is there a hostel?",
        "Where is the canteen?",
        "What is the exam pattern?",
        "Where is bike parking?",
        "What is the dress code?",
        "Give me CCET social media profiles",
        "Which companies recruit at CCET?"
    ]

    for index, question in enumerate(quick_questions):

        if st.button(
            question,
            key=f"quick_{index}"
        ):

            if "messages" not in st.session_state:
                st.session_state.messages = []

            st.session_state.messages.append({
                "role": "user",
                "content": question
            })

            answer = get_response(question)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            st.rerun()

    # ========================================================
    # SOCIAL LINKS
    # ========================================================

    st.markdown("---")

    st.markdown("### 📱 Social Connect")

    st.markdown(
        f"""
        <div class="social-box">
        📸 <b>Instagram</b><br>
        <a href="{SOCIAL_PROFILES["Instagram"]}" target="_blank">
        @ccetinsta
        </a>
        </div>

        <div class="social-box">
        📘 <b>Facebook</b><br>
        <a href="{SOCIAL_PROFILES["Facebook"]}" target="_blank">
        Christ College of Engineering and Technology
        </a>
        </div>

        <div class="social-box">
        💼 <b>LinkedIn</b><br>
        <a href="{SOCIAL_PROFILES["LinkedIn"]}" target="_blank">
        CCET LinkedIn
        </a>
        </div>

        <div class="social-box">
        🌐 <b>Official Website</b><br>
        <a href="{OFFICIAL_WEBSITE}" target="_blank">
        christcet.edu.in
        </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # SYSTEM
    # ========================================================

    st.markdown("---")

    st.markdown("### 🧠 System")

    st.caption("Rule-Based NLP")
    st.caption("Smart Intent Detection")
    st.caption("Natural Fallback Responses")
    st.caption("No LLM")
    st.caption("No API")
    st.caption("Python + Streamlit")

    st.markdown("---")

    st.caption("Built with ❤️ by Mohamed Imraan")

    if st.button(
        "🗑️ Clear Conversation",
        key="clear_chat"
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# MAIN HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🎓 CCET College Assistant
</div>

<div class="hero-subtitle">
Your intelligent college information assistant —
designed for CCET students, freshers and visitors.
</div>

<br>

<span class="status">
● System Online
</span>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INITIAL MESSAGE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content": """
### 👋 Welcome to CCET College Assistant!

I'm your **College Information Assistant**.

I can help you quickly find information about:

🏫 **College**  
🏢 **Departments & Blocks**  
🕘 **Timings**  
📝 **Examinations**  
🍽️ **Canteen**  
🚌 **Transportation**  
🅿️ **Parking**  
🏠 **Hostel**  
👔 **Dress & Footwear**  
📢 **Communication**  
📱 **Social Media Profiles**

### 💬 Try asking:

**"What are the college timings?"**

**"Where is the ECE department?"**

**"Are all shoes allowed?"**

**"Give me CCET social media profiles"**

**"What is the official website?"**

Ask me anything about CCET!
"""
        }

    ]


# ============================================================
# FEATURE CARDS
# ============================================================

def render_feature_card(icon, title, text):
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if len(st.session_state.messages) == 1:

    cols = st.columns(4)

    cards = [
        (
            "🏢",
            "Campus",
            "Blocks & departments"
        ),

        (
            "🕘",
            "Timings",
            "College & break timings"
        ),

        (
            "📝",
            "Exams",
            "Exam information"
        ),

        (
            "📱",
            "Connect",
            "Website & social profiles"
        )
    ]

    for col, (icon, title, text) in zip(
        cols,
        cards
    ):

        with col:
            render_feature_card(icon, title, text)


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    avatar = (
        "🧑‍🎓"
        if message["role"] == "user"
        else "🎓"
    )

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(
            message["content"],
            unsafe_allow_html=True
        )


# ============================================================
# CHAT INPUT
# ============================================================

prompt = st.chat_input(
    "Ask about college information..."
)


if prompt:

    # ========================================================
    # USER MESSAGE
    # ========================================================

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message(
        "user",
        avatar="🧑‍🎓"
    ):

        st.markdown(prompt)

    # ========================================================
    # BOT RESPONSE
    # ========================================================

    response = get_response(prompt)

    with st.chat_message(
        "assistant",
        avatar="🎓"
    ):

        message_placeholder = st.empty()

        words = response.split(" ")

        generated = ""

        for word in words:

            generated += word + " "

            message_placeholder.markdown(
                generated,
                unsafe_allow_html=True
            )

            time.sleep(0.008)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
    <div class="footer">

    🎓 CCET College Assistant
    • Smart Rule-Based Chatbot
    • Python + Streamlit

    <br><br>

    🌐 Official Website:
    <a href="{OFFICIAL_WEBSITE}" target="_blank">
    christcet.edu.in
    </a>

    <br><br>

    Developed by Mohamed Imraan

    </div>
    """,
    unsafe_allow_html=True
)