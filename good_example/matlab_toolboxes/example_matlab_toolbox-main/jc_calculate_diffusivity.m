function [Krho] = jc_calculate_diffusivity(eps, N2, gamma)
% jc_calculate_diffusivity  Estimate the turbulent diffusivity from dissipation and stratification.
%
%   Inputs
%   ------
%       eps [W kg-1] : turbulent kinetic energy dissipation rate
%       N2 [s-2] : buoyancy frequency squared (angular frequency squared e.g. radians)
%       gamma [-] : flux coefficient (or mixing efficiency)
%
%   Outputs
%   -------
%       Krho [m2 s-1] : turbulent diffusivity
%
%   Usage
%   -----
%   jc_calculate_diffusivity(eps, N2) uses a default flux coefficient of 0.2.
%
%   To specify the flux coefficient, use:
%   jc_calculate_diffusivity(eps, N2, gamma)
%
% Author: Jesse Cusack (jmcusack@marine.rutgers.edu)

if ~exist('gamma', 'var')
    gamma = 0.2;
end

Krho = gamma*eps./N2;
