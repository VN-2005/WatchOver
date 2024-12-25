# WatchOver: AI-Powered Emergency Training Platform

## Problem Statement
The lack of effective training tools for emergency dispatchers and responders often leads to delayed response times and suboptimal decisions during critical situations. This gap is particularly significant in addressing challenges such as scalable dispatcher training, enhancing real-time decision-making, and improving collaboration between emergency teams. These issues align with the Laerdal challenges of creating life-saving solutions through technology.

## Solution: WatchOver
**WatchOver** addresses these challenges by providing:
- AI-driven simulations for realistic dispatcher training.
- A grading and feedback system to evaluate decision-making skills.
- A seamless integration of first responders into emergencies using real-time communication.

The platform is designed to empower dispatchers and responders with tools to make quicker, more accurate decisions, ultimately improving outcomes in emergency situations.

---

## Features
### 1. Interactive Dispatcher Dashboard
- Simulate realistic emergency call scenarios using AI models.
- Get real-time feedback on responses.
- Graded performance analytics based on scenario-specific expectations.

### 2. Responder Tracking
- Locate and notify nearby first responders in real-time.
- Use geolocation to connect responders with emergencies.
- Monitor response progress and provide updates to dispatchers.

### 3. Persistent Chat and Feedback
- Maintain a record of user responses for continuous improvement.
- Provide comments and hints on missed steps or incorrect actions.

### 4. AI-Driven Scenarios
- Use **LangChain** and **OpenAI models** to generate emergency scenarios dynamically.
- Ensure scenarios align with best practices in emergency response.

---

## Technology Stack
### Frontend
- **Streamlit**: Interactive UI for dispatcher training and responder tracking.

### Backend
- **MongoDB**: Stores persistent chat logs, user performance, and grading information.
- **LangChain**: Manages the logic for conversational AI and scenario generation.
  - **Imports used**:
    - `from langchain.prompts import PromptTemplate`
    - `from langchain.chains import ConversationChain`
    - `from langchain.memory import ConversationBufferMemory`
- **OpenAI GPT-4**: Generates realistic emergency scenarios and AI responses.

### Additional Tools
- **pymongo**: For MongoDB integration.
- **dotenv**: Manages environment variables securely.
- **st-js-cookie-manager**: Handles cookies in Streamlit for user session management.

---

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/watchover.git
   cd watchover
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env.local` file and add:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   MONGO_URI=your_mongo_connection_string
   ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Future Enhancements
- **Multi-language Support**: Train dispatchers in multiple languages.
- **Mobile App Integration**: Extend real-time responder tracking to mobile devices.
- **Advanced Analytics**: Provide deeper insights into dispatcher performance trends.

---

## Contact Us
For queries, contact us at:
- 📧 Email: support@watchover.ai
- 🌐 Website: [www.watchover.ai](http://www.watchover.ai)
