import numpy as np
import pandas as pd
import ROOT as rt


    # Read data
FilePath="../../ExperimentData/muspeed/muspeed/muspeed0.csv"
wave=pd.read_csv(FilePath)
t = wave['Time(s)'].values
ch1 = wave["CH1V"].values
ch2 = wave["CH2V"].values
ch3 = wave["CH3V"].values

gd1=rt.TGraph()
gd1.SetLineColor(2)
gd2=rt.TGraph()
gd2.SetLineColor(3)
gd3=rt.TGraph()
gd3.SetLineColor(4)

for i in range (0,1000):
    gd1.SetPoint(i,t[i],ch1[i])
    gd2.SetPoint(i,t[i],ch2[i])
    gd3.SetPoint(i,t[i],ch3[i])

c1=rt.TCanvas()
# gd1.SetTitle()
gd1.GetXaxis().SetTitle("Time [s]")
gd1.GetYaxis().SetTitle("Voltage [V]")
gd1.Draw("AL")
gd2.Draw("SAME")
gd3.Draw("SAME")

gg=rt.TLegend(0.65,0.5,0.8,0.7)
gg.AddEntry(gd1,"CH1","l")
gg.AddEntry(gd2,"CH2","l")
gg.AddEntry(gd3,"CH3","l")

gg.Draw("SAME")

c1.SaveAs("../../ExperimentData/muspeed/muspeed/muspeed0.pdf")