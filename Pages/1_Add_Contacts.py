import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_phone_number import st_phone_number
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI')
CLIENT = MongoClient(MONGO_URI)

db = CLIENT["contacts_db"]
contacts_collec = db["contacts_collection"]


# Function to create a new contact
def create_new_contact(name, email, phone, address):

    country_code = phone.get('countryCallingCode', '')
    national_number = phone.get('nationalNumber', '')
    
    # Format the phone number in the desired format
    formatted_phone = f"+{country_code} {national_number}"
    
    # Create a dictionary to hold the contact details
    contact = {
        'name': name,
        'email': email,
        'phone': formatted_phone,
        'address': address,
    }
    try: 
        if contacts_collec.insert_one(contact):
            print('Contact added successfully')
        else:
            st.error('Failed to add contact')
    except Exception as e:
        st.error(f'An error occurred while adding the contact: {e}')
        print(e)


# Page layout
st.title("Add Contacts")
st.write('Please enter the details of the contact you would like to add.')

col1, col2 = st.columns(2)
with col1:
    fname = st.text_input('First Name')
with col2:
    lname = st.text_input('Last Name')

name = fname + " " + lname

email = st.text_input('Email')

st.write("Phone number")
phone = st_phone_number("", placeholder="xxxxxx", default_country="IN")
address = st.text_area('Address')


#Submit Button Linked ti function
if st.button('Add Contact', key="create_new_contact"):
    if len(name.strip()) > 1 and len(phone) > 1:
        create_new_contact(name, email, phone, address)
        st.success('✅ Contact added successfully!')
    else:
        st.warning('❌ Please enter the required fields. Give a name and phone number to add a contact.')
