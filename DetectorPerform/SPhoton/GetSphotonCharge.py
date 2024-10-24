import ROOT as rt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# the rasult :
# [SphotonCharge,SphotonError]=[1.5601533398631982e-11,2.4512332553841934e-12]
def ChargeIntergral(FilePath,CHName):
    # Read data
    wave=pd.read_csv(FilePath)
    t = wave['Time(s)'].values
    ch = wave[CHName].values
    BaseLine = np.average(ch[0:300]) #BaseLine
    BLError = np.std(ch[0:300]) 
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
        Qvar += delta_t**2*BLError**2
    # Calculate the Charge Error Because of baseline
    QError=np.sqrt(Qvar)
    return [Q,QError]     

[x,y,xe,ye]=[rt.std.vector('double')(),rt.std.vector('double')(),rt.std.vector('double')(),rt.std.vector('double')()]
for i in range(0,8):
    FilePath="../../ExperimentData/sphoton/sphoton"+str(i)+".csv"
    [Q,QError]=ChargeIntergral(FilePath,"CH1V")
    x.push_back(i)
    y.push_back(Q)
    xe.push_back(0)
    ye.push_back(QError)

SphotonCharge=np.average(y.data())
SphotonError=np.std(y.data())
print("Single photon charge:", SphotonCharge, "\nError:", SphotonError)
a=rt.TGraphErrors(8,x.data(),y.data(),xe.data(),ye.data())
#a.SaveAs("SphotonCharge.pdf")
a.SetTitle("Single Photon Charge Distribution")
a.SetMarkerColor(4)
a.SetMarkerStyle(21)
c1=rt.TCanvas()
a.GetYaxis().SetLimits(0,3e-11)
a.GetYaxis().SetTitle("Charge (V#cdot s)")
a.GetYaxis().SetTitle("Event")
a.Draw("AP")

c1.SaveAs("SphotonCharge.pdf")

#[SphotonCharge,SphotonError]=[1.5601533398631982e-11,2.4512332553841934e-12]

#print(x,y,yerror)
#plt.scatter(x,y)
#plt.errorbar(x, y, yerr=yerror)

#plt.savefig("SphotonCharge.pdf")




    

