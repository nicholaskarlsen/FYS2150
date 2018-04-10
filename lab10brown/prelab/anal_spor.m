tr = trackmatrix_new;
numpart=max(tr(:,4));
trny=[];
trnum = [];

%kontrollering av spor for å fjerne de partiklene som sitter fast
%loop gjennom alle partiklene for å kontrollere sporene.
figure(2), clf
hold on
m=1;
for n=1:numpart 
    I=find(tr(:,4)==n);
%     %de tre linjene nedenfor gir muligheten til å sjekke spor manuelt
%     figure(1), plot(tr(I,1),tr(I,2))
%      godta=input('Godta/Forkast sporet? g/f: ','s');
%     if godta=='g'
%         trny=[trny;tr(I,:)];
%         trnum(m)=n;
%         m=m+1;
%         figure(2),plot(tr(I,1),tr(I,2),'g') %plot godkjente spor i grønt
%     else
%         figure(2)
%         plot(tr(I,1),tr(I,2),'r') % og ikke godkjente i rødt
%     end
    % med de neste tre linjene tar man bare med partikler som har beveget
    % seg en viss lengde i x- og y-retning (alternativ til den manuelle
    % kontrollen)
    grense = 0; %sett inn et passende kriterium her, for å fjerne partikler som sitter fast
    ddxx = max(tr(I,1))-min(tr(I,1));
    ddyy = max(tr(I,2))-min(tr(I,2));
    if ddxx > grense && ddyy > grense
        figure(2), plot(tr(I,1),tr(I,2))
        trny=[trny;tr(I,:)];
        trnum(m)=n;
        m=m+1;
        plot(tr(I,1),tr(I,2),'g') %plot godkjente spor i grønt
    else 
        plot(tr(I,1),tr(I,2),'r') % og ikke godkjente i rødt
    end
   
   %plot(trny(I,1))
end
figure(2),title 'Partikkelspor. Grønt spor: godkjent, rødt: forkastet'
hold off,axis equal
tr=trny;
numpart=length(trnum);

% kalkulere forflytningene
m=max(tr(:,3));
t=1:m;
sumdx=zeros(m,1);
sumdy=zeros(m,1);
for n=1:numpart % loop gjennom alle partiklene
    I=find(tr(:,4)==trnum(n));
    % finne hvor langt partikkelen har flyttet seg fra startposisjonen ved 
    % hvert tidssteg
    dx=tr(I,1)-tr(I(1),1);
    dy=tr(I,2)-tr(I(1),2);
    sumdx=sumdx+dx.^2;
    sumdy=sumdy+dy.^2;
end
msdx=sumdx/numpart;
msdy=sumdy/numpart;
msdxy=(msdx+msdy);

% Plotte resultater 
figure(1)
plot(msdx,'b')
hold on
plot(msdy,'g')
plot(msdxy,'r')
hold off

% finne stigningstall
% tvinge løsningen til å gå gjennom origo.
px = t(:)\msdx(:);
py = t(:)\msdy(:);
pxy = t(:)\msdxy(:);
legend(['<x^2>, d<x^2>/dt=' num2str(px(1))],...
    ['<y^2>, d<y^2>/dt=' num2str(py(1))],...
    ['<x^2+y^2>, d<x^2+y^2>/dt=' num2str(pxy(1))],'Location','NorthWest')
xlabel('antall tidssteg')
ylabel('Midlere kvadratisk forflytning, piksler^2')
% hold on, plot(t,polyval(px,t),'b'), plot(t,polyval(py,t),'g'), plot(t,polyval(pxy,t),'r'), hold off
hold on, plot(t,px*t,'b'), plot(t,py*t,'g'), plot(t,pxy*t,'r'), hold off
title('Midlere forflytning av Brownske partikler')
axis tight

