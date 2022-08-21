from platformcommon import PlatformCommon
import os


class PlatformAmiga(PlatformCommon):
    def run(self):
        adfs = self.find_files_with_extension('adf')
        adzs = self.find_files_with_extension('adz')
        dmss = self.find_files_with_extension('dms')
        fdis = self.find_files_with_extension('fdi')
        ipfs = self.find_files_with_extension('ipf')
        hdfs = self.find_files_with_extension('hdf')
        hdzs = self.find_files_with_extension('hdz')
        lhas = self.find_files_with_extension('lha')
        slaves = self.find_files_with_extension('slave')
        infos = self.find_files_with_extension('info')
        cues = self.find_files_with_extension('cue')
        ccds = self.find_files_with_extension('ccd')
        nrgs = self.find_files_with_extension('nrg')
        mdss = self.find_files_with_extension('mds')
        isos = self.find_files_with_extension('iso')
        chds = self.find_files_with_extension('chd')
        uaes = self.find_files_with_extension('uae')
        m3us = self.find_files_with_extension('m3u')
        zips = self.find_files_with_extension('zip')
        zs = self.find_files_with_extension('7z')
        rp9s = self.find_files_with_extension('rp9')
        exes = self.find_files_with_extension('exe')

        if len(exes) == 0:
            exes = self.find_magic_cookies()
        if len(adfs) == 0:
            adfs = self.find_adf_files()
        # if len(adzs) == 0:
        #     adzs = self.find_adz_files()
        # if len(dmss) == 0:
        #     dmss = self.find_dms_files()
        # if len(fdis) == 0:
        #     fdis = self.find_fdi_files()
        # if len(ipfs) == 0:
        #     ipfs = self.find_ipf_files()
        # if len(hdfs) == 0:
        #     hdfs = self.find_hdf_files()
        # if len(hdzs) == 0:
        #     hdzs = self.find_hdz_files()
        # if len(lhas) == 0:
        #     lhas = self.find_lha_files()
        # if len(slaves) == 0:
        #     slaves = self.find_slave_files()
        # if len(infos) == 0:
        #     infos = self.find_info_files()
        # if len(cues) == 0:
        #     cues = self.find_cue_files()
        # if len(ccds) == 0:
        #     ccds = self.find_ccd_files()
        # if len(nrgs) == 0:
        #     nrgs = self.find_nrg_files()
        # if len(mdss) == 0:
        #     mdss = self.find_mds_files()
        # if len(isos) == 0:
        #     isos = self.find_iso_files()
        # if len(chds) == 0:
        #     chds = self.find_chd_files()
        # if len(uaes) == 0:
        #     uaes = self.find_uae_files()
        # if len(m3us) == 0:
        #     m3us = self.find_m3u_files()
        # if len(zips) == 0:
        #     zips = self.find_zip_files()
        # if len(zs) == 0:
        #     zs = self.find_7z_files()
        # if len(rp9s) == 0:
        #     rp9s = self.find_rp9_files()
        if len(adfs) == 0 and len(adzs) == 0 and len(dmss) == 0 and len(fdis) == 0 and len(ipfs) == 0 and len(hdfs) == 0 and len(hdzs) == 0 and len(lhas) == 0 and len(slaves) == 0 and len(infos) == 0 and len(cues) == 0 and len(ccds) == 0 and len(nrgs) == 0 and len(mdss) == 0 and len(isos) == 0 and len(chds) == 0 and len(uaes) == 0 and len(m3us) == 0 and len(zips) == 0 and len(zs) == 0 and len(rp9s) == 0:
            print("Didn't find any runable files.")
            exit(-1)

        #emulator = ['fs-uae', '--fullscreen', '--keep_aspect']
        emulator = ['retroarch']
        emulator.append('-L')
        emulator.append('puae_libretro')
        # emulator.append('--fullscreen')

        drives = []
        # Support only one for now..
        if len(exes) > 0:
            emulator = ['fs-uae']
            if emulator[0] == 'fs-uae':
                emulator.append('--hard_drive_0=.')
            if emulator[0] == 'retroarch':
                # emulator.append('--hard_drive_0=.')
                emulator = emulator + [exes[0]]

            if not os.path.exists(self.datadir + "/s"):
                os.makedirs(self.datadir + "/s")
# TODO: when find_files_with_extension works with paths relative to datadir, we can simplify this
                with open(self.datadir + "/s/startup-sequence", 'w') as f:
                    exename = exes[0].split('/')
                    exename = exename[len(exename)-1]
                    f.write(exename + "\n")
                    f.close()
        if len(dmss) > 0:
            drives = self.sort_disks(dmss)
            emulator = emulator + [dmss[0]]
        if len(adfs) > 0:
            drives = self.sort_disks(adfs)
            emulator = emulator + [adfs[0]]
        if len(adzs) > 0:
            drives = self.sort_disks(adzs)
            emulator = emulator + [adzs[0]]
        if len(fdis) > 0:
            drives = self.sort_disks(fdis)
            emulator = emulator + [fdis[0]]
        if len(ipfs) > 0:
            drives = self.sort_disks(ipfs)
            emulator = emulator + [ipfs[0]]
        if len(hdfs) > 0:
            drives = self.sort_disks(hdfs)
            emulator = emulator + [hdfs[0]]
        if len(hdzs) > 0:
            drives = self.sort_disks(hdzs)
            emulator = emulator + [hdzs[0]]

        if emulator[0] == 'fs-uae':
            amiga_model = 'A1200'
            if self.prod_platform == 'amigaocsecs':
                amiga_model = 'A500'

            if self.prod_platform == 'amigaaga':
                emulator.append('--fast_memory=8192')
    # --chip_memory=2048
            if len(drives) > 0:
                emulator.append('--floppy_drive_0=' + drives[0])
            if len(drives) > 1:
                emulator.append('--floppy_drive_1=' + drives[1])
            if len(drives) > 2:
                emulator.append('--floppy_drive_2=' + drives[2])
            if len(drives) > 3:
                emulator.append('--floppy_drive_3=' + drives[3])

            emulator.append('--model=' + amiga_model)
        if emulator[0] == 'retroarch':
            amiga_model = 'A1200'

            if self.prod_platform == 'amigaocsecs':
                amiga_model = 'A500'

    # --chip_memory=2048

            if len(drives) > 0:
                emulator.append('drives[0]')
            if len(drives) > 1:
                emulator.append('drives[1]')
            if len(drives) > 2:
                emulator.append('drives[2]')
            if len(drives) > 3:
                emulator.append('drives[3]')

        self.run_process(emulator)

    def supported_platforms(self):
        return ['amigaocsecs', 'amigaaga']

# Search demo files for amiga magic cookie (executable file)
    def find_magic_cookies(self):
        cookie_files = []
        for file in self.prod_files:
            with open(file, "rb") as fin:
                header = fin.read(4)
                if len(header) == 4:
                    # Signature for Amiga magic cookie
                    if header[0] == 0 and header[1] == 0 and header[2] == 3 and header[3] == 243:
                        cookie_files.append(file)
        return cookie_files

# Tries to identify adf files by any magic necessary
    def find_adf_files(self):
        adf_files = []
        for file in self.prod_files:
            size = os.path.getsize(file)
            if size == 174848:  # All adf:s seem to be this size..
                adf_files.append(file)
        return adf_files
