seconds = int(input("Enter seconds: "))

hours = seconds // 3600

minutes = (seconds // 60 ) % 60

last_seconds = seconds % 60

print("Hours", hours)
print("Minutes", minutes)
print("Seconds", last_seconds)