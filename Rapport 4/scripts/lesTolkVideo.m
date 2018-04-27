%---------------------------------------------------------------------
% Program for bildebehandling i laboppgave om luftmotstand for 
% FYS2150. Skrevet av Ole Ivar Ulven, V-12.
%---------------------------------------------------------------------

%---------------------------------------------------------------------
% Les inn film
% Studenten m� selv sette inn korrekt filnavn
%---------------------------------------------------------------------

videonavn   = '/home/nick/Videos/fys2150drag/A2.avi'; %Navnet p� filmen dere vil hente bilder fra
% videonavn   = 'litenmetallkule.avi'; %Navnet p� filmen dere vil hente bilder fra


film = VideoReader(videonavn);
nFrames = film.NumberOfFrames;
vidHeight = film.Height;
vidWidth = film.Width;
frameRate = film.frameRate;

%---------------------------------------------------------------------
% Innstillinger som studenten selv m� sette opp
%---------------------------------------------------------------------

nstart      = 1; %Nummeret p� det f�rste bildet du vil bruke i filmen
nslutt      = nFrames; %Nummeret p� det siste bildet du vil bruke i filmen

xpos        = 1:vidWidth; %Hvilke koordinater i x-retning du �nsker � ta med
ypos        = 67:215; %Hvilke koordinater i y-retning du �nsker � ta med
%ypos        = 1: vidHeight
%---------------------------------------------------------------------
% Sjekk at innstillinger er mulige
%---------------------------------------------------------------------

if nslutt > nFrames
    disp(' Feil: nslutt m� v�re mindre enn antall bilder i filmen'); return;
end
if xpos(end) > vidWidth
    disp(' Feil: St�rste xpos m� v�re mindre enn filmens bredde'); return;
end
if ypos(end) > vidHeight
    disp(' Feil: St�rste ypos m� v�re mindre enn filmens h�yde'); return;
end

%---------------------------------------------------------------------
% Initialiser n�dvendige variable
%---------------------------------------------------------------------

nBilder = nslutt-nstart+1; %Antall bilder som skal analyseres

bpos_x = zeros(nBilder,1); %Ballongens posisjon i hvert bilde, x
bpos_y = zeros(nBilder,1); %Ballongens posisjon i hvert bilde, y

%---------------------------------------------------------------------
% Juster bildeegenskaper, konverter til bin�rt format og beregn 
% massesenter.
% 
% Her kan dere selv bli n�dt til � endre p� enkelte faktorer for � f�
% gode nok bilder.
%
% For at algoritmen som finner massesenter skal fungere, er det viktig
% at det bare er ett objekt igjen i svarthvitt-bildet.
% (Det virker ogs� hvis ballongen alltid blir regnet som objekt 1
% av 'regionprops', men dette er det i praksis vanskelig � sikre.)
%---------------------------------------------------------------------
for i=1:nBilder
    % Les ut ett enkelt bilde fra filmen
    bilde = imcomplement(read(film,nstart+i-1)); 
    
    % Vis bildet, hvis �nskelig
    % figure(1); imshow(bilde);
    
    % Se kun p� det valgte utsnittet
    bscaled = bilde(ypos,xpos); 
    
    % Konverter til bin�rt
    % Her kan man velge mer avanserte metoder om n�dvendig, filtrere f�r 
    % konvertering osv. Det kan v�re n�dvendig � endre grenseverdien.
    bwscaled = im2bw(bscaled,0.8); 
    
    % Fjern un�dvendige pixler (armer, annet st�y).
    % Det kan v�re n�dvendig � endre st�rrelsen p� disken, eventuelt
    % legge til annen filtrering.
    bwop = imopen(bwscaled,strel('disk',0));
    
    % Fjern sammenhengende omr�der mindre enn et antall pixler
    bwop = bwareaopen(bwop,100);
    
    % Vis ferdig bilde, hvis �nskelig
    %figure(2); imshow(bwop);
    
    % Finn massesenter for hvert bilde.
    % Skriver feilmelding, og setter posisjon til NaN hvis det ikke er
    % hvite objekter igjen i bildet.
    c = regionprops(bwop,'centroid'); 
    if size(c,1) == 0
        disp('No object in frame');
        bpos_x(i) = NaN;
        bpos_y(i) = NaN;
    elseif size(c,1) > 1
        disp('Multiple objects in frame, using object 1');
        bpos_x(i) = c(1).Centroid(1,2);
        bpos_y(i) = c(1).Centroid(1,1); 
        fprintf(1,'Mass center: %i, x=%i y=%i\n',i,bpos_x(i),bpos_y(i));
    else
        bpos_x(i) = c.Centroid(1,2);
        bpos_y(i) = c.Centroid(1,1); 
        fprintf(1,'Mass center: %i, x=%i y=%i\n',i,bpos_x(i),bpos_y(i));
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

px2m = 1075;
rx = bpos_x / px2m      % x component of pos
ry = bpos_y / px2m      % y component of vel
vx = diff(rx);          % x component of velocity
vy = diff(ry);          % y ...
v = sqrt(vx.^2 + vy.^2);    % speed of ball (px/frame)
frames = 1:length(v);
time = frames / frameRate;

figure(1)
hold on;
plot(frames, v);
ylabel("Speed [m/s]");
xlabel("Time [frames]");
title("Speed of ball (" +videonavn+")");
hold off;

sta = input('Start = ');
sto = input('Stop = ');

%[m_x, c_x, dm_x, dc_x] = linfit(time(sta:sto), rx(sta:sto)); % linfit of x direction
%[m_y, c_y, dm_y, dc_y] = linfit(time(sta:sto), ry(sta:sto)); % linfit of y direction

[Px,Sx,MUx] = polyfit(time(sta:sto), rx(sta:sto).',1);
%[yhx, dx] = polyval(Px, Sx)
[Py,Sy,MUy] = polyfit(time(sta:sto), ry(sta:sto).',1);
%[yhy, dy] = polyval(Py, Sy);


v_c = sqrt(Px(1).^2 + Py(1).^2);
%dv_c = v_c .* (sqrt((mean(dx) / Px(1)).^2 + (mean(dy) / Py(1)).^2));


figure(2)
hold on;
plot(time(sta:sto), v(sta:sto));
ylabel("Speed [m/s]");
xlabel("Time [s]");
title("Speed of ball (" + videonavn + ")");
hold off;




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%---------------------------------------------------------------------
% Lagre resultat.
%---------------------------------------------------------------------

save('data/A2.mat','bpos_x', 'bpos_y', 'v','frameRate');
