# 🏗️ The Architect's Eye: Vision-Enabled Safety Compliance
The Architect's Eye" is a multi-agent AI system designed to automate construction site safety inspections. By leveraging Llama 3.2-Vision and a CrewAI-powered backend, the system analyzes site photos and text notes to generate comprehensive OSHA-compliant safety reports.

# 🛠️ Tech Stack
>Frontend: Streamlit

>Agentic Framework: CrewAI

>Vision/LLM: Ollama (Llama 3.2-Vision)

>Infrastructure: Linux/Docker compatible

# 🚀 Quick Start (Local Development)
1. **Install Ollama:** Open your terminal and run the following command:
   ```bash
   curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
   ```

2. After installation, pull the vision model: 
    ```bash
    ollama pull llama3.2-vision
    ```

3. Make sure you have the latest Pythob version setup

4. Clone the repo:
    ```bash
    git clone https://github.com/sounak1410/The-Architect-s-Eye.git
    cd The-Architect-s-Eye
    ```

5. Setup virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

6. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

7. Configure environment:
    Create a .env file in the root directory:

    OPENAI_API_KEY=NA
    OLLAMA_BASE_URL=http://localhost:11434
    VISION_MODEL=ollama/llama3.2-vision

8. Run the app:
    ```bash
    streamlit run app.py
    ```

# ☁️ Deployment (AMD GPU Cloud)

To run this on an AMD-optimized instance (e.g., DigitalOcean GPU Droplets):

1. Provision your Instance: Choose an AMD-optimized GPU instance running Ubuntu 22.04 LTS.

2. Install ROCm: Ensure the AMD ROCm drivers are installed to leverage GPU acceleration.
(Refer to AMD ROCm documentation for your specific distro).

3. Setup Ollama: 
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ollama pull llama3.2-vision
    ```

Deploy the Code:

>Clone your repo onto the server.

>Install requirements: 
    ```bash
    pip install -r requirements.txt.
    ```

>Start the server using the network-exposed address:
    ```bash
    streamlit run app.py --server.address 0.0.0.0
    ```

# 🧠 How It Works
1. Watcher Agent: Receives the raw image and site notes, identifying potential hazards using vision-enabled Llama 3.2.

2. Analyst Agent: Cross-references identified hazards against construction safety standards.

3. Reporter Agent: Synthesizes the data into a structured Markdown compliance report.

# 📝 Submission Notes
>This project was built for lablab.ai AMD Developer Hackathon.

>The app uses strictly local LLM inference via Ollama for data privacy and speed.

>No sensitive API keys are required beyond the local host configuration.

