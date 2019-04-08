n, k, x = map(int, raw_input().split())
array = map(int, raw_input().split())

maximumBalls = 0
begin = -1
end = -1

def ballsLeft(index, array):
    color = array[index]
    balls = 0
    while index >= 0 and array[index] == color:
        balls += 1
        index -= 1
    return balls

def ballsRight(index, array):
    color = array[index]
    balls = 0
    while index < len(array) and array[index] == color:
        balls += 1
        index += 1
    return balls

for i in range(len(array)):
    if array[i] == x:
        begin = i if (i == 0 or array[i - 1] != x) else begin
        if i == len(array) - 1:
            end = i
            totalBalls = end - begin + 1
            maximumBalls = totalBalls if totalBalls > maximumBalls and totalBalls > 1 else maximumBalls
    else:
        end = i - 1 if (i != 0 and array[i - 1] == x) else end
        if i != 0 or array[i - 1] == x:
            if begin > 0 and end < len(array) and array[begin - 1] == array[end + 1]:
                ballOnLeft = ballsLeft(begin - 1, array) 
                balllsOnRight = ballsRight(end + 1, array)
                ballsColor = end - begin + 1
                totalBalls = 0
                if ballsColor > 1:
                    totalBalls += ballsColor
                if ballsColor > 1 and ballOnLeft > 0 and balllsOnRight > 0 and (ballOnLeft + balllsOnRight) > 2:
                    totalBalls += (ballOnLeft + balllsOnRight)
                maximumBalls = totalBalls if totalBalls > maximumBalls else maximumBalls
            else:
                ballsColor = end - begin + 1
                if ballsColor > 1 and ballsColor > maximumBalls:
                    maximumBalls = ballsColor


print maximumBalls