"""Makes the link-preview images (1200x630) that LinkedIn, iMessage, Slack and others show for each page.
Writes assets/img/og/site.jpg and assets/img/og/<project>.jpg. Needs Google Chrome.
Run: python3 tools/make_og.py"""
import base64, subprocess, tempfile
from pathlib import Path

R = Path(__file__).resolve().parent.parent
OUT = R / 'assets' / 'img' / 'og'
OUT.mkdir(parents=True, exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
A = R / 'assets'

BASE = '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0}
html,body{width:1200px;height:630px;overflow:hidden}
body{background:#03070f;color:#f4f7fc;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display",system-ui,sans-serif;-webkit-font-smoothing:antialiased;position:relative}
.glow{position:absolute;inset:0;background:radial-gradient(ellipse 60% 75% at 78% 55%,COLOR55,transparent 70%),radial-gradient(ellipse 50% 60% at 10% 110%,rgba(29,95,214,.35),transparent 70%)}
.sig{position:absolute;left:72px;top:64px;width:230px;height:46px;background:#f4f7fc;-webkit-mask:url(SIG) left center/contain no-repeat}
.text{position:absolute;left:72px;top:190px;width:640px}
.k{font-size:30px;font-weight:600;color:#4da3ff;letter-spacing:-.01em}
h1{font-size:TITLESIZEpx;font-weight:700;letter-spacing:-.045em;line-height:1.02;margin-top:14px}
p{font-size:30px;color:#93a3bd;font-weight:500;line-height:1.3;margin-top:22px;letter-spacing:-.015em}
.url{position:absolute;left:72px;bottom:58px;font-size:24px;color:#7384a0;letter-spacing:-.01em}
.art{position:absolute;right:90px;top:50%;transform:translateY(-50%)}
.art img{display:block}
.icon{width:300px;height:300px;border-radius:24%;box-shadow:0 40px 100px rgba(0,0,0,.6)}
.logo{width:340px}
.photo{width:380px;height:470px;object-fit:cover;object-position:50% 25%;border-radius:36px;box-shadow:0 40px 100px rgba(0,0,0,.6)}
</style></head><body><div class="glow"></div><div class="sig"></div>
<div class="text"><div class="k">KICKER</div><h1>TITLE</h1><p>SUB</p></div><div class="art">ART</div><div class="url">URLTEXT</div></body></html>'''


def shot(name, kicker, title, sub, art, color='rgba(29,95,214,.', url='marcantoniopovolo.com', size=96):
    c = color if color.endswith('.') else color
    sig = 'data:image/png;base64,' + base64.b64encode((A / 'img' / 'signature-navy.png').read_bytes()).decode()
    html = (BASE.replace('TITLESIZE', str(size)).replace('COLOR55', f'{color}' if color.startswith('#') else 'rgba(29,95,214,.55)')
            .replace('SIG', sig).replace('KICKER', kicker).replace('TITLE', title)
            .replace('SUB', sub).replace('ART', art).replace('URLTEXT', url))
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
        f.write(html)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=1200,630', f'--screenshot={OUT / (name + ".png")}', Path(f.name).as_uri()],
                   check=True, capture_output=True)
    png = OUT / (name + '.png')
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '82', str(png), '--out', str(OUT / (name + '.jpg'))], check=True, capture_output=True)
    png.unlink()
    print('wrote', name + '.jpg')


def glow(hex_):
    return hex_ + '8c'   # the project colour at 55% opacity


shot('site', 'Marcantonio Povolo', 'Think Bigger.', 'Computer Engineering at TMU. I build apps and co-founded Cloudform.',
     f'<img class="photo" src="{(A / "img" / "portrait.jpg").as_uri()}">', size=104)

PROJECTS = [('markets', 'Markets by MP', 'My TSX and US stocks together, in Canadian dollars.', 'img/projects/markets.webp', '#10b981', False),
            ('cloudform', 'Cloudform', 'The company I co-founded, and its home on the web.', 'img/cloudform-logo.png', '#7ccfff', True),
            ('website', 'This website', 'marcantoniopovolo.com, built one page at a time.', 'img/projects/website.webp', '#4da3ff', False),
            ('coursework', 'Engineering coursework', 'Labs that build the foundation.', 'img/projects/coursework.webp', '#b3a0ff', False),
            ('trains', 'Trains by MP', 'Your GO trains, next to your classes.', 'img/projects/trains.webp', '#3b82f6', False),
            ('photos', 'Photos by MP', 'A proper home for my photography.', 'img/projects/photos.webp', '#8b5cf6', False),
            ('lineups', 'Lineups by MP', 'A research desk for daily fantasy.', 'img/projects/lineups.webp', '#f97316', False),
            ('closet', 'Closet by MP', 'A closet that builds itself.', 'img/projects/closet.webp', '#ec4899', False)]
for pid, name, tag, img, color, logo in PROJECTS:
    cls = 'logo' if logo else 'icon'
    shot(pid, 'Project', name, tag, f'<img class="{cls}" src="{(A / img).as_uri()}">', glow(color),
         f'marcantoniopovolo.com/projects/{pid}', 96 if len(name) < 16 else 76)
