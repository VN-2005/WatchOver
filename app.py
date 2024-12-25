from settings import *
from styling_py.style_navbar import *
from styling_py.style_mainpage import *
from styling_py.style_modal import *
from utils.load_session_variables import *
from utils.login_signup import *
from utils.db_helper import *
from tabs.home_page import home_page
from tabs.dispatcher_dashboard.dispatcher_dashboard import display_dispatcher_dashboard
# import threading

# def empty_screen():
#     st.write('emptying the screen')
#     print('before sleeping ')
#     time.sleep(2)
#     print('after sleeping')
#     st.write('woke up from the sleep')
#     st.empty()
#     print('emptying the screen')
#     st.rerun()

def main():
    # style_mainpage()
    selected_button=style_navbar()
    # st.write('the selected button is:', selected_button)

    if st.session_state.hasLoggedIn==None:

        if selected_button is not None:
            # DisplayModal("User hasn't logged yet", 2)
            st.info("Please login before trying to access the functionalities.")
            st.session_state.selected_tab=None
            # thread=threading.Thread(target=empty_screen)
            # thread.start()
        
        #Displaying the login, signup form.
        login_signup()
        if st.session_state.hasLoggedIn==True:
            st.selcted_tab="Home"
            st.empty()
    else:
        if st.session_state.selected_tab!="Dispatcher Simulator":
            st.session_state.simulation_started = False
            st.session_state.simulation_ended = False
            st.session_state.grade = None
            st.session_state.feedback = None
            st.session_state.chat_history = []
            push_chats_to_db()

        if st.session_state.selected_tab==None:
            st.empty()
            st.write("Please choose a tab and continue")
        elif st.session_state.selected_tab=="Home":
            home_page()
        elif st.session_state.selected_tab=="Dispatcher Simulator":
            display_dispatcher_dashboard()
        pass
    

if __name__=="__main__":
    initialize_all_session_variables()
    getConnection()
    main()
