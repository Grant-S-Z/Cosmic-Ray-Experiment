import numpy as np
import pandas as pd
import ROOT as rt

thd=-4e-1 
def FindTime(FilePath,CHName):
    # Read data
    wave=pd.read_csv(FilePath)
    t = wave['Time(s)'].values
    ch = wave[CHName].values
    iter=0
    if ch[0]<thd:
        return 2
    else:
        while(ch[iter]>thd):
            iter+=1
        if iter<900:
            return t[iter]
        else : 
            return 2

h1=rt.TH1F("h1","h1",50,-20,30)
for i in range(0,101):
    FilePath="../../ExperimentData/muspeed/muspeed/muspeed"+str(i)+".csv"
    t1=FindTime(FilePath,"CH1V")
    t2=FindTime(FilePath,"CH2V")
    if (t1<1)&(t2<1):
        deltat=(t1-t2)*1e9
        # print(deltat)
        h1.Fill(deltat)

h2=rt.TH1F("h2","h2",50,-20,30)
for i in range(0,109):
    FilePath="../../ExperimentData/muspeed/muspeed/musspeed"+str(i)+".csv"
    t1=FindTime(FilePath,"CH1V")
    t2=FindTime(FilePath,"CH2V")
    if (t1<1)&(t2<1):
        deltat=(t1-t2)*1e9
        h2.Fill(deltat)
    
c1=rt.TCanvas()
h1.SetXTitle("#Delta t [ns]")
h1.SetYTitle("Count")
h1.SetTitle("#mu speed")
h1.SetLineColor(3)
h2.SetLineColor(4)
h1.SetAxisRange(0,30,"Y")
h1.Draw()
h2.Draw("SAME")

f1=rt.TF1("f1","gaus[x]",-10,10)
f1.SetParameter(0,15)
f1.SetParameter(1,0)
f1.SetParameter(2,1)

f2=rt.TF1("f2","gaus[x]",-10,10)
f2.SetParameter(0,15)
f2.SetParameter(1,3)
f2.SetParameter(2,1)

f1.SetLineColor(5)
f2.SetLineColor(6)

h1.Fit(f1,"","",-10,10)
h2.Fit(f2,"","",-10,15)
lg=rt.TLegend(0.6,0.6,0.85,0.8)
lg.AddEntry(h1,"#Delta h_{1}=-7.0 cm","l")
lg.AddEntry(f1,"gauss fit of #Delta h_{1}","l")
lg.AddEntry(h2,"#Delta h_{2}=72.8 cm","l")
lg.AddEntry(f2,"gauss fit of #Delta h_{2}","l")

lg.Draw("SAME")
print(f1.GetParameter(1),f2.GetParameter(1))
speed=-0.798/(f1.GetParameter(1)-f2.GetParameter(1))*1e9/3e8
error=-speed*(np.sqrt(f1.GetParError(1)**2+f1.GetParError(1)**2)/(f1.GetParameter(1)-f2.GetParameter(1)))
rt.gStyle.SetOptStat(0)
tex = rt.TLatex(11.5,15,"v_{#mu}="+f"{speed:.2f}"+"#pm"+f"{error:.2f}"+" c")
tex.SetTextSize(0.05)
tex.SetLineWidth(1)
tex.Draw()
c1.SaveAs("muspeed.pdf")

