mkdir -p /home/haow/testing/checkpoint/tomcat.5
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/tomcat.5 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="tomcat" --clientbench="tomcat.5" --checkpoint-dir=../testing/checkpoint/tomcat.5 --clock="3GHz" --mem_lat="66.7ns" &
