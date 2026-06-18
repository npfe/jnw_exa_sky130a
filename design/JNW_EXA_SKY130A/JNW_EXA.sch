v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
T {IBP is a current source
- Vgs can be computed assuming:
	- Id 20uA
	- Vth 0.271V
	- Capacitive oxyde NMOS: 0.0083 fF/um^2
	- Carrier mobility NMOS: 0.01 V^-1
	- Vth: 0.251 V
	- Width: 12
	- Len: 5
- k = Carrier Mobility * Capacitive Oxyde * (Width / Length)
- Overdrive voltage Vov = sqrt(2 * Id/ k)
- Which gives Vgs = 0.529V } -890 -880 0 0 0.4 0.4 {}
N -150 -560 -150 -470 {lab=VSS}
N -150 -470 -130 -470 {lab=VSS}
N -150 -470 -150 -440 {lab=VSS}
N -150 -440 -130 -440 {lab=VSS}
N 50 -590 70 -590 {lab=VSS}
N 70 -590 70 -470 {lab=VSS}
N 50 -470 70 -470 {lab=VSS}
N 70 -470 70 -440 {lab=VSS}
N 50 -440 70 -440 {lab=VSS}
N -90 -470 10 -470 {lab=IBP}
N -90 -590 10 -590 {lab=IBP}
N -150 -590 -150 -560 {lab=VSS}
N -150 -590 -130 -590 {lab=VSS}
N -130 -560 -130 -500 {lab=#net1}
N 50 -560 50 -500 {lab=#net2}
N -150 -440 -150 -400 {lab=VSS}
N -160 -400 -150 -400 {lab=VSS}
N -150 -400 70 -400 {lab=VSS}
N 70 -440 70 -400 {lab=VSS}
N -210 -400 -160 -400 {lab=VSS}
N -130 -670 -130 -620 {lab=IBP}
N -210 -840 -130 -840 {lab=IBP}
N -130 -840 -130 -730 {lab=IBP}
N 50 -840 50 -620 {lab=IBN}
N 50 -840 70 -840 {lab=IBN}
N -130 -730 -130 -720 {lab=IBP}
N -130 -700 -130 -670 {lab=IBP}
N -130 -720 -130 -700 {lab=IBP}
N -130 -720 -40 -720 {lab=IBP}
N -40 -720 -40 -590 {lab=IBP}
N -40 -590 -40 -470 {lab=IBP}
C {devices/ipin.sym} -210 -400 0 0 {name=p2 lab=VSS}
C {devices/ipin.sym} -210 -840 0 0 {name=p1 lab=IBP}
C {devices/ipin.sym} 70 -840 0 1 {name=p3 lab=IBN}
C {cborder/border_s.sym} 330 -250 0 0 {company="npfe" user="npfe" user_updated="tcleval($env(USER))"}
C {JNW_ATR_SKY130A/JNWATR_NCH_12C5F0.sym} 10 -590 0 0 {name=x3}
C {JNW_ATR_SKY130A/JNWATR_NCH_12C5F0.sym} 10 -470 0 0 {name=x4}
C {JNW_ATR_SKY130A/JNWATR_NCH_12C5F0.sym} -90 -470 0 1 {name=x2}
C {JNW_ATR_SKY130A/JNWATR_NCH_12C5F0.sym} -90 -590 0 1 {name=x1}
