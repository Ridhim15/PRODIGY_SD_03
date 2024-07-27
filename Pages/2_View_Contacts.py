import streamlit as st
import pandas as pd

def view_contacts():
    # Assuming you have a list of contacts
    contacts = [
        {"name": "John Doe", "email": "johndoe@example.com"},
        {"name": "Jane Smith", "email": "janesmith@example.com"},
        {"name": "Bob Johnson", "email": "bobjohnson@example.com"}
    ]

    st.title("Contacts")
    
    # Convert the contacts list into a Pandas DataFrame
    df = pd.DataFrame(contacts)
    
    # Display the DataFrame using Streamlit
    st.dataframe(df)

if __name__ == "__main__":
    view_contacts()
