# Step 1: Create lists for each workshop
web_dev = ["Arjun", "Neha", "Vivek"]
data_science = ["Riya", "Kiran", "Ananya"]
ui_ux = ["Meera", "Rahul", "Sneha"]

# Step 2: Combine all three into a nested list
all_participants = [web_dev, data_science, ui_ux]
print("All participants:", all_participants)

# Step 3: Add a new participant to Web Development
web_dev.append("Divya")
print("Updated Web Development list:", web_dev)

# Step 4: Insert one participant at 2nd position in Data Science
data_science.insert(1, "Amit")
print("Updated Data Science list:", data_science)

# Step 5: Remove the last participant from UI/UX Design
ui_ux.pop()
print("Updated UI/UX Design list:", ui_ux)

# Step 6: Copy Data Science list and clear original
copied_data_science = data_science.copy()
data_science.clear()
print("Copied Data Science list:", copied_data_science)
print("Original Data Science list after clearing:", data_science)

# Step 7: Display only the first two participants in Web Development
print("First two Web Development participants:", web_dev[:2])

# Step 8: List comprehension for length of each name in copied Data Science list
name_lengths = [len(name) for name in copied_data_science]
print("Length of each name in copied Data Science list:", name_lengths)

# Step 9: Check whether “Asha” is in any workshop list
is_asha_present = any("Asha" in workshop for workshop in [web_dev, copied_data_science, ui_ux])
print("Is 'Asha' in any list?", is_asha_present)

# Step 10: Create a tuple with first participant from each workshop
# (Use copied_data_science since original was cleared)
first_participants = (web_dev[0], copied_data_science[0], ui_ux[0])
print("Tuple of first participants from each workshop:", first_participants)
