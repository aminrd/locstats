## 
## @package locstats
## @author Dimitri Kokkonis ([\@kokkonisd](https://github.com/kokkonisd))
## 
## This is the entry point for the `locstats` tool.
##

import sys
import os
import click

from .definitions import LANG_DATA, info, fail
from .loc import get_source_files, get_loc


@click.command()
@click.argument('language', nargs = 1)
@click.argument('src_dirs', nargs = -1)
@click.option('--strict',
              is_flag = True,
              default = False,
              help = "Run in strict mode (ignore comments and empty lines).")
@click.option('-m', '--minimal',
              is_flag = True,
              default = False,
              help = "Give minimal output (just the LOC count).")
@click.option('--silent',
              is_flag = True,
              default = False,
              help = "Silence all warnings (such as directories not being "\
                     "found).")
def main(language, src_dirs, strict, minimal, silent):
    """Counts the LOC in a given language in a given directory set."""

    # Check if language exists in database
    if language not in LANG_DATA:
        info(f"The language `{language}` doesn't exist or hasn't yet been "\
              "registered into our database.")

        info("\nHere's a list of all the languages we currently support:")
        print(f"{', '.join(sorted(list(LANG_DATA.keys())))}\n")

        info("If you'd like to contribute, you can check out locstats' "\
             "GitHub page: https://github.com/kokkonisd/locstats")
        exit(1)


    loc_count_per_file = []

    for src in src_dirs:
        # Get all the source files from the given directories
        source_files = get_source_files(
          src_dir = src,
          src_extensions = LANG_DATA[language]["extensions"],
          silent = silent
        )

        for file in source_files:
            # Count the LOC in each file
            loc_count_per_file.append((
              file,
              get_loc(file = file,
                      strict = strict,
                      comments = LANG_DATA[language]["comments"],
                      silent = silent)
            ))

    total_loc_count = sum(x[1] for x in loc_count_per_file)

    # Give the LOC count to the user
    if minimal:
        print(total_loc_count)
    else:
        print(f"You have written approximately {total_loc_count} LOC in "\
              f"{LANG_DATA[language]['official_name']}.")


if __name__ == "__main__":
    main()
