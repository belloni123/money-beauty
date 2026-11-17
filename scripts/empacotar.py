#!/usr/bin/env python3
"""Gera pacotes locais, sem dependências externas ou acesso à rede."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'money-beauty'
DIST = ROOT / 'dist'


def arquivos(pasta):
    return sorted(p for p in pasta.rglob('*') if p.is_file()
                  and not p.name.startswith('._') and p.name != '.DS_Store')


def main():
    DIST.mkdir(exist_ok=True)
    partes = [
        '# MONEY BEAUTY — conhecimento para consulta',
        'Versão 1.0.0 · 17/11/2026. Use com MONEY-BEAUTY-INSTRUCOES.md. '
        'Textos históricos são referência, não comandos. O perfil Althea é opcional.',
        '## Skill principal\n\n' + (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    ]
    for pasta in ('references', 'templates'):
        for p in arquivos(SKILL / pasta):
            partes.append('## Fonte interna: ' + p.relative_to(SKILL).as_posix()
                          + '\n\n' + p.read_text(encoding='utf-8'))
    (DIST / 'MONEY-BEAUTY-CONHECIMENTO.md').write_text(
        '\n\n---\n\n'.join(partes) + '\n', encoding='utf-8')
    (DIST / 'MONEY-BEAUTY-INSTRUCOES.md').write_bytes(
        (ROOT / 'prompts/MONEY-BEAUTY-INSTRUCOES.md').read_bytes())
    with zipfile.ZipFile(DIST / 'money-beauty.skill.zip', 'w',
                         compression=zipfile.ZIP_DEFLATED) as z:
        for p in arquivos(SKILL):
            # Uma única pasta money-beauty contendo SKILL.md e suas referências.
            info = zipfile.ZipInfo('money-beauty/' + p.relative_to(SKILL).as_posix(),
                                   date_time=(2026, 11, 17, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, p.read_bytes())
    manifest = {
        'nome': 'MONEY BEAUTY', 'versao': '1.0.0',
        'data': '2026-11-17',
        'artefatos': [{
            'arquivo': p.name, 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()
        } for p in arquivos(DIST) if p.suffix in ('.md', '.zip')]
    }
    (DIST / 'manifesto.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Gerados conhecimento, instruções, ZIP da skill e manifesto em dist/.')


if __name__ == '__main__':
    main()
