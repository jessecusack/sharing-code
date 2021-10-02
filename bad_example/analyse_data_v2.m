

load('/Users/johnsmith/mydata/dat.mat');

fig1 = figure(101);
m_proj('ortho','lat',lat','long',lon');
m_coast('patch', [0.5 0.5 0.5]);
m_grid('linest','-','xticklabels',[],'yticklabels',[]);
hold on
m_plot(lon, lat, '.r', 'MarkerSize', 30)

saveas(fig1, 'profile_location_matlab.png')


figure(102);
plot(tmp, d)
axis ij
xlabel('Temperature [deg C]')
ylabel('Depth [m]')

figure(103);
semilogx(e, d)
axis ij
xlabel('$\varepsilon$ [W kg-1]','Interpreter','latex')
ylabel('Depth [m]')

figure(104);
plot(n, d)
axis ij
xlabel('N2 [s-2]')
ylabel('Depth [m]')

nc = despike(n);

figure(105);
plot(nc, d)
axis ij
xlabel('N2 [s-2]')
ylabel('Depth [m]')


ns = smooth(nc, 60);

figure(105);
plot(n, d)
hold on
plot(ns, d)
axis ij
xlabel('N2 [s-2]')
ylabel('Depth [m]')
xlim([-0.2e-5 1e-5])

ns(ns < 1e-7) = NaN;


Krho = diff(e, ns, 0.2);

fig6 = figure(106);
semilogx(Krho, d)
axis ij
xlabel('$K_{\rho}$ [m2 s-1]','Interpreter','latex')
ylabel('Depth [m]')

saveas(fig6, 'diffusivity_matlab.png')
