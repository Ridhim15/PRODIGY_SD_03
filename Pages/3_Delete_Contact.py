import os
import streamlit as st
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI')
CLIENT = MongoClient(MONGO_URI)

db = CLIENT["contacts_db"]
contacts_collec = db["contacts_collection"]

# Function to delete a contact by a specific identifier (e.g., name or phone)
def delete_contact(identifier):
    result = contacts_collec.delete_one({"name": identifier})  # Use appropriate field
    return result.deleted_count

# Streamlit UI
st.write("## Delete Contact")
contact_name = st.text_input("Enter the name of the contact to delete:")

if st.button("Delete Contact"):
    if contact_name:
        deleted_count = delete_contact(contact_name)
        if deleted_count > 0:
            st.success(f"Contact '{contact_name}' deleted successfully!")
        else:
            st.error("Contact not found.")
    else:
        st.error("Please enter a contact name.")
