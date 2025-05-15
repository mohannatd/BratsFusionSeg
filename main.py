from data.prepare_data import prepare_dataset
from model.inference import run_inference
import argparse

def main(t1c_path, t1n_path, t2w_path, t2f_path, output_path):
    prepare_dataset(t1c_path, t1n_path, t2w_path, t2f_path)
    run_inference(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the main script with specified paths.')
    parser.add_argument('-t1c', required=True, help='Path to t1c file')
    parser.add_argument('-t1n', required=True, help='Path to t1n file')
    parser.add_argument('-t2w', required=True, help='Path to t2w file')
    parser.add_argument('-t2f', required=True, help='Path to t2f file')
    parser.add_argument('-output', required=True, help='Output directory')

    args = parser.parse_args()

    main(args.t1c, args.t1n, args.t2w, args.t2f, args.output)