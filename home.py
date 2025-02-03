import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Neurene - Mindful Breaks",
    page_icon="🌻",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
         'Get Help': "http://localhost:8501/faq",
         'Report a bug': "mailto:support@neurene.com",
         'About': "© 2024 Neurene Productivity Group GmbH. All rights reserved."
     }
)

# Sidebar with grouped pages
st.sidebar.title("Navigation")


# Group 3: User Tools
with st.sidebar.expander("🔒 User Tools"):
    if st.button("Login"):
        st.switch_page("pages/login.py")
    if st.button("Register"):
        st.query_params("home.py")
    if st.button("FAQ"):
        st.switch_page("pages/faq.py")

# Handle page content based on sidebar selection
# query_params = st.query_params()
page = st.query_params.get("page", ["home"])[0]

if page == "home":
    st.markdown(
    """
    <h1 style="text-align: center;">Welcome to Neurene</h1>
    """,
    unsafe_allow_html=True
)

elif page == "faq":
    st.title("FAQ")
    st.write("Here are frequently asked questions.")

elif page == "about":
    st.title("About Neurene")
    st.write("Learn more about our company.")

elif page == "pricing":
    st.title("Pricing Model")
    st.write("Detailed pricing model goes here.")

elif page == "partners":
    st.title("Partners")
    st.write("Details about our partners go here.")

elif page == "login":
    st.title("Login")
    st.text_input("Username")
    st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("Logged in!")

elif page == "register":
    st.title("Register")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        st.success("Registration successful!")


# Load the logo
logo_path = "./static/neurene_logo_light.jpg"


# Define the light blue color scheme
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
        font-family: Arial, sans-serif;
    }
    .section-header {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .pricing-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    .pricing-table th, .pricing-table td {
        border: 1px solid #ddd;
        text-align: center;
        padding: 8px;
    }
    .pricing-table th {
        background-color: #e3f2fd;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    # Logo and title section
    st.image(logo_path, use_container_width=True)
    st.markdown(
        """
        <div class="section-header">
            <h1>Neurene</h1>
            <h3>Mindful Breaks, Seamlessly Integrated</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Subheading and app description
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Discover small moments of mindfulness amidst your busy schedule. Neurene scans your calendar to find short, rejuvenating breaks tailored to you.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Container for sections
    with st.container():
        # Pricing Model
        with st.expander("📊 Pricing Model"):
            st.markdown(
                """
                <div class="container">
                    <h4>Our Pricing</h4>
                    <table class="pricing-table">
                        <tr>
                            <th>Subscription Model</th>
                            <th>Tier 1 (50-99 Employees)</th>
                            <th>Tier 2 (100-149 Employees)</th>
                            <th>Tier 3 (150-199 Employees)</th>
                            <th>Tier 4 (200-249 Employees)</th>
                        </tr>
                        <tr>
                            <td>Basic Subscription</td>
                            <td>12 €</td>
                            <td>11 €</td>
                            <td>10 €</td>
                            <td>9 €</td>
                        </tr>
                        <tr>
                            <td>Premium Subscription</td>
                            <td>15 €</td>
                            <td>14 €</td>
                            <td>13 €</td>
                            <td>12 €</td>
                        </tr>
                        <tr>
                            <td>Subscription Future Development</td>
                            <td>13.50 €</td>
                            <td>12.50 €</td>
                            <td>11.50 €</td>
                            <td>10.50 €</td>
                        </tr>
                    </table>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Competitor Comparison
        with st.expander("🤝 Comparison with Competitors"):
            st.markdown(
                """
                <div class="container">
                    <h4>Why Choose Us?</h4>
                    <table class="pricing-table">
                        <tr>
                            <th></th>
                            <th>Neurene</th>
                            <th>Reclaim AI</th>
                            <th>Clockwise</th>
                            <th>Motion</th>
                            <th>MS Viva Insights</th>
                        </tr>
                        <tr>
                            <td>Price per month</td>
                            <td>8-12€</td>
                            <td>8-12€</td>
                            <td>6.75-11.50€</td>
                            <td>12.00€</td>
                            <td>5.60-11.20€</td>
                        </tr>
                        <tr>
                            <td>Smart micro-breaks</td>
                            <td>✔️</td>
                            <td>✔️</td>
                            <td>✔️</td>
                            <td>❌</td>
                            <td>✔️</td>
                        </tr>
                        <tr>
                            <td>Disturbance blocking during breaks</td>
                            <td>✔️</td>
                            <td>➖</td>
                            <td>➖</td>
                            <td>➖</td>
                            <td>✔️</td>
                        </tr>
                        <tr>
                            <td>Corporate culture</td>
                            <td>✔️</td>
                            <td>❌</td>
                            <td>❌</td>
                            <td>❌</td>
                            <td>✔️</td>
                        </tr>
                        <tr>
                            <td>Emotion monitoring</td>
                            <td>✔️</td>
                            <td>❌</td>
                            <td>❌</td>
                            <td>❌</td>
                            <td>✔️</td>
                        </tr>
                        <tr>
                            <td>Assessing productivity cycles</td>
                            <td>✔️</td>
                            <td>✔️</td>
                            <td>➖</td>
                            <td>✔️</td>
                            <td>➖</td>
                        </tr>
                        <tr>
                            <td>Suggestions for mental health activities</td>
                            <td>✔️</td>
                            <td>❌</td>
                            <td>❌</td>
                            <td>❌</td>
                            <td>✔️</td>
                        </tr>
                    </table>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Partners Section
        with st.expander("🌟 Our Partners"):
            st.markdown(
                """
                <div class="container">
                    <h4>We Proudly Partner With:</h4>
                    <ul>
                        <li>Whoop</li>
                        <li>NRC</li>
                        <li>Headspace</li>
                        <li>Coursera</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Customers Section
        with st.expander("💼 Our Customers"):
            st.markdown(
                """
                <div class="container">
                    <h4>Our Happy Customers Include:</h4>
                    <ul>
                        <li>tbd</li>
                        <li>...</li>
                        <li>...</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Login Section
        with st.expander("🔒 Register Now"):
            st.markdown(
                """
                <div class="container">
                    <h4>Register now and start your journey with Neurene.</h4>
                """,
                unsafe_allow_html=True,
            )

            # Streamlit input widgets for login
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Register Now"):
                if username == "" or password == "":
                    st.error("Please fill in all fields.")
                else:
                    st.session_state.username = username
                    st.switch_page("pages/onboarding.py")
                        

    # Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <p>© 2024 Neurene Productivity Group GmbH. All rights reserved.</p>
            <p>For support, visit our <a href="/faq" target="_self">FAQ Page</a> or contact us at <a href="mailto:support@neurene.com">support@neurene.com</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
