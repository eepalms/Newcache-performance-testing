mkdir -p /home/haow/testing/checkpoint/mysql
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/mysql configs/example/fs.py --kernel=vmlinux --disk-image=mysqltest.img --mem-size="2048MB" --dual --serverbench="mysql" --clientbench="mysql" --checkpoint-dir=../testing/checkpoint/mysql --mem_lat="66.7ns" --clock="3GHz" &
