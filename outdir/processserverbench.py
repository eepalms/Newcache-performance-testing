import sys
import re
# keyword is a list of keywords in the stats file
def process_raw_stats(file_name, keywords):
	fin = open(file_name, 'r')
        lines = fin.readlines()
        results = []
        for i in range(len(keywords)):
		results.append('')

        for line in lines:
        	linefield = re.split('\s+', line)
                count = keywords.count(linefield[0]) 
                if count == 1:
			index = keywords.index(linefield[0])
                        results[index] = linefield[1]
	fin.close()
	return results	

############## global variables ###########
result_all = []
fout = open('/home/haow/CAL-icache.dat', 'w')
#fout = open('/home/haow/stats_mse3-1.dat', 'w')
#fout = open('/home/haow/stats_mse3-2.dat', 'w')

keywords = ['testsys.switch_cpus.ipc_total','testsys.cpu.icache.overall_miss_rate::total']

#keywords = ['testsys.switch_cpus.ipc_total','testsys.cpu.icache.overall_miss_rate::total','testsys.l2.overall_miss_rate::switch_cpus.inst',
#'testsys.l2.overall_misses::switch_cpus.inst', 'testsys.cpu.icache.overall_accesses::total']

#keywords = ['testsys.switch_cpus.ipc_total', 'testsys.cpu.dcache.overall_miss_rate::total','testsys.cpu.dcache.overall_mshr_misses::total',
#'testsys.switch_cpus.commit.committedInsts','testsys.l2.overall_misses::switch_cpus.data','testsys.cpu.dcache.overall_accesses::total']

#keywords = ['testsys.switch_cpus.ipc_total','testsys.cpu.icache.overall_miss_rate::total','testsys.cpu.icache.overall_mshr_misses::total',
#'testsys.switch_cpus.commit.committedInsts', 'testsys.l2.overall_misses::switch_cpus.inst', 'testsys.cpu.icache.overall_accesses::total']

#keywords = ['system.cpu.commit.committedInsts', 'system.cpu.dcache.overall_miss_rate::total', 'system.cpu.dcache.overall_mshr_misses::total', 'system.cpu.ipc_total', 'system.l2.demand_mshr_misses::total']

prog_names = ['apache/apache-','mysql/mysql-','mail_t1/mail_t1-','mail_t2/mail_t2-','mail_t5/mail_t5-','smbd.0/smbd.0-','smbd.1/smbd.1-', 'ffserver.x1/ffserver.x1-', 'ffserver.x3/ffserver.x3-', 'ffserver.x30/ffserver.x30-', 'tomcat.3/tomcat.3-', 'tomcat.4/tomcat.4-', 'tomcat.5/tomcat.5-']

#prog_names = ['canvas_redraw-', 'drawarc-', 'drawcircle-', 'drawcircle2-', 'drawimage-', 'drawrect-', 'drawtext-', 'gc-', 'kubench-', 'lesson08-', 'lesson16-2b-', 'teapot-', 'scimark2-', 'linpack-']

#prog_names = ['apache-l1i-mse/apache-','mysql-l1i-mse/mysql-','mail_t1-l1i-mse/mail_t1-','mail_t2-l1i-mse/mail_t2-','mail_t5-l1i-mse/mail_t5-','smbd.0-l1i-mse/smbd.0-','smbd.1-l1i-mse/smbd.1-', 'ffserver.x1-l1i-mse/ffserver.x1-', 'ffserver.x3-l1i-mse/ffserver.x3-', 'ffserver.x30-l1i-mse/ffserver.x30-', 'tomcat.3-l1i-mse/tomcat.3-', 'tomcat.4-l1i-mse/tomcat.4-', 'tomcat.5-l1i-mse/tomcat.5-']

base_dir = '/home/haow/testing/outdir/'

configs = ['l1d.SA.base-l1i.SA.base-l2.SA.base','l1i.new.nebit3-l1d.SA.base-l2.SA.base','l1i.new.base-l1d.SA.base-l2.SA.base','l1i.new.nebit5-l1d.SA.base-l2.SA.base','l1i.new.nebit6-l1d.SA.base-l2.SA.base']

#configs = ['l1i.new.nebit3-l1d.new.base-l2.SA.base','l1i.new.base-l1d.new.base-l2.SA.base','l1i.new.nebit5-l1d.new.base-l2.SA.base','l1i.new.nebit6-l1d.new.base-l2.SA.base','l1i.new.nebit3-l1d.new.nebit6-l2.SA.base','l1i.new.base-l1d.new.nebit6-l2.SA.base','l1i.new.nebit5-l1d.new.nebit6-l2.SA.base','l1i.new.nebit6-l1d.new.nebit6-l2.SA.base']

#configs = ['LRU-assoc2', 'LRU-assoc4', 'LRU-assoc8', 'LRU-size16', 'LRU-size64', 'new-base', 'new-size16', 'new-size64', 'new-nebit3', 'new-nebit5', 'new-nebit6']

for program in prog_names:
	for configuration in configs:
		file_name = base_dir + program + configuration + '/stats.txt'
		result = process_raw_stats(file_name, keywords)
		result_all.append(result)
		print result


#################### write formatted data to file

num_configs = len(configs)
num_columns = len(keywords)
num_programs = len(prog_names)

for col in range(num_columns):
	for prog in range(num_programs):
		for config in range(num_configs):
			row = prog*num_configs + config
			fout.write(result_all[row][col]+'\t') 
		fout.write('\n')

fout.close()









