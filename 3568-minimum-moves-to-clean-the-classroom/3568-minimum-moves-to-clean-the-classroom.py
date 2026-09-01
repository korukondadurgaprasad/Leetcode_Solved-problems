class Solution(object):

    def minMoves(self, classroom, energy):
        from collections import deque

        m = len(classroom)
        n = len(classroom[0])

        # Find start and litter positions
        sr = sc = 0
        litter = {}

        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]

                if ch == 'S':
                    sr, sc = r, c
                elif ch == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        full = (1 << k) - 1

        # best[(r,c,mask)] = maximum energy with which
        # we have reached this position having this mask.
        best = {}

        start = (sr, sc, 0)
        best[start] = energy

        q = deque()
        q.append((sr, sc, energy, 0))

        moves = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == full:
                    return moves

                # This state may have become dominated by
                # another path with more energy.
                if best.get((r, c, mask), -1) != e:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Need 1 energy to make the move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        bit = 1 << litter[(nr, nc)]
                        nmask |= bit

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    # Only keep the state if it gives us
                    # strictly more energy than before.
                    if ne > best.get(key, -1):
                        best[key] = ne
                        q.append((nr, nc, ne, nmask))

            moves += 1

        return -1