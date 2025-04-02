W,H,f,c,x1,y1,x2,y2=map(int,input().split())
f=min(f,W-f)
x=x2-x1
y=y2-y1
y*=c+1
x+=min(max(f-x1,0),x2-x1)
print(W*H-x*y)