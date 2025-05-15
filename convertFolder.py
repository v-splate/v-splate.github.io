# You can use this to convert a .ply file to a .splat file programmatically in python
# Alternatively you can drag and drop a .ply file into the viewer at https://antimatter15.com/splat

from plyfile import PlyData
import numpy as np
import argparse
from io import BytesIO
import os, sys
import gzip 
import shutil
def process_ply_to_splat(ply_file_path):
    plydata = PlyData.read(ply_file_path)
    vert = plydata["vertex"]
    sorted_indices = np.argsort(
        -np.exp(vert["scale_0"] + vert["scale_1"] + vert["scale_2"])
        / (1 + np.exp(-vert["opacity"]))
    )
    buffer = BytesIO()
    for idx in sorted_indices:
        v = plydata["vertex"][idx]
        position = np.array([v["x"], v["y"], v["z"]], dtype=np.float32)
        scales = np.exp(
            np.array(
                [v["scale_0"], v["scale_1"], v["scale_2"]],
                dtype=np.float32,
            )
        )
        rot = np.array(
            [v["rot_0"], v["rot_1"], v["rot_2"], v["rot_3"]],
            dtype=np.float32,
        )
        SH_C0 = 0.28209479177387814
        color = np.array(
            [
                0.5 + SH_C0 * v["f_dc_0"],
                0.5 + SH_C0 * v["f_dc_1"],
                0.5 + SH_C0 * v["f_dc_2"],
                1 / (1 + np.exp(-v["opacity"])),
            ]
        )
        buffer.write(position.tobytes())
        buffer.write(scales.tobytes())
        buffer.write((color * 255).clip(0, 255).astype(np.uint8).tobytes())
        buffer.write(
            ((rot / np.linalg.norm(rot)) * 128 + 128)
            .clip(0, 255)
            .astype(np.uint8)
            .tobytes()
        )
    return buffer.getvalue()


def save_splat_file(splat_data, output_path):
    with open(output_path, "ab+") as f:
        length = len(splat_data)
        f.write(length.to_bytes(4, 'big')) 
        f.write(splat_data)
        f.close()

def compress_file(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        with gzip.open(output_path, 'wb') as f_out:
            #shutil.copyfileobj(f_in, f_out)
            f_out.writelines(f_in)

def main():
    parser = argparse.ArgumentParser(description="Convert PLY files to SPLAT format.")
    parser.add_argument(
        "input_files", nargs="+", help="The input PLY files to process."
    )
    parser.add_argument(
        "--output", "-o", default="outputFrameVideoGS.vsplat", help="The output SPLAT file."
    )
    parser.add_argument(
        "--compress", "-c", default=False, help="Compress the splate data with Gzip, default is False."
    )
    args = parser.parse_args()
    #splat_data = bytearray()
    for input_file in args.input_files: 
        print(f"Processing {input_file}...")
        output_file = ( args.output if len(args.input_files) == 1 else input_file + ".splat"  )
        for filename in os.listdir(input_file): 
            file_path = os.path.join(input_file, filename) 
            print(f"in folder Processing {filename}...")
            splat_data = process_ply_to_splat(file_path) 
            save_splat_file(splat_data, output_file)
        print(f"Saved {output_file}")
    if args.compress is True:
        compress_file(output_file, output_file+".gz")

if __name__ == "__main__":
    main()
