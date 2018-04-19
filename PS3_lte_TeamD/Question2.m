%x0 = [0 0.1 0 0];
%x0 = [0 0.5 0 0];
%x0 = [0 1.0886 0 0];
x0 = [0 1.1 0 0];
t = 0:0.01:30;

%2C)
[t,x] = ode45(@q2c,t,x0);
plot(t,x)
grid on

% 2D)
[t,x] = ode45(@q2d,t,x0);
plot(t,x)
%grid on

function d = q2c(t,x)
R = 10;
B = [0;0;1;1];
A = [0 0 1 0; 0 0 0 1; 0 1 -3 0; 0 2 -3 0];
Q = [1 0 0 0; 0 5 0 0; 0 0 1 0; 0 0 0 5];
Kc = lqr(A,B,Q,R);
u_t = -Kc*x;
d = A*x+B*u_t;
end

function d = q2d(t,x)
% This seems to take forever...
R = 10;
B = [0; 0; 1; 1];
Q = [1 0 0 0; 0 5 0 0; 0 0 1 0; 0 0 0 5];
A = [0 0 1 0; 0 0 0 1; 0 1 -3 0; 0 2 -3 0];

k = lqr(A,B,Q,R);
u_t = -k*x;
d = zeros(4,1);
d(1) = x(3);
d(2) = x(4);
d(3) = (u_t-x(4)^2*sin(x(2))-3*x(3)+cos(x(2))*sin(x(2)))/(2-cos(x(2)^2));
d(4) = (cos(x(2))*u_t-cos(x(2))*x(4)^2*sin(x(2))-cos(x(2))*3*x(3)+2*sin(x(2)))/(2-cos(x(2)^2));
end
