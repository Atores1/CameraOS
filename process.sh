#ffmpeg -i videos/B-record.mp4 videos/B-photos/out%d.png
#ffmpeg -i videos/A-record.mp4 videos/A-photos/out%d.png
python3 calculateNdvi.py
#ffmpeg -framerate 30 -i videos/nir/img%03d.png -c:v libx264 -pix_fmt yuv420p 'videos/tmp/nir.mp4'
#ffmpeg -framerate 30 -i videos/red/img%03d.png -c:v libx264 -pix_fmt yuv420p 'videos/tmp/red.mp4'
#ffmpeg -i videos/tmp/red.mp4 -i videos/tmp/nir.mp4 -filter_complex "[1:v][0:v]scale2ref[wm][base];[base][wm]hstack=2" videos/final.mp4
ffmpeg -framerate 30 -i videos/ndvi/img%03d.png -c:v libx264 -pix_fmt yuv420p 'videos/tmp/ndvi.mp4'
ffmpeg -i videos/A-record.mp4 -i videos/tmp/ndvi.mp4 -filter_complex "[1:v][0:v]scale2ref[wm][base];[base][wm]hstack=2" videos/final.mov