mkdir -p /home/haow/testing/checkpoint/apache
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/apache configs/example/fs.py --kernel=vmlinux --disk-image=big.img --mem-size="2048MB" --dual --serverbench="apache" --clientbench="apache" --checkpoint-dir=../testing/checkpoint/apache --mem_lat="66.7ns" --clock="3GHz" &
