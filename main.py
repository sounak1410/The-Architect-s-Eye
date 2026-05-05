from crewai import Agent, Task, Crew, Process

# 1. Define the Agents
# Note: Added the watcher with the vision model
watcher = Agent(
    role='Site Watcher',
    goal='Analyze site images to detect safety hazards.',
    backstory='You are a visual inspection expert. You detect hazards in photos.',
    llm="ollama/llama3.2-vision" 
)

analyst = Agent(
    role='Safety Analyst',
    goal='Identify specific safety violations in the provided site notes.',
    backstory='You are a detail-oriented inspector. You only list the facts.',
    llm="ollama/llama3.2"
)

reporter = Agent(
    role='Compliance Reporter',
    goal='Format the analyst\'s findings into a professional, human-readable report.',
    backstory='You are a legal expert who knows how to write formal safety violations.',
    llm="ollama/llama3.2"
)

# 2. Refactor into a function so app.py can call it
def run_safety_pipeline(site_notes, image_path=None):
    
    # Task 1: Analyze visual data
    task1 = Task(
        description=f'Analyze the site notes: {site_notes}. If an image exists, analyze: {image_path}',
        expected_output='A list of safety violations found in notes and images.',
        agent=watcher # Changed to watcher to handle both
    )

    # Task 2: Format the report
    task2 = Task(
        description='Based on the list of violations, write a professional incident report.',
        expected_output='A fully formatted, professional safety report.',
        agent=reporter
    )

    # 3. Form the Crew
    crew = Crew(
        agents=[watcher, reporter], # Added watcher here
        tasks=[task1, task2],
        process=Process.sequential
    )

    # 4. Kickoff
    result = crew.kickoff()
    return result


if __name__ == "__main__":
    with open("sites_notes.txt", "r") as file:
        site_data = file.read()
    
    report = run_safety_pipeline(site_data)
    
    with open("final_report.md", "w") as f:
        f.write(str(report))
    print("\n--- DONE! Report saved to final_report.md ---")