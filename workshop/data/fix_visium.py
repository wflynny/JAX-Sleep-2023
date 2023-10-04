import gzip
from pathlib import Path

def gunzip(f: Path):
    with gzip.open(f, "rb") as infile, open(f.parent / f.stem, "wb") as outfile:
        outfile.write(infile.read())

visium_root = Path(".").resolve() / "visium"
accessions = list(set(["_".join(str(p.stem).split("_")[1:3]) for p in visium_root.glob("GSM*")]))

for p in visium_root.glob("*.gz"):
    if p.suffixes[0] in (".json", ".jpg", ".png", ".csv"):
        gunzip(p)

for acc in accessions:
    acc_root = visium_root / acc
    acc_spatial = acc_root / "spatial"
    acc_root.mkdir(exist_ok=True)
    acc_spatial.mkdir(exist_ok=True)
    
    for f in visium_root.glob(f"*{acc}*"):
        if not f.is_file(): continue
        fname = f.name.split(f"{acc}_")[-1]
        if f.suffix == ".h5":
            f.rename(acc_root / fname)
        else:
            f.rename(acc_spatial / fname)
