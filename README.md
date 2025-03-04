# CS50P_project
CS50P  graduation project (habit tracker)
#### Video Demo:  https://www.youtube.com/watch?v=ADuftwrVsdI
#### Description:
A simple Python program to track and edit habits and their daily streaks is described below.

The program begins by initializing a class with a dictionary that starts empty. It checks if there is a previous history of habits stored in a CSV file, which should have been created during a prior use of the program. If it finds this file, it imports the data into the dictionary. The dictionary contains key-value pairs where the key is the name of the habit and the value is its current streak. If there is no previous history, the initialized dictionary remains empty.

The program enters an infinite loop with `while True`, which only exits when the user decides to quit. It consistently displays instructions, allowing users to choose from the following options:

1. **Add a New Habit**: If the user inputs '1', the program prompts them to add a new habit to track. If the habit is new, it adds it to the dictionary and assigns a streak of 0. The program then displays a confirmation message. If the habit already exists in the dictionary, it notifies the user and presents the options again.

2. **Log a Habit**: If '2' is entered, the program asks which habit to log. Upon receiving an existing habit, it increments the value associated with that habit and displays a confirmation message along with the current streak. If the habit does not exist, it informs the user that they must add the habit before logging it and repeats the instructions.

3. **View Progress**: Selecting '3' will show a list of all habits along with their respective streaks.

4. **Reset a Habit**: If the user loses the streak of a habit and wants to reset it, they can select '4'. The program prompts for the habit name to reset. Upon providing a valid name, it resets the value in the dictionary back to zero and displays a confirmation message. If the habit does not exist, an error message is displayed, and the instructions are shown again.

5. **Show Habits**: By entering '5', the user can view a list of all the habit names. This option helps prevent errors due to typos or mistakenly adding the same habit with a different spelling. Although it may seem redundant, it serves as an informational tool to view habits without their streaks.

6. **Quit**: If '6' is selected, the program saves the current progress. If the original CSV file exists, it updates it; if this is the first use, it creates a new CSV file to store progress for future use. Finally, the program breaks the loop and displays a "Goodbye" message.

This structure helps users effectively manage their habits and track their progress.
