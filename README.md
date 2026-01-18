# Instagram Chat Analyzer (Version 1)

A Python project to analyze Instagram chat data (JSON export) between two people.
This project focuses on understanding communication patterns using real-world data.

---

## 🚀 Features (Version 1)

- Load and parse Instagram chat JSON data
- Ignore system messages (Meta AI)
- Analyze:
  - Total messages per person
  - Text-only message count
  - Reaction count
  - Average message length
  - Total words sent
  - Most-used words per person (basic NLP)
- Clean and structured project layout
- Beginner-friendly, step-by-step logic

---

## 📁 Project Structure

instagram-chat-analyzer/
│
├── data/
│ └── message_1.json # Instagram chat export (not pushed to GitHub)
│
├── src/
│ └── main.py # Main analysis script
│
├── outputs/ # Future graphs / reports
│
└── README.md


---

## 🛠️ Requirements

- Python 3.8+
- No external libraries required (pure Python)

---

## ▶️ How to Run

1. Place your Instagram chat JSON file inside the `data/` folder
2. Make sure the file is named `message_1.json`
3. Run the script:

```bash
python src/main.py



## 📊 Metrics Calculated

- **Message count per person**
- **Text-only message count** 
- **Reaction count**
- **Average characters per message**
- **Total words sent**
- **Top 10 most-used words per person** (stopwords filtered)

## 🧠 Learning Goals

This project is built as a learning-focused data analysis exercise:

- Python fundamentals
- JSON parsing
- Data cleaning
- Text processing
- Introductory NLP concepts
- Data analysis thinking

## 🔮 Future Versions

**Planned improvements:**

- Emoji usage analysis
- Response time analysis
- Conversation initiator detection
- Visualization (matplotlib)
- Sentiment analysis
- ML-based insights
