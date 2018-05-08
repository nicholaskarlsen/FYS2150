function [t,I,S]  = CapstoneImport(file)
%denne funksjonen henter ut målingene av tid (t), strøm (I) og
%skalavlesning på integratoren (S) fra en tabulator-separaret fil eksportert fra
%Capstone (Capstone -> File -> Export data -> tab-delimited). 
%Dette er bare tenkt brukt til magnetiserings-oppgaven "Magnetiske effekter" i
%FYS2150, og fungerer bare hvis brukeren har brukt capstone-programmet
%"Hysterese1120.cap" til å gjøre målingene. t,I og S returneres i
%n*m-matriser, hvor hver kolonne m tilsvarer en måleserie ("run"). n
%bestemmes av den lengste måleserien. De andre kolonnene fylles med nuller.

% Vi må bytte ut komma med punktum i Capstone-filen. Lag en ny fil med
% komma i stedet for punktum 
newFile = [file(1:end-4) '_commasreplaced' file(end-3:end)];
comma2dot(file,newFile); %denne funksjonen lager en ny fil

% Les inn alle data
allData = dlmread(newFile,'\t',2,0);

%plukk ut kolonnene vi vil ha
skipCol = 9; % det er ni kolonner vi ikke bryr oss om
t=allData(:,1:skipCol:end);
S=allData(:,8:skipCol:end);
I=allData(:,9:skipCol:end);


function comma2dot(f_old,f_new)
   FH = fopen(f_old,'rb');
   data = fread(FH,'char');
   fclose(FH);
   data(data==',') = '.';
   FH = fopen(f_new,'w');
   fwrite(FH,data,'char');
   fclose(FH);
end

end

