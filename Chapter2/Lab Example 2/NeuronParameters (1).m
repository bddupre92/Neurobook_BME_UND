%% Neuron Spreadsheet
 %
 clc
 clear 
 close all
%% Parameter setting

pars=[0.02    0.2    -65    6     14   ;...   tonic spiking
      0.02    0.2    -50    2     15   ];  %  tonic bursting
  
T = 2;           % select the neuron behaviour
par = pars(T,:); % parameters for the model

a = par(1);
b = par(2);
c = par(3);
d = par(4);
I = par(5);      % Input current peak

STOP = 500;      % Simulation time [s]
