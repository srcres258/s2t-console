# s2t-console

A terminal tool for converting Simplified Chinese into Traditional Chinese. 

# Usage

Ensure the requirements have been installed by pip at first:

```shell
pip install -r requirements.txt
```

Then execute either `s2t_console.py` or `s2t_file.py`.

For interactive use with shell, run `s2t_console.py`:

```shell
python s2t_console.py
```

For use with tons of files under a certain directory, use `s2t_file.py`:

```shell
python s2t_file.py pdir outdir
```

Where `pdir` stands for the directory of untranslated files, `outdir` stands
for the directory to output translated files.

# License

Licensed under [the MIT License](https://spdx.org/licenses/MIT.html). See [LICENSE.txt] for details.
