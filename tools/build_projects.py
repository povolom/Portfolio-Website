# Project pages on marcantoniopovolo.com: one Projects index and a page per project with two parts,
# "About the project" and "My experience". Run through build_site.py (shares page(), hero() etc.).
# Facts come from each project's repo (README and commit history) and the existing site. The
# experience answers are Marcantonio's to write; until then they say Coming soon.

SOON = 'Coming soon. I’m writing this part myself.'

PROJECTS = [
 dict(id='markets', name='Markets by MP', icon='assets/img/projects/markets.webp', color='#10b981', state='soon', label='Coming soon',
      tagline='My TSX and US stocks together, in Canadian dollars.',
      about=['Markets shows my TSX and US stocks together, in Canadian dollars: live US prices, today’s change, total return, allocation and a chart of the whole portfolio.',
             'It installs on a phone or computer like a regular app, walks new users through getting a free data key, and keeps keys and holdings in the browser. Visitors without a key see a demo portfolio.',
             'It began on September 27, 2026 as a Python and SQLite script on my laptop, with input validation and eight tests. A day later it was a web app called Portfolio Lab, then Investing Tracker. On October 3 it became Markets by MP: redesigned as a real investing app with live US prices, at its own address.',
             'Free data has tight limits. Finnhub allows 60 requests a minute for US prices and Alpha Vantage 25 a day for Toronto prices, so the app caches prices and spaces out its requests. All the maths lives in one file with no browser code, so it can be tested on its own.',
             'It’s built, and I’m testing it before opening it up.'],
      highlights=[('Live prices', 'Live US prices and delayed Toronto prices, converted at the daily rate.'),
                  ('The whole picture', 'Today’s change, total return, allocation and a chart of the portfolio.'),
                  ('Yours alone', 'No accounts. Keys and holdings never leave your device.')],
      timeline='September 2026 to now', role='Product decisions, review and testing',
      chips=['JavaScript', 'REST APIs', 'SVG charts', 'Installable web app', 'Python', 'SQLite'],
      links=[('Open the app', URL['markets'], None), ('View code', CODE + 'Markets-by-MP', None)],
      experience=[('My role', 'I decide what it should do, use AI coding tools to write the code faster, then review, test and fix each change.'),
                  ('What was hardest', SOON), ('What I learned', SOON), ('What I’d do differently', SOON)]),
 dict(id='cloudform', name='Cloudform', icon='assets/img/cloudform-logo.png', logo=True, color='#7ccfff', state='live', label='Live',
      tagline='The company I co-founded, and its home on the web.',
      about=['Cloudform is the game-development and early software company I <span class="nowrap">co-founded</span> in 2021 and led as CEO until 2026.',
             'It started with Roblox games in Lua, made with small online teams. Our game <em>The Lost Jungle</em> shipped eleven maps, built with scripters and freelance builders, modellers and animators.',
             'The website brings together the company story, a section for each division (Ciryx for games and Altyx for software), Explore pages for About, News, Careers and Events, and a store preview that sells nothing and collects nothing. I rebuilt it across more than 40 versions; version 41 is the one online today.',
             'It’s plain HTML, CSS and JavaScript with no build step. It now lives at cloudform.marcantoniopovolo.com, with the original files left exactly as they were.'],
      highlights=[('41 versions', 'Rebuilt and refined again and again until version 41.'),
                  ('11 maps', 'Shipped for <em>The Lost Jungle</em> with a small remote team.'),
                  ('Two divisions', 'Ciryx for games and Altyx for software.')],
      timeline='2021 to 2026', role='<span class="nowrap">Co-founder</span> and CEO',
      chips=['HTML', 'CSS', 'JavaScript', 'Branding', 'Team leadership'],
      links=[('Visit Cloudform', URL['cloudform'], None), ('View code', CODE + 'Cloudform-Website', None)],
      experience=[('My role', 'As <span class="nowrap">co-founder</span> and CEO, I worked on product direction, project planning, branding and team coordination.'),
                  ('What was hardest', SOON), ('What I learned', SOON), ('What I’d do differently', SOON)]),
 dict(id='website', name='This website', icon='assets/img/projects/website.webp', color='#4da3ff', state='live', label='Live',
      tagline='marcantoniopovolo.com, built one page at a time.',
      about=['The site you’re on: six pages, plus a page for every project, all written by one Python script so the content lives in one place and every page matches.',
             'It started on July 26, 2026 as a coming-soon page on GitHub. On September 28 it became a full portfolio with “Think Bigger.” as its slogan, then gained a proper favicon, a custom 404 page and my résumé. In October it added an Apps page and gave each app its own subdomain.',
             'It’s hosted on Cloudflare and redeploys whenever I push to GitHub. Every page is checked at phone, tablet and desktop widths, with keyboard navigation and a mobile menu. There’s no phone number or address anywhere, and photos have their location data removed.'],
      highlights=[('One script', 'Every page comes from one Python script.'),
                  ('Ships on push', 'GitHub to Cloudflare in under a minute.'),
                  ('No framework', 'Plain HTML, CSS and JavaScript.')],
      timeline='July 2026 to now', role='Content, design decisions and review',
      chips=['HTML', 'CSS', 'JavaScript', 'Python', 'Cloudflare', 'Git'],
      links=[('View code', CODE + 'Portfolio-Website', None)],
      experience=[('My role', 'Every fact on the site comes from me. AI coding tools help write the code, and I review and edit every change.'),
                  ('What was hardest', SOON), ('What I learned', SOON), ('What I’d do differently', SOON)]),
 dict(id='coursework', name='Engineering coursework', icon='assets/img/projects/coursework.webp', color='#b3a0ff', state='done', label='Completed',
      tagline='Labs that build the foundation.',
      about=['Second-year Computer Engineering at TMU pairs programming with circuits and digital logic. Three labs I’ve completed:',
             '<strong>Java OOP (COE318).</strong> A validated Resistor model and an immutable ComplexNumber class with arithmetic, equality and tested expected output.',
             '<strong>Digital logic in VHDL.</strong> One logic function implemented three ways in Quartus, with pin assignments and waveform checks against the truth table.',
             '<strong>Op-amp circuits (ELE302).</strong> Characterizing a μA741 op-amp, from equivalent-circuit models to saturation limits and measured graphs.'],
      highlights=[('Java', 'Classes with validation, immutability and tested output.'),
                  ('VHDL', 'One function built three ways and checked against its truth table.'),
                  ('Circuits', 'Op-amps from models to measured limits.')],
      timeline='Second year, TMU', role='My own lab work',
      chips=['Java', 'VHDL', 'Quartus', 'Analog circuits'], links=[],
      experience=[('What was hardest', SOON), ('What I learned', SOON)]),
 dict(id='trains', name='Trains by MP', icon='assets/img/projects/trains.webp', color='#3b82f6', state='soon', label='Coming soon',
      tagline='Your GO trains, next to your classes.',
      about=['Pick the GO trains you take and get calendar entries for them, so your commute sits next to your classes.',
             'It will use GO Transit’s free schedule data under Metrolinx’s terms.',
             'I’m starting with the product side: a one-page brief and a short survey of TMU commuters about what actually slows them down, then the smallest version that helps.'],
      highlights=[('Pick your trips', 'Choose the trains you actually take.'), ('Calendar entries', 'Your commute beside your classes.'), ('Free data', 'Official GO Transit schedules.')],
      timeline='Coming soon', role='Research, then the build', chips=['Product research', 'Transit data', 'Calendar files'],
      links=[('Open the app', URL['trains'], None), ('View code', CODE + 'Trains-by-MP', None)],
      experience=[('Why I want to build it', SOON)]),
 dict(id='photos', name='Photos by MP', icon='assets/img/projects/photos.webp', color='#8b5cf6', state='soon', label='Coming soon',
      tagline='A proper home for my photography.',
      about=['A fast, responsive gallery for my photography. I won my high school’s Arts Fest photography award in Grades 10 and 11, and I want a proper place to show that work.',
             'The plan: choose a small set of photos, design a layout that works well on phones, and keep every image sharp without making the page slow.'],
      highlights=[('Curated', 'A small, strong set of photos.'), ('Phone first', 'A layout made for small screens.'), ('Fast', 'Sharp images that still load quickly.')],
      timeline='Coming soon', role='Photography, design and the build', chips=['HTML', 'CSS', 'JavaScript', 'Photography'],
      links=[('Open the app', URL['photos'], None), ('View code', CODE + 'Photos-by-MP', None)],
      experience=[('Why I want to build it', SOON)]),
 dict(id='lineups', name='Lineups by MP', icon='assets/img/projects/lineups.webp', color='#f97316', state='soon', label='Coming soon',
      tagline='A research desk for daily fantasy.',
      about=['Bookmark players with their salaries, see who is worth their price tonight, build lineups under the cap and keep a ledger of results.',
             'It never connects to Yahoo. Salaries are typed or pasted by hand, and projections are labelled as estimates.'],
      highlights=[('Research', 'Players and salaries side by side.'), ('Build', 'Lineups that fit under the cap.'), ('Honest', 'Projections labelled as estimates.')],
      timeline='Coming soon', role='Planning it', chips=['TypeScript', 'SQL', 'Free sports data'],
      links=[('Open the app', URL['lineups'], None), ('View code', CODE + 'Lineups-by-MP', None)],
      experience=[('Why I want to build it', SOON)]),
 dict(id='closet', name='Closet by MP', icon='assets/img/projects/closet.webp', color='#ec4899', state='soon', label='Coming soon',
      tagline='A closet that builds itself.',
      about=['One mirror photo a day: the app finds each piece of clothing, works out whether it has seen it before, and keeps track of what I actually wear.',
             'Photos never leave the device, and faces are never stored.'],
      highlights=[('One photo a day', 'No typing in your clothes.'), ('Recognises clothes', 'Matches each piece to what it has seen.'), ('Stays on your phone', 'Photos never leave the device.')],
      timeline='Coming soon', role='Planning it', chips=['TypeScript', 'On-device models', 'IndexedDB'],
      links=[('Open the app', URL['closet'], None), ('View code', CODE + 'Closet-by-MP', None)],
      experience=[('Why I want to build it', SOON)]),
]


def link_html(label, href, toast_msg, primary):
    cls = 'pill' if primary else 'more'
    extra = f' data-toast="{toast_msg}"' if toast_msg else EXT
    return f'<a class="{cls}" href="{href}"{extra}>{label}</a>'


def disclose(title, body, open_=False):
    return (f'<div class="disclose{" open" if open_ else ""}"><button type="button" aria-expanded="{str(open_).lower()}">{title}<span class="plus" aria-hidden="true"></span></button>'
            f'<div class="panel"><div><p>{body}</p></div></div></div>')


for i, p in enumerate(PROJECTS):
    logo = ' logo' if p.get('logo') else ''
    ctas = ''.join(link_html(l, h, t, n == 0) for n, (l, h, t) in enumerate(p['links']))
    hero_html = (f'<section class="hero page-hero p-hero" style="--c:{p["color"]}"><div class="wrap">'
                 f'<div class="p-icon-wrap" data-in style="--i:0"><img class="p-icon{logo}" src="{p["icon"]}" alt="" width="400" height="400"></div>'
                 f'<div data-in style="--i:0"><span class="status-pill {p["state"]}">{p["label"]}</span></div>'
                 f'<h1 class="display p-title" data-in style="--i:1">{p["name"]}</h1><p class="sub" data-in style="--i:2">{p["tagline"]}</p>'
                 + (f'<div class="ctas" data-in style="--i:3">{ctas}</div>' if ctas else '') + '</div></section>')
    paras = p['about']
    # Phones show the first two paragraphs, with a button for the rest.
    story = f'<p class="lead">{paras[0]}</p>' + ''.join(f'<p>{x}</p>' for x in paras[1:2])
    if len(paras) > 2:
        story += ('<div class="story-more">' + ''.join(f'<p>{x}</p>' for x in paras[2:]) + '</div>'
                  '<button class="btn2 story-toggle" type="button" aria-expanded="false"><span>Read the full story</span></button>')
    chips = ''.join(f'<li>{c}</li>' for c in p['chips'])
    facts = (f'<aside class="facts tile"><dl><div><dt>Status</dt><dd><span class="status-pill {p["state"]}" style="margin:0">{p["label"]}</span></dd></div>'
             f'<div><dt>When</dt><dd>{p["timeline"]}</dd></div><div><dt>My role</dt><dd>{p["role"]}</dd></div>'
             f'<div><dt>Built with</dt><dd><ul class="chips">{chips}</ul></dd></div></dl>'
             + (f'<div class="facts-links">{"".join(link_html(l, h, t, False) for l, h, t in p["links"])}</div>' if p['links'] else '') + '</aside>')
    highlights = '<div class="bento p-high swipe">' + ''.join(f'<article class="tile t-third"><h3>{a}</h3><p>{b}</p></article>' for a, b in p['highlights']) + '</div>'
    about = (f'<section class="section tight"><div class="wrap"><h2 class="headline p-h2">About the project.</h2>'
             f'<div class="p-about"><div class="p-story">{story}</div>{facts}</div>{highlights}</div></section>')
    exp = ''.join(disclose(t, b, open_=(n == 0 and b != SOON)) for n, (t, b) in enumerate(p['experience']))
    experience = (f'<section class="section tight"><div class="wrap"><h2 class="headline p-h2">My experience.</h2>'
                  f'<div class="p-exp">{exp}</div></div></section>')
    def pager_tile(q, label, cls):
        if q is None:
            return f'<a class="tile pager-tile {cls} all" href="/projects.html"><p>{label}</p><h3>All projects</h3><span class="more">See every project</span></a>'
        ql = ' class="logo"' if q.get('logo') else ''
        return (f'<a class="tile pager-tile {cls}" href="/projects/{q["id"]}.html" style="--c:{q["color"]}"><img{ql} src="{q["icon"]}" alt="" width="96" height="96" loading="lazy">'
                f'<div><p>{label}</p><h3>{q["name"]}</h3></div></a>')
    prev_p = PROJECTS[i - 1] if i > 0 else None
    next_p = PROJECTS[i + 1] if i < len(PROJECTS) - 1 else None
    next_html = (f'<section class="section tight"><nav class="wrap pager2" aria-label="More projects">'
                 f'{pager_tile(prev_p, "Previous", "prev")}{pager_tile(next_p, "Next", "next")}</nav></section>')
    is_app = p['id'] in URL
    work = {'@type': 'SoftwareApplication' if is_app else 'CreativeWork', 'name': p['name'], 'description': p['tagline'],
            'url': f'https://marcantoniopovolo.com/projects/{p["id"]}', 'image': f'https://marcantoniopovolo.com/assets/img/og/{p["id"]}.jpg',
            'creator': {'@id': 'https://marcantoniopovolo.com/#me'}, 'keywords': ', '.join(p['chips'])}
    if is_app:
        work.update({'applicationCategory': 'WebApplication', 'operatingSystem': 'Any (web browser)', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'CAD'}})
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://marcantoniopovolo.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Projects', 'item': 'https://marcantoniopovolo.com/projects'},
        {'@type': 'ListItem', 'position': 3, 'name': p['name'], 'item': f'https://marcantoniopovolo.com/projects/{p["id"]}'}]}
    page(f'projects/{p["id"]}.html', p['name'],
         f'{p["name"]}: {p["tagline"].rstrip(".")}. About the project, and what Marcantonio Povolo learned building it.',
         hero_html + about + experience + next_html + contact_band(), og=p['id'], og_alt=f'{p["name"]}: {p["tagline"]}',
         ld=[{'@context': 'https://schema.org', '@graph': [PERSON, work, crumbs]}])


def ptile(p):
    logo = ' logo' if p.get('logo') else ''
    return (f'<a class="tile proj" href="/projects/{p["id"]}.html" style="--c:{p["color"]}"><span class="status-pill {p["state"]}">{p["label"]}</span>'
            f'<h3>{p["name"]}</h3><p>{p["tagline"]}</p><span class="more">About the project</span>'
            f'<img class="proj-icon{logo}" src="{p["icon"]}" alt="" width="200" height="200" loading="lazy"></a>')


page('projects.html', 'Projects', 'Markets by MP, Cloudform, this website, engineering coursework, Trains, Photos, Lineups and Closet by MP: what each project is and what it taught me.',
     hero('Think bigger.<br>Then build it.', 'Everything I’ve built or I’m building, and what each one taught me.')
     + f'<section class="section tight"><div class="wrap"><div class="proj-grid">{"".join(ptile(p) for p in PROJECTS)}</div></div></section>'
     + contact_band())
