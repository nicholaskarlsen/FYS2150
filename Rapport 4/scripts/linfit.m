% function [m, c, dm, dc] = linfit(X, Y)

X = [0 1 2 3 4 5 6 7 8 9 10]
Y = [0 3 3 5 6 7 6 8 9 9 11]

n = length(Y);
D = sum(X.^2) - (1.0 / n) .* sum(X).^2;
E = sum(X .* Y) - (1.0 / n) .* sum(X) .* sum(Y);
F = sum(Y.^2) - (1.0 / n) .* sum(Y).^2;

dm = sqrt(1.0 / (n - 2) .* (D .* F - E.^2) / D.^2);
dc = sqrt(1.0 / (n - 2) .* (D / n + mean(X)) .* ((D .* F - E.^2) / (D.^2)));
m = E / D;
c = mean(Y) - m .* mean(X);

% end