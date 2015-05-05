mkdir -p /home/haow/testing/checkpoint/clean
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/clean configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="clean" --clientbench="clean" --checkpoint-dir=../testing/checkpoint/clean --clock="3GHz" --mem_lat="66.7ns" &
