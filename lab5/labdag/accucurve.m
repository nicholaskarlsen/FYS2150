clear
%Last inn de to datasettene [-40,150]C og [0,70]C
ac1=load('accucurve1.dat');
ac2=load('accucurveW.dat');
%Legg dataene sammen i to vektorer
T=[ac1(:,1);ac2(:,1)];
iT=1./(T+273.15);
ac100k=[ac1(:,8);ac2(:,2)*1e5];
lnR=log(ac100k);
i1=ones(size(lnR));
%Lag Vandermondematrisen (tilpasningsmodellen)
V=[i1 lnR lnR.^3];
%Gjør multilineær regresjon
[b,E,Stdb] = mlinregr(iT,V,i1);
%Plott resultatene
figure(1)
subplot(2,1,1), plot(lnR,iT,'o')
hold on
x=linspace(min(lnR),max(lnR),100)';
Vplot=[ones(size(x)) x x.^3];
subplot(2,1,1), plot(x,Vplot*b)
hold off
axis([6 16 2e-3 5e-3])
xlabel('ln(R/R_0), R_0=1\Omega')
ylabel('1/T, 1/K')
subplot(2,1,1), text(6.1,4.6e-3,['1/T=',num2str(b(1),'%1.2e'),' + '...
    ,num2str(b(2),'%1.2e'),' ln(R/R_0) + ',num2str(b(3),'%1.2e'),...
    ' ln(R/R_0)^3'],'FontSize',9)
subplot(2,1,2), plot(T,T.*E./iT,'o')
axis([0 70 -.005 .005])
ylabel('Feil i tilpasning, K')
xlabel('Temperatur, ^oC')
