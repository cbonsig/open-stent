'''
Created on Apr 3, 2010

stent-calculator.py
Design tool for analytical prediction of stent performance characteristics

Copyright (C) 2010  Nitinol Devices & Components, Inc.
http://nitinol.com

Originally written by Craig Bonsignore
craig.bonsignore@nitinol.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

if __name__ == '__main__':
    pass

from string import *
from re import *
from sys import *
import sys
import re
import csv
import random
from math import *
from random import *
from csv import *


# The calculator() function is passed a dictionary containing all of the relevant stent design inputs,
# and a CSV file handle
                   
def calculator(StentDesign, outfile):

    # Stent Design Inputs
    N_col = StentDesign["N_col"]
    N_struts = StentDesign["N_struts"]
    D_tube = StentDesign["D_tube"]
    t_raw = StentDesign["t_raw"]
    L_strut_tangents = StentDesign["L_strut_tangents"]
    w_apex_raw = StentDesign["w_apex_raw"]
    X_bridge = StentDesign["X_bridge"]
    Y_bridge = StentDesign["Y_bridge"]
    w_bridge_raw = StentDesign["w_bridge_raw"]
    N_bridges = StentDesign["N_bridges"]

    # Process Parameters
    w_kerf = StentDesign["w_kerf"]
    m_width = StentDesign["m_width"]
    m_thickness = StentDesign["m_thickness"]
    Af = StentDesign["Af"]

    # Material Properties
    E_niti_Af1 = 61200
    Af1_matl = 14
    E_niti_Af2 = 40000
    Af2_matl = 27
    E_niti = E_niti_Af2+(E_niti_Af1-E_niti_Af2)*(Af2_matl-Af)/(Af2_matl-Af1_matl)
    density = 6.7
    strain_endurance = StentDesign["strain_endurance"]

    # Service Parameters
    D_set = StentDesign["D_set"]
    D_ves = StentDesign["D_ves"]
    D = D_ves
    C_percent = StentDesign["C_percent"]
    C_pressure = StentDesign["C_pressure"]
    P_systolic = StentDesign["P_systolic"]
    P_diastolic = StentDesign["P_diastolic"]

    # Stent Dimension Calcs
    N_cells = N_struts / 2
    D_crimp = D_tube
    L_strut = L_strut_tangents + 2*(w_apex_raw/2)
    w_strut_raw = ((D_tube * pi) / N_struts) - w_kerf
    w_strut = w_strut_raw - m_width
    w_bridge = w_bridge_raw - m_width
    w_apex = w_apex_raw - m_width
    t = t_raw - m_thickness

    # Strut Angles and Deflections
    theta_set = (180/pi) * asin(((D_set*pi - D_crimp*pi)/N_struts)/L_strut)
    theta_d = (180/pi) * asin(((D*pi - D_crimp*pi)/N_struts)/L_strut)
    delta_theta_d = theta_set - theta_d
    two_theta = 2 * theta_set
    delta_d = 2 * L_strut * sin(radians(delta_theta_d) / 2)
    theta_1mm = (180/pi) * asin((((D_set-1)*pi - D_crimp*pi)/N_struts)/L_strut)
    delta_theta_1mm = theta_set - theta_1mm
    delta_1mm = 2 * L_strut * sin(radians(delta_theta_1mm) / 2)

    # Stent Length Calculations
    X_cell_crimp = L_strut_tangents + 2*(w_apex_raw + X_bridge/2)
    X_total_crimp = X_cell_crimp * N_col - (X_bridge/2)*2
    X_cell = L_strut_tangents * cos(radians(theta_d)) + 2 * (w_apex_raw + X_bridge / 2)
    X_total = X_cell * N_col - (X_bridge/2)*2
    FS = (X_total_crimp-X_total)/X_total_crimp

    # Surface Area Calculations
    A_strut = (L_strut_tangents - w_kerf)*w_strut
    R_apex = w_strut + w_kerf/2 + m_width/2
    A_apex = 0.5 * (pi * (R_apex)**2 - pi*(R_apex)**2) + 2*(w_apex-w_strut)*R_apex
    A_bridge = (( X_bridge**2 + Y_bridge**2 )**0.5) * w_bridge
    A_contact = (A_strut+A_apex)*N_struts*N_col + A_bridge*N_bridges*(N_col-1)
    A_cylinder = pi * D * X_total
    PMA = A_contact / A_cylinder
    POA = 1-PMA
    w_strut_id = (((D_tube - 2*t) * pi) / N_struts) - w_kerf - m_width
    A_strut_id = A_strut * (w_strut_id / w_strut)
    A_apex_id =  A_apex * (w_strut_id / w_strut)
    A_bridge_id =  A_bridge * (w_strut_id / w_strut)
    V_strut = t * ((A_strut+A_strut_id)/2)
    V_apex = t * ((A_apex+A_apex_id)/2)
    V_bridge = t * ((A_bridge+A_bridge_id)/2)
    V_total = (V_strut+V_apex)*N_struts*N_col + V_bridge*N_bridges*(N_col-1)
    mass = density * V_total

    # Moment of Inertia
    R = D_tube / 2
    alpha = 0.5 * (w_strut/(D_tube*pi))*2*pi
    I = R**3 * t * (1 - ((3*t)/(2*R)) + t**2/R**2 - (t**3/(4*R**3)))*(alpha - sin(alpha)*cos(alpha))

    # Force and Strain Calculations
    F_total = ((12 * E_niti * I)/L_strut**3) * delta_d
    F_hoop = F_total 
    F_total_1mm = ((12 * E_niti * I)/L_strut**3) * delta_1mm
    F_hoop_1mm = F_total_1mm 
    strain_d = ((3 * w_strut)/L_strut**2) * delta_d
    strain_1mm = ((3 * w_strut)/L_strut**2) * delta_1mm

    # Pressure and Stiffness
    RF_hoop = (F_hoop_1mm / X_cell) * 10 # N/cm
    RF_trf = 2 * pi * RF_hoop
    P_eq = (F_hoop/(X_cell*(D/2)))*7500.6 # mmHg
    P_contact = ((F_hoop*2*pi*N_col)/A_contact)*1000 #kPa
    k_stent = F_hoop / (D_set - D)

    # Vessel Force and Stiffness
    CV_pressure = C_pressure * (1/7500.6)
    DV_zero = D
    DV_pressure = DV_zero * (1 + C_percent)
    FV_hoop = CV_pressure * (DV_pressure/2) * X_cell
    k_vessel = FV_hoop / (DV_pressure - DV_zero)

    # Balanced Diameter
    delta_D = D_set - D_ves
    delta_stent = (k_vessel / (k_stent + k_vessel) ) * delta_D
    delta_vessel = delta_D - delta_stent
    D_balanced = D_set - delta_stent
    delta_P = (P_systolic - P_diastolic) * (1/7500.6)
    P_amp = delta_P / 2
    delta_stent_systolic = ((k_vessel/(k_stent+k_vessel))*delta_D)-((P_amp*(D_balanced/2)*X_cell)/(k_stent+k_vessel))
    D_systolic = D_set - delta_stent_systolic
    D_diastolic = D_balanced - (D_systolic-D_balanced)
    theta_diastolic = (180/pi) * asin(((D_diastolic*pi - D_crimp*pi)/N_struts)/L_strut)
    delta_theta_diastolic = theta_set - theta_diastolic
    delta_diastolic = 2 * L_strut * sin(radians(delta_theta_diastolic)/2)
    theta_balanced = (180/pi) * asin(((D_balanced*pi - D_crimp*pi)/N_struts)/L_strut)
    delta_theta_balanced = theta_set - theta_balanced
    delta_balanced = 2 * L_strut * sin(radians(delta_theta_balanced)/2)

    # Strain and Safety Factor Calculations
    strain_vessel = ((3 * w_strut)/(L_strut**2)) * delta_d
    strain_diastolic = ((3 * w_strut)/(L_strut**2)) * delta_diastolic
    strain_balanced = ((3 * w_strut)/(L_strut**2)) * delta_balanced
    strain_mean = strain_balanced
    strain_amplitude = abs(strain_balanced - strain_diastolic)
    N_sf = strain_endurance / strain_amplitude


    # Write selected values to CSV file
    outfile.writerow([N_col,N_struts,D_tube,t_raw,L_strut_tangents,w_apex_raw,
                 X_bridge,Y_bridge,w_bridge_raw,N_bridges,w_kerf,m_width,
                 m_thickness,w_strut, t, Af,D_set,D_ves,D,delta_D,C_percent,C_pressure,P_systolic,
                 P_diastolic,strain_endurance,mass,RF_hoop,RF_trf,P_eq,P_contact,
                 strain_mean,strain_vessel,strain_amplitude,N_sf])

    debug = 1

    if debug:

        # Stent Design Inputs
        print 'N_col',N_col
        print 'N_struts',N_struts
        print 'D_tube',D_tube
        print 't_raw',t_raw
        print 'L_strut_tangents',L_strut_tangents
        print 'w_apex_raw',w_apex_raw
        print 'X_bridge',X_bridge
        print 'Y_bridge',Y_bridge
        print 'w_bridge_raw',w_bridge_raw
        print 'N_bridges',N_bridges

        # Process Parameters
        print 'w_kerf',w_kerf
        print 'm_width',m_width
        print 'm_thickness',m_thickness
        print 'Af',Af

        # Material Properties
        print 'E_niti_Af1',E_niti_Af1
        print 'Af1_matl',Af1_matl
        print 'E_niti_Af2',E_niti_Af2
        print 'Af2_matl',Af2_matl
        print 'E_niti',E_niti
        print 'density',density
        print 'strain_endurance',strain_endurance

        # Service Parameters
        print 'D_set',D_set
        print 'D_ves',D_ves
        print 'D',D
        print 'C_percent',C_percent
        print 'C_pressure',C_pressure
        print 'P_systolic',P_systolic
        print 'P_diastolic',P_diastolic

        # Stent Dimension Calcs
        print 'N_cells',N_cells
        print 'D_crimp',D_crimp
        print 'L_strut',L_strut
        print 'w_strut_raw',w_strut_raw
        print 'w_strut',w_strut
        print 'w_bridge',w_bridge
        print 'w_apex',w_apex
        print 't',t

        # Strut Angles and Deflections
        print 'theta_set',theta_set
        print 'theta_d',theta_d
        print 'delta_theta_d',delta_theta_d
        print 'two_theta',two_theta
        print 'delta_d',delta_d
        print 'theta_1mm',theta_1mm
        print 'delta_theta_1mm',delta_theta_1mm
        print 'delta_1mm',delta_1mm

        # Stent Length Calculations
        print 'X_cell_crimp',X_cell_crimp
        print 'X_total_crimp',X_total_crimp
        print 'X_cell',X_cell
        print 'X_total',X_total
        print 'FS',FS

        # Surface Area Calculations
        print 'A_strut',A_strut
        print 'A_apex',A_apex
        print 'A_bridge',A_bridge
        print 'A_contact',A_contact
        print 'A_cylinder',A_cylinder
        print 'PMA',PMA
        print 'POA',POA
        print 'w_strut_id',w_strut_id
        print 'A_strut_id',A_strut_id
        print 'A_apex_id',A_apex_id
        print 'A_bridge_id',A_bridge_id
        print 'V_strut',V_strut
        print 'V_apex',V_apex
        print 'V_bridge',V_bridge
        print 'V_total',V_total
        print 'mass',mass

        # Moment of Inertia
        print 'R',R
        print 'alpha',alpha
        print 'I',I
        
        # Force and Strain Calculations
        print 'F_total',F_total
        print 'F_hoop',F_hoop
        print 'F_total_1mm',F_total_1mm
        print 'F_hoop_1mm',F_hoop_1mm
        print 'strain_d',strain_d
        print 'strain_1mm',strain_1mm

        # Pressure and Stiffness
        print 'RF_hoop',RF_hoop
        print 'RF_trf',RF_trf
        print 'P_eq',P_eq
        print 'P_contact',P_contact
        print 'k_stent',k_stent

        # Vessel Force and Stiffness
        print 'CV_pressure',CV_pressure
        print 'DV_zero',DV_zero
        print 'DV_pressure',DV_pressure
        print 'FV_hoop',FV_hoop
        print 'k_vessel',k_vessel

        # Balanced Diameter
        print 'delta_D',delta_D
        print 'delta_stent',delta_stent
        print 'delta_vessel',delta_vessel
        print 'D_balanced',D_balanced
        print 'delta_P',delta_P
        print 'P_amp',P_amp
        print 'delta_stent_systolic',delta_stent_systolic
        print 'D_systolic',D_systolic
        print 'D_diastolic',D_diastolic
        print 'theta_diastolic',theta_diastolic
        print 'delta_theta_diastolic',delta_theta_diastolic
        print 'delta_diastolic',delta_diastolic
        print 'theta_balanced',theta_balanced
        print 'delta_theta_balanced',delta_theta_balanced
        print 'delta_balanced',delta_balanced

        # Strain and Safety Factor Calculations
        print 'strain_vessel',strain_vessel
        print 'strain_diastolic',strain_diastolic
        print 'strain_balanced',strain_balanced
        print 'strain_mean',strain_mean
        print 'strain_amplitude',strain_amplitude
        print 'N_sf',N_sf


f = open('output.csv','w')
csvFile = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

# write header line of CSV file

csvFile.writerow(['N_col','N_struts','D_tube','t_raw','L_strut_tangents','w_apex_raw',
                 'X_bridge','Y_bridge','w_bridge_raw','N_bridges','w_kerf','m_width',
                 'm_thickness','w_strut','t',
                  'Af','D_set','D_ves','D','delta_D','C_percent','C_pressure','P_systolic',
                 'P_diastolic','strain_endurance','mass','RF_hoop','RF_trf','P_eq','P_contact',
                 'strain_mean','strain_vessel','strain_amplitude','N_sf'])

import random

for N in range (0, 1):


    # Iterate for N cycles, each time choosing parameters according to fixed values or normal distribution as indicated below
    StentDesign = dict(N_col=10,
                       N_struts=42,
                       D_tube=1.92,
                       t_raw=0.17,
                       L_strut_tangents=1.2,
                       w_apex_raw=.130,
                       X_bridge=0.15,Y_bridge=0.0,
                       w_bridge_raw=0.125,
                       N_bridges=7,
                       w_kerf=0.025,
                       m_width=0.040,
                       m_thickness=0.065,
                       Af=25,
                       D_set=8.0,
                       D_ves=6.5,
                       C_percent=0.06,C_pressure=100,
                       P_systolic=150,P_diastolic=50,
                       strain_endurance=0.004)


    calculator(StentDesign,csvFile)

f.close()


