import matplotlib.pyplot as plt
import ROOT as rt

str1 = "00000010000000001000202000020000000000000010001000000010002300000100300000002000200001000000000000000000200000010000200000000200100200000000001020012000000000000000000000000000000000200000000010000020000000002"
str2 = "11532338531287189321621638311353172611242114316714382513525142415246217111231326129512458528114371211224412"

array1 = list(str1)
array2 = list(str2)

plt.figure()
plt.hist(array1, align='left', alpha=0.7, color='b')
plt.xticks(["0", "1", "2", "3"], ["no", "1-3", "3-10", "both"])
plt.xlabel(r"time($\mu$s)")
plt.ylabel("count")
plt.title("afterPulse1")
plt.savefig("fig/afterPulse01.pdf")

plt.figure()
plt.hist([int(char) for char in array2], bins=range(
    1, 11), align='left', alpha=0.7, color='g')
plt.xticks(range(1, 10))
plt.xlabel(r"time($\mu$s)")
plt.ylabel("count")
plt.title("afterPulse2")
plt.savefig("fig/afterPulse02.pdf")

c1 = rt.TCanvas("c1", "afterPulse2", 800, 600)
f1 = rt.TF1("f1", "[0]*exp([1]*x)+[2]", 0, 10)
f1.SetParameters(40, -0.3, 0)
h1 = rt.TH1F("h1", "afterPulse2", 9, 0.5, 9.5)
for str in str2:
    h1.Fill(int(str))

h1.Fit(f1)
rt.gStyle.SetOptFit(1111)
h1.SetXTitle("time(#mus)")
h1.SetYTitle("count")
h1.Draw()
f1.Draw("SAME")
c1.SaveAs("fig/afterPulse02r.pdf")
