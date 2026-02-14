from risk import score_url
from db import save_scan

target = input("Enter URL: ")
result = score_url(target)

save_scan(target, result)

print("Scan Result:", result)
print("Saved to database")
