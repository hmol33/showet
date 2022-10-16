import os
import os.path
from platformcommon import PlatformCommon

class Platform_3DS(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch', 'citra']
    cores = ['citra_libretro', 'citra2018_libretro', 'citra_canary_libretro', 'melonds_libretro', 'desmume_libretro', 'desmume2015_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['citra_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app']

        if emulator == 'retroarch':
            if core == 'citra_libretro' or core == 'citra2018_libretro' or core == 'citra_canary_libretro':
                extensions = ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app']
        
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['nintendods']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):
        if emulator[0] == 'retroarch':
            if core[0] == 'citra_libretro' or core[0] == 'citra2018_libretro' or core[0] == 'citra_canary_libretro':
                extensions = ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
        return ext_files

class Platform_N64(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch', 'mupen64plus-glide64', 'mupen64plus-glide64-lle', 'mupen64plus-gliden64']
    cores = ['mupen64plus_libretro', 'mupen64plus_next_libretro', 'parallel_n46_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['n64', 'v64', 'z64', 'bin', 'u1', 'ndd']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.        
        emulator = ['retroarch']
        core = ['mupen64plus_next_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['n64', 'v64', 'z64', 'bin', 'u1', 'ndd']
        
        if emulator == 'retroarch':
            if core == 'mupen64plus_next_libretro':
                extensions = ['n64', 'v64', 'z64', 'bin', 'u1', 'ndd']
                
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['nintendo64']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):
        
        if emulator[0] == 'retroarch':
            if core[0] == 'mupen64plus_next_libretro':
                extensions = ['n64', 'v64', 'z64', 'bin', 'u1', 'ndd']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
        return ext_files

class Platform_DS(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch', 'desmume', 'melonds']
    cores = ['melonds_libretro', 'desmume_libretro', 'desmume2015_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'nds', 'dsi']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.        
        emulator = ['retroarch']
        core = ['desmume_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'nds', 'dsi']
        
        if emulator == 'retroarch':
            if core == 'desmume_libretro':
                extensions = ['nds', 'dsi']
        
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.apppend('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['nintendods']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'desmume_libretro':
                extensions = ['nds', 'dsi']
                        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
        return ext_files

class Platform_Famicom(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch', 'higan', 'emux', 'fceumm', 'nestopia', 'quicknes', 'mesen']
    cores = ['quicknes_libretro', 'nestopia_libretro', 'mess_libretro', 'mess2016_libretro', 'mesen_libretro', 'fceumm_libretro', 'fceumm_mod_libretro', 'fbneo_nes_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'nes', 'fds', 'unf', 'unif', 'qd', 'nsf']

    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['fceumm_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'nes', 'fds', 'unf', 'unif', 'qd', 'nsf']

        if emulator == 'retroarch':
            if core == 'quicknes_libretro' or core == 'bnes_libretro':
                extensions = ['nes']
            if core == 'emux_nes_libretro':
                extensions = ['nes', 'bin', 'rom']
            if core == 'nestopia_libretro' or core == 'fceumm_libretro' or core == 'mesen_libretro':
                extensions = ['fds', 'nes', 'unif', 'unf']
                
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['nesfamicom']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'quicknes_libretro' or core[0] == 'bnes_libretro':
                extensions = ['nes']
            if core[0] == 'emux_nes_libretro':
                extensions = ['nes', 'bin', 'rom']
            if core[0] == 'nestopia_libretro' or core[0] == 'fceumm_libretro' or core[0] == 'mesen_libretro':
                extensions = ['fds', 'nes', 'unif', 'unf']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                    
        return ext_files

class Platform_FamicomDisksystem(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch', 'higan', 'emux', 'fceumm', 'nestopia', 'quicknes', 'mesen']
    cores = ['quicknes_libretro', 'nestopia_libretro', 'mess_libretro', 'mess2016_libretro', 'mesen_libretro', 'fceumm_libretro', 'fceumm_mod_libretro', 'fbneo_nes_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'nes', 'fds', 'unf', 'unif', 'qd', 'nsf']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['quicknes_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'nes', 'fds', 'unf', 'unif', 'qd', 'nsf']

        if emulator == 'retroarch':
            if core == 'quicknes_libretro' or core == 'bnes_libretro':
                extensions = ['nes']
            if core == 'emux_nes_libretro':
                extensions = ['nes', 'bin', 'rom']
            if core == 'nestopia_libretro' or core == 'fceumm_libretro' or core == 'mesen_libretro':
                extensions = ['fds', 'nes', 'unif', 'unf']

        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')

        
        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['nesfamicom']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'quicknes_libretro' or core[0] == 'bnes_libretro':
                extensions = ['nes']
            if core[0] == 'emux_nes_libretro':
                extensions = ['nes', 'bin', 'rom']
            if core[0] == 'nestopia_libretro' or core[0] == 'fceumm_libretro' or core[0] == 'mesen_libretro':
                extensions = ['fds', 'nes', 'unif', 'unf']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)

                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)

        return ext_files

class Platform_Gameboy(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    fullscreens = ['false']
    cores = ['gambatte_libretro', 'mess2016_libretro', 'mess_libretro', 'mgba_libretro', 'tgbdual_libretro']
    streaming = ['false']
    extensions = ['zip', 'gb', 'dmg', 'bin', 'u1', 'ndd', 'zip']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        fullscreen = ['false']
        core = ['mesen-s_libretro']
        streaming = ['false']
        extensions = ['zip', 'gb', 'dmg', 'bin', 'u1', 'ndd']
        
        if emulator == 'retroarch':
            #gb/c
            if core == 'emux_gb_libretro':
                extensions = ['gb', 'bin', 'rom']
            if core == 'gambatte_libretro':
                extensions = ['gb', 'gbc', 'dmg']
            if core == 'gearhub_libretro':
                extensions = ['gb', 'dmg', 'gbc', 'cgb', 'sgb']
            if core == 'sameboy_libretro':
                extensions = ['gb', 'gbc']
            if core == 'tgbdual_libretro':
                extensions = ['cgb', 'dmg', 'gb', 'gbc', 'sgb']                                                                
            #gba
            if core == 'mgba_libretro':
                extensions = ['gb', 'gbc', 'gba']
            if core == 'tempgba_libretro':
                extensions = ['gba', 'bin', 'agb', 'gbz']
            if core == 'mednafen_gba_libretro':
                extensions = ['gba', 'agb', 'bin']
            #snes
            if core == 'higan_sfc_libretro' or core == 'higan_sfc balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom']
            if core == 'mesen-s_libretro':
                extensions = ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc']

        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['gameboy']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            #gb/c
            if core[0] == 'emux_gb_libretro':
                extensions = ['gb', 'bin', 'rom']
            if core[0] == 'gambatte_libretro':
                extensions = ['gb', 'gbc', 'dmg']
            if core[0] == 'gearhub_libretro':
                extensions = ['gb', 'dmg', 'gbc', 'cgb', 'sgb']
            if core[0] == 'sameboy_libretro':
                extensions = ['gb', 'gbc']
            if core[0] == 'tgbdual_libretro':
                extensions = ['cgb', 'dmg', 'gb', 'gbc', 'sgb']                                                                
            #gba
            if core[0] == 'mgba_libretro':
                extensions = ['gb', 'gbc', 'gba']
            if core[0] == 'tempgba_libretro':
                extensions = ['gba', 'bin', 'agb', 'gbz']
            if core[0] == 'mednafen_gba_libretro':
                extensions = ['gba', 'agb', 'bin']
            #snes
            if core[0] == 'higan_sfc_libretro' or core[0] == 'higan_sfc balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom']
            if core[0] == 'mesen-s_libretro':
                extensions = ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc']
                            
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
            
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)

        return ext_files

class Platform_GameboyColor(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.    
    emulators = ['retroarch']
    cores = ['gambatte_libretro', 'mgba_libretro', 'tgbdual_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'gbc', 'dmg', 'bin', 'u1', 'ndd']

    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['mesen-s_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'gbc', 'dmg', 'bin', 'u1', 'ndd']

        if emulator == 'retroarch':
            #gb/c
            if core == 'emux_gb_libretro':
                extensions = ['gb', 'bin', 'rom']
            if core == 'gambatte_libretro':
                extensions = ['gb', 'gbc', 'dmg']
            if core == 'gearhub_libretro':
                extensions = ['gb', 'dmg', 'gbc', 'cgb', 'sgb']
            if core == 'sameboy_libretro':
                extensions = ['gb', 'gbc']
            if core == 'tgbdual_libretro':
                extensions = ['cgb', 'dmg', 'gb', 'gbc', 'sgb']                                                                
            #gba
            if core == 'mgba_libretro':
                extensions = ['gb', 'gbc', 'gba']
            if core == 'tempgba_libretro':
                extensions = ['gba', 'bin', 'agb', 'gbz']
            if core == 'mednafen_gba_libretro':
                extensions = ['gba', 'agb', 'bin']
            #snes
            if core == 'higan_sfc_libretro' or core == 'higan_sfc balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom']
            if core == 'mesen-s_libretro':
                extensions = ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc']
        
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]
                
        self.run_process(emulator)

    def supported_platforms(self):
        return ['gameboy', 'gameboycolor']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            #gb/c
            if core[0] == 'emux_gb_libretro':
                extensions = ['gb', 'bin', 'rom']
            if core[0] == 'gambatte_libretro':
                extensions = ['gb', 'gbc', 'dmg']
            if core[0] == 'gearhub_libretro':
                extensions = ['gb', 'dmg', 'gbc', 'cgb', 'sgb']
            if core[0] == 'sameboy_libretro':
                extensions = ['gb', 'gbc']
            if core[0] == 'tgbdual_libretro':
                extensions = ['cgb', 'dmg', 'gb', 'gbc', 'sgb']                                                                
            #gba
            if core[0] == 'mgba_libretro':
                extensions = ['gb', 'gbc', 'gba']
            if core[0] == 'tempgba_libretro':
                extensions = ['gba', 'bin', 'agb', 'gbz']
            if core[0] == 'mednafen_gba_libretro':
                extensions = ['gba', 'agb', 'bin']
            #snes
            if core[0] == 'higan_sfc_libretro' or core[0] == 'higan_sfc balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom']
            if core[0] == 'mesen-s_libretro':
                extensions = ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
        return ext_files

class Platform_GameboyAdvance(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    cores = ['meteor_libretro', 'vba_next_libretro', 'vbam_librertro', 'mgba_libretro', 'gpsp_librertro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'gb', 'gbc', 'gba', 'dmg', 'agb', 'bin', 'cgb', 'sgb']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['vba_next_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'gb', 'gbc', 'gba', 'dmg', 'agb', 'bin', 'cgb', 'sgb']

        if emulator == 'retroarch':
            if core == 'mednafen_gba_libretro':
                extensions = ['gba', 'agb', 'bin']
            if core == 'gpsp_libretro':
                extensions = ['gba', 'bin']
            if core == 'meteor_libretro':
                extensions = ['gba']                
            if core == 'mgba_libretro':
                extensions = ['gb', 'gbc', 'gba']
            if core == 'tempgba_libretro':
                extensions = ['gba', 'bin', 'agb', 'gbz']
            if core == 'vbam_libretro':
                extensions = ['dmg', 'gb', 'gbc', 'cgb', 'sgb', 'gba']            
            if core == 'vba_next_libretro':
                extensions = ['gba']
                
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')

        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]

        self.run_process(emulator)

    def supported_platforms(self):
        return ['gameboyadvance', 'gameboycolor', 'gameboy']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'mednafen_gba_libretro':
                extensions = ['gba', 'agb', 'bin']
            if core[0] == 'gpsp_libretro':
                extensions = ['gba', 'bin']
            if core[0] == 'meteor_libretro':
                extensions = ['gba']                
            if core[0] == 'mgba_libretro':
                extensions = ['gb', 'gbc', 'gba']
            if core[0] == 'tempgba_libretro':
                extensions = ['gba', 'bin', 'agb', 'gbz']
            if core[0] == 'vbam_libretro':
                extensions = ['dmg', 'gb', 'gbc', 'cgb', 'sgb', 'gba']            
            if core[0] == 'vba_next_libretro':
                extensions = ['gba']
                        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
            
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)                
                        
        return ext_files

class Platform_Gamecube(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    cores = ['dolphin_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.        
        emulator = ['retroarch']
        core = ['dolphin_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
        
        if emulator == 'retroarch':
            if core == 'dolphin_libretro':
                extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']

        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')
                
        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]

        self.run_process(emulator)

    def supported_platforms(self):
        return ['gamecube']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'dolphin_libretro':
                extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
            
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
            
        return ext_files

class Platform_Pokemini(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    cores = ['pokemini_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'min']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['pokemini_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'min']
        
        if emulator == 'retroarch':
            if core == 'pokemini_libretro':
                extensions = ['min']

        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]

        self.run_process(emulator)

    def supported_platforms(self):
        return ['pokemini']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'pokemini_libretro':
                extensions = ['min']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
            
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
        return ext_files

class Platform_SuperFamicom(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    cores = ['snes9x_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'sfc', 'smc', 'fig', 'swc', 'bs']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['snes9x_libretro']        
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'sfc', 'smc', 'fig', 'swc', 'bs']
        
        if emulator == 'retroarch':
            if core == 'bsnes_libretro' or core == 'bsnes_hd_beta_libretro' or core == 'bsnes_cplusplus98_libretro' or core == 'bsnes2014_accuracy_libretro' or core == 'bsnes2014_balanced_libretro' or core == 'bsnes2014_performance_libretro' or core == 'bsnes_mercury_accuracy_libretro' or core == 'bsnes_mercury_balanced_libretro' or core == 'bsnes_mercury_balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bs']
            if core == 'higan_sfc_libretro' or core == 'higan_sfc balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom']
            if core == 'mesen-s_libretro':
                extensions = ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc']
            if core == 'snes9x_libretro' or core == 'snes9x2002_libretro' or core == 'snes9x2005_libretro' or core == 'snes9x2005_plus_libretro' or core == 'snes9x2010_libretro':
                extensions = ['smc', 'sfc', 'swc', 'fig', 'bs', 'st']

        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]

        self.run_process(emulator)

    def supported_platforms(self):
        return ['snessuperfamicom']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'bsnes_libretro' or core[0] == 'bsnes_hd_beta_libretro' or core[0] == 'bsnes_cplusplus98_libretro' or core[0] == 'bsnes2014_accuracy_libretro' or core[0] == 'bsnes2014_balanced_libretro' or core[0] == 'bsnes2014_performance_libretro' or core[0] == 'bsnes_mercury_accuracy_libretro' or core[0] == 'bsnes_mercury_balanced_libretro' or core[0] == 'bsnes_mercury_balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bs']
            if core[0] == 'higan_sfc_libretro' or core[0] == 'higan_sfc balanced_libretro':
                extensions = ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom']
            if core[0] == 'mesen-s_libretro':
                extensions = ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc']
            if core[0] == 'snes9x_libretro' or core[0] == 'snes9x2002_libretro' or core[0] == 'snes9x2005_libretro' or core[0] == 'snes9x2005_plus_libretro' or core[0] == 'snes9x2010_libretro':
                extensions = ['smc', 'sfc', 'swc', 'fig', 'bs', 'st']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
        return ext_files

class Platform_Virtualboy(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    cores = ['mednafen_vb_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['zip', 'vb', 'vboy', 'bin']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['mednafen_vb_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['zip', 'vb', 'vboy', 'bin']
        
        if emulator == 'retroarch':
            if core == 'mednafen_vb_libretro':
                extensions = ['vb', 'vboy', 'bin']
                
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            # Set wether we should run in fullscreens or not.
            if fullscreen == 'true':
                emulator.append('--fullscreen')

        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')

        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]

        self.run_process(emulator)

    def supported_platforms(self):
        return ['virtualboy']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'mednafen_vb_libretro':
                extensions = ['vb', 'vboy', 'bin']
                        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
        
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
        return ext_files

class Platform_Wii(PlatformCommon):
    # Set up the emulator we want to run.
    # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
    # Set wether we should run in fullscreens or not.        
    # Supply A list of extensions that the specified emulator supports.
    emulators = ['retroarch']
    cores = ['dolphin_libretro']
    fullscreens = ['false']
    streaming = ['false']
    recording = ['true']
    extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
    
    def run(self):
        # Set up the emulator we want to run.
        # in case we are running retroarch, we need to set the libretro core (fullpath or shortname).
        # Set wether we should run in fullscreens or not.        
        # Supply A list of extensions that the specified emulator supports.
        emulator = ['retroarch']
        core = ['dolphin_libretro']
        fullscreen = ['false']
        streaming = ['false']
        recording = ['true']
        extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
        
        if emulator == 'retroarch':
            if core == 'dolphin_libretro':
                extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
        
        ext = []
        for ext in extensions:
            # Tries to identify files by the list of extensions
            files = self.find_files_with_extension(ext)
        if len(files) == 0:
            # Tries to identify files by the list of extensions in UPPERCASE
            files = self.find_files_with_extension(ext.upper())
        if len(files) == 0:
            # Tries to identify files by any magic necessary    
            files = self.find_ext_files(emulator,core)
        if len(files) == 0:
            print("Didn't find any runnable files.")
            exit(-1)

        # in case we are running retroarch, we need to provide some arguments to set the libretro core (fullpath or shortname).
        if emulator[0] == 'retroarch':
            emulator.append('-L')
            emulator.append(core[0])
            
            # Set wether we should start streaming or not.
            if streaming == ['true']:
                print("\tStreaming enabled!")
                recording = 'true'
                emulator.append('--record rtmp://live.twitch.tv/app/$YOUR_TWITCH_ID')
            
            if recording == ['true']:
                print("\tRecording enabled!")
                emulator.append('--recordconfig twitch.cfg')
                
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                print("\tFullscreen enabled!")
                emulator.append('--fullscreen')


        # in case we are not running retroarch, and we need to provide some arguments to the emulator we can do so here:
        if emulator[0] == '4do':
            # Set wether we should run in fullscreens or not.
            if fullscreen == ['true']:
                emulator.append('--fullscreen')
                
        # print status to console.
        print("\tUsing: " + str(emulator[0]))
        print("\tUsing core: " + str(core[0]))
        print("\tUsing fullscreen: " + str(fullscreen[0]))
        print("\tUsing streaming: " + str(streaming[0]))

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
            
            if emulator[0] == 'retroarch':
                emulator = emulator + [files[0]]
            if emulator[0] == '3do':
                emulator = emulator + ['-flipname', flipfile, files[0]]

        self.run_process(emulator)

    def supported_platforms(self):
        return ['wii', 'wiiu', 'nintendowii']

    # Tries to identify files by any magic necessary
    def find_ext_files(self,emulator,core):

        if emulator[0] == 'retroarch':
            if core[0] == 'dolphin_libretro':
                extensions = ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u']
        
        ext_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size > 0:
        
                # Tries to exclude files that end with certain extensions/we dont need.. Grrgrrgll.
                ext = []
                for ext in extensions:
            
                    if file.endswith(ext):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
                    if file.endswith(ext.upper()):
                        ext_files.append(file)
                        print("\tFound file: " + file)
                        
        return ext_files
