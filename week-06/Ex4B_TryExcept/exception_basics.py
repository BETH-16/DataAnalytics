# Description: This script practices handling exceptions using try/except blocks

# ValueError
# ─────────────────────────────────────────────
print("=== ValueError ===")
try:
    num = int("hello")
except ValueError:
    print("ValueError: Could not convert string to integer!")
else:
    print(f"Success! The number is {num}")
finally:
    print("Let's try another one...\n")

# Another ValueError example
print("=== ValueError (example 2) ===")
try:
    num = int("12.5")
except ValueError:
    print("ValueError: Could not convert decimal string to integer!")
else:
    print(f"Success! The number is {num}")
finally:
    print("Let's try another one...\n")

# ─────────────────────────────────────────────
# NameError
# ─────────────────────────────────────────────
print("=== NameError ===")
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable!")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# Another NameError example
print("=== NameError (example 2) ===")
try:
    print(undefined_variable)
except NameError:
    print("NameError: That variable does not exist!")
else:
    print("Success!")
finally:
    print("Let's try another one...\n")

# ─────────────────────────────────────────────
# TypeError
# ─────────────────────────────────────────────
print("=== TypeError ===")
try:
    result = "hello" + 5
except TypeError:
    print("TypeError: Cannot add a string and an integer together!")
else:
    print(f"Success! Result is {result}")
finally:
    print("Let's try another one...\n")

# Another TypeError example
print("=== TypeError (example 2) ===")
try:
    result = len(42)
except TypeError:
    print("TypeError: len() cannot be used on an integer!")
else:
    print(f"Success! Length is {result}")
finally:
    print("Let's try another one...\n")

# ─────────────────────────────────────────────
# ZeroDivisionError
# ─────────────────────────────────────────────
print("=== ZeroDivisionError ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide by zero!")
else:
    print(f"Success! Result is {result}")
finally:
    print("Let's try another one...\n")
