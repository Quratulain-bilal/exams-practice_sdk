# 📚 Exams Practice SDK - Fundamentals of Agentic AI

A comprehensive study repository and SDK examples for **Fundamentals of Agentic AI (FAI)**. This project contains notes, implementations, and study materials for building AI agents with tool use, structured output, and advanced error handling.

## 🚀 Key Features & Topics

- **🎯 Agentic Concepts:** Understanding Agents, Runners, and Model integration.
- **🛠️ Tool Integration:** Deep dive into `@function_tool`, `is_enabled` dynamic conditions, and Handoffs.
- **📊 Structured Output:** Mastery of `AgentOutputSchema`, Pydantic validation, and response wrapping.
- **🛡️ Error Handling:** Custom `failure_error_function` and SDK-level exception handling.
- **📖 Exam Preparation:** Topics covering Prompt Engineering, Pydantic dataclasses, and SDK defaults.

## 📁 Repository Structure

- `agent_as_tool/`: Examples of nested agent execution.
- `docstring_style_detection/`: Best practices for tool docstrings.
- `exam_fundamentals/`: Core concepts for FAI L1 exam.
- `exam_topics/`: Comprehensive exam schedule and topics.
- `function_tool_enabled/`: Logical conditions for tool availability.
- `function_tool_errors/`: Handling crashes and custom error responses.
- `output_schema/`: Parsing and validating structured LLM outputs.
- `run_input/`: Managing execution context and inputs.

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+
- An API Key (e.g., Google Gemini)

### Installation
```bash
# Install required dependencies
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
```

### Usage
Explore the directories for specific notes or run the example agent:
```bash
python agent_as_tool/app.py
```

## 📝 Acknowledgments
Special thanks to **Sir Daniyal** for the study materials and concepts shared in the FAI Fundamentals course.

## 🤝 Contributing
Contributions are welcome! If you have better examples or refined notes, feel free to open an issue or submit a PR.

## 📜 License
MIT License
