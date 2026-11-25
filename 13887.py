import sys

M0=1000000007
M6=166666668
K0=1048576

def f0(a,x):
 l,r=0,len(a)
 while l<r:
  m=(l+r)//2
  if a[m]<x:l=m+1
  else:r=m
 return l

def f1(t,k,r,d):
 while r<=k:
  t[r]+=d
  r+=r&-r

def f2(t,r):
 s=0
 while r>0:
  s+=t[r]
  r-=r&-r
 return s

def f3(t,k,st,tg):
 i=0
 while st:
  nx=i+st
  if nx<=k:
   if t[nx]<tg:
    tg-=t[nx]
    i=nx
  st//=2
 return i+1

def main():
 raw=sys.stdin.read().split()
 if not raw:return
 p0=0
 N=int(raw[p0]);p0+=1
 A=[int(raw[p0+i]) for i in range(N)];p0+=N
 M=int(raw[p0]);p0+=1
 B=512
 bk=[list(range(i,min(i+B,N+1))) for i in range(1,N+1,B)]
 ch=[[] for _ in range(N+M+1)]
 for i in range(N):ch[i].append(i+1)
 nu=N+1
 ops=[];qt=[];qc=0
 def f4(k):
  for b in bk:
   lb=len(b)
   if k<lb:return b[k]
   k-=lb
 for _ in range(M):
  t=int(raw[p0]);p0+=1
  if t%4==1:
   l=int(raw[p0])-1;r=int(raw[p0+1])-1;p0+=2
   ops.append((t,f4(l),f4(r),qc))
   qt.append(t);qc+=1
  elif t==2:
   x=int(raw[p0])-1;y=int(raw[p0+1]);p0+=2
   ops.append((2,f4(x),y))
  elif t==3:
   k=int(raw[p0])-1;p0+=1
   for bi,b in enumerate(bk):
    lb=len(b)
    if k<lb:
     ux=b.pop(k)
     if lb==1:bk.pop(bi)
     break
    k-=lb
   ops.append((3,ux))
  else:
   z=int(raw[p0]);y=int(raw[p0+1]);p0+=2
   u=nu;nu+=1
   if z==0:
    ch[0].append(u)
    if bk:
     b=bk[0];b[0:0]=[u]
     if len(b)>=1024:bk[1:1]=[b[B:]];b[B:]=[]
    else:bk.append([u])
   else:
    k=z-1
    for bi,b in enumerate(bk):
     lb=len(b)
     if k<lb:
      ch[b[k]].append(u);b[k+1:k+1]=[u]
      if lb+1>=1024:bk[bi+1:bi+1]=[b[B:]];b[B:]=[]
      break
     k-=lb
   ops.append((4,u,y))
 if qc==0:return
 L=nu-1
 ps=[0]*(L+1)
 sk=[0];tm=0
 while sk:
  u=sk.pop()
  if u:tm+=1;ps[u]=tm
  if ch[u]:sk.extend(ch[u])
 vp={};cv=[0]*(L+1)
 for u in range(1,N+1):
  p=ps[u];v=A[u-1];cv[p]=v
  vp.setdefault(v,[]).append(p)
 for o in ops:
  if o[0]%2==0:vp.setdefault(o[2],[]).append(ps[o[1]])
 oc={};vb={};vt={};vm={}
 for v,ls in vp.items():
  if len(ls)>1:ls=sorted(set(ls))
  oc[v]=ls;k=len(ls);vb[v]=[0]*(k+1);vt[v]=0
  pw=1
  while pw*2<=k:pw*=2
  vm[v]=pw
 ep=[];er=[];d0=[];d1=[];d2=[];d3=[]
 def f5(p,pr,v,sg):
  v2=(v*v)%M0;v3=(v2*v)%M0
  ep.append(p);er.append(pr);d0.append(sg)
  d1.append(v*sg);d2.append(v2*sg);d3.append(v3*sg)
 lp={}
 for p in range(1,L+1):
  v=cv[p]
  if v:
   f5(p,lp.get(v,0),v,1);lp[v]=p
   ls=oc[v];f1(vb[v],len(ls),f0(ls,p)+1,1);vt[v]+=1
 def f6(p,v,ad):
  ls=oc[v];k=len(ls);t=vb[v];mp=vm[v];r=f0(ls,p)+1
  if ad:vt[v]+=1;f1(t,k,r,1)
  tt=vt[v];c=f2(t,r)
  pp=ls[f3(t,k,mp,c-1)-1] if c>1 else 0
  np=ls[f3(t,k,mp,c+1)-1] if c<tt else 0
  if ad:
   f5(p,pp,v,1)
   if np:f5(np,pp,v,-1);f5(np,p,v,1)
  else:
   f5(p,pp,v,-1)
   if np:f5(np,p,v,-1);f5(np,pp,v,1)
   f1(t,k,r,-1);vt[v]=tt-1
 ql=[0]*qc;qr=[0]*qc;st=[0]*(qc+1);cb=0
 for o in ops:
  t=o[0]
  if t%4==1:
   qi=o[3];ql[qi]=ps[o[1]];qr[qi]=ps[o[2]]
   cb+=1;st[cb]=len(ep)
   if cb==qc:break
  else:
   p=ps[o[1]];ov=cv[p];nv=0 if t==3 else o[2]
   if ov==nv:continue
   cv[p]=nv
   if ov:f6(p,ov,0)
   if nv:f6(p,nv,1)
 a0=[0]*qc;a1=[0]*qc;a2=[0]*qc;a3=[0]*qc
 b0=[0]*(L+1);b1=[0]*(L+1);b2=[0]*(L+1);b3=[0]*(L+1);vs=[0]*(L+1);sn=[0]
 def f7(us,ue,lo,hi):
  for q in range(lo,hi+1):
   l=ql[q];r=qr[q]
   if qt[q]==5:
    s0=0
    for i in range(us,ue):
     if er[i]<l:
      if l<=ep[i]<=r:s0+=d0[i]
    a0[q]+=s0
   else:
    s1=s2=s3=0
    for i in range(us,ue):
     if er[i]<l:
      if l<=ep[i]<=r:s1+=d1[i];s2+=d2[i];s3+=d3[i]
    a1[q]+=s1;a2[q]+=s2;a3[q]+=s3
 def f8(us,ue,lo,hi):
  m=ue-us;nq=hi-lo+1
  if m<=0:return
  if nq<=0:return
  if m*nq<=128:f7(us,ue,lo,hi);return
  sn[0]+=1;cs=sn[0]
  ul=[er[i]*K0+i for i in range(us,ue)];ul.sort()
  qa=[ql[q]*K0+q for q in range(lo,hi+1)];qa.sort()
  ui=0
  for qk in qa:
   q=qk%K0;l=ql[q]
   while ui<m:
    if ul[ui]//K0>=l:break
    ix=ul[ui]%K0;p=ep[ix]
    x0=d0[ix];x1=d1[ix];x2=d2[ix];x3=d3[ix]
    while p<=L:
     vs[p]=cs;b0[p]+=x0;b1[p]+=x1;b2[p]+=x2;b3[p]+=x3
     p+=p&-p
    ui+=1
   r=qr[q]
   if qt[q]==5:
    s0=0;p=r
    while p>0:s0+=b0[p];p-=p&-p
    p=l-1
    while p>0:s0-=b0[p];p-=p&-p
    a0[q]+=s0
   else:
    s1=s2=s3=0;p=r
    while p>0:s1+=b1[p];s2+=b2[p];s3+=b3[p];p-=p&-p
    p=l-1
    while p>0:s1-=b1[p];s2-=b2[p];s3-=b3[p];p-=p&-p
    a1[q]+=s1;a2[q]+=s2;a3[q]+=s3
  for j in range(ui):
   p=ep[ul[j]%K0]
   while p<=L:
    if vs[p]!=cs:break
    vs[p]=0;b0[p]=b1[p]=b2[p]=b3[p]=0
    p+=p&-p
 f8(0,st[1],0,qc-1)
 def f9(lo,hi):
  if lo>hi:return
  if st[lo]==st[hi+1]:return
  if lo==hi:f7(st[lo],st[lo+1],lo,lo);return
  md=(lo+hi)//2
  f9(lo,md);f9(md+1,hi)
  f8(st[lo],st[md+1],md+1,hi)
 if qc>1:f9(1,qc-1)
 out=[]
 for q in range(qc):
  if qt[q]==5:out.append(str(a0[q]))
  else:
   p1=a1[q]%M0;p2=a2[q]%M0;p3=a3[q]%M0
   out.append(str(((p1*p1%M0*p1-3*p1*p2+2*p3)%M0)*M6%M0))
 print("\n".join(out))

main()
