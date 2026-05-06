import streamlit as st
import os
from crewai import Agent, Task, Crew, Process, LLM
# Define the local LLM configuration
local_llm = LLM(
    model="ollama/llama3.2-vision", # Ensure this model is pulled in Ollama
    base_url="http://localhost:11434" # This is the crucial part!
)

# --- Define Agents ---
watcher = Agent(
    role='Watcher', 
    goal='Analyze site photo and notes.', 
    backstory='You are an expert site inspector.',
    llm=local_llm, # Pass the object here
    verbose=True
)

# Ensure an 'uploads' directory exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")

st.title("🏗️ The Architect's Eye: Vision Enabled")

# 1. Text Input
site_notes = st.text_area("Input Site Observations:", height=150)

# 2. Image Upload
uploaded_file = st.file_uploader("Upload site photo (for Vision Analysis):", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Save the file to the 'uploads' folder
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(file_path, caption="Uploaded Site Photo", use_container_width=True)

# 3. Execution Logic
if st.button("Generate Compliance Report"):
    if site_notes or uploaded_file:
        with st.spinner("Analyzing site safety (Agents are working)..."):
            # 1. Prepare Context
            vision_context = f"Image Path: {file_path}" if uploaded_file else "No image provided."
            
            # 2. Define Tasks
            task1 = Task(description=f'Analyze site: {site_notes}. {vision_context}', expected_output='List of visual hazards.', agent=watcher)
            
            # 3. Initialize your Crew
            my_crew = Crew(
                agents=[watcher], 
                tasks=[task1], 
                process=Process.sequential
            )

            # 4. RUN the crew
            result = my_crew.kickoff()

            # 5. DISPLAY the result
            st.subheader("Final Safety Report")
            st.markdown(result)
            
            # ... (Rest of your download/save code)
            st.success("Analysis Complete!")
    else:
        st.warning("Please provide either text notes or a photo!")
    with st.spinner("Analyzing site safety (Agents are working)..."):
            # 1. Initialize your Crew
            my_crew = Crew(
                agents=[watcher], # Add your other agents here
                tasks=[task1],    # Add your other tasks here
                process=Process.sequential
            )

            # 2. RUN the crew and CAPTURE the result
            # 'result' will contain the final markdown report from your agents
            result = my_crew.kickoff()

            # 3. DISPLAY the result to the user
            st.subheader("Final Safety Report")
            st.markdown(result) # This renders the text nicely in the browser

            st.download_button(
                label="Download Compliance Report",
                data=str(result),
                file_name="compliance_report.md",
                mime="text/markdown"
            )
            
            # Optional: Save it locally so you have a copy
            with open("final_report.md", "w") as f:
                f.write(str(result))
            
            st.success("Analysis Complete!")