% Analysis of an individual VMP profile

% Import toolboxes!
addpath(genpath('../matlab_toolboxes/'))

% Load data
vmp_profile = load('../data/external/vmp_profile_SPAMEX_2014.mat');

%% Where is this profile located?
fig1 = figure(101);
m_proj('ortho','lat',vmp_profile.lat','long',vmp_profile.lon');
m_coast('patch', [0.5 0.5 0.5]);
m_grid('linest','-','xticklabels',[],'yticklabels',[]);
hold on
m_plot(vmp_profile.lon, vmp_profile.lat, '.r', 'MarkerSize', 30)

saveas(fig1, '../figures/profile_location_matlab.png')

%% What does the data look like?

figure(102);
plot(vmp_profile.temperature, vmp_profile.depth)
axis ij
xlabel('Temperature [deg C]')
ylabel('Depth [m]')

figure(103);
semilogx(vmp_profile.dissipation, vmp_profile.depth)
axis ij
xlabel('$\varepsilon$ [W kg-1]','Interpreter','latex')
ylabel('Depth [m]')

figure(104);
plot(vmp_profile.N_squared, vmp_profile.depth)
axis ij
xlabel('N2 [s-2]')
ylabel('Depth [m]')

%% Buoynacy frequency has some spikes! We need to get rid of those.
N2_clean = jc_despike_threshold(vmp_profile.N_squared);

figure(105);
plot(N2_clean, vmp_profile.depth)
axis ij
xlabel('N2 [s-2]')
ylabel('Depth [m]')

%% That looked a lot better. 
% But there are negative values and it seems noisy so we should smooth.

N2_smooth = jc_convolve_hanning(N2_clean, 60);

figure(105);
plot(vmp_profile.N_squared, vmp_profile.depth)
hold on
plot(N2_smooth, vmp_profile.depth)
axis ij
xlabel('N2 [s-2]')
ylabel('Depth [m]')
xlim([-0.2e-5 1e-5])

%% Even better, but there are still a few negative values we want to exclude.
N2_smooth(N2_smooth < 1e-7) = NaN;

%% Calculate the turbulent diffusivity.

Krho = jc_calculate_diffusivity(vmp_profile.dissipation, N2_smooth, 0.2);

fig6 = figure(106);
semilogx(Krho, vmp_profile.depth)
axis ij
xlabel('$K_{\rho}$ [m2 s-1]','Interpreter','latex')
ylabel('Depth [m]')

saveas(fig6, '../figures/diffusivity_matlab.png')
