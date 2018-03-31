k#labdag elastisitet

# Sjekke om F (m�leur) ligger i midten av kniv/stangendene A,B
#PEE WEE 2m Y612CM LUFKIN +- 0.01cm
L_B_til_F_feste = 71.1 * 10^(-2); #m  
L_A_til_F_feste = 71.2 * 10^(-2); #m

#masse til lodd (kg) fra balansevekt
m_a_balanse = 500.1 * 10^(-3) ; #kg
m_b_balanse = 1000.3 * 10^(-3); #kg
m_c_balanse = 2000.5 * 10^(-3); #kg

#Kalibrering av balansevekt med kalibreringslodd
m_ekte = [1/2,1,2]; #kg
m_balanse = [500.0,999.9,2000.1] * 10^(-3); #kg
[a,da,b,db,r] = myfunc(m_ekte,m_balanse);

#verdier tatt fra kalibrering for loddene 
m_a = (m_a_balanse - b)/a;
m_b = (m_b_balanse - b)/a;
m_c = (m_c_balanse - b)/a;

#lengde mellom yttersidene til festepunktene til knivene 
#PEE WEE 2m Y612CM LUFKIN +- 0.01cm
l_AB = 133.9 * 10^(-2); #m
#diameter til festepunkter
#Moore & Wright 1965 MI +- 0.01mm
l_AB_diameter = 4.09 * 10^(-3); #mm
#anta festepunktet er p� midtden s� trekk fra diameter totalt sett 
#l_AB - l_AB_diameter

#balansevekt m�lt forskjellige vinkler n�r stangen ligger p� sk�len
m_stang_og_feste = [2482.7, 2482.5, 2482.1 ] * 10^(-3); #kg
m_feste = 34.4 * 10^(-3); #kg

#verdier fra kalibrering 
m_stang = (mean(m_stang_og_feste) - m_feste - b)/a; #kg

#M�ling av lengde til stang, rotert rundt og m�lt p� lengste siden 
# PEE WEE 2m Y612CM LUFKIN +- 0.01cm
l_stang = [144.4,144.4,144.4] * 10^(-2); #m 
l_stang_m = mean(l_stang); #m

#M�linger av stangens diameter d p� forskjellige punkter
# Moore & Wright 1965 MI +- 0.01mm
d = [15.98, 15.99, 15.99, 16.00, 15.99, 15.99, 15.98, 15.99, 15.99, 15.99] * 10^(-3); #m
d_m = mean(d); #m

#M�linger Baker Dial Gauge +- 0.01mm
#Forstyrre dial gauge for � se p� om den er stabil f�r m�ling
#og n�len g�r tilbake til det den var -> ser bra ut
#dreide staven slik at utslaget var minst (st�rst) for � sjekke horisontalitet

#masse vektor for baker dial gauge m�linger
m = [0, m_a, m_b, m_a + m_b, m_c, m_a + m_c, m_b + m_c, m_a + m_b + m_c]; #kg

#Runde 1: (in order)
l_1 = [9.44, 8.72, 8.00, 7.28, 6.58, 5.84, 5.15, 4.43] * 10^(-3); #m

#Runde 2: (in order)
l_2 = [9.42, 8.70, 7.98, 7.26, 6.53, 5.80, 5.09, 4.39] * 10^(-3); #m

#Runde 3: (in order)
l_3 = [9.42, 8.71, 7.98, 7.26, 6.53, 5.80, 5.09, 4.37] * 10^(-3); #m

#Runde 4: (in order)
l_4 = [9.41, 8.69, 7.97, 7.25, 6.52, 5.79, 5.08, 4.36] * 10^(-3); #m

#Runde 5: (in order)
l_5 = [9.42, 8.70, 7.98, 7.26, 6.70, 5.87, 5.19, 4.51] * 10^(-3); #m

#Use average response for the linear fit
l_avg = zeros(length(l_1),1);
for i=1:length(l_1)
  l_avg(i) = 1/5 *( l_1(i) + l_2(i) + l_3(i) + l_4(i) + l_5(i) );
endfor

#compute linear fit
[a,da,b,db,r] = myfunc(m,l_avg')
l_fit = m*a + b;

#plot linear fit and data
plot([m,m,m,m,m],[l_1,l_2,l_3,l_4,l_5],'o',m,l_fit)
legend('data',strcat('linear fit R^2 = ',num2str(r)))
xlabel('mass [kg]')
ylabel('dial gauge reading [m]')

## siste test, trekker fra punkt ved null masse hver gang
l_6 = [0, 8.69 - 9.40, 7.96 - 9.40, 7.25 - 9.40, 6.52 - 9.41, 5.79 - 9.40, 5.80 - 9.41, 4.36 - 9.41] * 10^(-3);
[a,da,b,db,r] = myfunc(m,l_6)


#utregning grunnfrekvens f
#avstand mellom festepunkt (indre avstand)
l_kniver = l_AB - l_AB_diameter; #m
g = 9.82; #ms^-2
#skitten m�lestang kobber usikkerheter, festepunkt avstand 
f_teori = sqrt ( (l_kniver^3 * g ) / ( 12 * abs(a) * d_m^2 * m_stang * l_stang_m ) ) #Hz
E_teori = 4*l_kniver^3 * 9.81 / ( 3*pi * abs(a) * d_m^4) #Pa

#fra fourier analyse med samplingfrekvens = 8*1024 og duration 15s
#fra �re h�rte vi ingen forskjell p� 1214
f_ear = 1214; Hz
f_fft = 1213.75; #Hz
E_fft = 16*m_stang * l_stang_m *  f_fft^2 / ( pi * d_m^2 ) #Pa





