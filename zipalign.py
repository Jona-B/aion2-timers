#!/usr/bin/env python3
"""Minimal zipalign: rewrites an APK so every uncompressed entry starts on a 4-byte boundary.

Android 11+ refuses to install apps targeting API 30+ when resources.arsc is not
stored uncompressed and 4-byte aligned. Run this before signing.

Usage: python3 zipalign.py input.apk output.apk
"""
import sys
import zipfile

ALIGN = 4


def align(src, dst):
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, 'w') as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            out = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            out.compress_type = info.compress_type
            out.external_attr = info.external_attr
            out.create_system = info.create_system
            extra = b''
            if info.compress_type == zipfile.ZIP_STORED:
                header_offset = zout.fp.tell()
                data_offset = header_offset + 30 + len(info.filename.encode('utf-8'))
                extra = b'\0' * ((ALIGN - data_offset % ALIGN) % ALIGN)
            out.extra = extra
            zout.writestr(out, data)


def check(path):
    bad = []
    with zipfile.ZipFile(path) as z, open(path, 'rb') as f:
        for info in z.infolist():
            if info.compress_type != zipfile.ZIP_STORED:
                continue
            f.seek(info.header_offset)
            h = f.read(30)
            off = info.header_offset + 30 + int.from_bytes(h[26:28], 'little') + int.from_bytes(h[28:30], 'little')
            if off % ALIGN:
                bad.append((info.filename, off))
    return bad


if __name__ == '__main__':
    align(sys.argv[1], sys.argv[2])
    bad = check(sys.argv[2])
    if bad:
        sys.exit('zipalign failed: %r' % bad)
    print('aligned:', sys.argv[2])
