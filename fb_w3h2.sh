./tool_filter.py --input $1 --brightness 0.8 --saturation 0.1
./tool_slice.py --input ./temp/output.jpg --output=a.jpg --width-proportion 1 --height-proportion 2 1
./tool_slice.py --input ./temp/0,1a.jpg --output=b.jpg --width-proportion 1 1 1 --height-proportion 1

./tool_text.py --mode 2 --bgimage ./temp/0,0a.jpg \
    --fontcolor 200 200 0 255 --resize 1080 \
    --output 1.png
./tool_text.py --mode 0 --bgimage ./temp/0,0b.jpg \
    --fontcolor 200 200 0 255 --resize 1080 \
    --border 200 200 100 255 --footer="-- Louis" \
    --output 2.png
./tool_text.py --mode 0 --bgimage ./temp/1,0b.jpg \
    --fontcolor 200 200 0 255 --resize 1080 \
    --border 200 200 100 255 --footer="-- Louis" \
    --output 3.png
./tool_text.py --mode 0 --bgimage ./temp/2,0b.jpg \
    --fontcolor 200 200 0 255 --resize 1080 \
    --border 200 200 100 255 --footer="-- Louis" \
    --output 4.png

rm -fr ./temp/