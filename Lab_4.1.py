import math;
x=y=float();
A=B=dx=float();
print('Please enter value for start A\n');
A=float(input());
print('Please enter value for finish B\n');
B=float(input());
print('Please enter value for step DX\n');
dx=float(input());
x=A;
while True:
    if(3 + 2 * math.cos(x)==0):
        print(f'x={x:10.3f} y=ERROR:could not to calculate')
    else:
        y=1/(3 + 2 * math.cos(x));
        print(f'x={x:10.3f} y={y:10.3f}');
    x=x+dx;
    if x > B:
        break;