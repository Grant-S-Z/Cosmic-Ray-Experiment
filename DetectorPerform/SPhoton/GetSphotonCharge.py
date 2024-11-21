import ROOT as rt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# the result :
# [SphotonCharge,SphotonError]=[1.5601533398631982e-11,2.4512332553841934e-12]
# [charge1,charge3]=[34.5792709098031,15.09586244820734]
def ChargeIntergral(FilePath, CHName):
    # Read data
    wave = pd.read_csv(FilePath)
    t = wave["Time(s)"].values
    ch = wave[CHName].values
    BaseLine = np.average(ch[700:999])  # BaseLine
    BLError = np.std(ch[700:999])
    min = np.min(ch)
    miniter = np.argmin(ch)
    # Traverse arrays to find the integral interval
    Thd = ch - (0.1 * min + 0.9 * BaseLine)
    [iterbegin, iterend] = [miniter, miniter]
    while Thd[iterbegin] < 0:
        iterbegin -= 1
    while Thd[iterend] < 0:
        iterend += 1
    # Charge Intergral
    [Q, Qvar] = [0, 0]
    for j in range(iterbegin, iterend):
        delta_t = t[j + 1] - t[j]
        Q += delta_t * (BaseLine - ch[j])
        Qvar += delta_t**2 * BLError**2
    # Calculate the Charge Error Because of baseline
    QError = np.sqrt(Qvar)
    return [Q * 1e12, QError * 1e12]


h1 = rt.TH1F("h1", "specharge1", 50, 0, 100)
h2 = rt.TH1F("h2", "specharge3", 50, 0, 100)
for i in range(0, 100):
    FilePath = "../../ExperimentData/sphoton/sphoton/spe1" + str(i) + ".csv"
    [Q, QError] = ChargeIntergral(FilePath, "CH1V")
    h1.Fill(Q)

for i in range(10, 100):
    FilePath = "../../ExperimentData/sphoton/sphoton/spe3" + str(i) + ".csv"
    [Q, QError] = ChargeIntergral(FilePath, "CH3V")
    if Q < 10:
        print(i)
    h2.Fill(Q)
# a.SaveAs("SphotonCharge.pdf")

h1.SetTitle("Single Photoelectron Charge")
# a.SetMarkerColor(4)
# a.SetMarkerStyle(21)
c1 = rt.TCanvas()
# h1.GetYaxis().SetLimits(0,3e-11)
h1.GetYaxis().SetTitle("count ")
h1.SetAxisRange(0, 15, "Y")
h1.SetLineColor(3)
h2.SetLineColor(4)
h1.GetXaxis().SetTitle("charge [mV*ns]")
h1.Draw()
h2.Draw("SAME")

lg = rt.TLegend(0.5, 0.6, 0.7, 0.75)
lg.AddEntry(h1, "CH1", "l")
lg.AddEntry(h2, "CH2", "l")
lg.Draw("SAME")

[q1, q3] = [h1.GetMean(), h2.GetMean()]
[d1, d3] = [h1.GetStdDev(), h2.GetStdDev()]
e = 1.6e-19
R = 50
[G1, G3] = [q1 / R / e * 1e-12, q3 / R / e * 1e-12]
[D1, D3] = [d1 / R / e * 1e-12, d3 / R / e * 1e-12]


c1.SaveAs("SphotonCharge.pdf")
print(q1, q3)
print(G1, G3)
print(d1, d3)
print(D1, D3)

# [SphotonCharge,SphotonError]=[1.5601533398631982e-11,2.4512332553841934e-12]

# print(x,y,yerror)
# plt.scatter(x,y)
# plt.errorbar(x, y, yerr=yerror)

# plt.savefig("SphotonCharge.pdf")
