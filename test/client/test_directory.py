import copy

import pytest

from pynyaasi.client.directory import Directory, File


@pytest.mark.unittest
class TestClientDirectory:
    def test_simple(self, simple_dir, complex_dir, text_aligner):
        assert simple_dir == simple_dir
        assert simple_dir == copy.deepcopy(simple_dir)
        assert simple_dir != complex_dir
        assert simple_dir != 1
        assert simple_dir != None

        assert complex_dir == complex_dir
        assert complex_dir == copy.deepcopy(complex_dir)
        assert complex_dir != simple_dir

        assert hash(simple_dir) == hash(copy.deepcopy(simple_dir))
        assert hash(simple_dir) != hash(complex_dir)

        text_aligner.assert_equal(
            str(simple_dir),
            """
[AI-Raws][Fire Force] [folder, 20.6 GiB]
├── [AI-Raws] 炎炎の消防隊 #01 (BD HEVC 1920x1080 yuv444p10le FLAC)[00359E87].mkv [file, 1.1 GiB]
├── [AI-Raws] 炎炎の消防隊 #02 (BD HEVC 1920x1080 yuv444p10le FLAC)[DAC5E163].mkv [file, 807.8 MiB]
├── [AI-Raws] 炎炎の消防隊 #03 (BD HEVC 1920x1080 yuv444p10le FLAC)[ED84DE60].mkv [file, 1.1 GiB]
├── [AI-Raws] 炎炎の消防隊 #04 (BD HEVC 1920x1080 yuv444p10le FLAC)[4D006A6F].mkv [file, 935.0 MiB]
├── [AI-Raws] 炎炎の消防隊 #05 (BD HEVC 1920x1080 yuv444p10le FLAC)[25ACB9BA].mkv [file, 789.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #06 (BD HEVC 1920x1080 yuv444p10le FLAC)[ABE87DE7].mkv [file, 1.1 GiB]
├── [AI-Raws] 炎炎の消防隊 #07 (BD HEVC 1920x1080 yuv444p10le FLAC)[BD4F5594].mkv [file, 956.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #08 (BD HEVC 1920x1080 yuv444p10le FLAC)[62C1CD6B].mkv [file, 828.8 MiB]
├── [AI-Raws] 炎炎の消防隊 #09 (BD HEVC 1920x1080 yuv444p10le FLAC)[917EA0CE].mkv [file, 922.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #10 (BD HEVC 1920x1080 yuv444p10le FLAC)[B310DA52].mkv [file, 656.0 MiB]
├── [AI-Raws] 炎炎の消防隊 #11 (BD HEVC 1920x1080 yuv444p10le FLAC)[7DB51188].mkv [file, 671.2 MiB]
├── [AI-Raws] 炎炎の消防隊 #12 (BD HEVC 1920x1080 yuv444p10le FLAC)[5B313F70].mkv [file, 718.8 MiB]
├── [AI-Raws] 炎炎の消防隊 #13 (BD HEVC 1920x1080 yuv444p10le FLAC)[B0A57086].mkv [file, 737.4 MiB]
├── [AI-Raws] 炎炎の消防隊 #14 (BD HEVC 1920x1080 yuv444p10le FLAC)[205D3328].mkv [file, 1017.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #15 (BD HEVC 1920x1080 yuv444p10le FLAC)[F938397F].mkv [file, 874.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #16 (BD HEVC 1920x1080 yuv444p10le FLAC)[635E0F84].mkv [file, 845.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #17 (BD HEVC 1920x1080 yuv444p10le FLAC)[62A10712].mkv [file, 828.2 MiB]
├── [AI-Raws] 炎炎の消防隊 #18 (BD HEVC 1920x1080 yuv444p10le FLAC)[9EE1364F].mkv [file, 832.4 MiB]
├── [AI-Raws] 炎炎の消防隊 #19 (BD HEVC 1920x1080 yuv444p10le FLAC)[30EB7A35].mkv [file, 852.6 MiB]
├── [AI-Raws] 炎炎の消防隊 #20 (BD HEVC 1920x1080 yuv444p10le FLAC)[075B7425].mkv [file, 838.2 MiB]
├── [AI-Raws] 炎炎の消防隊 #21 (BD HEVC 1920x1080 yuv444p10le FLAC)[A92DBA56].mkv [file, 748.0 MiB]
├── [AI-Raws] 炎炎の消防隊 #22 (BD HEVC 1920x1080 yuv444p10le FLAC)[43A840DC].mkv [file, 820.5 MiB]
├── [AI-Raws] 炎炎の消防隊 #23 (BD HEVC 1920x1080 yuv444p10le FLAC)[4185E25F].mkv [file, 829.0 MiB]
├── [AI-Raws] 炎炎の消防隊 #24 (BD HEVC 1920x1080 yuv444p10le FLAC)[2B28C1FE].mkv [file, 851.3 MiB]
├── [AI-Raws] 炎炎の消防隊 ノンクレジットED (BD HEVC 1920x1080 yuv444p10le FLAC)[797400C4].mkv [file, 102.5 MiB]
├── [AI-Raws] 炎炎の消防隊 ノンクレジットED2 (BD HEVC 1920x1080 yuv444p10le FLAC)[40B0883F].mkv [file, 58.6 MiB]
├── [AI-Raws] 炎炎の消防隊 ノンクレジットOP (BD HEVC 1920x1080 yuv444p10le FLAC)[1B2232B5].mkv [file, 113.4 MiB]
└── [AI-Raws] 炎炎の消防隊 ノンクレジットOP2 (BD HEVC 1920x1080 yuv444p10le FLAC)[B452057F].mkv [file, 78.5 MiB]
            """
        )

        assert simple_dir.is_folder
        assert isinstance(simple_dir, Directory)
        assert len(simple_dir) == 28

        assert not simple_dir[0].is_folder
        assert isinstance(simple_dir[0], File)
        assert repr(simple_dir[0]) == \
               '<File [AI-Raws] 炎炎の消防隊 #01 (BD HEVC 1920x1080 yuv444p10le FLAC)[00359E87].mkv [file, 1.1 GiB]>'

        assert '1.0 GiB' < simple_dir[0].size < '1.2 GiB'
        assert '20 GiB' < simple_dir.size < '21 GiB'
