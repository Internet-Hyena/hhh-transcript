# a nice wrapper for img2webp
# load this script with `source`
# 
# example: `make_anim aradiabot_facepalm 500 500 500 100 100 100 500 100 100`
# converts ./aradiabot_facepalm1.png etc. to a webp with the given ms duration for each frame
function make_anim --argument filename durations
    set -fa pngs (string match -r $filename'_?\d+\.png' (ls $filename""*))
    set -f durations $argv[2..]
    set -f output (path change-extension "webp" $filename)

    if not set -q pngs[1]
        echo "Could not find any matching PNG files."
        return 1
    end

    for i in (seq (count $pngs))
        if set -q durations[$i]
            set -a img_args -d $durations[$i]
        end
        set -fa img_args $pngs[$i]
    end

    echo img2webp $img_args -o $output
    img2webp $img_args -o $output
end
