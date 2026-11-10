#!/usr/bin/env python3
"""data/ の CSV を data.js にまとめる（DESIGN.md ADR-6）。

画面は data.js を読む。ファイルを直接開いたページからは CSV を読めない（ブラウザが手元のファイルの読み込みを許さない）ため、
CSV の字をそのまま JavaScript の文字列として data.js に入れる。CSV の中身は変えない。

使い方：python3 tools/build_data.py        （data.js を書き出す）
        python3 tools/build_data.py --check（data.js が CSV と合っているかだけを確かめる。違えば終了コード 1）
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAMES = ['summary', 'monthly', 'age', 'hourly', 'weekday', 'booking_timing', 'booking_method', 'stops', 'district', 'area']
OUT = ROOT / 'data.js'


def build():
    csv = {}
    for n in NAMES:
        p = ROOT / 'data' / (n + '.csv')
        t = p.read_text(encoding='utf-8')
        if t.startswith('﻿'):
            t = t[1:]
        if not t.strip():
            sys.exit(f'止めた：{p.name} が空')
        csv[n] = t
    body = json.dumps(csv, ensure_ascii=False, indent=0, sort_keys=False).replace('</', '<\\/')
    return '/* data/*.csv から tools/build_data.py で生成。直接編集しない（DESIGN.md ADR-6）。 */\nconst CSV = ' + body + ';\n'


def main():
    s = build()
    if '--check' in sys.argv:
        old = OUT.read_text(encoding='utf-8') if OUT.exists() else ''
        if old != s:
            print('data.js が data/ の CSV と合っていない。python3 tools/build_data.py で作り直す')
            sys.exit(1)
        print('data.js は data/ の CSV と合っている（' + str(len(NAMES)) + ' 本）')
        return
    OUT.write_text(s, encoding='utf-8')
    print('data.js を書き出した（' + str(len(NAMES)) + ' 本、' + str(len(s.encode('utf-8'))) + ' バイト）')


if __name__ == '__main__':
    main()
