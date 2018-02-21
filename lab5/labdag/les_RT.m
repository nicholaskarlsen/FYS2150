clear all
close all
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Script for � m�le N motstander i t sekunder 
% enten **differensielt** eller **mot jord**
%
% **Mot jord** krever N+2 ledere til DAQ-boksen (som leser N+1 spenninger): 
%      AIGND: til jord i kretsen
%      AI0: spenning over R1 (r�d ledning)
%      AI1: spenning over R2 (gul ledning)
%      AI2: spenning over R3 (gr�nn ledning)
%      AI3: spenning over R4 (bl� ledning)
%      AI4: Spenning inn p� spenningsdeler (f.eks. 5V)
% Alle motstandene kobles med en side til jord:
% AI4 ----------------------------------------------
%           |         |         |         |
%         Rref1     Rref2     Rref3     Rref4
%           |         |         |         |
%       AI0-|     AI1-|     AI2-|     AI3-|
%           |         |         |         |
%           R1        R2        R3       R4
%           |         |         |         |
% AIGND-------------------------------------------
%
% **Differensielt** Krever 2N ledere til DAQ-boksen (som leser N spenninger):
% Jordet spenningsforsyning: legg til en leder fra jord til AIGND
% AI0+ og AI0- over Rref(1)
% AI1+ og AI1- over Rref(2)
% AI2+ og AI3- over Rref(3)
% AI3+ og AI3- over Rref(4)
% AI4+ og AI4- over spenning inn p� spenningsdeler
%
% Skrevet: 25.01.2016, DKD
% Testet OK p� 1 og 2 termistorer mot jord (m/labspenningsforsyning)
% Testet OK p� 1 termistor differensielt m/batteri
% Testet OK p� 1 termistor differensielt m/labforsyning med jord-kobling til AIGND.
% Testet p� fyspc-ulab11 og USB-6211 SN: 1356F4E
% Changelog: 01.02.2016: Lagt til valg: gj�r om til temperatur.
%            22.02.2016: (Alex Read) Flytter spenning inn til etter de andre pga.
%            crosstalk som tar mange kanaler � d� ut. Forst�r ikke
%            hvorfor differential skal ha flere kanaler!!!!
%****************************************************
%******* HER M� DU SKRIVE DINE PARAMETRE ************
%****************************************************
motjord=1;% =1 for m�le mot jord, =0 for � m�le differensielt
N=4      ;%Oppgi antall motstander som skal m�les
Varighet=600 ;%Oppgi hvor lenge (i sekund) det skal m�les
Rref=[119.51e3 119.59e3 120.02e3 119.78e3]; %Oppgi alle referansemotstandene i riktig rekkef�lge i Ohm
temp=1; %=1 gj�r om til temperatur med funksjonen "T=termistortemp(R)"
%****************************************************
%****************************************************
%****************************************************
%
if length(Rref)~=N, error('Antall motstander i Rref og N skal v�re like'), end %Sjekk at alle
if motjord 
    TerminalConfig='SingleEnded';
    NumCh=N+1;
else
    TerminalConfig='Differential';
    NumCh=N+1;
end
amplitude=10;%V Kan v�re 0.1, 1, 5 eller 10 V. Her kan du justere for � �ke presisjonen
samplerate=1000;% Hz
varighet=0.1;%s samplingstid for en m�ling. Alle samplinger innenfor denne perioden midles til en m�ling
%Reset old session and create a session
[DS,devicename]=initDaqSessions(NumCh,varighet,samplerate,0);
%Initialize the analog input
AI=initADchannels(DS,devicename,NumCh,TerminalConfig,amplitude);


if temp ~= 1
    figure(1), hold on, xlabel('sekund'), ylabel('motstand (kOhm)')
else
    figure(1), hold on, xlabel('sekund'), ylabel('temperatur (C)')
end
starttime=now;
tid=(now-starttime)*1e5;
meanValues=zeros(2,2);
i=1;
M=['os*+d']; %Plottesymboler
C=['rmgbk']; %Plottefarger
while tid<Varighet
    for j=1:NumCh
        [datain time] = startForeground(DS(j));%f� data med tilh�rende tidsverdier fra AI
        release(DS(j));
        U(i,j)=mean(datain,1);%Ta middelverdien av alle spenningene
    end
    tid=(now-starttime)*1e5;
    t(i)=tid;
    
    %Beregn motstandene:
    R(i,1:N)=Rref.*U(i,1:N)./(U(i,NumCh)-U(i,1:N)); 

    if temp
        T(i,:)=termistortemp(R(i,:));
        if size(T,2) ~= N
            fprintf('termistortemp returnerer feil lengde T\n');
            return
        end
        p=plot(t(i),T(i,:));
    else
        p=plot(t(i),R(i,:));
    end
    for j=1:N %Skill hver motstand/temperatur med egne symboler og farger
        p(j).Marker=M(j);
        p(j).Color=C(j);
    end
    i=i+1;
end
figure(1), hold off
%%%% Lagre data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
filename = input('Hvilket filnavn vil du bruke for � lagre dataene?','s');
save(filename,'t','T','R','U','Rref')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
