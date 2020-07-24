from visualiser import visualise


def bubble(data):

    for _ in range(len(data)):
        
        for i in range(len(data)):

            y=i+1




            if i==len(data)-1:
                pass
            elif i<len(data)-1:
                # print(data[i], data[y])
                if data[i]>data[y]:
                    # print("swapping")
                    data[i],data[y]=data[y],data[i]
                    # print(data)

                yield i



    return data




import random

numbers = [random.randint(1, 10) for _ in range(30)]
visualise(bubble, numbers, auto=0.01)
