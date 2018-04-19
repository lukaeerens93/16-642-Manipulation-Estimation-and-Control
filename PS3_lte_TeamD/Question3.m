% Laplace frequence domain transfer function with negative unity feedback
s_y_s = tf([200], [1 22 141 202]);

% Use the step function
step_function = step(s_y_s);

% Plot this step function
plot(step_function);
xlabel("Time: In centi-seconds");
ylabel("Amplitude");