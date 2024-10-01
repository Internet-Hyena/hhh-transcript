# a nice wrapper for img2webp
# load this script with `source`
# 
# example: `make_anim aradiabot_facepalm 500 500 500 100 100 100 500 100 100`
# converts ./aradiabot_facepalm1.png etc. to a webp with the given ms duration for each frame
function make_anim --argument filename durations
    set -fa pngs (string match -r $filename'_?\d+'.png (ls))
    set -f durations $argv[2..]
    set -f output ./$filename.webp

    for i in (seq (count $pngs))
        if set -q durations[$i]
            set -a img_args -d $durations[$i]
        end
        set -fa img_args $pngs[$i]
    end

    echo img2webp $img_args -o $output
    img2webp $img_args -o $output
end
