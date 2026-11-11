"""Package the current handbook using only Python's standard library."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import re
import shutil
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
FILES = ('index.html', 'README.md', '.gitignore', '.nojekyll',
         'package.cmd', 'package_release.py')

def main():
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError('Required release file missing: ' + name)
    data = (ROOT / 'index.html').read_bytes()
    page = data.decode('utf-8')
    if 'Project Y' not in page or 'id="content"' not in page:
        raise ValueError('index.html is not the expected Project Y handbook.')
    version = re.search(r'文档版本[：:]\s*([^<]+)', page)
    stamp = datetime.now().astimezone()
    metadata = {
        'project': 'Project Y Art Handbook',
        'document_version': version.group(1).strip() if version else 'unspecified',
        'packaged_at': stamp.isoformat(timespec='seconds'),
        'entrypoint': 'index.html',
        'sha256': hashlib.sha256(data).hexdigest(),
        'files': [*FILES, 'release.json'],
    }
    meta = json.dumps(metadata, ensure_ascii=False, indent=2) + '\n'
    out = ROOT / 'releases'
    out.mkdir(exist_ok=True)
    target = out / ('ProjectY-Art-Handbook-' + stamp.strftime('%Y%m%d-%H%M%S-%f') + '.zip')
    with ZipFile(target, 'x', compression=ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(ROOT / name, name)
        archive.writestr('release.json', meta.encode('utf-8'))
    with ZipFile(target) as archive:
        assert archive.testzip() is None
        assert archive.read('index.html') == data
        assert set(archive.namelist()) == set(metadata['files'])
    (ROOT / 'release.json').write_text(meta, encoding='utf-8')
    latest = out / 'ProjectY-Art-Handbook-latest.zip'
    shutil.copyfile(target, latest)
    print('Release: ' + str(target))
    print('Latest:  ' + str(latest))
    print('Verified: 7 files; index.html matches the current source exactly.')

if __name__ == '__main__':
    main()
