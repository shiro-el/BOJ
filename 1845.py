import sys

def dist_info(s, n):
    m = 2 * n + 2
    u = [0] * m
    for i in range(1, n + 1):
        x = s[i]
        if x > 0:
            u[2 * i - 1], u[2 * i] = 2 * x - 1, 2 * x
        else:
            u[2 * i - 1], u[2 * i] = -2 * x, -2 * x - 1
    u[m - 1] = m - 1
    pos = [0] * m
    for i, v in enumerate(u):
        pos[v] = i
    
    seen = [False] * m
    cyc = 0
    cyc_id = [-1] * m
    for st in range(m):
        if seen[st]:
            continue
        p = st
        while not seen[p]:
            seen[p] = True
            cyc_id[p] = cyc
            q = p ^ 1 
            seen[q] = True
            cyc_id[q] = cyc
            v = u[q]
            w = v ^ 1
            p = pos[w]
        cyc += 1
        
    E = []
    for k in range(n + 1):
        a, b = pos[2 * k], pos[2 * k + 1]
        if a > b:
            a, b = b, a
        if b == a + 1 and a % 2 == 0:
            continue
        E.append((a, b, (a - b) % 2 == 0))
    E = len(E)
    par = list(range(E))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for i in range(E):
        a1, b1, _ = E[i]
        for j in range(i + 1, E):
            a2, b2, _ = E[j]
            if (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1):
                ri, rj = find(i), find(j)
                if ri != rj:
                    par[ri] = rj
                    
    first = {}
    for i in range(E):
        c = cyc_id[E[i][0]]
        if c in first:
            ri, rj = find(i), find(first[c])
            if ri != rj:
                par[ri] = rj
        else:
            first[c] = i
    oriented = {}
    for i in range(E):
        r = find(i)
        oriented[r] = oriented.get(r, False) or E[i][2]
    owner = [-1] * m
    for i in range(E):
        r = find(i)
        if not oriented[r]:
            owner[E[i][0]] = r
            owner[E[i][1]] = r
    lst = [owner[p] for p in range(m) if owner[p] != -1]

    def hurdles(lst):
        comps = set(lst)
        if len(comps) == 1:
            return list(comps)
        trans = {}
        L = len(lst)
        for t in range(L):
            if lst[t] != lst[t - 1]:
                trans[lst[t]] = trans.get(lst[t], 0) + 1
        return [c for c in comps if trans[c] == 1]

    hs = hurdles(lst) if lst else []
    h = len(hs)
    f = 0
    if h % 2 == 1 and h >= 3:
        allsuper = True
        hset = set(hs)
        for H in hs:
            rest = [x for x in lst if x != H]
            nh = hurdles(rest)
            if not any(c not in hset for c in nh):
                allsuper = False
                break
        if allsuper:
            f = 1
    d = n + 1 - cyc + h + f
    return d, hs, E, find, cyc_id


def rev(s, a, b):
    s[a:b + 1] = [-x for x in reversed(s[a:b + 1])]


def solve(n, arr):
    s = [0] + arr + [n + 1]
    ops = []
    full = (1 << (n + 1)) - 1
    while True:
        pos = [0] * (n + 2)
        neg = 0
        for i, x in enumerate(s):
            pos[abs(x)] = i
            if x < 0:
                neg |= 1 << (-x)
        if all(s[i] == i for i in range(n + 2)):
            break
        pref = [0] * (n + 3)
        for i in range(n + 2):
            pref[i + 1] = pref[i] | (1 << abs(s[i]))
        best = None
        for k in range(n + 1):
            i, j = pos[k], pos[k + 1]
            if (s[i] < 0) == (s[j] < 0):
                continue
            if i > j:
                i, j = j, i
            if s[i] + s[j] == 1:
                a, b = i, j - 1
            else:
                a, b = i + 1, j
            X = neg ^ pref[b + 1] ^ pref[a]
            sc = bin((X ^ (X >> 1)) & full).count("1")
            if best is None or sc > best[0]:
                best = (sc, a, b)
        if best is not None:
            rev(s, best[1], best[2])
            ops.append((best[1], best[2]))
            continue
        
        d, hs, edges, find, cyc_id = dist_info(s, n)
        
        hb = {}
        hcyc = {}
        for idx, (a, b, _) in enumerate(edges):
            r = find(idx)
            if r in hs:
                for p in (a, b):
                    bi = p // 2
                    hb.setdefault(r, set()).add(bi)
                    hcyc.setdefault((r, cyc_id[p]), set()).add(bi)
        cands = []
        h = len(hs)
        order = sorted(hs, key=lambda r: min(hb[r]))
        if h % 2 == 0 or h >= 3:
            if h == 2:
                pairs = [(0, 1)]
            else:
                pairs = [(0, 2)] + [(x, y) for x in range(h) for y in range(x + 1, h)]
            for x, y in pairs[:1]:
                cands.append(("m", order[x], order[y]))
        for r in order:
            cands.append(("c", r, None))
        for x in range(h):
            for y in range(x + 1, h):
                cands.append(("m", order[x], order[y]))
                
        for typ, r1, r2 in cands:
            if typ == "m":
                b1 = min(hb[r1]); b2 = min(hb[r2])
            else:
                cs = [v for (r, c), v in hcyc.items() if r == r1 and len(v) >= 2]
                if not cs:
                    continue
                v = sorted(cs[0])
                b1, b2 = v[0], v[1]
            i, j = min(b1, b2), max(b1, b2)
            a, b = i + 1, j
            t = s[:]
            rev(t, a, b)
            if dist_info(t, n)[0] == d - 1:
                s = t
                ops.append((a, b))
                break
    return ops[::-1]


data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:1 + n]))
ops = solve(n, arr)
out = [str(len(ops))] + [f"{a} {b}" for a, b in ops]
print("\n".join(out))

