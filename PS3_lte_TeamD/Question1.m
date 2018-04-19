A = [0 1 0; 0 0 1; 1 5 7];
B = [1; 0; 0];
C = [0 1 3];
X0 = [0;1;0];

% d)
%t = linspace(0,2);
%y = arrayfun(@(t) C * expm(A.*t)* X0, t);
%plot(t,y);
%xlabel("Time");
%ylabel("Output of the Unforced System");

% e)
%p = [-1+1i -1-1i -2];
%K = place(A, B, p);
%disp(K)

% f)
t = linspace(0,10);
y = arrayfun(@(t) C * expm((A - B*K).*t) * X0, t);
plot(t,y);
xlabel("Time");
ylabel("Output of the System Under Feedback Law");