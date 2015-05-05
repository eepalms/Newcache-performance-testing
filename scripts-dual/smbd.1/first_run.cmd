mkdir -p /home/haow/testing/checkpoint/smbd.1
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/smbd.1 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="smbd" --clientbench="smbd.1" --checkpoint-dir=../testing/checkpoint/smbd.1 --clock="3GHz" --mem_lat="66.7ns" --maxinsts=1000000000 &
