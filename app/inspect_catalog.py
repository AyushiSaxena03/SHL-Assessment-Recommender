import json

with open("data/shl_catalog.json", "r", encoding="utf-8") as file:
    text = file.read()

# Invalid newline ko remove karo jo JSON strings ke andar aa gaya hai
text = text.replace("Microsoft \n    365 (New)", "Microsoft 365 (New)")

data = json.loads(text)

print("Total Assessments:", len(data))
print("\nKeys:")
print(data[0].keys())

print("\nFirst Assessment:\n")
for key, value in data[0].items():
    print(f"{key}: {value}")

missing_description = 0
missing_duration = 0
missing_languages = 0

for assessment in data:
    if not assessment["description"].strip():
        missing_description += 1

    if not assessment["duration"].strip():
        missing_duration += 1

    if len(assessment["languages"]) == 0:
        missing_languages += 1

print("\n----- DATA QUALITY -----")
print("Missing Description :", missing_description)
print("Missing Duration    :", missing_duration)
print("Missing Languages   :", missing_languages)