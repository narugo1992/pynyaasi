import pytest
from hbutils.testing import TextAligner

from pynyaasi.client.directory import Directory, File


@pytest.fixture()
def text_aligner():
    return TextAligner().multiple_lines()


@pytest.fixture()
def simple_dir():
    return Directory('[AI-Raws][Fire Force]', [
        File(
            '[AI-Raws] 炎炎の消防隊 #01 (BD HEVC 1920x1080 yuv444p10le FLAC)[00359E87].mkv',
            '1.1 GiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #02 (BD HEVC 1920x1080 yuv444p10le FLAC)[DAC5E163].mkv',
            '807.8 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #03 (BD HEVC 1920x1080 yuv444p10le FLAC)[ED84DE60].mkv',
            '1.1 GiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #04 (BD HEVC 1920x1080 yuv444p10le FLAC)[4D006A6F].mkv',
            '935.0 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #05 (BD HEVC 1920x1080 yuv444p10le FLAC)[25ACB9BA].mkv',
            '789.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #06 (BD HEVC 1920x1080 yuv444p10le FLAC)[ABE87DE7].mkv',
            '1.1 GiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #07 (BD HEVC 1920x1080 yuv444p10le FLAC)[BD4F5594].mkv',
            '956.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #08 (BD HEVC 1920x1080 yuv444p10le FLAC)[62C1CD6B].mkv',
            '828.8 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #09 (BD HEVC 1920x1080 yuv444p10le FLAC)[917EA0CE].mkv',
            '922.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #10 (BD HEVC 1920x1080 yuv444p10le FLAC)[B310DA52].mkv',
            '656.0 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #11 (BD HEVC 1920x1080 yuv444p10le FLAC)[7DB51188].mkv',
            '671.2 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #12 (BD HEVC 1920x1080 yuv444p10le FLAC)[5B313F70].mkv',
            '718.8 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #13 (BD HEVC 1920x1080 yuv444p10le FLAC)[B0A57086].mkv',
            '737.4 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #14 (BD HEVC 1920x1080 yuv444p10le FLAC)[205D3328].mkv',
            '1017.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #15 (BD HEVC 1920x1080 yuv444p10le FLAC)[F938397F].mkv',
            '874.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #16 (BD HEVC 1920x1080 yuv444p10le FLAC)[635E0F84].mkv',
            '845.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #17 (BD HEVC 1920x1080 yuv444p10le FLAC)[62A10712].mkv',
            '828.2 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #18 (BD HEVC 1920x1080 yuv444p10le FLAC)[9EE1364F].mkv',
            '832.4 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #19 (BD HEVC 1920x1080 yuv444p10le FLAC)[30EB7A35].mkv',
            '852.6 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #20 (BD HEVC 1920x1080 yuv444p10le FLAC)[075B7425].mkv',
            '838.2 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #21 (BD HEVC 1920x1080 yuv444p10le FLAC)[A92DBA56].mkv',
            '748.0 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #22 (BD HEVC 1920x1080 yuv444p10le FLAC)[43A840DC].mkv',
            '820.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #23 (BD HEVC 1920x1080 yuv444p10le FLAC)[4185E25F].mkv',
            '829.0 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 #24 (BD HEVC 1920x1080 yuv444p10le FLAC)[2B28C1FE].mkv',
            '851.3 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 ノンクレジットED (BD HEVC 1920x1080 yuv444p10le FLAC)[797400C4].mkv',
            '102.5 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 ノンクレジットED2 (BD HEVC 1920x1080 yuv444p10le FLAC)[40B0883F].mkv',
            '58.6 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 ノンクレジットOP (BD HEVC 1920x1080 yuv444p10le FLAC)[1B2232B5].mkv',
            '113.4 MiB'),
        File(
            '[AI-Raws] 炎炎の消防隊 ノンクレジットOP2 (BD HEVC 1920x1080 yuv444p10le FLAC)[B452057F].mkv',
            '78.5 MiB')
    ])


@pytest.fixture()
def complex_dir():
    return Directory(
        '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Ma10p_1080p]', [
            Directory('CDs', [
                Directory(
                    '[190130] ｢気ままな天使たち／ハッピー・ハッピー・フレンズ｣／わたてん☆5 (flac+webp)', [
                        Directory('Scans', [
                            File('01.webp', '696.6 KiB'),
                            File('02.webp', '960.0 KiB'),
                            File('03.webp', '803.4 KiB'),
                            File('04.webp', '826.6 KiB'),
                            File('05.webp', '934.0 KiB'),
                            File('06.webp', '899.1 KiB'),
                            File('07.webp', '745.6 KiB'),
                            File('08.webp', '474.3 KiB'),
                            File('09.webp', '663.4 KiB'),
                            File('10.webp', '517.4 KiB'),
                            File('11.webp', '654.6 KiB'),
                            File('12.webp', '1.0 MiB'),
                            File('13.webp', '101.8 KiB'),
                            File('14.webp', '728.0 KiB'),
                            File('15.webp', '468.4 KiB'),
                            File('16.webp', '422.6 KiB'),
                            File('17.webp', '338.0 KiB'),
                            File('18.webp', '607.5 KiB')
                        ]),
                        File('01. 気ままな天使たち.flac', '31.8 MiB'),
                        File('02. ハッピー・ハッピー・フレンズ.flac', '29.8 MiB'),
                        File('03. 気ままな天使たち -Instrumental-.flac', '30.3 MiB'),
                        File('04. ハッピー・ハッピー・フレンズ -Instrumental-.flac', '28.7 MiB'),
                        File('Cover01.jpg', '54.6 KiB'),
                        File('Cover02.jpg', '1.5 MiB'),
                        File('VTZL-152.log', '4.3 KiB')
                    ]),
                Directory(
                    '[190130] ｢気ままな天使たち／ハッピー・ハッピー・フレンズ｣／わたてん☆5 [24bit_48kHz] (flac)',
                    [
                        File('01. 気ままな天使たち.flac', '57.0 MiB'),
                        File('02. ハッピー・ハッピー・フレンズ.flac', '53.4 MiB')
                    ]),
                Directory('[190227] キャラクターソングアルバム ｢~天使のうたごえ~｣ (flac+webp)', [
                    Directory('Scans', [
                        File('01.webp', '604.4 KiB'),
                        File('02.webp', '744.5 KiB'),
                        File('03.webp', '964.1 KiB'),
                        File('04.webp', '1.1 MiB'),
                        File('05.webp', '853.7 KiB'),
                        File('06.webp', '979.3 KiB'),
                        File('07.webp', '700.3 KiB'),
                        File('08.webp', '879.2 KiB'),
                        File('09.webp', '130.8 KiB'),
                        File('10.webp', '172.8 KiB'),
                        File('11.webp', '265.8 KiB'),
                        File('12.webp', '627.7 KiB'),
                        File('13.webp', '502.8 KiB'),
                        File('14.webp', '883.3 KiB')
                    ]),
                    File('01. シュガーコート・ドリーム.flac', '37.3 MiB'),
                    File('02. やっぱりみゃー姉なんばーわん.flac', '31.6 MiB'),
                    File('03. アタシ♡カワイイ♡宣言!!!.flac', '33.4 MiB'),
                    File('04. あかいろリトルリーダー.flac', '31.6 MiB'),
                    File('05. とっておきのことば.flac', '37.3 MiB'),
                    File('06. 私に 好き が舞い降りた.flac', '33.1 MiB'),
                    File('07. シュガーコート・ドリーム-Instrumental-.flac', '36.8 MiB'),
                    File('08. やっぱりみゃー姉なんばーわん-Instrumental-.flac', '30.9 MiB'),
                    File('09. アタシ♡カワイイ♡宣言!!!-Instrumental-.flac', '32.3 MiB'),
                    File('10. あかいろリトルリーダー-Instrumental-.flac', '31.3 MiB'),
                    File('11. とっておきのことば-Instrumental-.flac', '36.4 MiB'),
                    File('12. 私に 好き が舞い降りた-Instrumental-.flac', '32.3 MiB'),
                    File('Cover.jpg', '1.4 MiB'),
                    File('VTCL-60483.log', '6.2 KiB')
                ]),
                Directory(
                    '[190227] キャラクターソングアルバム ｢~天使のうたごえ~｣ [24bit_48kHz] (flac)', [
                        File('01. シュガーコート・ドリーム.flac', '65.7 MiB'),
                        File('02. やっぱりみゃー姉なんばーわん.flac', '56.1 MiB'),
                        File('03. アタシ カワイイ 宣言！！！.flac', '59.5 MiB'),
                        File('04. あかいろリトルリーダー.flac', '55.5 MiB'),
                        File('05. とっておきのことば.flac', '66.6 MiB'),
                        File("06. 私に''好き''が舞い降りた.flac", '58.6 MiB'),
                        File('07. シュガーコート・ドリーム -Instrumental-.flac', '65.2 MiB'),
                        File('08. やっぱりみゃー姉なんばーわん -Instrumental-.flac', '55.2 MiB'),
                        File('09. アタシ カワイイ 宣言！！！ -Instrumental-.flac', '57.9 MiB'),
                        File('10. あかいろリトルリーダー -Instrumental-.flac', '55.2 MiB'),
                        File('11. とっておきのことば -Instrumental-.flac', '65.7 MiB'),
                        File("12. 私に''好き''が舞い降りた -Instrumental-.flac", '57.8 MiB')
                    ]),
                Directory('[190327] SPCD 01 キャラクターイメージソング／わたてん☆5 (flac)', [
                    File('01. 晴れルヤ.flac', '37.4 MiB'),
                    File('02. 晴れルヤ -Instrumental-.flac', '35.7 MiB'),
                    File('TGCS-11162.log', '3.5 KiB')
                ]),
                Directory('[190403] サウンドコレクション／伊賀拓郎 (flac+webp)', [
                    Directory('Scans', [
                        File('01.webp', '1.1 MiB'),
                        File('02.webp', '767.5 KiB'),
                        File('03.webp', '706.0 KiB'),
                        File('04.webp', '630.7 KiB'),
                        File('05.webp', '761.9 KiB'),
                        File('06.webp', '645.6 KiB'),
                        File('07.webp', '271.6 KiB'),
                        File('08.webp', '546.2 KiB')
                    ]),
                    File('01. 爽やかなる決意.flac', '11.9 MiB'),
                    File('02. 私に天使が舞い降りた! I.flac', '9.9 MiB'),
                    File('03. 私に天使が舞い降りた！ II.flac', '11.0 MiB'),
                    File('04. みやこエキサイト.flac', '9.5 MiB'),
                    File('05. 幸せな一日.flac', '7.3 MiB'),
                    File('06. もにょっとした気持ち.flac', '8.2 MiB'),
                    File('07. いっくぞー！.flac', '13.5 MiB'),
                    File('08. 応援があれば頑張れる！.flac', '8.0 MiB'),
                    File('09. 苦労して手に入れたお菓子.flac', '7.7 MiB'),
                    File('10. 幸せな時間.flac', '10.7 MiB'),
                    File('11. 小悪魔.flac', '10.6 MiB'),
                    File('12. サイキョーにカワイイ.flac', '9.4 MiB'),
                    File('13. トラブルメーカー.flac', '9.4 MiB'),
                    File('14. 想う気持ち.flac', '8.7 MiB'),
                    File('15. 焦り.flac', '5.5 MiB'),
                    File('16. 友達詐欺.flac', '7.5 MiB'),
                    File('17. どんより.flac', '7.6 MiB'),
                    File('18. ドタバタパニック.flac', '8.2 MiB'),
                    File('19. 勝負 II.flac', '7.7 MiB'),
                    File('20. 夢うつつ.flac', '7.6 MiB'),
                    File('21. 勝負 I.flac', '8.1 MiB'),
                    File('22. 無駄骨徒労で報われず.flac', '6.4 MiB'),
                    File('23. 信頼 I.flac', '7.9 MiB'),
                    File('24. 何でも遊び心.flac', '7.2 MiB'),
                    File('25. 夢は叶えるもの.flac', '9.1 MiB'),
                    File('26. 信頼 II.flac', '9.1 MiB'),
                    File('27. 憧れの人.flac', '10.9 MiB'),
                    File('28. 悲しみ.flac', '6.3 MiB'),
                    File('29. 優しさを感じて.flac', '11.8 MiB'),
                    File('30. 右往左往.flac', '8.1 MiB'),
                    File('31. ホッコリタイム.flac', '8.5 MiB'),
                    File('32. 一段落.flac', '7.6 MiB'),
                    File('33. ナイスアイデア.flac', '7.7 MiB'),
                    File('34. 疲れた….flac', '4.4 MiB'),
                    File('35. 回想.flac', '3.5 MiB'),
                    File('36. なんてこった.flac', '4.1 MiB'),
                    File('37. ご満悦.flac', '6.6 MiB'),
                    File('38. Eye Catch.flac', '418.6 KiB'),
                    File('39. 神殿にて.flac', '5.7 MiB'),
                    File('40. 天使の眼差し Prologue.flac', '6.8 MiB'),
                    File('41. 私を呼ぶ声.flac', '11.3 MiB'),
                    File('42. ようこそ天使の国へ.flac', '8.9 MiB'),
                    File('43. 恋するお菓子屋さん.flac', '6.9 MiB'),
                    File('44. あの子に会いたい.flac', '12.3 MiB'),
                    File('45. 決意.flac', '8.2 MiB'),
                    File('46. 受け継ぐ心.flac', '14.4 MiB'),
                    File('47. 天使の眼差し Epilogue.flac', '6.9 MiB'),
                    File('Cover01.jpg', '1.2 MiB'),
                    File('Cover02.jpg', '278.2 KiB'),
                    File('VTCL-60494.log', '12.1 KiB')
                ]),
                Directory('[190403] サウンドコレクション／伊賀拓郎 [24bit_48kHz] (flac)', [
                    File('01. 爽やかなる決意.flac', '24.2 MiB'),
                    File('02. 私に天使が舞い降りた！ I.flac', '21.5 MiB'),
                    File('03. 私に天使が舞い降りた！ II.flac', '22.8 MiB'),
                    File('04. みやこエキサイト.flac', '19.7 MiB'),
                    File('05. 幸せな一日.flac', '18.8 MiB'),
                    File('06. もにょっとした気持ち.flac', '19.6 MiB'),
                    File('07. いっくぞー！.flac', '26.3 MiB'),
                    File('08. 応援があれば頑張れる！.flac', '19.7 MiB'),
                    File('09. 苦労して手に入れたお菓子.flac', '17.7 MiB'),
                    File('10. 幸せな時間.flac', '22.2 MiB'),
                    File('11. 小悪魔.flac', '22.5 MiB'),
                    File('12. サイキョーにカワイイ.flac', '21.0 MiB'),
                    File('13. トラブルメーカー.flac', '20.0 MiB'),
                    File('14. 想う気持ち.flac', '21.6 MiB'),
                    File('15. 焦り.flac', '14.6 MiB'),
                    File('16. 友達詐欺.flac', '17.7 MiB'),
                    File('17. どんより.flac', '17.4 MiB'),
                    File('18. ドタバタパニック.flac', '16.9 MiB'),
                    File('19. 勝負 II.flac', '16.7 MiB'),
                    File('20. 夢うつつ.flac', '17.9 MiB'),
                    File('21. 勝負 I.flac', '16.9 MiB'),
                    File('22. 無駄骨徒労で報われず.flac', '15.4 MiB'),
                    File('23. 信頼 I.flac', '18.1 MiB'),
                    File('24. 何でも遊び心.flac', '16.9 MiB'),
                    File('25. 夢は叶えるもの.flac', '19.7 MiB'),
                    File('26. 信頼 II.flac', '20.3 MiB'),
                    File('27. 憧れの人.flac', '24.1 MiB'),
                    File('28. 悲しみ.flac', '15.7 MiB'),
                    File('29. 優しさを感じて.flac', '24.1 MiB'),
                    File('30. 右往左往.flac', '17.3 MiB'),
                    File('31. ホッコリタイム.flac', '18.2 MiB'),
                    File('32. 一段落.flac', '18.2 MiB'),
                    File('33. ナイスアイデア.flac', '17.0 MiB'),
                    File('34. 疲れた….flac', '11.3 MiB'),
                    File('35. 回想.flac', '10.4 MiB'),
                    File('36. なんてこった.flac', '10.2 MiB'),
                    File('37. ご満悦.flac', '14.1 MiB'),
                    File('38. Eye Catch.flac', '2.1 MiB'),
                    File('39. 神殿にて.flac', '13.4 MiB'),
                    File('40. 天使の眼差し Prologue.flac', '14.2 MiB'),
                    File('41. 私を呼ぶ声.flac', '24.6 MiB'),
                    File('42. ようこそ天使の国へ.flac', '17.5 MiB'),
                    File('43. 恋するお菓子屋さん.flac', '14.5 MiB'),
                    File('44. あの子に会いたい.flac', '26.3 MiB'),
                    File('45. 決意.flac', '17.6 MiB'),
                    File('46. 受け継ぐ心.flac', '30.1 MiB'),
                    File('47. 天使の眼差し Epilogue.flac', '14.3 MiB')
                ]),
                Directory('[190424] SPCD 02 キャラクターイメージソング／わたてん☆5 (flac)', [
                    File('01. GO！GO！GO！.flac', '29.8 MiB'),
                    File('02. GO！GO！GO！ -Instrumental-.flac', '28.5 MiB'),
                    File('TGCS-11164.log', '3.5 KiB')
                ]),
                Directory('[190524] SPCD 03 ラジオ (flac)', [
                    File('01. Special Radio CD.flac', '388.1 MiB'),
                    File('Cover.jpg', '170.3 KiB'),
                    File('TGCS-11166.log', '3.0 KiB')
                ])
            ]),
            Directory('SPs', [
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [CM01][Ma10p_1080p][x265_flac].mkv',
                    '7.3 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [CM02][Ma10p_1080p][x265_flac].mkv',
                    '13.3 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [CM03][Ma10p_1080p][x265_flac].mkv',
                    '7.1 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [CM04][Ma10p_1080p][x265_flac].mkv',
                    '13.1 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [CM05][Ma10p_1080p][x265_flac].mkv',
                    '6.4 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [CM06][Ma10p_1080p][x265_flac].mkv',
                    '6.4 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [IV][Ma10p_1080p][x265_aac].mkv',
                    '735.1 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Menu01_1][Ma10p_1080p][x265_flac].mkv',
                    '38.0 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Menu01_2][Ma10p_1080p][x265_flac].mkv',
                    '33.0 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Menu02_1][Ma10p_1080p][x265_flac].mkv',
                    '41.0 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Menu02_2][Ma10p_1080p][x265_flac].mkv',
                    '36.2 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Menu03_1][Ma10p_1080p][x265_flac].mkv',
                    '43.8 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Menu03_2][Ma10p_1080p][x265_flac].mkv',
                    '38.1 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [NCED01][Ma10p_1080p][x265_flac].mkv',
                    '132.0 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [NCED02][Ma10p_1080p][x265_flac].mkv',
                    '132.2 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [NCOP01][Ma10p_1080p][x265_flac].mkv',
                    '89.4 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [NCOP02][Ma10p_1080p][x265_flac].mkv',
                    '89.7 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [PV01][Ma10p_1080p][x265_flac].mkv',
                    '26.8 MiB'),
                File(
                    '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [PV02][Ma10p_1080p][x265_flac].mkv',
                    '40.5 MiB')
            ]),
            Directory('Scans', [
                Directory('Vol. 01', [
                    File('01.webp', '1.3 MiB'),
                    File('02.webp', '3.0 MiB'),
                    File('03.webp', '3.6 MiB'),
                    File('04.webp', '394.0 KiB'),
                    File('05.webp', '454.7 KiB'),
                    File('06.webp', '10.4 MiB'),
                    File('07.webp', '755.8 KiB'),
                    File('08.webp', '2.4 MiB'),
                    File('Booklet01.webp', '3.5 MiB'),
                    File('Booklet02.webp', '13.4 MiB'),
                    File('Booklet03.webp', '7.2 MiB'),
                    File('Booklet04.webp', '7.0 MiB'),
                    File('Booklet05.webp', '7.3 MiB'),
                    File('Booklet06.webp', '8.2 MiB'),
                    File('Booklet07.webp', '5.4 MiB'),
                    File('Booklet08.webp', '5.7 MiB'),
                    File('Booklet09.webp', '6.3 MiB'),
                    File('Booklet10.webp', '6.1 MiB'),
                    File('Booklet11.webp', '6.6 MiB'),
                    File('Booklet12.webp', '4.3 MiB'),
                    File('Booklet13.webp', '3.6 MiB'),
                    File('Card01.webp', '5.6 MiB'),
                    File('Card02.webp', '4.5 MiB'),
                    File('Card03.webp', '5.6 MiB'),
                    File('Card04.webp', '4.7 MiB'),
                    File('Card05.webp', '76.7 KiB')
                ]),
                Directory('Vol. 02', [
                    File('01.webp', '754.9 KiB'),
                    File('02.webp', '887.9 KiB'),
                    File('03.webp', '108.7 KiB'),
                    File('04.webp', '122.1 KiB'),
                    File('05.webp', '699.2 KiB'),
                    File('06.webp', '787.5 KiB'),
                    File('07.webp', '100.5 KiB'),
                    File('08.webp', '92.4 KiB'),
                    File('09.webp', '78.7 KiB'),
                    File('10.webp', '2.5 MiB'),
                    File('11.webp', '290.8 KiB'),
                    File('12.webp', '594.0 KiB'),
                    File('Booklet01.webp', '945.3 KiB'),
                    File('Booklet02.webp', '2.6 MiB'),
                    File('Booklet03.webp', '1.5 MiB'),
                    File('Booklet04.webp', '1.6 MiB'),
                    File('Booklet05.webp', '1.6 MiB'),
                    File('Booklet06.webp', '1.6 MiB'),
                    File('Booklet07.webp', '1.2 MiB'),
                    File('Booklet08.webp', '1.4 MiB'),
                    File('Booklet09.webp', '1.5 MiB'),
                    File('Booklet10.webp', '1.5 MiB'),
                    File('Booklet11.webp', '1.4 MiB'),
                    File('Booklet12.webp', '1.1 MiB'),
                    File('Booklet13.webp', '887.9 KiB'),
                    File('Card01.webp', '1.1 MiB'),
                    File('Card02.webp', '1.4 MiB'),
                    File('Card03.webp', '1.4 MiB'),
                    File('Card04.webp', '1.2 MiB'),
                    File('Card05.webp', '22.1 KiB')
                ]),
                Directory('Vol. 03', [
                    File('01.webp', '3.7 MiB'),
                    File('02.webp', '2.9 MiB'),
                    File('03.webp', '335.8 KiB'),
                    File('04.webp', '10.1 MiB'),
                    File('05.webp', '709.5 KiB'),
                    File('06.webp', '1.9 MiB'),
                    File('07.webp', '3.1 MiB'),
                    File('08.webp', '383.3 KiB'),
                    File('09.webp', '192.6 KiB'),
                    File('10.webp', '195.1 KiB'),
                    File('11.webp', '3.5 MiB'),
                    File('12.webp', '2.9 MiB'),
                    File('13.webp', '346.4 KiB'),
                    File('Booklet01.webp', '2.9 MiB'),
                    File('Booklet02.webp', '8.7 MiB'),
                    File('Booklet03.webp', '6.8 MiB'),
                    File('Booklet04.webp', '6.3 MiB'),
                    File('Booklet05.webp', '6.8 MiB'),
                    File('Booklet06.webp', '6.1 MiB'),
                    File('Booklet07.webp', '5.0 MiB'),
                    File('Booklet08.webp', '6.2 MiB'),
                    File('Booklet09.webp', '5.6 MiB'),
                    File('Booklet10.webp', '5.2 MiB'),
                    File('Booklet11.webp', '5.1 MiB'),
                    File('Booklet12.webp', '4.5 MiB'),
                    File('Booklet13.webp', '2.7 MiB'),
                    File('Card01.webp', '4.6 MiB'),
                    File('Card02.webp', '4.7 MiB'),
                    File('Card03.webp', '4.3 MiB'),
                    File('Card04.webp', '4.2 MiB'),
                    File('Card05.webp', '642.5 KiB')
                ])
            ]),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [01][Ma10p_1080p][x265_flac].chs.ass',
                '43.5 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [01][Ma10p_1080p][x265_flac].cht.ass',
                '43.7 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [01][Ma10p_1080p][x265_flac].mkv',
                '600.2 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [02][Ma10p_1080p][x265_flac].chs.ass',
                '40.3 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [02][Ma10p_1080p][x265_flac].cht.ass',
                '40.3 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [02][Ma10p_1080p][x265_flac].mkv',
                '714.6 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [03][Ma10p_1080p][x265_flac].chs.ass',
                '47.7 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [03][Ma10p_1080p][x265_flac].cht.ass',
                '47.6 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [03][Ma10p_1080p][x265_flac].mkv',
                '712.1 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [04][Ma10p_1080p][x265_flac].chs.ass',
                '38.9 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [04][Ma10p_1080p][x265_flac].cht.ass',
                '38.9 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [04][Ma10p_1080p][x265_flac].mkv',
                '718.7 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [05][Ma10p_1080p][x265_flac].chs.ass',
                '37.9 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [05][Ma10p_1080p][x265_flac].cht.ass',
                '37.9 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [05][Ma10p_1080p][x265_flac].mkv',
                '694.0 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [06][Ma10p_1080p][x265_flac].chs.ass',
                '41.4 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [06][Ma10p_1080p][x265_flac].cht.ass',
                '41.4 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [06][Ma10p_1080p][x265_flac].mkv',
                '721.4 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [07][Ma10p_1080p][x265_flac].chs.ass',
                '40.7 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [07][Ma10p_1080p][x265_flac].cht.ass',
                '40.7 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [07][Ma10p_1080p][x265_flac].mkv',
                '641.0 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [08][Ma10p_1080p][x265_flac].chs.ass',
                '38.6 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [08][Ma10p_1080p][x265_flac].cht.ass',
                '38.7 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [08][Ma10p_1080p][x265_flac].mkv',
                '772.3 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [09][Ma10p_1080p][x265_flac].chs.ass',
                '39.0 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [09][Ma10p_1080p][x265_flac].cht.ass',
                '39.0 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [09][Ma10p_1080p][x265_flac].mkv',
                '664.9 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [10][Ma10p_1080p][x265_flac].chs.ass',
                '39.2 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [10][Ma10p_1080p][x265_flac].cht.ass',
                '39.2 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [10][Ma10p_1080p][x265_flac].mkv',
                '709.6 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [11][Ma10p_1080p][x265_flac].chs.ass',
                '42.4 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [11][Ma10p_1080p][x265_flac].cht.ass',
                '42.4 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [11][Ma10p_1080p][x265_flac].mkv',
                '592.5 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [12][Ma10p_1080p][x265_flac].chs.ass',
                '46.6 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [12][Ma10p_1080p][x265_flac].cht.ass',
                '46.6 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [12][Ma10p_1080p][x265_flac].mkv',
                '648.8 MiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [13(OVA)][Ma10p_1080p][x265_flac].chs.ass',
                '30.2 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [13(OVA)][Ma10p_1080p][x265_flac].cht.ass',
                '30.2 KiB'),
            File(
                '[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [13(OVA)][Ma10p_1080p][x265_flac].mkv',
                '735.5 MiB'),
            File('[Airota&VCB-Studio] Watashi ni Tenshi ga Maiorita! [Fonts].rar',
                 '44.1 MiB'),
            File('readme about WebP.txt', '1.2 KiB')
        ])
