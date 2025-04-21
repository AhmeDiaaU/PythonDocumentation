def counter(distance):
    _steps = [1,2,3,4,5]
    counter = 0 
    if distance in _steps:
        return 1
    else :
        while distance > 0 :
            if distance > _steps[-1]:
                distance -= _steps[-1]
                counter +=1
            if distance <= _steps[-1]:
                counter +=1
                break
    return counter

if __name__ == "__main__":
    distance = int(input())
    print(counter(distance))