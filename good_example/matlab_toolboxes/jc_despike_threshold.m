function [x_clean] = jc_despike_threshold(x, x_max)
% jc_despike_threshold  Replaces bad values of 'x' with NaN using a threshold.
%
%   x_clean = jc_despike_threshold(x) uses a default threshold of 1.
%
%   To specify the threshold, use:
%
%   x_clean = jc_despike_threshold(x, x_max)
%
% Author: Jesse Cusack (jmcusack@marine.rutgers.edu)

if ~exist('x_max', 'var')
    x_max = 1;
end

x_clean = x;
x_clean(x > x_max) = NaN;
