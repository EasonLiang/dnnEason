General :
	in2_out2_h1n2.cpp is a dnn sample application invoking libeason.so realized in C++.
	About the DNN realized by eason :
					input layer 	: 2 nodes : i1 i2
					output layer : 2 nodes : (target)o1 (target)o2
		hidden(neural) layer 	: 2 neurons : h1n1 h1n2
			activation function : sigmoid
	====================================================
	weights:	w1/2/3/4 = 0.15/0.20/0.25/0.30 ;
				w5/6/7/8 = 0.40/0.45/0.50/0.55 ;
	learning rate : 0.5 ;	bias_1 = 0.35 ; bias_2 = 0.60

		i1 ----w1---- h1n1 ----w5------ o1 
			    \	    		/		 \			/
			 	\	 w2			  \		  w6
			     	      .						.
			 	 /	\				   /	    \
			  / 	 w3				/	  w7
			  /	    	    \			      /			\
		i2 ----w4---- h1n2 ----w8------ o2
			  +bias_1+			+bias_2+

	For masked code statement : // element.train(80000) : It need 80000 turns training to get a satisfied mse .
	So run code statement : element.setInput_TargetOutput({input_i1,input_i2},{output_o1,output_o2}) : to set o1 to 0.13 (in include/eason.h) to narrow down the turns.
	For code statement : element.train(8000,false) : You could see 8000 turns training is enough to get 0.129986413|0.13 , 0.982519705|0.99 .
	=====================================================
	eason::train(...) : parameter 01 : turns (default to 20);
	eason::train(...) : parameter 02 : logOut (default to true to control the log output when training);
	eason::train(...) : parameter 03 : autoTrain (default to false, when enabled it will train automatically according to mse in last parameter);
	eason::train(...) : parameter 04 : mse_threshold (along with parameter 03);

(A) instruction for dnn realized by eason 
platforms : Archlinux + Ubuntu16.04.7 + Ubuntu22.04.2 
depends : no
compile : run command ' g++ -o what -Llibs -lAutoInfer_ArchLinux main_autoInfer.cpp  -I include/autoInferClass'

env_set :  $ export LD_LIBRARY_PATH=libs/

run-01 (manually assigned 80000 turns to train, then change weights to take 8000 epchs to train) : ./elf_autoInfer_ArchLinux
run-02 (manually assigned 80000 turns to train, then automatically train when mse less than value input in cmd-line) : ./elf_autoInfer_ArchLinux 0.000027985
	PS : for run-02 , the cmd-line input value is listed in weights_mse_calculator.pdf, just round up the last digit in column 'MSE'
		  example:
				for value 0.000027996 in turns-7997-column-mse 
					run : $ ./elf_autoInfer_ArchLinux 0.000027997
				for value 0.000027984 in turns-7999-column-mse
					run : $ ./elf_autoInfer_ArchLinux 0.000027985
			then the elf_autoInfer_ArchLinux will automatically inferring until the mse less than the input value , output the epochs iterated in last.