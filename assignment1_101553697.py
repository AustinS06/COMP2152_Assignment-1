"""
Author: Austin Samms
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" 
preferred_weight_kg = 20.5
highest_reps = 25                  
membership_active = True

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (50, 40, 35)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [list(workout_stats[friend]) for friend in workout_stats if "_Total" not in friend]

# Step f: Slice the workout_list
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for friend in workout_stats:
    if "_Total" in friend and workout_stats[friend] >= 120:
        original_name = friend.replace("_Total", "")
        print(f"Great job staying active, {original_name}!")

# Step h: User input to look up a friend
user_input = input("Enter a friend's name: ")

if user_input in workout_stats:
    if "_Total" not in user_input:
        activities = workout_stats[user_input]
        total = workout_stats[user_input + "_Total"]
        print(f"{user_input}'s workout minutes:")
        print("Yoga:", activities[0])
        print("Running:", activities[1])
        print("Weightlifting:", activities[2])
        print("Total minutes:", total)
else:
    print(f"Friend {user_input} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals_only = {k: v for k, v in workout_stats.items() if "_Total" in k}

highest_friend = max(totals_only, key=totals_only.get)
lowest_friend = min(totals_only, key=totals_only.get)

print("Friend with highest total workout minutes:", highest_friend.replace("_Total", ""))
print("Friend with lowest total workout minutes:", lowest_friend.replace("_Total", ""))

