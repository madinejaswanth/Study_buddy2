import json
import random
import time
from pathlib import Path
from datetime import datetime, date

DATA_FILE = Path("study_data.json")


def load_data():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())

    return {
        "study_minutes": {},
        "flashcards": [], 
        "streak": 0,
        "last_study_date": None
    }


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))


def study_timer():
    data = load_data()
    subject = input("Which subject are you studying? ").strip()

    if not subject:
        print("Subject cannot be empty.")
        return

    try:
        minutes = int(input("Study duration in minutes: "))
        if minutes <= 0:
            print("Enter a positive number.")
            return
    except ValueError:
        print("Invalid number.")
        return

    print(f"\nStudying {subject} for {minutes} minutes...")
    print("Press Ctrl+C to stop early.\n")

    studied_minutes = 0

    try:
        for minute in range(minutes):
            time.sleep(60)
            studied_minutes += 1
            print(f"{studied_minutes} minute(s) completed.")
    except KeyboardInterrupt:
        print("\nSession stopped early.")

    if studied_minutes == 0:
        print("No time recorded.")
        return

    today = str(date.today())
    data["study_minutes"][subject] = data["study_minutes"].get(subject, 0) + studied_minutes

    if data["last_study_date"] != today:
        yesterday = str(date.fromordinal(date.today().toordinal() - 1))

        if data["last_study_date"] == yesterday:
            data["streak"] += 1
        else:
            data["streak"] = 1

        data["last_study_date"] = today

    save_data(data)

    print(f"\nGreat job! You studied {subject} for {studied_minutes} minutes.")
    print(f"Current streak: {data['streak']} day(s).")


def add_flashcard():
    data = load_data()
    subject = input("Subject: ").strip()
    question = input("Question: ").strip()
    answer = input("Answer: ").strip()

    if subject and question and answer:
        data["flashcards"].append({
            "subject": subject,
            "question": question,
            "answer": answer
        })
        save_data(data)
        print("Flashcard added.")
    else:
        print("All fields are required.")


def revise_flashcards():
    data = load_data()

    if not data["flashcards"]:
        print("No flashcards available. Add some first.")
        return

    cards = data["flashcards"][:]
    random.shuffle(cards)

    print("\nRevision mode. Press Enter to see the answer.\n")

    for card in cards:
        print(f"[{card['subject']}] {card['question']}")
        input("Press Enter to reveal answer...")
        print(f"Answer: {card['answer']}\n")

        again = input("Continue? (y/n): ").strip().lower()
        if again != "y":
            break


def study_report():
    data = load_data()

    if not data["study_minutes"]:
        print("No study data available yet.")
        return

    total_minutes = sum(data["study_minutes"].values())

    print("\n===== Study Report =====")
    print(f"Total study time: {total_minutes} minutes")
    print(f"Current streak: {data['streak']} day(s)")
    print("\nSubject-wise time:")

    for subject, minutes in sorted(
        data["study_minutes"].items(),
        key=lambda item: item[1],
        reverse=True
    ):
        percentage = (minutes / total_minutes) * 100
        print(f"{subject:<20} {minutes:>5} min ({percentage:.1f}%)")


def main():
    while True:
        print("\n===== Study Buddy =====")
        print("1. Start study session")
        print("2. Add flashcard")
        print("3. Revise flashcards")
        print("4. View study report")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            study_timer()
        elif choice == "2":
            add_flashcard()
        elif choice == "3":
            revise_flashcards()
        elif choice == "4":
            study_report()
        elif choice == "5":
            print("Keep studying!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()