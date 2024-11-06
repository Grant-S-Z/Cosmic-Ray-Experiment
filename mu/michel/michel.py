import ROOT as rt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

[SphotonCharge,SphotonError]=[93558636508.93161,27594809057.003414]
def ChargeIntergral(FilePath,CHName):
    # Read data
    wave=pd.read_csv(FilePath)
    t = wave['Time(s)'].values
    ch = wave[CHName].values
    BaseLine = np.average(ch[700:1000]) #BaseLine
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
    print(Q)
    return Q

f=5016837581.882691 

hq=rt.TH1F("Energy","Energy",10,0,50)
for i in range(5,47):
    FilePath="../../ExperimentData/michel/mu"+str(i)+".csv"
    q1=ChargeIntergral(FilePath,"CH1V")
    q2=ChargeIntergral(FilePath,"CH2V")
 #   print(q1,q1)
    hq.Fill(np.sqrt(q1*q2)*f)

# rt.gStyle.SetOptFit(1111)
# f=rt.TF1("f","gaus",1e-9,4e-9)
# hq.Fit(f,"","",1e-9,4e-9)
c1=rt.TCanvas()
hq.SetXTitle("Energy [MeV]")
hq.SetYTitle("count/5 MeV")
hq.SetTitle("Michel electron energy")

hq.Draw()
c1.SaveAs("michel.pdf")

# meanqq=f.GetParameter("Mean")
# depth=5
# DE=1.936*1.03*5
# fp=DE/meanqq
# fe=f.GetParameter("Sigma")*DE/meanqq**2
# #f=8.66e10 (MeV*s^-1*mV^*1)
# #f=5016837581.882691 
# print(meanqq,hq.GetMeanError())
# print(fp,fe)
# print("Energy resolution:", fp/fe)
# L=1.5
# [L0,L0e]=[1.6432367739667197,0.13148465514315455]

# PE=fp*SphotonCharge*np.exp(L/2/L0)
# PEE=PE*np.sqrt((fe/fp)**2+(SphotonError/SphotonCharge)**2+(L/2/L0**2*L0e)**2)
# print(PE,PEE)





