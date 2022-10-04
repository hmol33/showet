import os
import os.path
from platformcommon import PlatformCommon

class Platform_Odyssey(PlatformCommon):
    emulators = ['retroarch']
    cores = ['o2em_libretro']
    fullscreens = ['false']

    emulator = ['retroarch']
    core = ['o2em_libretro']
    fullscreen = ['false']

    def run(self):
        extensions = ['bin']
        ext = []
        for ext in extensions:
            files = self.find_files_with_extension(ext)
        # if len(files) == 0:
        #      files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            files = self.find_ext_files()
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        emulator = ['retroarch']
        core = ['o2em_libretro']
        fullscreen = ['false']

        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append('o2em_libretro')
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))

        flipfile = self.datadir + "/fliplist.vfl"
        m3ufile = self.datadir + "/fliplist.m3u"
        with open(flipfile, "w") as f:
            f.write("UNIT 8\n")
            for disk in files:
                f.write(disk + "\n")
        with open(m3ufile, "w") as f:
            f.write("UNIT 8\n")
            for disk in files:
                f.write(disk + "\n")
        if len(files) > 0:
            files = self.sort_disks(files)
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
        self.run_process(emulator)

    def supported_platforms(self):
        return ['intellivision']

    # Tries to identify files by any magic necessary
    def find_ext_files(self):
        ext_files = []
        exclusions = ['json', 'txt', 'nfo', 'doc', 'me']
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
                if not file.endswith(str(exclusions)) and not file.endswith(str(exclusions).upper()):
                    ext_files.append(file)
                    print("\tFound file: " + file)
        return ext_files
