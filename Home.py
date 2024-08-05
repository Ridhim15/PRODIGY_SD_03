import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(
    page_title="LINKup - Contact Management App",
    page_icon="📇",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load an image (optional logo)
# logo = Image.open("path/to/logo.png")

# Main title and subtitle
st.title("📇 LINKup")
st.subheader("Your Smart Contact Management Solution")

# Add a logo (optional)
# st.image(logo, use_column_width=True)

# Divider
st.markdown("---")

# Introduction and description
st.markdown(
    """
    ### Welcome to LINKup!
    LINKup is a powerful and intuitive contact management application that allows you to efficiently manage and organize your contacts. Whether you're keeping track of personal connections or business relationships, LINKup has you covered with its seamless integration with MongoDB.
    
    **Features:**
    - 📄 **View Contacts**: Access and visualize your contacts in a user-friendly table format.
    - ➕ **Add New Contacts**: Easily add new contacts with detailed information.
    - 🔍 **Search Contacts**: Quickly find contacts using our search functionality.
    - ❌ **Delete Contacts**: Remove outdated or unwanted contacts effortlessly.
    - 🗄️ **Organize Contacts**: Categorize and manage your contacts for better efficiency.
    """
)

# Instructions
st.markdown(
    """
    ### Getting Started
    To begin using LINKup, use the navigation menu on the left to:
    - **Add Contacts**: Input new contact details into your database.
    - **View Contacts**: Check out the list of all your stored contacts.
    - **Search**: Find contacts quickly using names or numbers.
    - **Delete**: Manage your contact list by removing entries as needed.

    ---
    """
)

# Call to action
st.markdown(
    """
    ### Ready to manage your contacts more effectively?
    Let's **LINKup** your connections today!
    """
)

# This is a simple strealit app for a contact management system ( i interegrated mongodb with it)
