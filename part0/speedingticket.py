def speeding(limit, speed):
    total = speed - limit
    if total <= -10:
        return 50
    elif total >= 6 and total <= 20:
        return 75    
    elif total >= 21 and total <= 40:
        return 150
    elif total > 40:
        return 300
    else:
        return 0
    
if __name__ == "__main__":
    print(speeding(35,45))
    print(speeding(35,26))
    print(speeding(-35,26))


