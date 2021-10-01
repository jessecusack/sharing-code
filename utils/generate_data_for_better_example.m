function [] = generate_data_for_better_example()
% load an individual profile
load('~/Dropbox/Data/SPAMEX/vmp/SP_VMP_3500m.mat', 'SP2_P5_01')
vmp = SP2_P5_01;

depth = vmp.depth;
temperature = vmp.t;
salinity = vmp.s;
dissipation = vmp.epsilon;
N_squared = vmp.n2;
lat = vmp.lat;
lon = vmp.lon;

save('../better_example/vmp_profile_SPAMEX_2014.mat', 'N_squared', 'temperature', 'salinity', 'dissipation', 'depth', 'lat', 'lon', '-v7')
% also save to Dropbox
save('~/Dropbox/Data/example_data_for_resuable_code/vmp_profile_SPAMEX_2014.mat', 'N_squared', 'temperature', 'salinity', 'dissipation', 'depth', 'lat', 'lon', '-v7')
