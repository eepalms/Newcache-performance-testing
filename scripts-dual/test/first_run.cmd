mkdir -p /home/haow/testing/checkpoint/test
cd /home/haow/gem5-stable-50ff05095970
build/X86/gem5.opt --outdir=../testing/outdir/test configs/example/fs.py --kernel=vmlinux --disk-image=ain.img --mem-size="2048MB" --dual --serverbench="clean" --clientbench="clean" --checkpoint-dir=../testing/checkpoint/test  &
