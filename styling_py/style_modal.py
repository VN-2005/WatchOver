import streamlit as st
import time

def inject_modal_css():
    """
    Injects the CSS required for the modal into the Streamlit app.
    """
    modal_css = """
    <style>
    /* Modal Background */
    .modal-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.6); /* Dark translucent background */
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000; /* Ensure it is above all other elements */
        visibility: hidden; /* Initially hidden */
        opacity: 0; /* Transparent initially */
        transition: opacity 0.3s ease, visibility 0.3s ease;
    }

    /* Modal Box */
    .modal-content {
        background: white;
        padding: 20px;
        border-radius: 8px;
        width: 400px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Show Modal */
    .modal-container.active {
        visibility: visible;
        opacity: 1;
    }
    </style>
    """
    st.markdown(modal_css, unsafe_allow_html=True)

def create_modal_structure(message: str):
    """
    Creates the modal HTML structure and injects it into the Streamlit app.
    """
    modal_html = f"""
    <div class="modal-container" id="custom-modal">
        <div class="modal-content">
            <h3 style="color: red;">Notification</h3>
            <p>{message}</p>
        </div>
    </div>
    """
    st.markdown(modal_html, unsafe_allow_html=True)

def show_modal_js(duration: int):
    """
    Injects JavaScript to make the modal visible and hides it after a delay.
    """
    modal_js = f"""
    <script>
    const modal = document.getElementById('custom-modal');
    modal.classList.add('active');
    setTimeout(() => modal.classList.remove('active'), {duration * 1000});
    </script>
    """
    st.markdown(modal_js, unsafe_allow_html=True)

def DisplayModal(message: str, duration: int = 2):
    """
    Displays a modal with the specified message for the given duration.

    Args:
        message (str): The message to display in the modal.
        duration (int): The number of seconds to display the modal.
    """
    inject_modal_css()
    create_modal_structure(message)
    show_modal_js(duration)
