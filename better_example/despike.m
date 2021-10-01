function [x_clean] = despike(x, x_max)

if ~exist('x_max', 'var')
    x_max = 1;
end

x_clean = x;
x_clean(x > x_max) = NaN;
