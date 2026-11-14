"""Builds marcantoniopovolo.com: the six pages, a page per project, and the 404.
Run from anywhere: python3 tools/build_site.py  (it writes into the repo root). Then check, commit and push."""
import json
from datetime import date
from pathlib import Path
from html import escape
R = Path(__file__).resolve().parent.parent
SITE = 'https://marcantoniopovolo.com/'
URL = {k: f'https://{k}.marcantoniopovolo.com/' for k in ('markets', 'trains', 'photos', 'lineups', 'closet', 'cloudform')}
CODE = 'https://github.com/povolom/'
EMAIL = 'contact@marcantoniopovolo.com'
EMAIL_BR = 'contact<wbr>@marcantoniopovolo.com'   # lets a narrow screen break the address at the @, never mid-word
NAV = [('index.html', 'Home'), ('projects.html', 'Projects'), ('apps.html', 'Apps'), ('about.html', 'About'), ('resume.html', 'Résumé'), ('contact.html', 'Contact')]
MENU = '<span class="burger" aria-hidden="true"><span></span><span></span></span>'
PAGES = []   # every published address, for sitemap.xml
PERSON = {'@type': 'Person', '@id': 'https://marcantoniopovolo.com/#me', 'name': 'Marcantonio Povolo', 'url': 'https://marcantoniopovolo.com/',
          'image': 'https://marcantoniopovolo.com/assets/img/portrait.jpg', 'jobTitle': 'Computer Engineering student',
          'affiliation': {'@type': 'CollegeOrUniversity', 'name': 'Toronto Metropolitan University'},
          'sameAs': ['https://www.linkedin.com/in/marcantoniopovolo/', 'https://github.com/povolom']}
EXT = ' target="_blank" rel="noopener noreferrer"'

FOOTER = f'''<footer class="footer"><div class="wrap foot-top">
<div class="foot-brand"><span class="signature" role="img" aria-label="Marcantonio Povolo"></span><strong>Think Bigger.</strong><p>Computer Engineering at Toronto Metropolitan University. Based in GTA.</p></div>
<div class="foot-col"><h2>Explore</h2><ul><li><a href="index.html">Home</a></li><li><a href="projects.html">Projects</a></li><li><a href="apps.html">Apps</a></li><li><a href="about.html">About</a></li></ul></div>
<div class="foot-col"><h2>Résumé</h2><ul><li><a href="resume.html">View résumé</a></li><li><a href="assets/Marcantonio-Povolo-Resume.pdf" download>Download PDF</a></li></ul></div>
<div class="foot-col"><h2>Connect</h2><ul><li><a href="mailto:{EMAIL}">Email</a></li><li><a href="https://www.linkedin.com/in/marcantoniopovolo/">LinkedIn</a></li><li><a href="https://github.com/povolom">GitHub</a></li></ul></div>
</div><div class="wrap foot-bottom"><span>© 2026 Marcantonio Povolo</span><span>Built by hand in HTML and CSS, generated with a little Python.</span></div></footer>'''


def page(file, title, desc, body, og='site', og_type='website', ld=None, og_alt=None):
    full = f'Marcantonio Povolo | {title}' if file == 'index.html' else f'{title} | Marcantonio Povolo'
    path = '' if file == 'index.html' else file.removesuffix('.html')
    url = f'{SITE}{path}'
    img = f'{SITE}assets/img/og/{og}.jpg'
    alt = og_alt or f'{title}, by Marcantonio Povolo'
    links = ''.join(f'<a href="{f}"' + (' aria-current="page"' if f == file else '') + f'>{t}</a>' for f, t in NAV)
    noindex = file == '404.html'
    if not noindex: PAGES.append(url)
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False, separators=(",", ":"))}</script>' for x in (ld or []))
    head = (f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<title>{escape(full)}</title><meta name="description" content="{escape(desc)}"><meta name="author" content="Marcantonio Povolo">'
            + ('<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{url}">') +
            '<meta name="theme-color" content="#03070f"><meta name="color-scheme" content="dark"><meta name="format-detection" content="telephone=no">'
            '<meta name="apple-mobile-web-app-title" content="Marcantonio"><link rel="manifest" href="/site.webmanifest">'
            '<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48"><link rel="icon" type="image/png" sizes="192x192" href="/assets/icons/favicon-192.png"><link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">'
            f'<meta property="og:site_name" content="Marcantonio Povolo"><meta property="og:locale" content="en_CA"><meta property="og:type" content="{og_type}">'
            f'<meta property="og:title" content="{escape(full)}"><meta property="og:description" content="{escape(desc)}">'
            + ('' if noindex else f'<meta property="og:url" content="{url}">') +
            f'<meta property="og:image" content="{img}"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{escape(alt)}">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(full)}"><meta name="twitter:description" content="{escape(desc)}"><meta name="twitter:image" content="{img}"><meta name="twitter:image:alt" content="{escape(alt)}">'
            f'{ld_html}<link rel="stylesheet" href="assets/css/premium.css"><script src="assets/js/premium.js" defer></script>')
    out = f'''<!doctype html><html lang="en-CA"><head>{head}</head><body><a class="skip" href="#main">Skip to content</a><header class="nav-bar"><div class="wrap"><a class="signature" href="index.html" aria-label="Marcantonio Povolo, home"></a><button class="menu" aria-expanded="false" aria-controls="navigation" aria-label="Open menu">{MENU}</button><nav class="nav" id="navigation" aria-label="Main">{links}</nav></div></header><main id="main">{body}</main>{FOOTER}</body></html>'''
    import re
    out = re.sub(r'(href|src)="(?!https?:|mailto:|#|/)', r'\1="/', out)
    out = re.sub(r' data-(reveal|stagger)', '', out)
    # Clean addresses: Cloudflare serves /projects for projects.html (and redirects the .html form).
    out = re.sub(r'href="/index\.html"', 'href="/"', out)
    out = re.sub(r'href="(/[^"#]*?)\.html(#[^"]*)?"', lambda m: f'href="{m.group(1)}{m.group(2) or ""}"', out)
    (R / file).parent.mkdir(parents=True, exist_ok=True)
    (R / file).write_text(out)


def hero(title, sub='', extra='', kicker=''):
    """A centred page opening; each line rises in, in order."""
    parts = []
    if kicker: parts.append(f'<p class="kicker" data-in style="--i:0">{kicker}</p>')
    parts.append(f'<h1 class="display" data-in style="--i:1">{title}</h1>')
    if sub: parts.append(f'<p class="sub" data-in style="--i:2">{sub}</p>')
    if extra: parts.append(f'<div data-in style="--i:3">{extra}</div>')
    return f'<section class="hero page-hero"><div class="wrap">{"".join(parts)}</div></section>'


def contact_band(title='Got a big idea?<br>Let’s talk.', sub='Engineering, software, or something worth figuring out.'):
    return f'<section class="contact"><div class="wrap" data-reveal><h2 class="headline">{title}</h2><p class="sub">{sub}</p><a class="email" href="mailto:{EMAIL}">{EMAIL_BR}</a><div class="ctas" style="margin-top:22px"><button class="btn2" type="button" data-copy="{EMAIL}"><svg viewBox="0 0 16 16" aria-hidden="true"><rect x="5" y="5" width="8.5" height="8.5" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M3 10.5V4a1.5 1.5 0 0 1 1.5-1.5H11" fill="none" stroke="currentColor" stroke-width="1.5"/></svg><span>Copy email</span></button></div></div></section>'


# ---------- Home ----------
WORK = [('markets', 'assets/img/projects/markets.webp', 'Markets by MP', 'My TSX and US stocks together, in Canadian dollars.', 'Live US prices, total return, allocation and a chart of the whole portfolio.', 'soon', 'Coming soon'),
        ('cloudform', 'assets/img/cloudform-logo.png', 'Cloudform', 'The company I co-founded.', 'I led it as CEO from 2021 to 2026. Its website went through more than 40 versions.', 'live', 'Live'),
        ('website', 'assets/img/projects/website.webp', 'This website', 'One script. Every page.', 'Generated from a single Python script and deployed from GitHub to Cloudflare.', 'live', 'Live'),
        ('coursework', 'assets/img/projects/coursework.webp', 'Engineering coursework', 'The foundation.', 'Object-oriented Java, digital logic in VHDL and op-amp circuits from second-year Computer Engineering.', '', 'Completed')]


def wtile(a, img, n, lead, d, cls, st):
    logo = ' logo' if a == 'cloudform' else ''
    return (f'<a class="tile" href="/projects/{a}.html" data-reveal><p class="state {cls}">{st}</p><h3>{n}</h3><p class="lead">{lead}</p>'
            f'<p style="margin:10px auto 0">{d}</p><span class="more">Learn more</span><img class="icon{logo}" src="{img}" alt="" width="400" height="400" loading="lazy"></a>')


page('index.html', 'Think Bigger.', 'Marcantonio Povolo is a Computer Engineering student at Toronto Metropolitan University who builds apps like Markets by MP and co-founded the game-development company Cloudform.', f'''
<section class="hero"><div class="wrap">
 <p class="kicker" data-in style="--i:0">Marcantonio Povolo</p>
 <h1 class="display" data-in style="--i:1">Think Bigger.</h1>
 <p class="sub" data-in style="--i:2"><span class="d-only">Computer Engineering at TMU. I build apps like Markets by MP, and I <span class="nowrap">co-founded</span> Cloudform, a <span class="nowrap">game-development</span> company.</span><span class="m-only">Computer Engineering at TMU. I build apps and <span class="nowrap">co-founded</span> Cloudform.</span></p>
 <div class="ctas" data-in style="--i:3"><a class="pill" href="projects.html">See my projects</a><a class="more" href="about.html">More about me</a></div>
 <p class="aside" data-in style="--i:4">Wait, doesn’t Cloudform say that? It does. I <span class="nowrap">co-founded</span> it, so the motto came with me.</p>
 <figure class="portrait" data-in style="--i:5"><img src="assets/img/portrait.jpg" alt="Marcantonio Povolo by the waterfront" width="1025" height="840" fetchpriority="high"></figure>
</div></section>

<section class="section"><div class="wrap">
 <div class="section-intro" data-reveal><h2 class="headline">Right now.</h2></div>
 <div class="bento swipe" data-stagger>
  <article class="tile t-third" data-reveal><p class="label">CS50x</p><h3>Harvard’s intro to computer science.</h3><p>In progress, alongside school.</p><div class="big-stat">Week 3</div></article>
  <a class="tile t-third" href="/projects/markets.html" data-reveal><p class="label">Markets by MP</p><h3>Built. Now in testing.</h3><p>It opens to the public once testing is done.</p><img class="tile-icon" src="assets/img/projects/markets.webp" alt="" width="72" height="72" loading="lazy"></a>
  <article class="tile t-third" data-reveal><p class="label">Next</p><h3>Summer 2027 internships.</h3><p>Especially structured programs in product, program and project management.</p><span class="spacer"></span><a class="more" href="resume.html">See my résumé</a></article>
 </div>
</div></section>

<section class="section tight"><div class="wrap">
 <div class="section-intro" data-reveal><h2 class="headline">Selected work.</h2><div class="ctas" style="margin-top:12px"><a class="more" href="projects.html">All projects</a></div></div>
 <div class="work" data-stagger>{''.join(wtile(*w) for w in WORK)}</div>
</div></section>

<section class="section tight"><div class="wrap">
 <div class="section-intro" data-reveal><h2 class="headline">Think bigger.<br>Start small.</h2><p class="sub">Big ideas start with a real problem. I build the smallest version that helps, then improve it.</p></div>
 <ol class="steps" data-stagger>
  <li data-reveal><h3>Understand the problem</h3><p>Start with people, constraints and what would actually help.</p></li>
  <li data-reveal><h3>Make something tangible</h3><p>Explore through code, interfaces and small working prototypes.</p></li>
  <li data-reveal><h3>Learn from the details</h3><p>Test assumptions, ask questions and improve the next version.</p></li>
 </ol>
</div></section>
{contact_band()}''', ld=[{'@context': 'https://schema.org', '@graph': [PERSON, {'@type': 'WebSite', '@id': 'https://marcantoniopovolo.com/#site', 'url': 'https://marcantoniopovolo.com/', 'name': 'Marcantonio Povolo', 'publisher': {'@id': 'https://marcantoniopovolo.com/#me'}, 'inLanguage': 'en-CA'}]}])


# ---------- Apps ----------
APPS = [('markets', 'Markets', '#10b981', 'My TSX and US stocks in Canadian dollars, with live US prices.'),
        ('trains', 'Trains', '#3b82f6', 'Pick your GO train trips and get calendar entries for them.'),
        ('photos', 'Photos', '#8b5cf6', 'A fast gallery for my photography.'),
        ('lineups', 'Lineups', '#f97316', 'A research desk for daily fantasy.'),
        ('closet', 'Closet', '#ec4899', 'A closet that builds itself from daily photos.')]
strip = ''.join(f'<li><a href="#app-{s}"><img src="assets/icons/apps/{s}.png" alt="" width="56" height="56">{w}</a></li>' for s, w, c, d in APPS)
apps = ''.join(f'<section class="app-hero" id="app-{s}" style="--glow:{c}"><div class="wrap" data-reveal><img src="assets/icons/apps/{s}.png" alt="" width="148" height="148" loading="lazy"><h2>{w} <span>by MP</span></h2><p class="sub">{d}</p><div class="app-meta"><strong>Coming soon</strong><br>{s}.marcantoniopovolo.com</div><div class="ctas" style="margin-top:18px"><a class="pill" href="{URL[s]}">Open the app</a><a class="more" href="/projects/{s}.html">How I built it</a></div></div></section>' for s, w, c, d in APPS)
page('apps.html', 'Apps', 'Five apps by Marcantonio Povolo, each at its own web address: Markets, Trains, Photos, Lineups and Closet by MP. All coming soon, and open source.',
     hero('Small apps.<br>Built to be used.', 'Each one gets its own web address and a download for your phone or computer. None are open yet.', f'<ul class="app-strip">{strip}</ul>')
     + apps + contact_band('Want to try one early?', 'Tell me which app and what you’d use it for.'))


# ---------- About ----------
def timeline(items):
    rows = ''.join(f'<li><span class="when">{w}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for w, t, d in items)
    more = f'<button class="btn2 show-all" type="button" aria-expanded="false"><span>Show all {len(items)}</span></button>' if len(items) > 3 else ''
    return f'<div class="clip"><ul class="timeline">{rows}</ul>{more}</div>'


EXPERIENCE = [('Sep 2026 to now', 'TMU Velocity', 'Software team member on the autonomous vehicles design team, which competes in RoboRacer (F1TENTH).'),
              ('Sep 2026 to now', 'MUES Communications Committee', 'Committee member with the Metropolitan Undergraduate Engineering Society.'),
              ('2025 to now', 'Engineers for a Sustainable World, TMU', 'General member.'),
              ('Oct 2025 to May 2026', 'TMU MetRobotics', 'Outreach team member.'),
              ('2021 to 2026', 'Cloudform LLC', '<span class="nowrap">Co-founder</span> and CEO. Product direction, project planning, branding and team coordination.'),
              ('Aug 2023 to now', 'Metro', 'Part-time produce clerk, alongside school.')]
SCHOOL = [('2024 to 2025', 'Core Retreat Leader', 'Helped run the school’s outreach initiatives, led the school Eco Team, co-led a colour group, and helped organize school-wide events like the Thanksgiving Food Drive.'),
          ('2023 to 2024', 'Retreat Leader', 'Supported the Eco Club, Domestic Outreach and Students 4 Action, and took part in retreats run by the Core Retreat Leaders.'),
          ('2021 to 2025', 'Student Ambassador', 'Set up and helped run school events including graduation, student votes and uniform sales.'),
          ('2023 to 2025', 'Clubs and outreach', 'Best Buddies, Domestic Outreach (Thanksgiving, Christmas and Electro Drives), International Outreach, Students 4 Action, Safe and Caring, and Woodworking Club.'),
          ('Events', 'Multicultural Night and Colour Run', 'Built and ran the Italy classroom for Multicultural Night, with an interactive game and presentation, and volunteered at the school Colour Run.'),
          ('Awards', 'Honour Roll, Grades 9 to 11', 'Highest-grade subject awards in Automotive, Construction Technology and History; Arts Fest Photography Award in Grades 10 and 11.')]
page('about.html', 'About', 'About Marcantonio Povolo: Computer Engineering at TMU, the TMU Velocity software team, co-founding Cloudform, leadership, and a background in photography, guitar and dance.',
     hero('Thinking bigger<br>since 2021.', 'I’m Marcantonio, a second-year Computer Engineering student at Toronto Metropolitan University. Based in GTA.')
     + f'''<section class="section tight"><div class="wrap story"><img src="assets/img/portrait.jpg" alt="Marcantonio Povolo" width="1025" height="840" loading="lazy" data-reveal><div data-reveal>
<p class="lead">Building is how I learn. I’m drawn to technical product development and the space where hardware meets software.</p>
<p>I started building in 2021, making Roblox games in Lua with small online teams. That turned into Cloudform, a game-development and early software company I <span class="nowrap">co-founded</span> and led as CEO until 2026. Our team delivered eleven maps for our game <em>The Lost Jungle</em>, and I learned how much planning, communication and scope decide whether a project actually gets finished. Our motto was “Think Bigger,” and it still shapes how I take on projects.</p>
<p>At TMU I’m building the engineering foundation: Java object-oriented programming, C, digital logic in VHDL and electronic circuits. This fall I joined the software team at TMU Velocity, where I’m learning ROS 2 by working on autonomous race cars. Alongside school I’m working through Harvard’s CS50x.</p>
<p>Outside engineering I’m a photographer (twice winning my high school’s Arts Fest photography award), a self-taught guitarist, and a former competitive dancer. Eight years of dance taught me discipline and how to learn fast when the plan changes.</p>
</div></div></section>
<section class="section tight"><div class="wrap"><div class="bento" data-stagger>
 <article class="tile t-wide" data-reveal><p class="label">Learning now</p><h3>CS50x: Introduction to Computer Science</h3><p>Harvard / edX. C, arrays, memory and algorithms, then Python, SQL and web. Working through it on the train and on weekends, alongside my own projects.</p><div class="big-stat m-block">Week 3</div><span class="spacer"></span><div class="ctas" style="justify-content:flex-start"><a class="more" href="https://cs50.harvard.edu/x/"{EXT}>About the course</a></div></article>
 <article class="tile t-narrow d-block"><p class="label">Progress</p><h3>In progress</h3><div class="big-stat">Week 3</div></article>
</div></div></section>
<section class="section tight"><div class="wrap"><div class="section-intro" data-reveal><h2 class="headline">Learning alongside<br>other people.</h2><p class="sub">Engineering is also about communicating clearly and contributing to a team.</p></div>{timeline(EXPERIENCE)}</div></section>
<section class="section tight"><div class="wrap"><div class="section-intro" data-reveal><h2 class="headline">Where I learned<br>to lead.</h2><p class="sub">High school, 2021 to 2025.</p></div>{timeline(SCHOOL)}</div></section>
''' + contact_band())


# ---------- Résumé ----------
def rsec(label, inner):
    return f'<section class="r-sec" data-reveal><h2>{label}</h2><div>{inner}</div></section>'


RESUME = ''.join([
    rsec('Education', '<div class="r-item"><h3>Toronto Metropolitan University</h3><h4>Bachelor of Engineering, Computer Engineering. Second year.</h4><p>CGPA 3.79 out of 4.33. Dean’s List in Fall 2025 and Winter 2026, my first two terms. Coursework in Java object-oriented programming, C, digital systems (VHDL), electronic circuits and physics.</p></div><div class="r-item"><h3>High school</h3><h4>2021 to 2025</h4><p>Honour Roll (Grades 9 to 11); highest-grade subject awards in Automotive, Construction Technology and History; Arts Fest Photography Award.</p></div>'),
    rsec('Certification', '<div class="r-item"><h3>CS50x: Introduction to Computer Science</h3><h4>Harvard / edX. In progress.</h4></div>'),
    rsec('Skills', '<dl class="skills"><dt>Languages</dt><dd>C, Java, Lua, VHDL, HTML (learning), CSS (learning), JavaScript (learning), Python (learning)</dd><dt>Robotics and systems</dt><dd>ROS 2, Docker, Linux (Ubuntu), Git and GitHub</dd><dt>Hardware and tools</dt><dd>Quartus, MultiSIM, circuit analysis, VS Code, Geany, NetBeans</dd><dt>Design</dt><dd>UI design, Photoshop, Premiere Pro, Canva, photography, Figma</dd></dl>'),
    rsec('Experience', '<div class="r-item"><h3>TMU Velocity</h3><h4>Software Team Member. 2026 to now.</h4><ul><li>Completed software onboarding Labs 1 and 2 for the RoboRacer (F1TENTH) autonomous racing program in ROS 2 on Ubuntu.</li><li>Set up the RoboRacer simulator in Docker and wrote an AI-assisted emergency-braking safety node, tested in simulation.</li></ul></div><div class="r-item"><h3>Cloudform LLC</h3><h4><span class="nowrap">Co-founder</span> and CEO. 2021 to 2026.</h4><ul><li>Led an independent game-development and early software company: product direction, planning, branding and team coordination.</li><li>Directed the Roblox game <em>The Lost Jungle</em> through 11 delivered maps with scripters and freelance builders, modellers and animators.</li></ul></div><div class="r-item"><h3>Metro</h3><h4>Produce Clerk. August 2023 to now.</h4><p>Part-time, alongside full-time studies.</p></div>'),
    rsec('Leadership', '<div class="r-item"><h3>Campus and community</h3><ul><li>TMU Velocity Software Team, September 2026 to now</li><li>MUES Communications Committee, September 2026 to now</li><li>TMU MetRobotics Outreach Team, October 2025 to May 2026</li><li>Engineers for a Sustainable World, TMU, 2025 to now</li></ul></div><div class="r-item"><h3>High school leadership</h3><ul><li>Core Retreat Leader and Eco Team lead, 2024 to 2025</li><li>Retreat Leader, 2023 to 2024</li><li>Student Ambassador, 2021 to 2025</li></ul><p>Also Best Buddies, Domestic and International Outreach, Students 4 Action, Safe and Caring, Thanksgiving Food Drive and Multicultural Night.</p></div>'),
    rsec('Projects', '<div class="r-item"><h3>Markets by MP</h3><p>Installable investing app: live US prices, TSX prices, CAD conversion, a portfolio chart and allocation. Built with AI coding tools; I review and test each change.</p></div><div class="r-item"><h3>This website</h3><p>Responsive portfolio generated with Python and deployed on Cloudflare.</p></div><div class="r-item"><h3>Trains by MP and Photos by MP</h3><p>Coming soon: GO train trips as calendar entries, and a fast gallery for my photography.</p></div><div class="ctas" style="justify-content:flex-start;margin-top:16px"><a class="more" href="projects.html">Explore project details</a></div>'),
])
page('resume.html', 'Résumé', 'The résumé of Marcantonio Povolo, a TMU Computer Engineering student looking for Summer 2027 internships: education, skills, experience and projects, with a PDF to download.',
     hero('The bigger picture,<br>on one page.', 'Computer Engineering student looking for Summer 2027 internships.', '<div class="ctas"><a class="pill" href="assets/Marcantonio-Povolo-Resume.pdf" download>Download PDF</a><a class="more" href="contact.html">Get in touch</a></div>')
     + f'''<div class="wrap resume section tight"><div>{RESUME}</div><aside class="r-aside tile" data-reveal><h2>Take a copy.</h2><p>A one-page résumé for internships in software, technical product and program roles.</p><a class="pill" href="assets/Marcantonio-Povolo-Resume.pdf" download>Download PDF</a><p class="small">Updated September 2026</p></aside></div><div class="m-dock"><span>Résumé, one page</span><a class="pill" href="assets/Marcantonio-Povolo-Resume.pdf" download>Download PDF</a></div>''')


# ---------- Contact ----------
page('contact.html', 'Contact', 'Get in touch with Marcantonio Povolo about internships, engineering, software and product work, by email, LinkedIn or GitHub.',
     hero('Let’s build<br>something bigger.', 'Have a project in mind, an opportunity to share, or an idea worth talking about? I’d love to hear it.')
     + f'''<section class="section tight"><div class="wrap"><div class="c-grid" data-stagger>
 <a class="tile c-full c-email" href="mailto:{EMAIL}"><p class="label">Email</p><h3>{EMAIL_BR}</h3><p>The best place to start a conversation.</p><span class="more">Write to me</span></a>
 <a class="tile c-half" href="https://www.linkedin.com/in/marcantoniopovolo/"><p class="label">LinkedIn</p><h3>Connect professionally.</h3><p>Education, experience and updates.</p><span class="more">Open LinkedIn</span></a>
 <a class="tile c-half" href="https://github.com/povolom"><p class="label">GitHub</p><h3>povolom</h3><p>Code, experiments and ongoing learning.</p><span class="more">Open GitHub</span></a>
 <article class="tile c-full"><p class="label">Based in GTA</p><h3>Interested in what’s next.</h3><p>I’m exploring Summer 2027 opportunities in software development, firmware, embedded systems and technical product development, especially on teams that connect software with hardware and put thoughtful products in people’s hands.</p><span class="spacer"></span><div class="ctas" style="justify-content:flex-start"><a class="more" href="resume.html">View my résumé</a></div></article>
</div></div></section>''')

# ---------- 404 ----------
page('404.html', 'Page not found', 'This page could not be found.',
     hero('A small detour.', 'The page you’re looking for isn’t here.', '<div class="ctas"><a class="pill" href="/">Back home</a><a class="more" href="projects.html">See my projects</a></div>'))

exec((Path(__file__).resolve().parent / 'build_projects.py').read_text())

# Search engines and installs
today = date.today().isoformat()
(R / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                               + ''.join(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n' for u in PAGES) + '</urlset>\n')
(R / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
(R / 'site.webmanifest').write_text(json.dumps({'name': 'Marcantonio Povolo', 'short_name': 'Marcantonio', 'description': 'Think Bigger. Projects and apps by Marcantonio Povolo.',
    'start_url': '/', 'scope': '/', 'display': 'minimal-ui', 'background_color': '#03070f', 'theme_color': '#03070f',
    'icons': [{'src': '/assets/icons/favicon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '/assets/icons/apple-touch-icon.png', 'sizes': '180x180', 'type': 'image/png'}]}, indent=2) + '\n')
print('Built', len(PAGES), 'pages, the 404, sitemap.xml, robots.txt and site.webmanifest.')
