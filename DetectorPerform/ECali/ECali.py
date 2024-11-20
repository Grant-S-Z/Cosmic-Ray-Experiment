import ROOT as rt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

[charge1,charge3]=[34.5792709098031,15.09586244820734]
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
    Q=0
    for j in range(iterbegin, iterend):
        delta_t = t[j + 1] - t[j]
        Q += delta_t * (BaseLine - ch[j])
    # Calculate the Charge Error Because of baseline
    return Q*1e12

hq=rt.TH1F("Energy","Energy",25,0,10000)
for i in range(0,100):
    FilePath="../../ExperimentData/ECali/mu"+str(i)+".csv"
    q1=ChargeIntergral(FilePath,"CH1V")
    q2=ChargeIntergral(FilePath,"CH2V")
 #   print(q1,q1)
    if np.sqrt(q1*q2)>600 :
        hq.Fill(np.sqrt(q1*q2))

rt.gStyle.SetOptFit(1111)
f=rt.TF1("f","gaus",0,6000)
hq.Fit(f,"","",0,6000)
c1=rt.TCanvas()
hq.SetXTitle("#sqrt{q_{1}q_{2}} (mV*ns)")
hq.SetYTitle("count/20 (mV*ns)")
hq.Draw()
c1.SaveAs("qqEdist.pdf")

meanqq=f.GetParameter("Mean")
depth=5
DE=1.936*1.03*5
fp=DE/meanqq
fe=f.GetParameter("Sigma")*DE/meanqq**2
#f=8.66e10 (MeV*s^-1*mV^*1)
print(meanqq,hq.GetMeanError())
print(fp,fe)
print("Energy resolution:", fp/fe)
L=1.5
[L0,L0e]=[1.6432367739667197,0.13148465514315455]

# PE=fp*SphotonCharge*np.exp(L/2/L0)
# PEE=PE*np.sqrt((fe/fp)**2+(SphotonError/SphotonCharge)**2+(L/2/L0**2*L0e)**2)
# print(PE,PEE) 
 




