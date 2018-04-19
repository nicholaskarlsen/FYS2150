videonavn = '/home/nick/Videos/fys2150drag/B1.avi';

film = VideoReader(videonavn);
nFrames = film.NumberOfFrames;
vidHeight = film.Height
vidWidth = film.Width
bilde = read(film,1);
imagesc(bilde),axis equal tight

% velg passende utsnitt av bildet
xval = 1:vidWidth;
yval = 1:vidHeight;

% velg passende utsnitt av frames
nstart = 1;
nslutt = nFrames;

% velg terskel for svart/hvit bilde
bwterskel = 0.25;

for i = nstart:nslutt
    bilde = read(film,i);
    bwbilde = im2bw(bilde,bwterskel);
    imshow(bwbilde)
    drawnow
    fprintf('Frame %d\n',i);
end
