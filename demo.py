import streamlit as st
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NEXORA | Innovation & Incubation Centre",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# WEBSITE DATA
# ============================================================

EVENTS = [
    {
        "time": "09:30 AM",
        "title": "Startup Mentoring Hour",
        "place": "Mentoring Room",
        "type": "MENTORING"
    },
    {
        "time": "11:00 AM",
        "title": "Design Thinking Workshop",
        "place": "Innovation Lab",
        "type": "WORKSHOP"
    },
    {
        "time": "02:30 PM",
        "title": "Career Connect Session",
        "place": "Seminar Hall",
        "type": "CAREER"
    },
    {
        "time": "04:30 PM",
        "title": "Founder Networking Meet",
        "place": "Collaboration Lounge",
        "type": "NETWORKING"
    }
]

PROGRAMS = [
    {
        "icon": "🚀",
        "title": "Startup Launchpad",
        "text": "A guided journey for students who want to transform an idea into a practical startup concept.",
        "tag": "ENTREPRENEURSHIP"
    },
    {
        "icon": "🎯",
        "title": "Career Accelerator",
        "text": "Industry-focused sessions that help students improve technical, communication and professional skills.",
        "tag": "CAREER"
    },
    {
        "icon": "🧪",
        "title": "Prototype Studio",
        "text": "A collaborative space where innovators can experiment, build prototypes and test their solutions.",
        "tag": "INCUBATION"
    }
]

BLOGS = [
    {
        "category": "STARTUP",
        "title": "How a Student Idea Becomes a Startup",
        "text": "A simple journey from identifying a problem to validating an idea and developing a first prototype."
    },
    {
        "category": "CAREER",
        "title": "5 Skills Every Young Professional Needs",
        "text": "Explore communication, problem solving, teamwork, digital skills and adaptability."
    },
    {
        "category": "INNOVATION",
        "title": "Why Innovation Starts With Problems",
        "text": "Great solutions often begin by understanding real problems faced by people and communities."
    }
]

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f6f8fc;
}

.block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* =========================================================
TOP HEADER
========================================================= */

.topbar {
    background: #ffffff;
    border-bottom: 1px solid #e8edf5;
    padding: 18px 28px;
    border-radius: 0 0 18px 18px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 22px;

    box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
}

.logo {
    font-size: 25px;
    font-weight: 800;
    color: #14213d;
}

.logo span {
    color: #2563eb;
}

.logo-small {
    font-size: 11px;
    color: #64748b;
    margin-top: 3px;
}

.status {
    background: #ecfdf5;
    color: #047857;
    padding: 8px 14px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
}

/* =========================================================
HERO
========================================================= */

.hero {
    min-height: 430px;

    border-radius: 28px;

    padding: 55px;

    background:
        linear-gradient(
            120deg,
            #0f172a 0%,
            #172554 45%,
            #2563eb 100%
        );

    color: white;

    position: relative;

    overflow: hidden;

    margin-bottom: 28px;

    box-shadow: 0 20px 50px rgba(30, 64, 175, 0.20);
}

.hero::before {
    content: "";

    position: absolute;

    width: 380px;
    height: 380px;

    right: -130px;
    top: -170px;

    background: rgba(96, 165, 250, 0.18);

    border-radius: 50%;
}

.hero::after {
    content: "";

    position: absolute;

    width: 200px;
    height: 200px;

    right: 170px;
    bottom: -120px;

    background: rgba(129, 140, 248, 0.15);

    border-radius: 50%;
}

.hero-content {
    max-width: 720px;
    position: relative;
    z-index: 2;
}

.hero-badge {
    display: inline-block;

    background: rgba(255,255,255,0.12);

    border: 1px solid rgba(255,255,255,0.18);

    padding: 8px 14px;

    border-radius: 30px;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1px;

    margin-bottom: 18px;
}

.hero h1 {
    font-size: 46px;

    line-height: 1.12;

    margin: 0;

    font-weight: 800;
}

.hero h1 span {
    color: #60a5fa;
}

.hero p {
    color: #dbeafe;

    line-height: 1.8;

    font-size: 15px;

    max-width: 680px;

    margin-top: 18px;
}

.hero-points {
    margin-top: 25px;

    color: #e0e7ff;

    font-size: 12px;
}

.hero-points span {
    margin-right: 22px;
}

/* =========================================================
SECTION
========================================================= */

.section {
    margin-top: 32px;
    margin-bottom: 18px;
}

.eyebrow {
    color: #2563eb;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 1.7px;

    text-transform: uppercase;
}

.section h2 {
    color: #111827;

    font-size: 28px;

    font-weight: 800;

    margin: 5px 0;
}

.section p {
    color: #64748b;

    font-size: 13px;

    max-width: 800px;
}

/* =========================================================
DAILY EVENTS
========================================================= */

.daily {
    background: #111827;

    border-radius: 22px;

    padding: 27px;

    color: white;

    margin-top: 12px;

    box-shadow: 0 15px 35px rgba(15, 23, 42, 0.15);
}

.daily-title {
    font-size: 21px;
    font-weight: 800;
}

.daily-subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 5px;
    margin-bottom: 20px;
}

.event {
    background: #1f2937;

    border: 1px solid #374151;

    border-radius: 15px;

    padding: 16px;

    min-height: 125px;
}

.event-time {
    color: #60a5fa;

    font-size: 11px;

    font-weight: 800;
}

.event-title {
    font-size: 13px;

    font-weight: 700;

    margin-top: 7px;
}

.event-place {
    color: #94a3b8;

    font-size: 10px;

    margin-top: 7px;
}

/* =========================================================
FEATURE CARDS
========================================================= */

.feature {
    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 20px;

    padding: 25px;

    min-height: 245px;

    transition: 0.25s;

    box-shadow: 0 7px 25px rgba(15,23,42,0.04);
}

.feature:hover {
    transform: translateY(-5px);

    box-shadow: 0 16px 38px rgba(37,99,235,0.12);
}

.feature-icon {
    width: 54px;
    height: 54px;

    background: #eff6ff;

    border-radius: 15px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 24px;

    margin-bottom: 16px;
}

.feature h3 {
    color: #111827;

    font-size: 17px;

    margin-bottom: 9px;
}

.feature p {
    color: #64748b;

    font-size: 12px;

    line-height: 1.8;
}

.tag {
    display: inline-block;

    background: #eff6ff;

    color: #2563eb;

    padding: 5px 9px;

    border-radius: 20px;

    font-size: 9px;

    font-weight: 800;

    margin-top: 10px;
}

/* =========================================================
INFO PANEL
========================================================= */

.info-panel {
    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 20px;

    padding: 28px;

    box-shadow: 0 6px 25px rgba(15,23,42,0.04);
}

.info-panel h3 {
    color: #111827;

    font-size: 19px;
}

.info-panel p {
    color: #64748b;

    font-size: 12px;

    line-height: 1.9;
}

.check {
    color: #2563eb;

    font-size: 12px;

    margin: 9px 0;
}

/* =========================================================
STATS
========================================================= */

.stat {
    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 17px;

    text-align: center;

    padding: 22px;
}

.number {
    color: #2563eb;

    font-size: 29px;

    font-weight: 800;
}

.stat-label {
    color: #64748b;

    font-size: 10px;

    margin-top: 3px;
}

/* =========================================================
BLOG
========================================================= */

.blog {
    background: white;

    border: 1px solid #e5eaf2;

    border-radius: 18px;

    overflow: hidden;

    box-shadow: 0 7px 25px rgba(15,23,42,0.04);
}

.blog-line {
    height: 6px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        );
}

.blog-content {
    padding: 22px;
}

.category {
    color: #2563eb;

    font-size: 9px;

    font-weight: 800;

    letter-spacing: 1px;
}

.blog h3 {
    color: #111827;

    font-size: 16px;

    margin: 8px 0;
}

.blog p {
    color: #64748b;

    font-size: 11px;

    line-height: 1.8;
}

/* =========================================================
FOOTER
========================================================= */

.footer {
    margin-top: 45px;

    background: #0f172a;

    color: #94a3b8;

    border-radius: 20px 20px 0 0;

    padding: 32px;

    text-align: center;
}

.footer-brand {
    color: white;

    font-size: 20px;

    font-weight: 800;
}

.footer-brand span {
    color: #60a5fa;
}

.footer p {
    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="topbar">

    <div>
        <div class="logo">
            NEXORA <span>Innovation Hub</span>
        </div>

        <div class="logo-small">
            Entrepreneurship • Careers • Incubation • Innovation
        </div>
    </div>

    <div class="status">
        ● CENTRE ACTIVE
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

home, entrepreneurship, career, incubation, events = st.tabs([
    "🏠 Home",
    "💡 Entrepreneurship",
    "🎯 Career Development",
    "🏢 Incubation",
    "📰 Events & Blogs"
])


# ============================================================
# HOME
# ============================================================

with home:

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.markdown("""
    <div class="hero">

        <div class="hero-content">

            <div class="hero-badge">
                WELCOME TO NEXORA
            </div>

            <h1>
                Where Ideas Become <span>Possibilities.</span>
            </h1>

            <p>
                NEXORA Innovation Hub is a collaborative ecosystem
                for students, aspiring entrepreneurs and innovators.
                Explore opportunities, develop your skills, connect
                with mentors and turn promising ideas into meaningful
                projects and ventures.
            </p>

            <div class="hero-points">

                <span>🚀 Build Ideas</span>

                <span>🎓 Grow Skills</span>

                <span>🤝 Meet Mentors</span>

                <span>💡 Create Impact</span>

            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # DAILY ACTIVITY
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            CENTRE ACTIVITY
        </div>

        <h2>
            📅 Today's Events & Programs
        </h2>

        <p>
            See what's happening at the Innovation Hub today.
            Students and registered participants can join the
            sessions according to the schedule.
        </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="daily">

        <div class="daily-title">
            What's happening today?
        </div>

        <div class="daily-subtitle">
            Innovation Hub • Daily Activity Schedule
        </div>

    </div>
    """, unsafe_allow_html=True)


    event_columns = st.columns(4)

    for col, event in zip(event_columns, EVENTS):

        with col:

            st.markdown(f"""
            <div class="event">

                <div class="event-time">
                    {event["time"]}
                </div>

                <div class="event-title">
                    {event["title"]}
                </div>

                <div class="event-place">
                    📍 {event["place"]}
                </div>

                <div style="
                    margin-top:10px;
                    color:#64748b;
                    font-size:9px;
                    font-weight:700;
                ">
                    {event["type"]}
                </div>

            </div>
            """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # EXPLORE AREAS
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            EXPLORE THE HUB
        </div>

        <h2>
            Everything You Need to Move Forward
        </h2>

        <p>
            Whether you have a startup idea, want to improve your
            career skills or need support developing a project,
            explore the different areas of the centre.
        </p>

    </div>
    """, unsafe_allow_html=True)


    cols = st.columns(3)

    for col, program in zip(cols, PROGRAMS):

        with col:

            st.markdown(f"""
            <div class="feature">

                <div class="feature-icon">
                    {program["icon"]}
                </div>

                <h3>
                    {program["title"]}
                </h3>

                <p>
                    {program["text"]}
                </p>

                <div class="tag">
                    {program["tag"]}
                </div>

            </div>
            """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # ABOUT SECTION
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            ABOUT THE CENTRE
        </div>

        <h2>
            More Than Just a Workspace
        </h2>

    </div>
    """, unsafe_allow_html=True)


    left, right = st.columns([1.25, 1])

    with left:

        st.markdown("""
        <div class="info-panel">

            <h3>
                🌱 A place to learn, build and connect
            </h3>

            <p>
                The Innovation Hub brings together students,
                faculty, entrepreneurs, mentors and industry
                professionals under one ecosystem.
            </p>

            <p>
                Our objective is to encourage an innovation mindset,
                support entrepreneurial thinking and create pathways
                for students to convert knowledge into practical
                solutions.
            </p>

            <div class="check">
                ✓ Idea development and validation
            </div>

            <div class="check">
                ✓ Mentorship and expert guidance
            </div>

            <div class="check">
                ✓ Skill development programs
            </div>

            <div class="check">
                ✓ Prototype and project support
            </div>

            <div class="check">
                ✓ Industry and founder networking
            </div>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="info-panel">

            <h3>
                🎯 Our Focus Areas
            </h3>

            <p>
                We currently focus on four major areas:
            </p>

            <div class="check">
                💡 Entrepreneurship
            </div>

            <div class="check">
                🎯 Career Development
            </div>

            <div class="check">
                🏢 Startup Incubation
            </div>

            <div class="check">
                📰 Events & Knowledge Sharing
            </div>

            <p>
                Through these initiatives, students can discover
                opportunities beyond the classroom and participate
                in a growing innovation ecosystem.
            </p>

        </div>
        """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # STATS
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            OUR COMMUNITY
        </div>

        <h2>
            Growing With Every Idea
        </h2>

    </div>
    """, unsafe_allow_html=True)


    stats = [
        ("350+", "Students Engaged"),
        ("48", "Startup Ideas"),
        ("26", "Industry Mentors"),
        ("72+", "Programs Conducted")
    ]

    stat_cols = st.columns(4)

    for col, (number, label) in zip(stat_cols, stats):

        with col:

            st.markdown(f"""
            <div class="stat">

                <div class="number">
                    {number}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # LATEST BLOGS
    # --------------------------------------------------------

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            KNOWLEDGE CORNER
        </div>

        <h2>
            Latest From the Hub
        </h2>

    </div>
    """, unsafe_allow_html=True)


    blog_cols = st.columns(3)

    for col, blog in zip(blog_cols, BLOGS):

        with col:

            st.markdown(f"""
            <div class="blog">

                <div class="blog-line"></div>

                <div class="blog-content">

                    <div class="category">
                        {blog["category"]}
                    </div>

                    <h3>
                        {blog["title"]}
                    </h3>

                    <p>
                        {blog["text"]}
                    </p>

                    <div style="
                        color:#94a3b8;
                        font-size:9px;
                        margin-top:14px;
                    ">
                        Read more →
                    </div>

                </div>

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# ENTREPRENEURSHIP
# ============================================================

with entrepreneurship:

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            ENTREPRENEURSHIP
        </div>

        <h2>
            💡 From Problem to Opportunity
        </h2>

        <p>
            Entrepreneurship programs help students understand
            how ideas are identified, tested and developed into
            meaningful business opportunities.
        </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)

    entrepreneur_items = [
        (
            "🧠",
            "Ideation",
            "Learn how to identify real problems and generate creative solutions."
        ),
        (
            "🔎",
            "Validation",
            "Understand customer needs and test whether your solution has potential."
        ),
        (
            "📊",
            "Business Planning",
            "Explore business models, target markets, competition and growth strategies."
        )
    ]

    for col, (icon, title, text) in zip(
        [c1, c2, c3],
        entrepreneur_items
    ):

        with col:

            st.markdown(f"""
            <div class="feature">

                <div class="feature-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {text}
                </p>

            </div>
            """, unsafe_allow_html=True)


    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            STARTUP JOURNEY
        </div>

        <h2>
            How We Help Your Idea Grow
        </h2>

    </div>
    """, unsafe_allow_html=True)


    startup_steps = [
        ("01", "Identify", "Find a meaningful problem worth solving."),
        ("02", "Ideate", "Develop possible solutions through creative thinking."),
        ("03", "Validate", "Talk to users and test your assumptions."),
        ("04", "Prototype", "Build an early version of your solution."),
        ("05", "Pitch", "Present your idea to mentors and stakeholders.")
    ]

    for number, title, text in startup_steps:

        st.markdown(f"""
        <div class="program-strip">

            <span class="program-number">
                {number}
            </span>

            <span class="program-name">
                {title}
            </span>

            <div class="program-description">
                {text}
            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# CAREER DEVELOPMENT
# ============================================================

with career:

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            CAREER DEVELOPMENT
        </div>

        <h2>
            🎯 Prepare for Your Professional Journey
        </h2>

        <p>
            Career development initiatives focus on helping students
            build the skills, confidence and industry awareness needed
            for future opportunities.
        </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)

    career_items = [
        (
            "💻",
            "Technical Skills",
            "Workshops covering technology, programming, tools and emerging industry trends."
        ),
        (
            "🗣️",
            "Professional Skills",
            "Develop communication, teamwork, presentation and leadership abilities."
        ),
        (
            "💼",
            "Career Readiness",
            "Resume guidance, interview preparation, internship awareness and industry interaction."
        )
    ]

    for col, (icon, title, text) in zip(
        [c1, c2, c3],
        career_items
    ):

        with col:

            st.markdown(f"""
            <div class="feature">

                <div class="feature-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {text}
                </p>

            </div>
            """, unsafe_allow_html=True)


    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            UPCOMING ACTIVITIES
        </div>

        <h2>
            Career Development Programs
        </h2>

    </div>
    """, unsafe_allow_html=True)


    career_programs = [
        (
            "01",
            "Resume & Portfolio Workshop",
            "Learn how to showcase your projects, skills and achievements professionally."
        ),
        (
            "02",
            "Mock Interview Day",
            "Practice technical and HR interviews with experienced mentors."
        ),
        (
            "03",
            "Industry Connect",
            "Interact with professionals and understand current industry expectations."
        ),
        (
            "04",
            "Leadership Development",
            "Build decision-making, teamwork and leadership skills through activities."
        )
    ]

    for number, title, text in career_programs:

        st.markdown(f"""
        <div class="program-strip">

            <span class="program-number">
                {number}
            </span>

            <span class="program-name">
                {title}
            </span>

            <div class="program-description">
                {text}
            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# INCUBATION
# ============================================================

with incubation:

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            INCUBATION CENTRE
        </div>

        <h2>
            🏢 Turn Promising Ideas Into Ventures
        </h2>

        <p>
            The incubation centre provides structured support for
            innovators and early-stage teams working on promising ideas.
        </p>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)

    incubation_items = [
        (
            "🧑‍💼",
            "Mentorship",
            "Get guidance from experienced mentors across technology, business and strategy."
        ),
        (
            "🧪",
            "Prototype Support",
            "Develop, test and improve early versions of your product or solution."
        ),
        (
            "🌐",
            "Networking",
            "Connect with founders, professionals, industry experts and innovation communities."
        )
    ]

    for col, (icon, title, text) in zip(
        [c1, c2, c3],
        incubation_items
    ):

        with col:

            st.markdown(f"""
            <div class="feature">

                <div class="feature-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {text}
                </p>

            </div>
            """, unsafe_allow_html=True)


    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            INCUBATION PROCESS
        </div>

        <h2>
            How an Idea Moves Through the Centre
        </h2>

    </div>
    """, unsafe_allow_html=True)


    process = [
        (
            "01",
            "Submit an Idea",
            "Share your project, problem statement or startup concept."
        ),
        (
            "02",
            "Initial Review",
            "The incubation team evaluates feasibility, innovation and potential impact."
        ),
        (
            "03",
            "Mentoring",
            "Selected teams work with mentors to refine their idea and plan."
        ),
        (
            "04",
            "Build & Test",
            "Teams develop prototypes and collect feedback from users."
        ),
        (
            "05",
            "Launch",
            "Promising projects receive guidance for implementation and growth."
        )
    ]

    for number, title, text in process:

        st.markdown(f"""
        <div class="program-strip">

            <span class="program-number">
                {number}
            </span>

            <span class="program-name">
                {title}
            </span>

            <div class="program-description">
                {text}
            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# EVENTS & BLOGS
# ============================================================

with events:

    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            EVENTS & BLOGS
        </div>

        <h2>
            📰 What's Happening Around the Hub?
        </h2>

        <p>
            Stay updated with workshops, talks, competitions,
            founder interactions and stories from our innovation community.
        </p>

    </div>
    """, unsafe_allow_html=True)


    # EVENT CARDS

    event1, event2 = st.columns(2)

    with event1:

        st.markdown("""
        <div class="info-panel">

            <div class="category">
                UPCOMING EVENT
            </div>

            <h3>
                🚀 Student Startup Bootcamp
            </h3>

            <p>
                A three-day practical program covering ideation,
                customer discovery, business models, prototyping
                and startup pitching.
            </p>

            <div class="check">
                📅 15–17 December 2026
            </div>

            <div class="check">
                📍 Innovation Hub Seminar Hall
            </div>

            <div class="check">
                👥 Open to student teams
            </div>

        </div>
        """, unsafe_allow_html=True)


    with event2:

        st.markdown("""
        <div class="info-panel">

            <div class="category">
                SPECIAL SESSION
            </div>

            <h3>
                🎤 Founder Connect Series
            </h3>

            <p>
                An interactive conversation with a young entrepreneur
                about building a company, overcoming early challenges
                and finding the first customers.
            </p>

            <div class="check">
                📅 20 December 2026
            </div>

            <div class="check">
                📍 Collaboration Lounge
            </div>

            <div class="check">
                👥 Students & aspiring founders
            </div>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <div class="section">

        <div class="eyebrow">
            FROM OUR BLOG
        </div>

        <h2>
            Stories & Insights
        </h2>

    </div>
    """, unsafe_allow_html=True)


    blog_cols = st.columns(3)

    for col, blog in zip(blog_cols, BLOGS):

        with col:

            st.markdown(f"""
            <div class="blog">

                <div class="blog-line"></div>

                <div class="blog-content">

                    <div class="category">
                        {blog["category"]}
                    </div>

                    <h3>
                        {blog["title"]}
                    </h3>

                    <p>
                        {blog["text"]}
                    </p>

                    <div style="
                        color:#2563eb;
                        font-size:10px;
                        font-weight:700;
                        margin-top:12px;
                    ">
                        Read article →
                    </div>

                </div>

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <div class="footer-brand">
        NEXORA <span>Innovation Hub</span>
    </div>

    <p>
        A collaborative platform for entrepreneurship,
        career development, incubation and innovation.
    </p>

    <p>
        💡 Ideas &nbsp;&nbsp; 🚀 Startups &nbsp;&nbsp;
        🎓 Careers &nbsp;&nbsp; 🤝 Community
    </p>

    <div style="
        margin-top:15px;
        font-size:9px;
        color:#64748b;
    ">
        Demo Website • Sample Content • For Presentation
    </div>

</div>
""", unsafe_allow_html=True)
