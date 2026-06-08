#Program for text compression analyzer
message="AAABBBCCCDDDAAA"

#TASK 1 & 2. Count occurrences and create frequency dictionary
freq={}

for ch in message:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch] = 1

#TASK 3. Display unique characters
unique_chars=[]
for ch in message:
    if unique_chars.count(ch)==0:
        unique_chars.append(ch)

#TASK 4. Find most frequent character
most_char=list(freq.keys())[0]
for ch in freq:
    if freq[ch]>freq[most_char]:
        most_char=ch

#TASK 5. Create compressed output
compressed=""
current_char=message[0]
count=1

for i in range(1,len(message)):

    if message[i]==current_char:
        count+=1
    else:
        compressed=compressed+current_char+str(count)
        current_char=message[i]
        count=1

compressed=compressed+current_char+str(count)

#TASK 6. Calculate compression ratio
original_length=len(message)
compressed_length=len(compressed)

compression_ratio=compressed_length/original_length

# Display Results
print("Original Message:", message)
print("Character Frequencies:", freq)
print("Unique Characters:", unique_chars)
print("Most Frequent Character:", most_char)
print("Compressed Output:", compressed)
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", compression_ratio)