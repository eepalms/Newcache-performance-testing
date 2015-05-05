mkdir -p /home/haow/testing/checkpoint/smbd.0
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/smbd.0 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="smbd" --clientbench="smbd.0" --checkpoint-dir=../testing/checkpoint/smbd.0 --mem_lat="66.7ns" --clock="3GHz" --maxinsts=1000000000 &
