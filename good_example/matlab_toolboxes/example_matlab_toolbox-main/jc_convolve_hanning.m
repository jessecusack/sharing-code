function [xs] = jc_convolve_hanning(x, win)
% jc_convolve_hanning  Smooth data by convolving a hanning function of length 'win'.
%
%   jc_convolve_hanning(x) uses a default window of 5.
%
%   To specify the window length, use:
%
%   jc_convolve_hanning(x, win)
%
% Author: Jesse Cusack (jmcusack@marine.rutgers.edu)

if ~exist('win', 'var')
    win = 5;
end

w = hann(win);

xs = conv2(x, w, 'same')/sum(w);
