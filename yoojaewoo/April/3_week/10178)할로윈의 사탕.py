# 문제
# 할로윈데이에 한신이네는 아부지가 사탕을 나눠주신다.
# 하지만 한신이의 형제들은 서로 사이가 좋지않아 서른이 넘어서도 사탕을 공정하게 나누어 주지 않으면 서로 싸움이 난다.
# 매년 할로윈데이때마다 아부지는 사탕을 자식들에게 최대한 많은 사탕을 나누어 주시기 원하며 자신에게는 몇개가 남게되는지에 알고 싶어 하신다.
# 이런 아부지를 도와서 형제간의 싸움을 막아보자.

# 입력
# 가장 첫 번째 줄에는 테스트 케이스의 수가 입력되고, 각 테스트 케이스마다 사탕의 개수 c와 형제의 수 v가 차례대로 입력된다.

# 출력
# 출력은 예제를 보고 ”You get __ piece(s) and your dad gets __ piece(s).” 형식에 맞추어 적절하게 출력하라.

# 제한
# 1 ≤ c, v ≤ 1,000

# 예제 입력 1
# 5
# 22 3
# 15 5
# 99 8
# 7 4
# 101 5

# 예제 출력 1
# You get 7 piece(s) and your dad gets 1 piece(s).
# You get 3 piece(s) and your dad gets 0 piece(s).
# You get 12 piece(s) and your dad gets 3 piece(s).
# You get 1 piece(s) and your dad gets 3 piece(s).
# You get 20 piece(s) and your dad gets 1 piece(s).

# 첫번째 시도
# case = int(input())
# for _ in range(case):
#     c, v = map(int, input())
#     print("You get {0} piece(s) and your dad gets {1} piece(s).".format(c % v, c // v))

# 두번째 시도
# case = int(input())
# for _ in range(case):
#     c, v = map(int, input())
#     print("You get {0} piece(s) and your dad gets {1} piece(s).".format((c // v), (c % v)))

# 정답
for _ in range(int(input())):
    c, v = map(int, input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(
        c // v, c % v))
