# Variable — change to test different hours
# ─────────────────────────────────────────────
hour = 23  # 0-23 format

# ─────────────────────────────────────────────
# Step 1 & 2: Greeting based on hour
# ─────────────────────────────────────────────
if hour >= 23 or hour < 4:
    print("What are you doing up so late??")
elif hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")
else:
    print("Good evening!")