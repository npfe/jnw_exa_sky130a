

all: typical etc mc summary



#TB=tran
TB=sweep
#VIEW=Sch
VIEW=Lay
CELL=JNW_EXA
LIB =JNW_EXA_SKY130A
OPT=

include ../../tech/make/sim.make

test:
	${MAKE} typical OPT="Debug"

typical: netlist
	cicsim run --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

slow: netlist
	cicsim run --name ${VIEW}_slow ${TB} ${OPT} ${VIEW} Gt Kss "Th,Tl" Vl

fast: netlist
	cicsim run --name ${VIEW}_fast ${TB} ${OPT} ${VIEW} Gt Kff "Th,Tl" Vh

tfs: netlist
	cicsim run --name ${VIEW}_tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt,Th,Tl" "Vt,Vl,Vh"

etc: netlist
	cicsim run --name ${VIEW}_etc ${TB} ${OPT} ${VIEW} Gt "Kss,Kff,Ksf,Kfs" "Th,Tl" "Vl,Vh"

mc: netlist
	cicsim run --name ${VIEW}_mc --count 30 --threads 8 --progress ${TB} ${OPT} ${VIEW} Gt "Kttmm" "Tt" "Vt"

ntc: netlist
	cicsim run --name ${VIEW}_ntc ${TB} ${OPT} ${VIEW} Gt "Ktt,Kss,Kff" "Tt" Vt

temp: netlist
	cicsim run --name ${VIEW}_temp ${TB} ${OPT} ${VIEW} Gt "Ktt" "Tt,Th,Tl" Vt

summary:
	cicsim summary --output "README.md"

slide:
	pandoc -s  -t slidy README.md -o README.html

fix_layout_paths:
	sed -i "s|~/pro/aicex/ip/$(shell echo $(LIB) | tr A-Z a-z)/design|..|g" ../../design/$(LIB)/$(CELL).mag


clean:
	-rm -rf output_*
	-rm -rf __pycache__
	-rm *.run
	-rm *.pdf
	-rm *.csv
