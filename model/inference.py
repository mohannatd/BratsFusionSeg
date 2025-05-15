import torch
import os
def check_cuda():
    if not torch.cuda.is_available():
        raise EnvironmentError("CUDA not available.")
    print("CUDA is available.")

def run_inference(output_path):
    check_cuda()
    print("Running inference... (placeholder)")
    nnUNet_raw = os.path.join('nnUNet_raw')
    os.environ["nnUNet_results"] = output_path
    os.environ["nnUNet_preprocessed"] = os.path.join('.')
    os.environ["nnUNet_raw"] = os.path.join('.')
    os.system(f"nnUNetv2_predict -i {nnUNet_raw} -o {output_path} -d 13 -c 3d_fullres -f all -tr nnUNetTrainerDiceCELoss_noSmooth")
