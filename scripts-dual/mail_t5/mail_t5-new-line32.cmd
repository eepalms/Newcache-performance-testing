cd /home/haow/newcache_v2/
build/X86/gem5.opt --outdir=../testing/outdir/mail_t5/mail_t5-new-line32 configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --checkpoint-dir=../testing/checkpoint/mail_t5 -r 1 --cpu-type=detailed --caches --l1d_size="32kB" --cacheline_size=32 --l1d_assoc=1024 --l1d_nebit=4 --l1d_alg="NEWCACHE" --l1d_index_pos="" --l1d_num_mshr=6 --l1d_num_target=8 --l1i_size="32kB" --l1i_assoc=4 --l2cache --l2_size="2MB" --l2_assoc=8 --maxinsts=1000000000 &