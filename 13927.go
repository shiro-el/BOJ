package main

import (
	"bufio"
	"math/bits"
	"os"
	"sort"
	"strconv"
)

type bitVector struct {
	words  []uint64
	prefix []int32
}

func (bv *bitVector) rank1(idx int32) int32 {
	w := idx >> 6
	mask := (uint64(1) << (uint(idx) & 63)) - 1
	return bv.prefix[w] + int32(bits.OnesCount64(bv.words[w]&mask))
}

type waveletMatrix struct {
	levels int
	zeros  []int32
	bvs    []bitVector
}

func buildWaveletMatrix(data []int32, levels int, buf []int32) waveletMatrix {
	m := len(data)
	wm := waveletMatrix{
		levels: levels,
		zeros:  make([]int32, levels),
		bvs:    make([]bitVector, levels),
	}

	cur := data
	nxt := buf[:m]
	numWords := (m >> 6) + 1

	for b := levels - 1; b >= 0; b-- {
		words := make([]uint64, numWords)
		prefix := make([]int32, numWords)
		var z int32
		for i := 0; i < m; i++ {
			if (cur[i]>>uint(b))&1 == 0 {
				z++
			} else {
				words[i>>6] |= 1 << (uint(i) & 63)
			}
		}
		var sum int32
		for w := 0; w < numWords; w++ {
			prefix[w] = sum
			sum += int32(bits.OnesCount64(words[w]))
		}
		wm.zeros[b] = z
		wm.bvs[b] = bitVector{words: words, prefix: prefix}

		if b > 0 {
			zi := int32(0)
			oi := z
			for i := 0; i < m; i++ {
				v := cur[i]
				if (v>>uint(b))&1 == 0 {
					nxt[zi] = v
					zi++
				} else {
					nxt[oi] = v
					oi++
				}
			}
			cur, nxt = nxt, cur
		}
	}
	return wm
}

func (wm *waveletMatrix) countLess(l, r, val int32) int32 {
	if val <= 0 {
		return 0
	}
	if wm.levels == 0 || val >= (int32(1)<<uint(wm.levels)) {
		return r - l
	}
	var ans int32
	for b := wm.levels - 1; b >= 0 && l < r; b-- {
		l1 := wm.bvs[b].rank1(l)
		r1 := wm.bvs[b].rank1(r)
		l0 := l - l1
		r0 := r - r1
		if (val>>uint(b))&1 == 1 {
			ans += r0 - l0
			z := wm.zeros[b]
			l = z + l1
			r = z + r1
		} else {
			l = l0
			r = r0
		}
	}
	return ans
}

const smallThreshold = 32

type bitNode struct {
	pos  []int32
	prev []int32 // kept only when len(pos) <= smallThreshold
	wm   waveletMatrix
}

func (node *bitNode) query(l, r int32) int32 {
	pos := node.pos
	m := len(pos)
	if m == 0 || pos[0] > r || pos[m-1] < l {
		return 0
	}
	// lowerBound(pos, l)
	lo, hi := 0, m
	for lo < hi {
		mid := int(uint(lo+hi) >> 1)
		if pos[mid] < l {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	L := lo

	// upperBound(pos, r)
	lo, hi = L, m
	for lo < hi {
		mid := int(uint(lo+hi) >> 1)
		if pos[mid] <= r {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	R := lo

	if L >= R {
		return 0
	}
	if m <= smallThreshold {
		var cnt int32
		prev := node.prev
		for i := L; i < R; i++ {
			if prev[i] < l {
				cnt++
			}
		}
		return cnt
	}
	return node.wm.countLess(int32(L), int32(R), l)
}

type fastScanner struct {
	r   *bufio.Reader
	buf []byte
	idx int
	n   int
}

func newFastScanner() *fastScanner {
	return &fastScanner{
		r:   bufio.NewReaderSize(os.Stdin, 1<<20),
		buf: make([]byte, 1<<20),
	}
}

func (fs *fastScanner) readByte() byte {
	if fs.idx >= fs.n {
		n, err := fs.r.Read(fs.buf)
		fs.idx = 0
		fs.n = n
		if n == 0 || err != nil && n == 0 {
			return 0
		}
	}
	b := fs.buf[fs.idx]
	fs.idx++
	return b
}

func (fs *fastScanner) nextInt64() int64 {
	b := fs.readByte()
	for b <= ' ' && b != 0 {
		b = fs.readByte()
	}
	var neg bool
	if b == '-' {
		neg = true
		b = fs.readByte()
	}
	var x int64
	for b >= '0' && b <= '9' {
		x = x*10 + int64(b-'0')
		b = fs.readByte()
	}
	if neg {
		return -x
	}
	return x
}

func main() {
	fs := newFastScanner()
	n := int(fs.nextInt64())

	a := make([]int32, n+1)
	vals := make([]int32, n)
	for i := 1; i <= n; i++ {
		v := int32(fs.nextInt64())
		a[i] = v
		vals[i-1] = v
	}

	sort.Slice(vals, func(i, j int) bool { return vals[i] < vals[j] })
	// unique
	u := 0
	for i := 0; i < n; i++ {
		if i == 0 || vals[i] != vals[i-1] {
			vals[u] = vals[i]
			u++
		}
	}
	vals = vals[:u]

	comp := make([]int32, n+1)
	prev := make([]int32, n+1)
	lastPos := make([]int32, u+1)
	sz := make([]int32, u+1)

	for i := 1; i <= n; i++ {
		// binary search a[i] in vals
		lo, hi := 0, u
		target := a[i]
		for lo < hi {
			mid := int(uint(lo+hi) >> 1)
			if vals[mid] < target {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		c := int32(lo + 1)
		comp[i] = c
		prev[i] = lastPos[c]
		lastPos[c] = int32(i)

		for idx := int(c); idx <= u; idx += idx & -idx {
			sz[idx]++
		}
	}

	var totalSize int64
	maxNodeSize := 0
	for idx := 1; idx <= u; idx++ {
		totalSize += int64(sz[idx])
		if int(sz[idx]) > maxNodeSize {
			maxNodeSize = int(sz[idx])
		}
	}

	allPos := make([]int32, totalSize)
	allPrev := make([]int32, totalSize)
	bit := make([]bitNode, u+1)
	fill := make([]int32, u+1)
	var offset int64
	for idx := 1; idx <= u; idx++ {
		s := int64(sz[idx])
		bit[idx].pos = allPos[offset : offset+s]
		bit[idx].prev = allPrev[offset : offset+s]
		offset += s
	}

	for i := 1; i <= n; i++ {
		p := int32(i)
		pr := prev[i]
		for idx := int(comp[i]); idx <= u; idx += idx & -idx {
			k := fill[idx]
			bit[idx].pos[k] = p
			bit[idx].prev[k] = pr
			fill[idx] = k + 1
		}
	}

	// Build wavelet matrices for nodes larger than smallThreshold
	buf := make([]int32, maxNodeSize)
	for idx := 1; idx <= u; idx++ {
		if len(bit[idx].pos) > smallThreshold {
			var maxP int32
			pr := bit[idx].prev
			for _, v := range pr {
				if v > maxP {
					maxP = v
				}
			}
			levels := 0
			for (int32(1) << uint(levels)) <= maxP {
				levels++
			}
			if levels > 0 {
				bit[idx].wm = buildWaveletMatrix(pr, levels, buf)
			}
			bit[idx].prev = nil
		}
	}

	maxBit := bits.Len(uint(u)) - 1

	m := int(fs.nextInt64())
	out := bufio.NewWriterSize(os.Stdout, 1<<20)
	var outBuf []byte
	var ans int64

	n64 := int64(n)
	for q := 0; q < m; q++ {
		ai := fs.nextInt64()
		bi := fs.nextInt64()
		ci := fs.nextInt64()
		di := fs.nextInt64()
		ki := int32(fs.nextInt64())

		prevAns := ans
		if prevAns < 0 {
			prevAns = 0
		}
		l := int32((ai*prevAns+bi)%n64) + 1
		r := int32((ci*prevAns+di)%n64) + 1
		if l > r {
			l, r = r, l
		}

		cur := 0
		var acc int32
		for b := maxBit; b >= 0; b-- {
			nxt := cur + (1 << uint(b))
			if nxt <= u {
				cnt := bit[nxt].query(l, r)
				if acc+cnt < ki {
					acc += cnt
					cur = nxt
				}
			}
		}

		if cur+1 > u {
			ans = -1
		} else {
			ans = int64(vals[cur])
		}
		outBuf = strconv.AppendInt(outBuf[:0], ans, 10)
		outBuf = append(outBuf, '\n')
		out.Write(outBuf)
	}
	out.Flush()
}
