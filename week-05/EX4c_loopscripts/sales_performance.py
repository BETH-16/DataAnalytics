# Step # 2: Sales data — list of tuples
# ─────────────────────────────────────────────
sales_data = [
    ('Marcus Webb',    'East',  4250.00),
    ('Priya Sharma',   'West',  5875.50),
    ('DeShawn Carter', 'East',  3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen',     'West',  4980.25),
]

# ─────────────────────────────────────────────
# BONUS: Variable to track total sales
# ─────────────────────────────────────────────
total_sales = 0.00

# ─────────────────────────────────────────────
# Step 3, 4 & BONUS: Loop through sales data
# ─────────────────────────────────────────────
for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")

    # Step 4: Flag top performers
    if sales > 5000:
        print(" ^ Top performer!")

    # BONUS: Add to running total
    total_sales += sales

# ─────────────────────────────────────────────
# BONUS: Print overall total after loop
# ─────────────────────────────────────────────
print(f"\nTotal Sales (All Regions): ${total_sales:,.2f}")