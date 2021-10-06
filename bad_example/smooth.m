function [xs] = smooth(x, win)

if ~exist('win', 'var')
    win = 5;
end

w = hann(win);

xs = conv2(x, w, 'same')/sum(w);
