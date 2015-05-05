mkdir -p /home/haow/testing/checkpoint/ffserver.x3
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/ffserver.x3 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="ffserver" --clientbench="ffserver.x3" --checkpoint-dir=../testing/checkpoint/ffserver.x3 --mem_lat="66.7ns" --clock="3GHz" --maxinsts=2000000000 &
