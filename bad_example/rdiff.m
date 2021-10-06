function [Krho] = rdiff(eps, N2, gamma)

if ~exist('gamma', 'var')
    gamma = 0.2;
end

Krho = gamma*eps./N2;
