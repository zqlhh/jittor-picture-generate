import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', type=str)
parser.add_argument('--img_path', type=str)
parser.add_argument('--ed_path', type=str)
parser.add_argument('--which_epoch', type=int)
args = parser.parse_args()
cmd_str = f'python spade_test.py --name bs4vae/1691505133 --dataset_mode custom --label_dir {args.input_path} --image_dir {args.img_path} --edge_dir {args.ed_path} --label_nc 29 --no_instance --use_vae --which_epoch {args.which_epoch} --no_pairing_check'
subprocess.call(cmd_str, shell=True)#

