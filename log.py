with open("log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

count = 0

for line in lines:
    if "ERROR" in line:
        print(line.strip())
        count += 1

print("Number of errors:", count)