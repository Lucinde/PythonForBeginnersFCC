value = True
count = 0

while value:  # implies that while value is true or exists
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue  # continue starts from while again so the value is now false and the loop will end  # noqa: E501
