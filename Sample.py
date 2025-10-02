# Task-14 File Handling in Python using r+, w+, a+
# Student Notes Manager 

filename = "student_notes.txt"

# 1. Create or overwrite notes (w+)
print("=== Example of 'w+' mode (Create/Overwrite) ===")
with open(filename, "w+") as f:
    f.write("Student Name: Mukarram\n")
    f.write("Course: Full Stack Development\n")
    f.write("Internship: VCodez\n")
    f.seek(0)  # Move cursor to start
    print("File after w+ :\n", f.read())

print("\n" + "-"*50 + "\n")

# 2. Update existing notes (r+)
print("=== Example of 'r+' mode (Read/Update) ===")
with open(filename, "r+") as f:
    print("Before update:\n", f.read())
    f.seek(0)   # Move to beginning
    f.write("Student Name: Mukarram T. Bambot\n")  # Update first line
    f.seek(0)
    print("After update:\n", f.read())

print("\n" + "-"*50 + "\n")

# 3. Add extra notes without losing data (a+)
print("=== Example of 'a+' mode (Append) ===")
with open(filename, "a+") as f:
    f.write("Remark: Completed 11 internship tasks successfully.\n")
    f.seek(0)   # Read full file again
    print("File after a+ :\n", f.read())
