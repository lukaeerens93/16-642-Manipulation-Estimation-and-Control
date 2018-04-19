% Define the transfer function
G_s = tf([0 1 10],[1 71 1070 1000 0])

% don't forget about negative unity feedback
H = [1];

% Define the response
response = feedback(G_s,H);

% Define the proportional (Kp), Differential (Kd), and Integral (Ki) gains
% You have to manually tune these until you get variable values that are
% just right
Kp=550;
Kd=345;
Ki=35;

% Define the PID transfer function
Gpid = pid(Kp, Ki, Kd);

% Define response from factoring in this PID transfer function
response2 = feedback(Gpid*G_s,H);

% Display the new step response
step(response2);
grid on;

% Display the information about the step response
stepinfo(response2)