from platformcommon import PlatformCommon
import os

fullscreen = ['false']


class PlatformEnterprise(PlatformCommon):
    def run(self):
        extensions = ['img', 'dsk', 'tap', 'dtf', 'com',
                      'trn', '128', 'bas', 'cas', 'cdt', 'tzx', '.']
        for ext in extensions:
            print("looking for files ending with: " + ext)
            files = self.find_files_with_extension(ext)

        if len(files) == 0:
            files = self.find_ext_files()

        if len(files) == 0:
            print("Didn't find any runable files.")
            exit(-1)

        emulator = ['retroarch']
        fullscreen = ['false']
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append('ep128emu_core_libretro')
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

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
        return ['enterprise']

 # Tries to identify files by any magic necessary

    def find_ext_files(self):
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
                if not file.endswith('.json'):
                    ext_files.append(file)
                    print("Found file: " + file)

        return ext_files