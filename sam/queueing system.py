num = 6
interArrivalTime = [0, 2, 4, 1, 2, 6]
serviceTime = [2, 1, 3, 2, 1, 4]

serviceStart = []
serviceEnd = []
waitingTime = []
idleTime = 0

arrivalTime = []
sum1 = 0
for i in range(num):
    sum1 = sum1 + interArrivalTime[i]
    arrivalTime.append(sum1)

for i in range(num):
    if i == 0:
        serviceStart1 = arrivalTime[i]
        serviceStart.append(serviceStart1)

    elif serviceEnd[i-1] == arrivalTime[i]:
        serviceStart1 = arrivalTime[i]
        serviceStart.append(serviceStart1)

    else:
        serviceStart1 = max(serviceEnd[i-1], arrivalTime[i])
        serviceStart.append(serviceStart1)

    serviceEnd1 = serviceStart[i] + serviceTime[i]
    serviceEnd.append(serviceEnd1)
    waitingTime1 = serviceStart[i] - arrivalTime[i]
    waitingTime.append(waitingTime1)

# Printing the results in table
print("\nCustomers\tInter-arrival\t   Arrival\tService_Start\tService_Duration\tService_End\tWaiting_Time")
for i in range(num):
    print(f"\n\t{i+1}\t\t{interArrivalTime[i]}\t\t{arrivalTime[i]}\t\t{serviceStart[i]}\t\t{serviceTime[i]}"
          f"\t\t\t{serviceEnd[i]}\t\t{waitingTime[i]}")

# calculating the idle time
for i in range(num):
    if i-1 >= 0:
        idleTime = idleTime + (serviceStart[i] - serviceEnd[i-1])

# Probability of servers utilization
totalRunTime = serviceEnd[-1] - serviceStart[0]
serverUtilize = totalRunTime - idleTime
probServerUtilize = serverUtilize / serviceEnd[-1]
print(f"\nProbability of server utilization is {round(probServerUtilize, 2)}")

# Probability of servers being idle
probIdleTime = idleTime / serviceEnd[-1]
print(f"Probability of server being idle is {round(probIdleTime, 2)}")

# average time spent in system per customer
timeInSystem = 0
for i in range(num):
    timeInSystem = timeInSystem + (serviceEnd[i] - arrivalTime[i])
print(f"Average time spent in the system per customer is {round(timeInSystem/num, 2)}")

# average time spent in queue per customer
timeInQueue = sum(waitingTime)
print(f"Average time spent in the queue per customer is {round(timeInQueue/num, 2)}")

