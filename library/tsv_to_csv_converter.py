# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:10:00 2021

@author: Benjamin Plattner
"""


def get_gzip(file_path):
    """
    Returns the appropriate function for handling the files. It is either
    a gzipped, or an uncompressed file.

    Parameters
    ----------
    file_path : str
        The path of the file which is either gzipped or uncompressed.

    Returns
    -------
    function
        Returns the appropriate function to open a file, either gzip or plain.

    """
    if(file_path.split('.')[-1] == 'gz'):
        import gzip
        return gzip.open
    else:
        return open


def conversion(in_file, out_file, remove_header):
    """
    Convert tsv to csv, replace commas with semicolons,
    escape single quotes, replace \\N with null and replace double quotes
    with double single quotes. Optionally remove the header.

    Gzipped files can be handled

    Parameters
    ----------
    in_file : str
        Path to input file, must be gzipped tsv or csv.
    out_file : str
        Path to output file, must be gzipped tsv or csv.
    remove_header : bool
        Remove header (true) or not (false).

    Returns
    -------
    None.

    """
    func_in = get_gzip(in_file)
    func_out = get_gzip(out_file)

    with func_in(in_file, mode='rt', encoding='utf-8') as file_in:
        print('Get number of lines - this may take a while...')
        num_lines = sum(1 for _ in file_in)

    print(f"Start conversion of {num_lines:,} from tsv to csv...")

    with func_in(in_file, mode='rt', encoding='utf-8') as file_in:
        with func_out(out_file, mode='wt', encoding='utf-8') as file_out:
            for i, line in enumerate(file_in):
                if(remove_header and i == 0):
                    print('Removed header')
                else:
                    if(i % (num_lines//20+1) == 0):
                        print(f"{(i/num_lines)*100:>5.1f}% - {i:>{len(str(num_lines))+4},}")
                    line = line.replace(",", ";")  # replace commas
                    # line = line.replace("\"", '\\"')  # escape double quote
                    # line = line.replace("\'\'", '\\"')  # first transform double single quotes to double quote
                    line = line.replace("\"", "\'\'")  # transform double quotes to double single quotes
                    line = line.replace("'", "''")  # then escape single quotes
                    line = line.replace("\t", ",")  # replace tab with comma
                    # line = line.replace(",\\N,", ",,")  # replace \N with nothing/null for PostgreSQL database
                    file_out.write(line)
    print("Complete")


if __name__ == "__main__":

    import os

    folder = "C:/Users/bnz/Downloads/"
    file_name  = "title.ratings"
    ending_in  = ".tsv.gz"
    ending_out = "1.csv.gz"
    remove_header = True

    in_file = os.path.join(folder, file_name+ending_in)
    out_file = os.path.join(folder, file_name+ending_out)

    conversion(in_file, out_file, remove_header)
