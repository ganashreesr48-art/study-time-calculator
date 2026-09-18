# study-time-calculator
A simple python program to calculate total study time
# Study Time Calculator

print("===== STUDY TIME CALCULATOR =====")

topics = int(input("Enter number of topics: "))
time_per_topic = float(input("Average time per topic (minutes): "))
sessions = int(input("Enter number of study sessions: "))
break_time = float(input("Break time per session (minutes): "))

study_time = topics * time_per_topic
total_break = (sessions - 1) * break_time
total_time = study_time + total_break

hours = int(total_time // 60)
minutes = int(total_time % 60)

print("\n===== RESULT =====")
print(f"Study time: {study_time:.0f} minutes")
print(f"Break time: {total_break:.0f} minutes")
print(f"Total time required: {hours} hours {minutes} minutes")

if total_time <= 120:
    print("Suggestion: You can complete this in one sitting.")
elif total_time <= 300:
    print("Suggestion: Divide your study into multiple sessions.")
else:
    print("Suggestion: Make a study plan across multiple days.")
