%Akvisisjonparametre
duration = 3; %[s] akvisisjontid
samplerate=96000; 

%Parametre for analysen
fin=6000; %Velg en frekvens litt (>500Hz lavere) under frekvensen målt i ro
wp2=14; %Antall sample i hvert tidsvindu blir 2.^wp2

%Gjør klar og samle inn data
[DS,devicename]=initDaqSession(duration,samplerate,1);
addAudioInputChannel(DS,devicename, 1);
fprintf('Datainnsamling starter...\n')
[data, time] = startForeground(DS);
figure(1), plot(time,data), xlabel('tid, s'), ylabel('amplitude')

%Gjør FFT på tidsvinduer
[tw,fw,n,fut,power]=stykkevisFFT(time,data,wp2,fin);
%Plott frekvensene som funksjon av tid
figure(2),plot(tw,fw,'o'),xlabel('tid, s'),ylabel('frekvens, Hz')
%Plott ut Power-spekteret for intervall i (1<=i<=n)
i=1;
figure(3),plot(fut(2:end),power(i,2:end),'.-')
xlabel('frekvens, Hz')
ylabel('Energi')
%Lag din egen funksjon v(fw) og plott
%figure(3), plot(tw,v)

filename = input('Hvilket filnavn vil du bruke for å lagre dataene?','s');

save(filename)

