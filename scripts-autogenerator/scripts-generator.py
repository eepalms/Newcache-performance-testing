import os,sys,stat


gem5_base = 'cd /home/haow/newcache_v2/'
gem5_exe = 'build/X86/gem5.opt'
outdir_base = '/home/haow/testing/outdir/'
checkpoint_base = '/home/haow/testing/checkpoint/'

scripts_base = './'

# benchmark parameters
# bm[0]: benchmark suite name / client script name / outdir name / checkpoint name
# bm[1]: disk image
# bm[2]: server script name
benchmarks = [  ['apache', 'big.img', 'apache', 'NA'] ,
                ['mysql', 'mysqltest.img', 'mysql', 'NA'], 
                ['mail_t1', 'ain.img', 'mail', '1000000000'],
                ['mail_t2', 'ain.img', 'mail', '1000000000'],
                ['mail_t5', 'ain.img', 'mail', '1000000000'],
                ['smbd.0', 'ain.img', 'smbd', '1000000000'],
                ['smbd.1', 'ain.img', 'smbd', '1000000000'],
                ['ffserver.x1', 'ain.img', 'ffserver', 'NA'],
                ['ffserver.x3', 'ain.img', 'ffserver', '2000000000'],
                ['ffserver.x30', 'ain.img', 'ffserver', '3000000000'],
                ['tomcat.3', 'ain.img', 'tomcat', '2000000000'],
                ['tomcat.4', 'ain.img', 'tomcat', '2000000000'],
                ['tomcat.5', 'ain.img', 'tomcat', '3000000000'],
             ]

# gem5 configurations
#configuration[0]:                                 [1]line   [2]data-cache           [6]instruction-cache           [10]l2                   
configs = [  ['-l1i.new.base-l1d.SA.base-l2.SA.base', '64', 'LRU', '32kB', '8', '', 'NEWCACHE', '32kB', '512', '4', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit3-l1d.SA.base-l2.SA.base', '64', 'LRU', '32kB', '8', '', 'NEWCACHE', '32kB', '512', '3', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit5-l1d.SA.base-l2.SA.base', '64', 'LRU', '32kB', '8', '', 'NEWCACHE', '32kB', '512', '5', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit6-l1d.SA.base-l2.SA.base', '64', 'LRU', '32kB', '8', '', 'NEWCACHE', '32kB', '512', '6', 'LRU', '256kB', '8', ''],

             ['-l1i.new.base-l1d.new.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '4', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit3-l1d.new.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '3', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit5-l1d.new.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '5', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit6-l1d.new.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '6', 'LRU', '256kB', '8', ''],

             ['-l1i.new.base-l1d.new.nebit6-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '6', 'NEWCACHE', '32kB', '512', '4', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit3-l1d.new.nebit6-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '6', 'NEWCACHE', '32kB', '512', '3', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit5-l1d.new.nebit6-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '6', 'NEWCACHE', '32kB', '512', '5', 'LRU', '256kB', '8', ''],
             ['-l1i.new.nebit6-l1d.new.nebit6-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '6', 'NEWCACHE', '32kB', '512', '6', 'LRU', '256kB', '8', ''],


             #l1d tests
             ['-l1d.SA.base-l1i.SA.base-l2.SA.base', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.SA.size16-l1i.SA.base-l2.SA.base', '64', 'LRU', '16kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.SA.size64-l1i.SA.base-l2.SA.base', '64', 'LRU', '64kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.SA.assoc2-l1i.SA.base-l2.SA.base', '64', 'LRU', '32kB', '2', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.SA.assoc4-l1i.SA.base-l2.SA.base', '64', 'LRU', '32kB', '4', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],

             ['-l1d.new.base-l1i.SA.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '4', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.new.size16-l1i.SA.base-l2.SA.base', '64', 'NEWCACHE', '16kB', '256', '4', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.new.size64-l1i.SA.base-l2.SA.base', '64', 'NEWCACHE', '64kB', '1024', '4', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.new.nebit3-l1i.SA.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '3', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''],
             ['-l1d.new.nebit5-l1i.SA.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '5', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''], 
             ['-l1d.new.nebit6-l1i.SA.base-l2.SA.base', '64', 'NEWCACHE', '32kB', '512', '6', 'LRU', '32kB', '4', '', 'LRU', '256kB', '8', ''], 

             #l2 tests
             ['-l1d.SA.base-l1i.SA.base-l2.SA.size128', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '128kB', '8', ''],
             ['-l1d.SA.base-l1i.SA.base-l2.SA.size512', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '512kB', '8', ''],
             ['-l1d.SA.base-l1i.SA.base-l2.SA.assoc4', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '4', ''],
             ['-l1d.SA.base-l1i.SA.base-l2.SA.assoc16', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'LRU', '256kB', '16', ''],

             ['-l1d.SA.base-l1i.SA.base-l2.new.base', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'NEWCACHE', '256kB', '4096', '4'],
             ['-l1d.SA.base-l1i.SA.base-l2.new.size128', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'NEWCACHE', '128kB', '2048', '4'],
             ['-l1d.SA.base-l1i.SA.base-l2.new.size512', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'NEWCACHE', '512kB', '8192', '4'],
             ['-l1d.SA.base-l1i.SA.base-l2.new.nebit3', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'NEWCACHE', '256kB', '4096', '3'],
             ['-l1d.SA.base-l1i.SA.base-l2.new.nebit5', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'NEWCACHE', '256kB', '4096', '5'],
             ['-l1d.SA.base-l1i.SA.base-l2.new.nebit6', '64', 'LRU', '32kB', '8', '', 'LRU', '32kB', '4', '', 'NEWCACHE', '256kB', '4096', '6'],

             #l1d-l2 tests
             ['-l1d.new.base-l1i.SA.base-l2.new.base', '64', 'NEWCACHE', '32kB', '512', '4', 'LRU', '32kB', '4', '', 'NEWCACHE', '256kB', '4096', '4'],

             #l1i old tests
             ['-l1d.new.base-l1i.new.base-l2.new.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '256kB', '4096', '4'],
             ['-l1d.new.base-l1i.new.nebit3-l2.new.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '3', 'NEWCACHE', '256kB', '4096', '4'],
             ['-l1d.new.base-l1i.new.nebit5-l2.new.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '5', 'NEWCACHE', '256kB', '4096', '4'],
             ['-l1d.new.base-l1i.new.nebit6-l2.new.base', '64', 'NEWCACHE', '32kB', '512', '4', 'NEWCACHE', '32kB', '512', '6', 'NEWCACHE', '256kB', '4096', '4']
          ]



for bm in benchmarks:

    dir_name = scripts_base + bm[0]
    if not os.path.exists(dir_name):
      os.mkdir(dir_name)

    for configuration in configs:
      file_name = dir_name + '/' + bm[0] + configuration[0]
      #if not os.path.exists(file_name):
      fd = open(file_name, 'w')

      fd.write(gem5_base)
      fd.write('\n')
      fd.write(gem5_exe)

      #--outdir
      temp_string = ' --outdir=' + outdir_base + bm[0] + '/' + bm[0] + configuration[0]
      fd.write(temp_string)

      #configs and --kernel
      fd.write(' configs/example/fs.py --kernel=vmlinux')

      #--disk-image
      temp_string = ' --disk-image=' + bm[1]
      fd.write(temp_string)

      #--mem-size
      fd.write(' --mem-size="2048MB"')

      #--dual --serverbench --clientbench
      temp_string = ' --dual --serverbench="' + bm[2] + '" --clientbench="' + bm[0] + '"'
      fd.write(temp_string)

      #--checkpoint-dir
      temp_string = ' --checkpoint-dir=' + checkpoint_base + bm[0] + ' -r 1'
      fd.write(temp_string)

      #
      fd.write(' --clock="3GHz" --mem_lat="66.7ns" --cpu-type=detailed --caches')

      #--cacheline_size
      temp_string = ' --cacheline_size=' + configuration[1]
      fd.write(temp_string)

      #l1d
      temp_string = ' --l1d_alg="'+ configuration[2] + '" --l1d_size="' + configuration[3] + '" --l1d_assoc=' + configuration[4]
      fd.write(temp_string)

      if configuration[2] == 'NEWCACHE':
        temp_string = ' --l1d_nebit=' + configuration[5]
        fd.write(temp_string)
      
      fd.write(' --l1d_index_pos=""')

      #l1i
      temp_string = ' --l1i_alg="'+ configuration[6] + '" --l1i_size="' + configuration[7] + '" --l1i_assoc=' + configuration[8]
      fd.write(temp_string)

      if configuration[6] == 'NEWCACHE':
        temp_string = ' --l1i_nebit=' + configuration[9]
        fd.write(temp_string)

      #l2
      fd.write(' --l2cache')
      temp_string = ' --l2_alg="'+ configuration[10] + '" --l2_size="' + configuration[11] + '" --l2_assoc=' + configuration[12]
      fd.write(temp_string)
      if configuration[10] == 'NEWCACHE':
        temp_string = ' --l2_nebit=' + configuration[13]
        fd.write(temp_string)

      #l3
      fd.write(' --l3cache --l3_size="2MB" --l3_assoc=16')

      #max-inst
      if bm[3] != 'NA':
        temp_string = ' --maxinsts=' + bm[3]
        fd.write(temp_string)

      fd.write(' &\n')
      fd.close()

      st = os.stat(file_name)
      os.chmod(file_name, st.st_mode | stat.S_IEXEC)