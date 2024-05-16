import opencc
import alive_progress as ap
import logging
import os
import argparse

logger: logging.Logger = None
converter: opencc.OpenCC = None


def s2t(words: str) -> str:
    return converter.convert(words)


def get_child_dir(pfdir, cfdir):
    return cfdir[len(pfdir): len(cfdir)]


def s2t_for_file(origin, target):
    oFile = open(origin)
    tFile = open(target, mode='w')
    lines = oFile.read().split('\n')
    with ap.alive_bar(len(lines)) as bar:
        for line in lines:
            tFile.write(s2t(line))
            tFile.write('\n')
            bar()


def walk_files(pdir, outdir):
    logger.info("PDir    >" + pdir)
    logger.info("OutDir  >" + outdir)
    if not os.path.exists(outdir):
        logger.info("(!) OutDir not existing, created.")
        os.makedirs(outdir)
    for root, dirs, files in os.walk(pdir):
        logger.info("**** Current RootDir Begin ****")
        outroot = os.path.join(outdir, get_child_dir(pdir, root))
        logger.info("Root    >" + root)
        logger.info("OutRoot >" + outroot)
        if not os.path.exists(outroot):
            logger.info("(!) OutRoot not existing, created.")
            os.makedirs(outroot)
        for i, name in enumerate(files):
            logger.info("**** Current File Begin ****")
            f = os.path.join(root, name)
            outf = os.path.join(outdir, get_child_dir(pdir, f))
            logger.info("File    >" + f)
            logger.info("OutFile >" + outf)
            s2t_for_file(f, outf)
            logger.info("**** Current File End ****")
        logger.info("**** Current RootDir End ****")


def main():
    global logger, converter

    parser = argparse.ArgumentParser()
    parser.add_argument("pdir", type=str, help="the directory of untranslated files")
    parser.add_argument("outdir", type=str, help="the directory to output translated files")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("s2t_file")
    converter = opencc.OpenCC("s2t.json")

    pdir: str = args.pdir
    outdir: str = args.outdir
    # Ensure the dir strings end with sep
    sep = os.path.sep
    if not pdir.endswith(sep):
        pdir += sep
    if not outdir.endswith(sep):
        outdir += sep

    walk_files(pdir, outdir)


if __name__ == "__main__":
    main()
