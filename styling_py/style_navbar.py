import streamlit as st

sidebar_style = """
    <style>
        /* Sidebar background with smooth dynamic gradient */
        @keyframes move-gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        [data-testid="stSidebar"] {
            background: radial-gradient(circle, #000000 15%, #006400 70%, #0000FF 15%);
            background-size: 300% 300%; /* Large gradient for smooth animation */
            animation: move-gradient 8s ease infinite; /* Smooth animation for gradient */
            padding: 20px;
            color: white;
        }

        /* Style for each button (menu item) */
        [data-testid="stSidebarUserContent"] .stButton button {
            display: block;
            width: 100%;
            padding: 10px 15px;  /* Reduced padding */
            margin: 5px 0;  /* Reduced margin between buttons */
            text-align: center;
            font-size: 16px;  /* Smaller font size */
            font-weight: bold;
            color: white; /* Text color set to white for better contrast */
            border-radius: 8px;  /* Slightly smaller border radius */
            background: linear-gradient(45deg, green, black, blue); /* Gradient rotated 45 degrees */
            transition: all 0.3s ease-in-out;
            position: relative;
            cursor: pointer;
        }

        /* Hover effect for buttons */
        [data-testid="stSidebarUserContent"] .stButton button:hover {
            transform: scale(1.05); /* Slightly enlarge button on hover */
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        }

        /* Add glowing outline effect on hover */
        [data-testid="stSidebarUserContent"] .stButton button:hover::after {
            content: '';
            position: absolute;
            top: -3px;
            left: -3px;
            right: -3px;
            bottom: -3px;
            border-radius: 12px;
            background: linear-gradient(45deg, lightgreen, cyan, violet);
            z-index: -1;
            animation: glow 1s infinite;
        }

        /* Animation for glowing border */
        @keyframes glow {
            0% {
                filter: brightness(1);
            }
            50% {
                filter: brightness(1.5);
            }
            100% {
                filter: brightness(1);
            }
        }

        /* Title in the sidebar */
        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: white;
        }
    </style>
"""


def style_navbar():
    st.markdown(sidebar_style, unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-title">Navigation</div>', unsafe_allow_html=True)

    #The buttons for the tabs
    button_texts=['Home','Dispatcher Simulator', 'Responder Tracking', 'About', 'Profile Settings']
    tab_buttons=[]
    for button_text in button_texts:
        tab_button=st.sidebar.button(button_text,key=button_text)
        tab_buttons.append(tab_button)

    for idx,tab_button in enumerate(tab_buttons):
        if tab_button:
            st.session_state.selected_tab=button_texts[idx]
            break

    return st.session_state.selected_tab
