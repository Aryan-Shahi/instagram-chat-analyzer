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



## 📋 Quick Updates Summary for Version 2:

**New features added:**
1. **Multi-chat analysis** - Processes entire `inbox/` directory
2. **Enhanced media tracking** - Photos, videos, audio, reels separately
3. **Better project structure** - Organized for scalability
4. **Improved word analysis** - More accurate frequency counting
5. **Most used words by each user** - Find the top 10 most used words by each user


# Instagram Chat Analyzer - Version 2
Version 2 introduces merging multiple chat files and analyzing the top 10 most used words per participant.

## Features (Version 2)
- **Merge multiple JSON chat files** from a conversation folder into a single dataset.
- **Top 10 words per participant**: Identify the most frequently used words in the conversation.
- **Media behavior summary**: Number of photos, videos, audio, and attachments sent by each participant.

## Project Structure
instagram_chat_analyzer/
├── data/
│   └── inbox/
│       ├── chat_folder_1/     # Instagram chat export folders
│       └── chat_folder_2/     # Each folder contains message_1.json, message_2.json, etc.
├── src/
│   └── main.py                # Main analysis script
├── outputs/                   # Future graphs / reports
└── README.md