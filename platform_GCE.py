import os
import os.path
import inquirer

from platformcommon import PlatformCommon

debugging = False

class Platform_Vectrex(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set whether we should run in fullscreens or not.
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch', 'vecx']
    cores = ['vecx_libretro']
    fullscreens = ['false']
    streamings = ['false', 'twitch', 'youtube', 'restream']
    recordings = ['true', 'false']
    extensions = ['zip', 'bin', 'vec']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set whether we should run in fullscreens or not.
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['vecx_libretro']
        emulators = ['retroarch', 'vecx']
        cores = ['vecx_libretro']
        
        fullscreen = ['false']
        streaming = ['false']
        recording = ['false']
        extensions = ['zip', 'bin', 'vec']

        emulator = []
        core = []
        def multiman(emulators,cores):
            # If multiple emulators are specified (e.g. 'retroarch', 'vice') ask the user to specify which one to use.
            if len(emulators) > 1:
                print('Info: Multiple emulators are supported: ' + str(emulators))
                prompt = [
                    inquirer.List('emulators', message='Please select one of the supported emulators to continue', choices=emulators),
                ]
                emulator = inquirer.prompt(prompt).get('emulators').strip().lower()
                if debugging != False:
                    print('Info: You selected: ' + str(emulator))
                    emulator = str(emulator)
            else:
                emulator = emulators
                print('Info: Only 1 emulator is supported: ' + str(emulator))
            # If multiple cores are specified (e.g. 'vice_x64sc_libretro', 'frodo_libretro') ask the user to specify which one to use.
            if len(cores) > 1:
                print('Info: Multiple cores are supported: ' + str(cores))
                prompt = [
                    inquirer.List('cores', message='Please select one of the supported emulators to continue', choices=cores),
                ]
                core = inquirer.prompt(prompt).get('cores').strip().lower()
                if debugging != False:
                    print('Info: You selected: ' + str(core))
                    core = str(core)
            else:
                core = cores
                print('Info: Only 1 core is supported: ' + str(core))

        multiman(emulators,cores)
        
        if emulator == 'retroarch':
            if core[0] == 'vecx_libretro':
                extensions = ['bin', 'vec']

        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions.
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE.
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary.
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            # Set whether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator == 'vecx':
            # Set whether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        if debugging != False:
            print("\tUsing emulator: " + str(emulator))
            print("\tUsing core: " + str(core))
            print("\tUsing extensions: " + str(extensions))
            print("\tUsing fullscreen: " + str(fullscreen))
            print("\tUsing recording: " + str(recording))
            print("\tUsing streaming: " + str(streaming))

        if len(files) > 0:
            # Sort the files.
            files = self.sort_disks(files)
            flipfile = self.datadir + "/fliplist.vfl"
            m3ufile = self.datadir + "/fliplist.m3u"
            with open(flipfile, "w") as f:
                #f.write("UNIT 8\n")
                for disk in files:
                    f.write(disk + "\n")
                f.write("#SAVEDISK:\n")
            with open(m3ufile, "w") as f:
                #f.write("UNIT 8\n")
                for disk in files:
                    f.write(disk + "\n")
                f.write("#SAVEDISK:\n")
            if emulator == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator == 'vecx':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['vectrex']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator == 'retroarch':
            if core[0] == 'vecx_libretro':
                extensions = ['bin', 'vec']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
                    if file.endswith(ext):
                        ext_files.append(file)
                        if debugging != False:
                            print("\tFound file: " + file)
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        if debugging != False:
                            print("\tFound file: " + file)
        return ext_files
