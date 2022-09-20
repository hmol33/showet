import os
from platformcommon import PlatformCommon

# emulator = ['dosbox']
emulators = ['retroarch']
cores = ['dosbox_core_libretro']
fullscreen = ['false']


class PlatformMsdos(PlatformCommon):
    def run(self):
        extensions = ['exe', 'com', 'bat', 'conf', 'zip']
        for ext in extensions:
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            files = self.find_ext_files()
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        emulator = emulators[0]
        core = cores[0]
        fullscreen = fullscreens[0]

        if emulator == 'retroarch':
            emulator.append('-L')
            emulator.append(core)
            if fullscreen == ['true']:
                emulator.append('--fullscreen')
        if emulator == 'dosbox':
            emulator.append('-userconf')
            if fullscreen == ['true']:
                emulator.append('-fullscreen')
            emulator.append('-c')

        print("\tUsing: " + emulator)
        print("\tUsing core: " + core)
        print("\tUsing fullscreen: " + fullscreen)

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
            if emulator == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator == 'dosbox':
                emulator = emulator + ['-flipname', flipfile, files[0]]
        self.run_process(emulator)

    def supported_platforms(self):
        return ['msdos', 'msdosgus']

    # Tries to identify files by any magic necessary
    def find_ext_files(self):
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0 and not file.endswith('.json') and not file.endswith('.txt'):
                ext_files.append(file)
                print("\tFound file: " + file)
        return ext_files
