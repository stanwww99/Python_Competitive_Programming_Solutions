#USACO 2024 December Silver P3 - 2D Conveyor Belt
import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]   # L, R, U, D
dc = [-1, 1, 0, 0]

def dirIndex(ch):
    if ch == 'L': return 0
    if ch == 'R': return 1
    if ch == 'U': return 2
    return 3  # 'D'

def inBounds(r, c, N):
    return 0 <= r < N and 0 <= c < N

def pointsTo(grid, fromR, fromC, toR, toC):
    ch = grid[fromR][fromC]
    if ch == '?':
        return True
    d = dirIndex(ch)
    nr = fromR + dr[d]
    nc = fromC + dc[d]
    return nr == toR and nc == toC

def canExitDirectly(grid, r, c, N):
    ch = grid[r][c]
    if ch == '?':
        return r == 0 or r == N - 1 or c == 0 or c == N - 1
    d = dirIndex(ch)
    nr = r + dr[d]
    nc = c + dc[d]
    return not inBounds(nr, nc, N)

def initialBFS(grid, N):
    good = [[False]*N for _ in range(N)]
    dq = deque()
    goodCount = 0

    # Seed with cells that can exit
    for r in range(N):
        for c in range(N):
            if canExitDirectly(grid, r, c, N):
                good[r][c] = True
                goodCount += 1
                dq.append((r, c))

    # Reverse BFS
    while dq:
        r, c = dq.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not inBounds(nr, nc, N):
                continue
            if good[nr][nc]:
                continue
            if grid[nr][nc] == '?' or pointsTo(grid, nr, nc, r, c):
                good[nr][nc] = True
                goodCount += 1
                dq.append((nr, nc))

    return good, goodCount

def expandFrom(grid, good, N, sr, sc, goodCount):
    dq = deque()
    good[sr][sc] = True
    goodCount += 1
    dq.append((sr, sc))

    while dq:
        r, c = dq.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not inBounds(nr, nc, N):
                continue
            if good[nr][nc]:
                continue
            if grid[nr][nc] == '?' or pointsTo(grid, nr, nc, r, c):
                good[nr][nc] = True
                goodCount += 1
                dq.append((nr, nc))

    return goodCount


def main():
    N, Q = map(int, input().split())
    qr = [0]*Q
    qc = [0]*Q
    qt = ['?']*Q

    grid = [['?']*N for _ in range(N)]

    for i in range(Q):
        r, c, ch = input().split()
        r = int(r) - 1
        c = int(c) - 1
        qr[i] = r
        qc[i] = c
        qt[i] = ch

    # Apply all queries
    for i in range(Q):
        grid[qr[i]][qc[i]] = qt[i]

    # Compute initial good cells
    good, goodCount = initialBFS(grid, N)

    total = N * N
    ans = [0]*Q
    ans[Q-1] = total - goodCount

    # Reverse process
    for i in range(Q-1, 0, -1):
        r = qr[i]
        c = qc[i]

        # Remove belt
        grid[r][c] = '?'

        if not good[r][c]:
            becomesGood = False

            if canExitDirectly(grid, r, c, N):
                becomesGood = True
            else:
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if inBounds(nr, nc, N) and good[nr][nc]:
                        becomesGood = True
                        break

            if becomesGood:
                goodCount = expandFrom(grid, good, N, r, c, goodCount)

        ans[i-1] = total - goodCount

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
