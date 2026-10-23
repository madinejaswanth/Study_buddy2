# 📚 Study Buddy

**Study Buddy** is a Python-based study management application designed to help students improve their learning habits, track study time, revise topics using flashcards, and monitor their daily study progress.

## ✨ Features

- **Study Timer:** Track study sessions by subject and duration.
- **Study Streak Tracker:** Maintain a record of consecutive days of studying.
- **Flashcard Management:** Create flashcards with questions and answers for different subjects.
- **Revision Mode:** Review flashcards in a randomized order to improve memory and understanding.
- **Study Report:** View total study time, subject-wise study minutes, and percentage distribution.
- **Data Persistence:** Save study records and flashcards locally in a JSON file.
- **Input Validation:** Handle invalid study durations and empty fields.

## 🛠️ Technologies Used

- **Python** — Core programming language.
- **JSON** — Stores study records and flashcard data.
- **Pathlib** — Handles file paths and checks whether the data file exists.
- **Random** — Shuffles flashcards during revision.
- **Time** — Implements the study timer.
- **Datetime** — Tracks study dates and daily streaks.

## 📂 Project Structure

```text
Study-Buddy/
│
├── study_buddy.py
├── study_data.json
└── README.md
```

**Note:** `study_data.json` is created when the application saves data for the first time.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Study-Buddy
```

### 3. Run the Application

Make sure Python 3 is installed on your system.

```bash
python study_buddy.py
```

On some systems, use:

```bash
python3 study_buddy.py
```

No external Python packages are required.

## 🚀 How to Use

After running the application, the following menu appears:

```text
===== Study Buddy =====
1. Start study session
2. Add flashcard
3. Revise flashcards
4. View study report
5. Exit
```

### 1. Start Study Session
- Enter the subject you want to study.
- Enter the study duration in minutes.
- The application tracks completed minutes.
- Press `Ctrl+C` to stop the session early.
- Completed study time is saved automatically.

### 2. Add Flashcard
- Enter a subject.
- Enter a question.
- Enter the answer.
- The flashcard is saved for future revision.

### 3. Revise Flashcards
- Review flashcards in random order.
- Press Enter to reveal each answer.
- Choose whether to continue revising.

### 4. View Study
