import elice_utils

from time import sleep


def merge(input_filenames, output_filename):
    with open("./{}".format(output_filename), "w") as f:
        for fn in input_filenames:
            with open(fn, "r") as g:
                lines = g.readlines()
                f.writelines(lines)
    return


merge(["kaist1.txt", "kaist2.txt", "kaist3.txt"], "output.txt")

sleep(0.5)  # Wait 0.5 seconds before creating a download link.
elice_utils.send_file("output.txt")
