#!/usr/bin/python3
import urllib.request
import json
import os
import argparse
from platformnec import PlatformSupergrafx
from platformmicrosoft import PlatformWindows, PlatformMsx, PlatformXbox
from platformmsdos import PlatformMsdos
from platformelektronika import PlatformPdp11
from platformamiga import PlatformAmigaOSECS, PlatformAmigaAGA, PlatformAmigaPPCRTG
from platformapple import PlatformApple
from platformamstrad import PlatformCaprice, PlatformCrocods
from platformnintendo import PlatformGameboy, PlatformGameboyColor, PlatformGameboyAdvance, PlatformFamicom, PlatformSuperFamicom, PlatformVirtualboy, PlatformN64, PlatformGamecube, PlatformWii, PlatformPokemini, PlatformDS
from platformatari import PlatformAtarist, PlatformAtarixlxe, PlatformFalcon, PlatformJaguar, PlatformLynx, PlatformVcs
from platformsinclair import PlatformZx81, PlatformZxspectrum
from platformcommodore import PlatformCommodore64, PlatformCommodorePet, PlatformCommodore128, PlatformCommodorePlus4, PlatformCommodoreVIC20, PlatformCommodoreCBM
from platformlinux import PlatformLinux
from platformtic80 import PlatformTic80
from platformsega import PlatformMegadrive, PlatformGamegear, PlatformMastersystem, PlatformGenesis, PlatformFlycast, PlatformSaturn
from platformneogeo import PlatformNeogeo, PlatformNeopocket, PlatformNeopocketcolor
from platformsony import PlatformPsx, PlatformPsp, PlatformPs2
from platformmattel import PlatformIntellivision
from platformarchimedes import PlatformAcorn
from platformenterprise import PlatformEnterprise
from platformwild import PlatformGamemusic, PlatformVideoMPV, PlatformVideoFFMPEG
from platformjava import PlatformJava
from platformpalm import PlatformPalm
from platformpico8 import PlatformPico8
from platformvectrex import PlatformVectrex

parser = argparse.ArgumentParser(description='Show a demo on screen.')
parser.add_argument('pouetid', type=int, nargs='?',
                    help='Pouet ID of the production to show')
parser.add_argument('--platforms', action="store_true",
                    help='List supported platforms and exit')
parser.add_argument('--random', action="store_true",
                    help='Play random productions')

args = parser.parse_args()

# In priority order
platform_runners = [PlatformAmigaOSECS(), PlatformAmigaAGA(), PlatformAmigaPPCRTG(),
                    PlatformCaprice(), PlatformCrocods(), PlatformFamicom(),
                    PlatformSuperFamicom(), PlatformN64(), PlatformGameboy(),
                    PlatformGameboyColor(), PlatformGameboyAdvance(), PlatformAtarist(),
                    PlatformAtarixlxe(), PlatformFalcon(), PlatformFalcon(), PlatformJaguar(),
                    PlatformLynx(), PlatformVcs(), PlatformZx81(), PlatformZxspectrum(),
                    PlatformCommodore64(), PlatformCommodorePet(), PlatformCommodore128(),
                    PlatformCommodorePlus4(), PlatformCommodoreVIC20(), PlatformCommodoreCBM(),
                    PlatformGamecube(), PlatformWii(), PlatformPokemini(), PlatformDS(),
                    PlatformVirtualboy(), PlatformWindows(), PlatformMsdos(), PlatformLinux(),
                    PlatformApple(), PlatformTic80(), PlatformNeogeo(), PlatformNeopocket(),
                    PlatformNeopocketcolor(), PlatformSupergrafx(), PlatformMsx(), PlatformXbox(),
                    PlatformGamegear(), PlatformMastersystem(), PlatformMegadrive(),
                    PlatformGenesis(), PlatformSaturn(), PlatformEnterprise(), PlatformPsx(),
                    PlatformPs2(), PlatformPsp(), PlatformIntellivision(), PlatformJava(),
                    PlatformAcorn(), PlatformPalm(), PlatformPico8(), PlatformVectrex(),
                    PlatformFlycast(), PlatformPdp11(), PlatformGamemusic(), PlatformVideoMPV(),
                    PlatformVideoFFMPEG()]

if args.platforms:
    for r in platform_runners:
        for p in r.supported_platforms():
            print(p)
    exit(0)

showetdir = os.path.expanduser("~/.showet")

if not os.path.exists(showetdir):
    os.makedirs(showetdir)

if not args.pouetid:
    print("No pouet id specified. Use --help to see options.")
    exit(-1)

prod_id = args.pouetid
prod_url = "http://api.pouet.net/v1/prod/?id=" + str(prod_id)
datadir = showetdir + "/data/" + str(prod_id)
prod_download_url = None
prod_download_filename = None
prod_json = None
prod_json_filename = datadir + "/pouet.json"

# Get the json data:
if os.path.exists(prod_json_filename):
    print("Json already downloaded")
    with open(prod_json_filename, 'r') as f:
        prod_json = f.read()
else:
    if not os.path.exists(datadir + '/json'):
        os.makedirs(datadir + '/json')
    with urllib.request.urlopen(prod_url) as url:
        prod_json = url.read().decode()
    with open(prod_json_filename, 'w') as f:
        f.write(prod_json)
        f.close()

# print(prod_json)

data = json.loads(prod_json)

prod_platform = None

runner = None

platforms = []
for p in data['prod']['platforms'].values():
    platforms.append(p['slug'])

for prunner in platform_runners:
    for demoplat in platforms:
        if prod_platform is None and demoplat in prunner.supported_platforms():
            prod_platform = demoplat
            runner = prunner

if not runner:
    print("ERROR: Platform " + str(platforms) + " not supported (yet!).")
    exit(-1)

if len(platforms) > 1:
    print("Demo supports platform platforms ", platforms,
          "of which", prod_platform, "rules the most.")

print("\tName: " + data['prod']['name'])
try:
    print("\tBy: " + data['prod']['groups'][0]['name'])
except IndexError:
    pass
print("\tType: " + data['prod']['type'])
# print("\tReleased: " + data['prod']['releaseDate'])
print("\tPlatform: " + prod_platform)

# Get necessary fields from the data

prod_download_url = data['prod']['download']
prod_download_url = prod_download_url.replace(
    "https://files.scene.org/view", "https://files.scene.org/get")

if os.path.exists(datadir + "/.FILES_DOWNLOADED"):
    print("\tFile already downloaded")
else:
    print("\n\tDownloading prod file from " + prod_download_url + "...")
    filedata = urllib.request.urlopen(prod_download_url)
    filename = os.path.basename(filedata.url)
    if len(filename) == 0:
        print("Error downloading file at ", prod_download_url)
        exit(-1)
    print("\n\tFilename: ", filename)
    prod_download_filename = datadir + "/" + filename
    datatowrite = filedata.read()

    with open(prod_download_filename, 'wb') as f:
        f.write(datatowrite)

    print("\tDownloaded: ", prod_download_filename,
          "\n\tFilesize: ", os.path.getsize(prod_download_filename))

    # Decompress the file if needed
    if prod_download_filename.endswith(".lha"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("lhasa x " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".7z"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("7z x " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".zip"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("unzip -u -d " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".tar.bz2"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("tar xjvf " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".tar.gz"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("tar xzvf " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".bz2"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("bunzip2 " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".rar"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("7z x " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".gz"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("gunzip " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".tar"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("tar xf " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".tbz2"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("tar xjvf " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".tgz"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("tar xzvf " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    if prod_download_filename.endswith(".7z"):
        print("\tExtracting:", prod_download_filename)
        ret = os.system("7z x " + datadir + " " + prod_download_filename)
        if ret == 1:
            print("\tExtracting file failed!")

    open(datadir + "/.FILES_DOWNLOADED", 'a').close()

runner.setup(showetdir, datadir, prod_platform)
runner.run()
