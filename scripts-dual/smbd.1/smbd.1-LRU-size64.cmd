cd /home/haow/newcache_v2/
build/X86/gem5.opt --outdir=../testing/outdir/smbd.1/smbd.1-LRU-size64 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="smbd" --clientbench="smbd.1" --checkpoint-dir=../testing/checkpoint/smbd.1 -r 1 --clock="3GHz" --mem_lat="66.7ns" --cpu-type=detailed --caches --l1d_size="64kB" --cacheline_size=64 --l1d_assoc=8 --l1d_alg="LRU" --l1d_index_pos="" --l1i_size="32kB" --l1i_assoc=4 --l2cache --l2_size="256kB" --l2_assoc=8 --l3cache --l3_size="2MB" --l3_assoc=16 --maxinsts=1000000000 &
