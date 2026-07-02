# AI Notes Generator using Ollama and Streamlit

### Author

**Nayan Shankar Banarase**


---

# Abstract

The **AI Notes Generator** is an offline educational application developed using **Python**, **Streamlit**, **Ollama**, and **Large Language Models (LLMs)** such as **Llama 3** or **Phi-3**. The application automatically generates well-structured study notes based on a user-provided topic. The generated notes include an introduction, explanation, key points, definitions, questions with answers, and a summary. Additionally, the application allows users to export the generated notes as a PDF document. Since the model runs locally through Ollama, the system ensures user privacy, faster response times after model loading, and eliminates dependency on paid cloud-based AI APIs.

**Keywords:** Artificial Intelligence, Large Language Model, Ollama, Streamlit, Python, PDF Generation, Offline AI, Prompt Engineering.

---

# 1. Introduction

Artificial Intelligence has significantly transformed the education sector by providing intelligent learning tools that improve students' productivity. Preparing structured study notes manually is often time-consuming and requires extensive research. Large Language Models (LLMs) have demonstrated exceptional capabilities in understanding natural language and generating high-quality educational content.

The AI Notes Generator is designed to automate the process of creating comprehensive study notes. Users simply enter a topic, and the application generates organized notes suitable for academic preparation. The project operates entirely offline using Ollama, making it cost-effective and privacy-friendly.

---

# 2. Literature Review

Several AI-based text generation systems have been developed in recent years. OpenAI's ChatGPT, Google's Gemini, and Anthropic's Claude have shown remarkable capabilities in generating human-like responses. However, these services primarily rely on cloud computing and paid APIs, making them less suitable for offline educational environments.

Open-source LLMs such as **Llama 3**, **Phi-3**, and **TinyLlama** have made local AI deployment feasible. Frameworks like **Ollama** simplify running these models on personal computers without requiring internet connectivity after installation.

For the application interface, **Streamlit** has become one of the most popular Python frameworks for building interactive AI applications due to its simplicity and rapid development capabilities.

---

# 3. Methodology

The application follows the following workflow:

1. The user launches the Streamlit application.
2. The user enters the desired study topic.
3. A prompt is created using prompt engineering techniques.
4. The prompt is sent to the locally running LLM through Ollama.
5. The model generates structured educational notes.
6. The generated content is displayed in the Streamlit interface.
7. The notes are converted into a PDF using the ReportLab library.
8. The user downloads the generated PDF.

### Workflow

```
User
   │
   ▼
Streamlit Interface
   │
   ▼
Prompt Engineering
   │
   ▼
Ollama (Llama 3 / Phi-3)
   │
   ▼
Generated Notes
   │
   ├────────► Display on UI
   │
   └────────► PDF Generation (ReportLab)
                 │
                 ▼
            Download PDF
```

---

# 4. Implementation

The project is implemented using Python and several open-source libraries.

### Programming Language

* Python 3.10+

### Framework

* Streamlit

### AI Framework

* Ollama

### Large Language Model

* Llama 3
* Phi-3 (optional)

### Libraries Used

* Streamlit
* Ollama
* ReportLab
* Python Standard Library

### Features

* Offline AI-based note generation
* User-friendly interface
* Structured educational notes
* Automatic PDF generation
* Download generated notes
* Fast local inference
* Session-based note generation
* Simple prompt engineering
* No internet required after model installation
* No paid API required

---

# 5. System Requirements

### Hardware

* Intel Core i5 or higher
* Minimum 8 GB RAM (16 GB Recommended)
* NVIDIA RTX GPU (Optional but recommended)
* 10 GB free storage

### Software

* Windows 10/11
* Python 3.10+
* Visual Studio Code
* Ollama
* Streamlit

---

# 6. Project Structure

```
AI-Notes-Generator
│
├── app.py
├── requirements.txt
├── README.md
├── generated_notes.pdf
├── assets/
│
├── models/
│
└── screenshots/
```

---

# 7. Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Notes-Generator.git

cd AI-Notes-Generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama from:

[https://ollama.com](https://ollama.com)

### Download Model

```bash
ollama pull llama3
```

### Run Ollama

```bash
ollama run llama3
```

### Run Application

```bash
python -m streamlit run app.py
```

---

# 8. Results

The application successfully generates high-quality study notes for user-specified topics.

Each generated note contains:

* Introduction
* Detailed Explanation
* Key Points
* Definitions
* Questions and Answers
* Summary

Users can instantly download the generated notes as PDF documents.

---

# 9. Advantages

* Completely offline
* No subscription cost
* Free to use
* Fast response after model loading
* Privacy-preserving
* Easy-to-use interface
* Automatic PDF export
* AI-powered educational assistant

---

# 10. Limitations

* Initial model download is large.
* First-time loading is slower.
* Performance depends on system hardware.
* Output quality depends on prompt design.

---

# 11. Conclusion

The AI Notes Generator demonstrates the practical application of local Large Language Models in educational content generation. By integrating Streamlit with Ollama and Llama 3, the system provides a cost-effective, offline, and user-friendly platform for generating structured study notes. The project successfully combines artificial intelligence with document generation, offering students an efficient learning assistant without relying on cloud-based AI services.

---

# 12. Future Scope

The project can be extended with several advanced features:

* Multi-language note generation
* Voice-based topic input
* Text-to-speech support
* Image generation for concepts
* Diagram generation
* Quiz generation
* Flashcard generation
* AI chatbot for doubt solving
* Cloud deployment
* User login and authentication
* Note editing and saving
* Database integration
* Mobile application development
* Personalized learning recommendations
* Integration with Learning Management Systems (LMS)

---

# References

[1] Touvron, H., et al., "Llama 3: Open Foundation and Fine-Tuned Chat Models," Meta AI, 2024.

[2] Ollama, *Official Documentation*. Available: [https://ollama.com](https://ollama.com)

[3] Streamlit Documentation. Available: [https://docs.streamlit.io](https://docs.streamlit.io)

[4] Python Software Foundation. *Python Documentation*. Available: [https://docs.python.org/3/](https://docs.python.org/3/)

[5] ReportLab User Guide. Available: [https://www.reportlab.com/documentation/](https://www.reportlab.com/documentation/)

[6] Brown, T. B., et al., "Language Models are Few-Shot Learners," *Advances in Neural Information Processing Systems (NeurIPS)*, 2020.

[7] Vaswani, A., et al., "Attention Is All You Need," *NeurIPS*, 2017.

---


