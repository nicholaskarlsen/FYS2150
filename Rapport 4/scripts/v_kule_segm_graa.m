%Et lite skript for å vise hvordan man kan bruke gråtoneverdier eller segmentering 
%til å finne kuleposisjonen og hastigheten til kulen.
clear all
close all

%% Les inn filmen og fjern ujevn bakgrunn (5 linjer kode)
filename='litenmetallkule.avi';
V=VideoReader(filename); %åpner film-objektet
IV=read(V,[180,1300]);  %les inn bilde 180 til 1300
I=double(squeeze(IV(:,:,1,:))); %gjør om fra farge til gråtone (1 av 3 like kopier) og gjør om til flyttall
Ir=I-I(:,:,1);         %trekk fra første bilde for å justere for ujevn belysning

%% Gråtonebehandling med matriseoperasjoner (uten løkker, 3 linjer kode)
Iyt=squeeze(sum(Ir,1));%summer intensitetene i horisontalretning (i alle bildene)
[m,yg]=min(Iyt);       %finn minima: posisjoner i matrisen = yg (og verdier m) 
pg=polyfit(700:1000,yg(700:1000),1); %gjør lineærtilpasning til siste del av banen

%% Segmentering (7 linjer kode)
Ibw=Ir<-50; % Threshold: sett bakgrunn til 0 og kule til 1
for i=20:1000 %gå gjennom alle bildene og finn senterkoordinatene til kulen
    s = regionprops(Ibw(:,:,i),'centroid');
    centroids = cat(1, s.Centroid);
    ys(i)=centroids(1);  %vertikalposisjonen %x(i)=centroids(2); %horisontalposisjonen
end
ps=polyfit(700:1000,ys(700:1000),1);%gjør lineærtilpasning til siste del av banen

%% Plotting
%
figure(1)
subplot(4,1,1), imagesc(Ir(:,:,200)), colorbar
title('t=200')
xlabel('vertikal posisjon')
ylabel('horisontal posisjon')
subplot(4,1,2), plot(Iyt(:,200))
axis tight
title('t=200')
xlabel('vertikal posisjon')
ylabel('Intensitet \Sigma_x I(t=200)-I(t=1)')
subplot(4,1,3), imagesc(Iyt), colorbar
xlabel('Tid')
ylabel('vertikal posisjon')
subplot(4,1,4), plot(yg,'.')
xlabel('Tid')
ylabel('vertikal posisjon til kulen')
%axis tight
yf=polyval(pg,10:1000);
hold on, plot(10:1000,yf,'-r'), hold off
text(300,1200,['v=',num2str(pg(1))])


figure(2)
subplot(4,1,1), imagesc(Ibw(:,:,200)), colorbar
title('t=200')
xlabel('vertikal posisjon')
ylabel('horisontal posisjon')
subplot(4,1,2), imagesc(Ibw(:,:,600)), colorbar
title('t=600')
xlabel('vertikal posisjon')
ylabel('horisontal posisjon')
subplot(4,1,3), imagesc(Ibw(:,:,1000)), colorbar
title('t=1000')
xlabel('vertikal posisjon')
ylabel('horisontal posisjon')
subplot(4,1,4), plot(20:1000,ys(20:1000),'.')
yf=polyval(ps,20:1000);
xlabel('Tid')
ylabel('vertikal posisjon til kulen')
hold on, plot(20:1000,yf,'-r'), hold off
text(300,1200,['v=',num2str(ps(1))])

   
