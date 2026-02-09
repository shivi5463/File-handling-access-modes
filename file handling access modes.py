# write mode (w) – create/overwrite file
f = open("students.txt", "w")
f.write("Roy - Maths\n")
f.close()

# append mode (a) – add data
f = open("students.txt", "a")
f.write("Anita - Science\n")
f.close()

# read mode (r) – read file
f = open("students.txt", "r")
print(f.read())
f.close()
