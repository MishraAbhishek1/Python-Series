# 4. Collect User Ratings

ratings = []
while True:
    rate = input("Enter rating(or 'stop'): ")
    if rate.lower() == 'stop':
        break
    ratings.append(int(rate))

print("Average Rating: ", sum(ratings)/len(ratings))