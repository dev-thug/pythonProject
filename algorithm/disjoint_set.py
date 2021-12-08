N = 0  # 원소 개수
parents = []  # 부모원소를 관리(트리처럼 사용)


# 모든 원소를 자신을 대표자로 만듦
for i in range(N):
    parents[i] = i


# a가 속한 집합의 대표자 찾기
def find(parents, a):
    if a==parents[a]:
        return a
    
