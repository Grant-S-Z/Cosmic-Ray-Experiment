#include "TChain.h"
#include "TFile.h"
#include "TString.h"
#include "TMath.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TSystem.h" 
#include "TClass.h"
#include "TVector3.h"
#include "TCanvas.h"
#include "./WaveRead.h"
#include <cstdlib>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main(){

    TTree* wavedata=new TTree("wavedata","wavedata");
    float_t q1,q2,t1,t2;
    wavedata->Branch("q1",&q1);
    wavedata->Branch("q2",&q2);
    wavedata->Branch("t1",&t1);
    wavedata->Branch("t2",&t2);

    for(int_t i=0;i<=40;i++){
        waveform a=dataread(i);
        q1=a.getq1();
        q2=a.getq1();
        t1=a.gett1();
        t2=a.gett2();
        wavedata->Fill();
    }

    wavedata->SaveAs("wavedata.root");
    delete wavedata;
    return 0;
}
