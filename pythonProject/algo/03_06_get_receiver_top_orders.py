# Q 수평직선에 탑N대를 세웠씁니다.
# 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치.
# 높이가 4인 다섯번째 탑에서 발사한 신호는 높이 7인 7번째 탑에서 쉰.
#  높이 7  네번째 탑 신호 높이 9
# 높이 5  신ㅎ높이 9 두번째 탑
# 6, 9, 5, 7, 4
# I         <- 레이저
# I
# I I
# II I
# IIII
# IIIII
# IIIII
# IIIII
# IIIII
# 왼쪾 에 있는 탑이 신호를 받아줌.
# 0, 0, 2, 2, 4
top_heights = [6, 9, 5, 7, 4]


# 0 1 4 7
# 0 2 4 5
# 0 3 4 9
# 0 4 4 6

# 1 2 7 5
# 1 3 7 9
# 1 4 7 6

# 2 3 5 9
# 2 4 5 6

# 3 4 9 6
def get_receiver_top_orders(heights):
    heights_size = len(heights);
    result = [0 for i in range(heights_size)]

    for x in range(heights_size):
        for y in range(1 + x, heights_size):
            now = top_heights[heights_size - x - 1]
            left = top_heights[heights_size - y - 1]
            # print(x,y,now,left)
            if top_heights[heights_size - x - 1] <= top_heights[heights_size - y - 1]:
                result[heights_size - x - 1] = heights_size - y
                # print(x, y, now, left)
                break
    return result

#O(N^2)
def get_receiver_top_orders2(heights):

    result = [0] * len(heights)

    while heights:
        height = heights.pop()
        for idx in range(len(heights)-1,0,-1):
            #print(idx)
            if heights[idx]>height:
                result[len(heights)] = idx + 1
                break

    return result


print(get_receiver_top_orders2(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
