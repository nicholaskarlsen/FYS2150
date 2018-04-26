function [nu,mu, rho] = nuOlje(T)
% Beregne kinematisk (nu) og dynamisk (mu) vikositet for Shell-oljen nr. 68
% som en funksjon av temperatur i grader C. 
%
% nu er oppgitt i centistokes (cSt): 1 cSt = 10^-6 m^2/s.

a=[1033.05 -90.7992 4.08103 -0.104967 0.00143595 -8.02259*10^-6]
rho = 886; % kg/m^3 ved 15 C

Tpoly=[1,T,T^2,T^3,T^4,T^5];

nu = sum(a.*Tpoly);
mu = rho*nu;

end

