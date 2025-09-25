import time

while True:
    number = input("Insert any number that shows your love: ")

    if not number.isdigit():
        print("❌ Please insert a NUMBER!")
        continue

    number = int(number)

    if number > 1000:
        print("❌ You cannot insert a number greater than 1000!")
        continue
    
    break

for i in range(1, number + 1):
    time.sleep(1)
    print(f"❤️ I love Jadi {i} time")