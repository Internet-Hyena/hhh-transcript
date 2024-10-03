# fixes file paths while renaming asset files
# parses the output from `git status` and replaces the resulting paths across files
# run in src
function fix_file_paths_from_diff
    for diff in (git status --short)
        set -f paths (string match -g -r "R  (.*) -> (.*)" $diff)
        if not set -q paths[2]
            continue
        end
        set -f old $paths[1]
        set -f new $paths[2]
        sd -F $old $new *.md
    end
end