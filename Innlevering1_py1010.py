"""
Innleveringsoppgave 1 i PY1010

Laget av Elena Dubinina

Alle prisene er oppgitt i NOK
"""

x=15000  # Antall kilometer kjørt per år
FE=5000  # Forsikring på elbil per år
FB=7500  # Forsikring på bensinbil per år
N=365  # Antall kalenderdager per år
t=8.38  # Trafikkforsikringsavgift per dag
dE=0.2*2  # Drivstoffpris elbil per km
dB=1  # Drivstoffpris bensinbil per km
bE= 0.1  # Bompengeravgift elbil per km
bB= 0.3  # Bompengeravgift per km

T=t*N  # Trafikkforsikringsavgift per år - lik for elbil og bensinbil
DE=dE*x  # Drivstoffutgifter elbil per år
DB=dB*x  # Drivstoffutgifter bensinbil per år
BE=bE*x  # Bompengeravgift elbil per år
BB=bB*x  # Bompengeravgift bensinbil per år
KOST_E=FE+T+DE+BE  # Total kostnad for drift av elbil per år
KOST_B=FB+T+DB+BB  # Total kostnad for drift av bensinbil per år
DIFF=KOST_E - KOST_B  # Differansen mellom elbil og bensinbil per år

print("Differanse mellom kostnader for elbil og bensinbil per år")
print("ved årlig kjørelengde på",x, "km")
print("Alle priser er i NOK")
print("*")
print("ELBIL - utgifter per år")
print("Forsikring =", FE)
print("Trafikkforsikringsavgift =", T)
print("Drivstoff =", DE)
print("Bompenger =", BE)
print("Total kostnad per år =", KOST_E)
print("*")
print("BENSINBIL - utgifter per år")
print("Forsikring =", FB)
print("Trafikkforsikringsavgift =", T)
print("Drivstoff =", DB)
print("Bompenger =", BB)
print("Total kostnad per år =", KOST_B)
print("***")
print("RESULTAT")
if DIFF>0:  
    print("Bensinbil er", DIFF, "kroner billigere i drift enn elbil per år.")
if DIFF<0:
    print("Elbil er", DIFF*(-1), "kroner billigere i drift enn bensinbil per år.")
    





