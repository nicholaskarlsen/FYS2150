function T = termistortemp(R)
a = 8.420e-004;
b = 2.068e-004;
c = 8.593e-008;
T = (a + b * log(R) + c * (log (R)).^3 ).^(-1) - 273.15;
end