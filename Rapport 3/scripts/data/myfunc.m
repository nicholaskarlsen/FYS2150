function [A,dA,B,dB,R_squared] = myfunc(x,y)
  #fit data to line y = A*x + B
  
  n = length(x);
  x_mean = mean(x);
  y_mean = mean(y);
  D = sum( (x - mean(x)).^2);
  # slope A and intercept B
  A = sum((x-x_mean).*y)/D;
  B = y_mean - A*x_mean;
  R = sum( (y - A*x - B).^2);
  #standard error estimates for A and B
  dA = sqrt( 1/D * R * 1/(n-2) );
  dB = sqrt( (1/n + x_mean^2/D) * R * 1/(n-2) );
  
  #coefficient of determination
  ss_tot = sum( (y-y_mean).*(y-y_mean) );
  y_fit = A*x+B;
  ss_res = sum((y-y_fit).*(y-y_fit));
  R_squared = 1 - ss_res/ss_tot;
 
  endfunction