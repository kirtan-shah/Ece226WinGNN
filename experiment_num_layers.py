import subprocess

for num_layers in range(1, 6):
    cmd = (f"python main.py --dataset uci-msg --lr 0.01 --maml_lr 0.008 --drop_rate 0.16 --window_num 8 --num_layers {num_layers} --cuda_device 0")
    out = subprocess.check_output(cmd, shell=True)
    results = out.decode().split('\n')[-2]
    print(f"{num_layers} layers", results)

 #python main.py --dataset uci-msg --lr 0.01 --maml_lr 0.008 --drop_rate 0.16 --window_num 8 --num_layers 2 --cuda_device 0