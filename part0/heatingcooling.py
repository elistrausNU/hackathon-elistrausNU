def tempchecker():
    int_temp = 0
    heatingdays = 0
    coolingdays = 0
    while int_temp >= -459:
        temp = input("Enter the average daily temperature: ")
        int_temp = int(temp)
        if int_temp < 60 and int_temp >= -459:
            heatingdays = heatingdays + 1
        elif int_temp > 80:
            coolingdays = coolingdays + 1
        elif int_temp < -459:
            print('Heating days:', heatingdays),
            print('Cooling days:', coolingdays)

if __name__ == "__main__":
    tempchecker()