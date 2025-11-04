N, M = map(int, input().split())
split_days_list = input().split("0")

logo_needed = 0
shirt_needed = 0
for split_days in split_days_list:
    shirt_needed = max(shirt_needed, len(split_days))
    event_count = 0
    for day in split_days:
        if day == "2":
            event_count += 1
    logo_needed = max(event_count, logo_needed)

shirt_needed = max(0, shirt_needed - M)
print(max(logo_needed, shirt_needed))
