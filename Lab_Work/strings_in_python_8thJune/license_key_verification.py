#Program for license key verification
license_key="ABCD-EFGH-IJKL-MNOP"

#TASK 1. Create list of groups
groups=license_key.split("-")

#TASK 2. Verify there are exactly 4 groups
valid=False

if len(groups)==4:
    valid = True

# Verify each group has exactly 4 characters
    for group in groups:
        if len(group)!=4:
            valid=False

#TASK 3. Count total letters
letter_count=0
for ch in license_key:
    if ch.isalpha():
        letter_count+=1

#TASK 4. Count vowels
vowel_count=0

for ch in license_key:
    if ch.upper() in "AEIOU":
        vowel_count+=1

#TAK 5. Remove hyphens
merged_key=license_key.replace("-", "")

# Display Results
print("License Key:", license_key)
print("Groups:", groups)
print("Number of Groups:", len(groups))
print("Total Letters:", letter_count)
print("Total Vowels:", vowel_count)
print("Merged Key:", merged_key)

if valid==True:
    print("Key Format is VALID")
else:
    print("Key Format is INVALID")