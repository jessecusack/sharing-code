function [] = generate_data_for_bad_example()
% load an individual profile
load('~/Dropbox/Data/SPAMEX/vmp/SP_VMP_3500m.mat', 'SP2_P5_01')
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