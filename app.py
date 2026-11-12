
import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "light_mode" not in st.session_state:
    st.session_state.light_mode = False

if "notifications" not in st.session_state:
    st.session_state.notifications = True


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.title("My Dashboard")
    st.write("Navigation")

    page = st.radio(
        "Menu",
        ("Home", "Analysis", "Projects", "Settings", "Contact")
    )


# ---------------- THEME COLORS ----------------

if st.session_state.light_mode:

    bg = "#FFFFFF"
    sidebar = "#F1F5F9"
    card = "#FFFFFF"
    text = "#1E293B"
    muted = "#64748B"
    border = "#E2E8F0"
    input_bg = "#FFFFFF"
    button = "#2563EB"
    scheme = "light"

else:

    bg = "#0F172A"
    sidebar = "#1E293B"
    card = "#1E293B"
    text = "#F8FAFC"
    muted = "#CBD5E1"
    border = "#334155"
    input_bg = "#334155"
    button = "#2563EB"
    scheme = "dark"


# ---------------- GLOBAL CSS ----------------

st.markdown(
    f"""
    <style>

    :root {{
        color-scheme: {scheme};
    }}

    .stApp,
    [data-testid="stAppViewContainer"] {{
        background-color: {bg};
        color: {text};
    }}

    [data-testid="stHeader"] {{
        background-color: {bg};
    }}

    [data-testid="stSidebar"] {{
        background-color: {sidebar};
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {text} !important;
    }}

    p, label, li {{
        color: {text};
    }}

    .stCaption {{
        color: {muted};
    }}

    [data-testid="stMetric"] {{
        background-color: {card};
        border: 1px solid {border};
        padding: 18px;
        border-radius: 12px;
    }}

    [data-testid="stMetricLabel"] {{
        color: {muted} !important;
    }}

    [data-testid="stMetricValue"] {{
        color: {text} !important;
    }}

    [data-testid="stMetricDelta"] {{
        color: #22C55E !important;
    }}

    [data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {card};
        border-color: {border};
        border-radius: 12px;
    }}

    .stButton > button {{
        background-color: {button};
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
    }}

    .stButton > button:hover {{
        background-color: #1D4ED8;
        color: white;
        border: none;
    }}

    input, textarea {{
        background-color: {input_bg} !important;
        color: {text} !important;
    }}

    [data-baseweb="select"] > div {{
        background-color: {input_bg};
        color: {text};
    }}

    hr {{
        border-color: {border};
    }}

    [data-testid="stProgressBar"] > div > div {{
        background-color: #3B82F6;
    }}

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {{
        color: {text} !important;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label {{
        color: {text} !important;
    }}

    [data-testid="stVegaLiteChart"] text {{
        fill: {text};
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
#                    HOME PAGE
# ==================================================

if page == "Home":

    st.title("Home Page")
    st.write("Welcome to Your Dashboard!")

    st.divider()

    # Metrics

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Users", "1,234", "+5%")
    col2.metric("Revenue", "$5,200", "+8%")
    col3.metric("Projects", "12", "+2")
    col4.metric("Completed", "8", "+3")

    st.divider()

    # Project Progress

    st.subheader("Project Progress")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Web Development")
        st.progress(0.70)

        st.write("Mobile App Development")
        st.progress(0.40)

    with col2:
        st.write("Dashboard Design")
        st.progress(0.80)

        st.write("Data Analysis")
        st.progress(0.60)

    st.divider()

    # Quick Actions

    st.subheader("Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Add New Project", use_container_width=True):
            st.success("New Project Added!")

            if st.session_state.notifications:
                st.toast("Your project was added successfully!")

    with col2:
        if st.button("View Analysis", use_container_width=True):
            st.toast("Go to the Analysis page from the sidebar.")

    with col3:
        if st.button("Manage Settings", use_container_width=True):
            st.toast("Go to Settings from the sidebar.")


# ==================================================
#                  ANALYSIS PAGE
# ==================================================

elif page == "Analysis":

    st.title("Analysis")
    st.write("Here is an overview of your project performance.")

    st.divider()

    # Chart Data

    projects_data = pd.DataFrame({
        "Category": [
            "Web Development",
            "Mobile Apps",
            "Dashboard",
            "Data Analysis"
        ],
        "Projects": [5, 3, 2, 2]
    })

    status_data = pd.DataFrame({
        "Status": ["Completed", "In Progress", "Pending"],
        "Number": [8, 3, 1]
    })

    revenue_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [1200, 1800, 1500, 2500, 3200, 5200]
    })

    activity_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Projects": [2, 3, 2, 4, 5, 8]
    })

    # Charts

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Projects by Category")
        st.bar_chart(
            projects_data,
            x="Category",
            y="Projects"
        )

    with col2:
        st.subheader("Project Status")
        st.bar_chart(
            status_data,
            x="Status",
            y="Number"
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Monthly Revenue")
        st.line_chart(
            revenue_data,
            x="Month",
            y="Revenue"
        )

    with col2:
        st.subheader("Monthly Project Activity")
        st.area_chart(
            activity_data,
            x="Month",
            y="Projects"
        )


# ==================================================
#                  PROJECTS PAGE
# ==================================================

elif page == "Projects":

    st.title("My Projects")
    st.write("Here are some of the projects I have worked on.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):
            st.subheader("Movie Time")

            st.markdown(
                '<span style="background:#2563EB;color:white;'
                'padding:5px 10px;border-radius:6px;">APPS</span>',
                unsafe_allow_html=True
            )

            st.write("A movie application project.")

            if st.button("View Project 1", key="project1"):
                st.toast("Opening Movie Time...")

        with st.container(border=True):
            st.subheader("Dashboard")

            st.markdown(
                '<span style="background:#7C3AED;color:white;'
                'padding:5px 10px;border-radius:6px;">STREAMLIT</span>',
                unsafe_allow_html=True
            )

            st.write("An interactive data dashboard.")

            if st.button("View Project 3", key="project3"):
                st.toast("Opening Dashboard...")

    with col2:

        with st.container(border=True):
            st.subheader("Talabat")

            st.markdown(
                '<span style="background:#059669;color:white;'
                'padding:5px 10px;border-radius:6px;">WEB</span>',
                unsafe_allow_html=True
            )

            st.write("A food ordering website.")

            if st.button("View Project 2", key="project2"):
                st.toast("Opening Talabat...")

        with st.container(border=True):
            st.subheader("To Do List")

            st.markdown(
                '<span style="background:#D97706;color:white;'
                'padding:5px 10px;border-radius:6px;">FLUTTER</span>',
                unsafe_allow_html=True
            )

            st.write("A task management application.")

            if st.button("View Project 4", key="project4"):
                st.toast("Opening To Do List...")


# ==================================================
#                  SETTINGS PAGE
# ==================================================

elif page == "Settings":

    st.title("Settings")
    st.write("Adjust your dashboard settings.")

    st.divider()

    # Appearance

    st.subheader("Appearance")

    st.toggle(
        "Light Mode",
        key="light_mode"
    )

    if st.session_state.light_mode:
        st.caption("Light Mode is currently enabled.")
    else:
        st.caption("Dark Mode is currently enabled.")

    st.divider()

    # Notifications

    st.subheader("Notifications")

    st.toggle(
        "Enable Notifications",
        key="notifications"
    )

    if st.session_state.notifications:
        st.caption("You will receive in-app notifications.")
    else:
        st.caption("In-app notifications are disabled.")


# ==================================================
#                  CONTACT PAGE
# ==================================================

elif page == "Contact":

    st.title("Contact")

    st.write("Feel free to contact me for any questions or projects.")

    st.divider()

    st.subheader("Get in Touch")

    st.write("Email: seeko.karim@outlook.com")
    st.write("GitHub: ")
    st.write("Whatsapp: +20 1063955804")
