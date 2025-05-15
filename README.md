# V-Splat
This is a WebGL implementation of a real-time renderer for frame-based video [3D Gaussian Splatting for Real-Time Radiance Field Rendering (3DGS)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) 

To generate the frame-based video splat file, first prepare all sequence of 3DGS  PLY files in a folder, run the [convertFolder.py](./convertFolder.py). You will get the outputFrameVideoGS.vsplat file which pack all frames data into a single binary file. 
Afterward, You can drag this vsplat file to our web viewer, [try it out here](https://v-splate.github.io/).

## controls

movement (arrow keys)

- left/right arrow keys to strafe side to side
- up/down arrow keys to move forward/back
- `space` to jump

camera angle (wasd)

- `a`/`d` to turn camera left/right
- `w`/`s` to tilt camera up/down
- `q`/`e` to roll camera counterclockwise/clockwise
- `i`/`k` and `j`/`l` to orbit

trackpad
- scroll up/down to orbit down
- scroll left/right to orbit left/right
- pinch to move forward/back
- ctrl key + scroll up/down to move forward/back
- shift + scroll up/down to move up/down
- shift + scroll left/right to strafe side to side

mouse
- click and drag to orbit
- right click (or ctrl/cmd key) and drag up/down to move forward/back
- right click (or ctrl/cmd key) and drag left/right to strafe side to side

touch (mobile)
- one finger to orbit
- two finger pinch to move forward/back
- two finger rotate to rotate camera clockwise/counterclockwise
- two finger pan to move side-to-side and up-down

other
- press 0-9 to switch to one of the pre-loaded camera views
- press '-' or '+'key to cycle loaded cameras
- press `p` to resume default animation
- drag and drop .ply file to convert to .splat
- drag and drop cameras.json to load cameras

## other features

- press `v` to save the current view coordinates to the url
- open custom `.vsplat` and `.splat` files by adding a `url` param to a CORS-enabled URL
- drag and drop a `.ply` file which has been processed with the 3d gaussian splatting software onto the page and it will automatically convert the file to the `.splat` format

## examples

note that as long as your `.vsplat` and `.splat` file is hosted in a CORS-accessible way, you can open it with the `url` field. 
 
- https://v-splate.github.io/?url=filepath.vsplat 

## acknowledgements

This work is modified based on the [WebGL 3D Gaussian Splat Viewer by Kevin Kwok (Antimatter15) ](https://github.com/antimatter15/splat).
Thanks to [Kevin Kwok(Antimatter15) ](https://github.com/antimatter15/splat) for the major contribution.  