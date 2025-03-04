import csv
import os


def main():
    tracker = HabitTracker()
    tracker.load_habits_from_csv()
    while True:
        print("\n1. Add Habit")
        print("2. Log Habit")
        print("3. View Progress")
        print("4. Reset Habit")
        print("5. Show Habits")
        print("6. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            habit_name = input("Enter the name of the habit: ").strip()
            add_habit(tracker, habit_name)
        elif choice == '2':
            habit_name = input("Enter the name of the habit to log: ").strip()
            log_habit(tracker, habit_name)
        elif choice == '3':
            view_progress(tracker)
        elif choice == '4':
            habit_name = input("Enter the name of the habit to reset: ").strip()
            reset_habit(tracker, habit_name)
        elif choice == '5':
            show_habits(tracker)
        elif choice == '6':
            tracker.save_habits_to_csv()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def add_habit(tracker, habit_name):
    if habit_name not in tracker.habits:
        tracker.habits[habit_name] = 0
        print(f"Habit '{habit_name}' added!")
    else:
        print(f"Habit '{habit_name}' already exists.")


def log_habit(tracker, habit_name):
    if habit_name in tracker.habits:
        tracker.habits[habit_name] += 1
        print(f"Logged '{habit_name}'! Total days: {tracker.habits[habit_name]}")
    else:
        print(f"Habit '{habit_name}' does not exist. Add it first.")


def view_progress(tracker):
    if not tracker.habits:
        print("No habits tracked yet.")
    else:
        print("Habit Progress:")
        for habit, days in tracker.habits.items():
            print(f"{habit}: {days} day(s)")


def reset_habit(tracker, habit_name):
    if habit_name in tracker.habits:
        tracker.habits[habit_name] = 0
        print(f"'{habit_name}' has been reset to 0 days.")
    else:
        print(f"Habit '{habit_name}' does not exist.")


def show_habits(tracker):
    if not tracker.habits:
        print("No habits tracked yet.")
    else:
        print("Tracked Habits:")
        for habit in tracker.habits:
            print(f"- {habit}")


class HabitTracker:
    def __init__(self):
        self.habits = {}

    def load_habits_from_csv(self, filename="habits.csv"):
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        habit, count = row
                        self.habits[habit] = int(count)

    def save_habits_to_csv(self, filename="habits.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for habit, count in self.habits.items():
                writer.writerow([habit, count])


if __name__ == "__main__":
    main()
    