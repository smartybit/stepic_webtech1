CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    # 'python': '/usr/bin/python',
    'args': (
         '--bind=0.0.0.0:8000',
        '--workers=2',
        '--max-requests=1',
        '--timeout=60',
        'ask.wsgi',
    ),
}
#bind = "0.0.0.0:8000"
#chdir = '/home/box/web/ask/ask'
