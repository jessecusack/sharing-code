function [] = generate_data_for_bad_example()
% load an individual profile
load('SP2_P5_01_VMP_SPAMEX_2014.mat', 'SP2_P5_01')
vmp = SP2_P5_01;

% use uninformative variable names
d = vmp.depth;
tmp = vmp.t;
sal = vmp.s;
e = vmp.epsilon;
n = vmp.n2;
lat = vmp.lat;
lon = vmp.lon;

% save to uninformative file name
save('../bad_example/dat.mat', 'tmp', 'sal', 'e', 'd', 'n', 'lat', 'lon', '-v7')