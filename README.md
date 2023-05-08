# renaim

`renaim` is a simple Python script to rename image files in a specific format within the same directory. The script renames the files in a sequential order without any missing numbers. This is particularly useful when you have a collection of images with missing numbers in their filenames and want to fix the numbering.

![renaim](images/renaim.jpg)

## Usage

1. Place the `renaim.py` file in the directory containing the image files you want to rename.
2. Make sure the image files have names in the format `number-suffix.jpg`. For example, `1-image.jpg`, `3-image.jpg`, `5-image.jpg`, etc.
3. Run the script using Python:

```bash
python renaim.py
