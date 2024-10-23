import ROOT as rt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

[SphotonCharge,SphotonError]=[1.5601533398631982e-11,2.4512332553841934e-12]
def ChargeIntergral(FilePath,CHName):
    # Read data
    wave=pd.read_csv(FilePath)
    t = wave['Time(s)'].values
    ch = wave[CHName].values
    BaseLine = np.average(ch[0:300]) #BaseLine
    min = np.min(ch)
    miniter = np.argmin(ch)
    # Traverse arrays to find the integral interval
    Thd = ch - (0.1 * min + 0.9 * BaseLine)
    [iterbegin,iterend]=[miniter,miniter]
    while (Thd[iterbegin] < 0):
        iterbegin -= 1
    while (Thd[iterend] < 0):
        iterend += 1
    # Charge Intergral
    [Q,Qvar]=[0,0]
    for j in range(iterbegin, iterend):
        delta_t = t[j + 1] - t[j]
        Q += delta_t * (BaseLine - ch[j])
    # Calculate the Charge Error Because of baseline
    return Q

hq=rt.TH1F("Energy","Energy",20,0,4e-10)
for i in range(0,101):
    FilePath="../../ExperimentData/Ecali/ecali"+str(i)+".csv"
    q1=ChargeIntergral(FilePath,"CH1V")
    q2=ChargeIntergral(FilePath,"CH2V")
    print(q1,q1)
    hq.Fill(np.sqrt(q1*q2))

c1=rt.TCanvas()
hq.SetXTitle("#sqrt(q_{1}q_{2}) (V*s)")
hq.SetYTitle("count/2#times 10^{-11} (V*s)")
hq.Draw()
c1.SaveAs("qqdist.pdf")

meanqq=hq.GetMean()
depth=5
DE=1.936*1.03*5
f=DE/meanqq
fe=hq.GetStdDev()*DE/meanqq**2
#f=8.66e10 (MeV*s^-1*mV^*1)
print(meanqq,hq.GetMeanError())
print(f,fe)
L=1.5
[L0,L0e]=[1.6432367739667197,0.13148465514315455]

PE=f*SphotonCharge*np.exp(L/2/L0)
PEE=PE*np.sqrt((fe/f)**2+(SphotonError/SphotonCharge)**2+(L/2/L0**2*L0e)**2)
print(PE,PEE)





