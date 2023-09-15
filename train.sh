#CUDA_VISIBLE_DEVICES="2,3" mpirun -np 2 python train.py --input_path /home/lizg/zhq/gaugan/train_resized #
CUDA_VISIBLE_DEVICES="0"  python train.py --input_path ./train_resized
#0,1,2,
