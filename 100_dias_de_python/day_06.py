def my_function(count): 
    print("---")
    if count == 0:
        print("It's true")

count = 0
while count < 5:
    print(count)
    my_function(count)
    count += 1

count = 0
while count < 10:
    if count % 2 == 0:
        print(f"{count} é par")
    else:
        print(f"{count} é ímpar")
    count += 1
    
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # Pula o resto do loop quando count é 5
    if count == 8:
        break  # Sai do loop quando count é 8
    print(count)
    
outer_count = 0
while outer_count < 3:
    inner_count = 0
    while inner_count < 3:
        print(f"outer_count: {outer_count}, inner_count: {inner_count}")
        inner_count += 1
    outer_count += 1