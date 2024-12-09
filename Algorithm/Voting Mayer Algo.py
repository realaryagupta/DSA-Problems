arr = [1,2,3,4,4,5,4,4,4]

count = 0 
candidate = None

for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count = count + 1
    else:
        count = count - 1
    
count = 0
for num in arr:
    if num == candidate:
        count = count + 1

if count > int(len(arr)/2):
    print(f"Max Number is {candidate}")
else:
    print("No max")