## About
A terminal utility to sort image files based on their characteristics.

## Motivation
This program was developed after I've realized that I had too many wallpapers, and too little time. Although there are more advanced programs with a wider range of features (e.g.: [variety](https://peterlevi.com/variety/), [hydrus](https://hydrusnetwork.github.io/hydrus/)) most of the times I just want to filter my wallpapers by resolution or ratio from my downloads to my wallpaper folder, without leaving my terminal.

As so this tool was born, a minimal solution, which is meant to be used in a terminal ecosystem with other common utilities found in Linux based OSs, to assist the user in filtering image files.


## Installation
### Dependencies
This program requires Python version 3 as well as the following packages:
- [Pillow](https://pillow.readthedocs.io/en/stable/)

These packages are automatically resolved by `pip`.

### Stable version
Install this program directly from Pypi:
```console
$ pip install imgsort
```

### Development version
For the latests updates, install the program directly from the dev branch on this repository:
```console
$ pip install -e git+https://github.com/jpmvferreira/imgsort.git@dev#egg=imgsort
```

If instead you want to make changes to the source code, then clone this repository locally and install it in editable mode:
```console
$ git clone https://github.com/jpmvferreira/imgsort
$ pip install -e imgsort
```


## Usage
Let us now see this program in action with a few examples. Remember that at any time the help dialog (`-h` or `--help`) is available to provide information regarding the available flags.

To tell if `wallpaper1.jpg` in your current working directory is 1920x1080, then using the `-s` or `--size` flag:
```console
$ imgsort wallpaper1.jpg -s 1920x1080
```

If the file is 1920x1080 then it will print its name, otherwise, it will print nothing.

If instead you want to know if `wallpaper1.jpg` is 16:9, you can use the same flag with with a ':' instead of the 'x':
```console
$ imgsort wallpaper1.jpg -s 16:9
```

This can also be used for several files, with different formats:
```console
$ imgsort wallpaper1.jpg wallpaper2.png -s 1920x1080
```

Naturally you can make use of bash's features, for example the wildcard statement, to filter a set of files which match a given pattern, in this case all of the .jpg files in the current working directory:
```console
$ imgsort *.jpg -s 1920x1080
```

This program also reads from STDIN, which means that you can create pipelines with it.

For example, if you wish to tell if all your wallpapers, located at `~/wallpapers` and respective subfolders, are 1920x1080, then create the following pipeline with `find`:
```bash
$ find ~/wallpapers | imgsort -s 1920x1080
```

If you wish to filter out all the wallpapers that are not 1920x1080, then you can rely on the `-o` or `--opposite` flag, which prints the file name if it doesn't match the provided size:
```bash
$ find ~/wallpapers | imgsort -s 1920x1080 -o
```

You can keep on adding to this pipeline to apply further actions.

Let's say you're trying to move all of your 1920x1080 wallpapers from `~/wallpapers/unsorted` to `~/wallpapers/fullhd`. By using the pipeline created above, and using [xargs](https://man7.org/linux/man-pages/man1/xargs.1.html) to which converts content found in STDIN to command line arguments, we can move all of those files to their designated location:
```bash
$ find ~/wallpapers/unsorted | imgsort -s 1920x1080 | xargs -I '{}' mv {} ~/wallpapers/fullhd
```

If you want to be sure that the program isn't doing anything funny, which you should, use `-v` or `--verbose` to print the image resolution or ratio to STDERR, which shouldn't affect the pipeline.


## Contributing
If you happen to find a bug, have a question or would like to suggest a feature or simply share some fancy terminal wizardry, feel free to open up an issue.

## Release cycle
This is a (very) small project, however, I do like to keep things tidy. As such I made a release cycle which goes as follows.

The first version will be 1.0.0, which is released once I consider that the program is good enough, and all the following versions will have the format X.Y.Z.

Each time that there is an update which does not modify the program behavior (e.g.: documentation, packaging) it will increment Z (e.g.: 1.0.0 -> 1.0.1).

Each time that there is an update which modifies the program behavior (e.g.: adding features, fixing bugs) it will increment Y and reset Z (e.g.: 1.0.1 -> 1.1.0).

Each time that there is an update which is not backwards compatible (e.g.: removing features, fundamental change on how the program is used) it will increment X and reset both Y and Z (e.g.: 1.1.2 -> 2.0.0).

In this Github repository you will find branches for the stable version (master) and the development version (dev). All modifications are done in the development branch and, after being tested, are included in the stable version, with the appropriate version bump.

## License
MIT
