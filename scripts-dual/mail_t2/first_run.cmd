mkdir -p /home/haow/testing/checkpoint/mail_t2
cd /home/haow/newcache_v2
build/X86/gem5.opt --outdir=../testing/outdir/mail_t2 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="mail" --clientbench="mail_t2" --checkpoint-dir=../testing/checkpoint/mail_t2 --mem_lat="66.7ns" --clock="3GHz" --maxinsts=1000000000 &
