#ifndef _WAVEREAD_H
#define _WAVEREAD_H
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
#include "TGraph.h"
#include <cstdlib>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

class waveform{
    public:
    float_t tlist[1000];
    float_t ch1list[1000];
    float_t ch2list[1000];
    waveform(int_t a);
    floa_t gett1(void);
    floa_t gett2(void);
    floa_t getq1(void);
    floa_t getq2(void);
    ~waveform();
}

waveform::waveform(int_t a){
    string FilePath=Form("/home/wangyp/exptdata/comsicrayexpt/data/lengtha%d",a);
    ifstream ifile(FilePath, ios::app);
    string temp;
    int_t i=0;
    
    while(getline(ifile,temp)){
        string[3] arr=temp.split(',');
        if (arr[0]!='Time(s)'){
            tlist[i]=stof(arr[0]);
            ch1list[i]=stof(arr[1]);
            ch2list[i]=stof(arr[2]);
            i++;
        }
        if(i=1000){
            break;
        }
    }
    ifile.close();
}
float_t waveform::gett1(){
    TGraph* g1=new TGraph(1000,tlist,ch1list);
    float_t vmax=g1.GetMaximum ();
    float_t vmin=g1.GetMinimum ();
    float_t trigger=0.9*vmax+0.1*vmin;
    float_t tbegin=tlist[500];
    for (int i=0;i<1000;i++){
        if (ch1list[i]<trigger){
            tbegin=tlist[i];
            g1->delete();
            return tbegin;
        }
    }
}

float_t waveform::gett2(){
    TGraph* g2=new TGraph(1000,tlist,ch2list);
    float_t vmax=g2.GetMaximum();
    float_t vmin=g2.GetMinimum();
    float_t trigger=0.9*vmax+0.1*vmin;
    float_t tbegin=tlist[500];
    for (int i=0;i<1000;i++){
        if (ch2list[i]<trigger){
            tbegin=tlist[i];
            g2->delete();
            return tbegin;
        }
    }
}

float_t waveform::getq1(){
    TGraph* g1=new TGraph(1000,tlist,ch1list);
    float_t vmax=g1.GetMaximum ();
    float_t vmin=g1.GetMinimum ();
    float_t trigger=0.9*vmax+0.1*vmin;
    int_t tbegin=500;
    int_t tend=750;
    float_t baseline=vmax;
    float_t total=0;
    for (int i=0;i<250,i++){
        total+=ch1list[i];
    }
    baseline=total/250;
    for (int i=0;i<1000;i++){
        if ((ch1list[i]-trigger>0) &&(ch1list[i+1]-trigger<0)){
            tbegin=i;
        }else if((ch1list[i]-trigger<0) &&(ch1list[i+1]-trigger>0)){
            tend=i;
            break;
        }
    }
    float1 q1=0;
    for (int i=tbegin;i<=tend;i++){
        q1+=(tlist[i+1]=tlist[i])*(baseline-ch1list[i]);
    }
    g1->delete();
    return q1;
}

float_t waveform::getq2(){
    TGraph* g1=new TGraph(1000,tlist,ch2list);
    float_t vmax=g1.GetMaximum ();
    float_t vmin=g1.GetMinimum ();
    float_t trigger=0.9*vmax+0.1*vmin;
    int_t tbegin=500;
    int_t tend=750;
    float_t baseline=vmax;
    float_t total=0;
    for (int i=0;i<250,i++){
        total+=ch2list[i];
    }
    baseline=total/250;
    for (int i=0;i<1000;i++){
        if ((ch2list[i]-trigger>0) &&(ch2list[i+1]-trigger<0)){
            tbegin=i;
        }else if((ch2list[i]-trigger<0) &&(ch2list[i+1]-trigger>0)){
            tend=i;
            break;
        }
    }
    float1 q1=0;
    for (int i=tbegin;i<=tend;i++){
        q1+=(tlist[i+1]=tlist[i])*(baseline-ch1list[i]);
    }
    g1->delete();
    return q1;
}


#endif
