# Description: This script practices reading files

f = open('about_me.txt', 'r')
# print(f.read())
# f.close()

#print(f.read(50))
#print(f.read(50))

# print(f.readline(10))
# print(f.readline())

#for i in range(1, 5):
#    print(f.readline())

# print(f.readlines())

# Test 1:
#print(f.readlines(1))

#Test 2
#print(f.readlines(10))

# Test 3

# print(f.readlines(100))

#Test 4
# print(f.readlines(-1))

# a) First 50 characters
first_50 = f.read(50)

# b) Next 4 lines using readline() loop
next_lines = []
for i in range(1, 5):
    next_lines.append(f.readline())

# c) Next 100 characters as list of lines
next_100 = f.readlines(100)

f.close()

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")







