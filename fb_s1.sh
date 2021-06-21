./tool_filter.py --input $1 --brightness 0.8 --saturation 0.5
./tool_text.py --mode 0 --bgimage ./temp/output.jpg \
    --fontcolor 200 200 100 255 --resize 1080 \
    --border 200 200 200 255 --footer="-- Louis" \
    --output 1.png --textalign="center"

rm -fr ./temp/