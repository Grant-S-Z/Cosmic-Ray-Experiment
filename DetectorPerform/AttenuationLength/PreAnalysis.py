import ROOT as rt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# the result :
# [L0,L0e]=[1.6432367739667197,0.13148465514315455]
[SphotonCharge, SphotonError] = [1.5601533398631982e-11, 2.4512332553841934e-12]


def ChargeIntergral(FilePath, CHName):
    # Read data
    wave = pd.read_csv(FilePath)
    t = wave["Time(s)"].values
    ch = wave[CHName].values
    BaseLine = np.average(ch[0:300])  # BaseLine
    BLError = np.std(ch[0:300])
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
        Qvar += delta_t * BLError**2
    # Calculate the Charge Error Because of baseline
    QError = np.sqrt(Qvar)
    return [Q, QError, t[iterbegin]]


n = 1.581
DetectorLength = 0.605
dt = 1e-9
# hh=rt.TH1F("AttenuationLength","AttenuationLength")
L = 1.5
L0 = 0.83
p = np.exp(-1 * DetectorLength / L0)
gr = rt.TGraphErrors()
for i in range(0,100):
    # Read csv files
    FilePath = "../../ExperimentData/ECali/mu" + str(i) + ".csv"
    [q1, q1e, t1] = ChargeIntergral(FilePath, "CH1V")
    [q2, q2e, t2] = ChargeIntergral(FilePath, "CH3V")
    ddt = - t1 + t2
    ddte = 0.5e-9*np.sqrt(1/6)
    dlogq = np.log(q1 / q2)
    p1 = np.sqrt(q1 / q2 * np.exp(-L / L0))
    p2 = p1 * q2 / p1
    N = q1 / p1 / SphotonCharge
    # print(q1,q2,N)
    dloge = np.sqrt(
        2 * SphotonCharge**2 * N * p1 * (1 - p1) / q1**2
        + 2 * SphotonCharge**2 * N * p1 * (1 - p1) / q2**2
    )
    gr.SetPoint(i,dlogq,ddt)
    gr.SetPointError(i,dloge,ddte)
    # delta_t.push_back(ddt)
    # delta_te.push_back(ddte)
    # logq.push_back(dlogq)
    # logqe.push_back(dloge)


gr.SetTitle("AttenuationLength")
gr.GetXaxis().SetTitle("log(q_{1}/q_{2})")
gr.GetYaxis().SetTitle("t_{1}-t_{2} (s)")
f = rt.TF1("f", "-[0]*x/3e8*1.583+[1]", -5, 0)
f.SetParameter(0, L0 )
f.SetParameter(1, 3e-9)
f.SetParLimits(0, 0,3 * L0)
f.SetParLimits(1, -1e-7, 1e-7)
f.SetParName(0,"L0")
gr.Fit(f)
LL0 = f.GetParameter(0) 
LL0e = f.GetParError(0) 
rho = gr.GetCorrelationFactor()
print("AttenuationLength", LL0, "\nError", LL0e, "\nCorrelationFactor", rho**2)
tex =rt.TLatex(-2,38e-9,"#rho^{2}="+f"{rho**2:.3f}")
tex.SetTextSize(0.04)
tex.SetLineWidth(1)
c1 = rt.TCanvas()
rt.gStyle.SetOptFit(1111)
gr.Draw("AP")
tex.Draw("SAME")
c1.SaveAs("figs/AttenuationLength.pdf")


# dt = t1 - t2
# logq = np.log(q1/q2)
# plt.scatter(logq, dt)
# plt.title("Distribution and Fitting")
# plt.xlabel("q ratio")
# plt.ylabel("delta t")

# z, cov = np.polyfit(logq, dt, 1, cov=True) # higher power first
# slope, intercept, r_value, p_value, std_err = ss.linregress(logq, dt)

# t1 = np.linspace(0, 1.5, 100)

# plt.plot(t1, t1*slope + intercept, 'r-')
# plt.savefig("figs/AttenuationLengthOriginal.pdf")

# L0=-z[0] * 3e8/n

# print("Result: ", L0)
# print("Correlation: ", r_value**2)
# print(np.sqrt(np.diag(cov)))

# print("Uncetainty: ", np.sqrt(np.diag(cov))[0] / -z[0])

# print("Stat uncertainty :",np.sqrt(np.diag(cov))[0] / -z[0]*L0)
