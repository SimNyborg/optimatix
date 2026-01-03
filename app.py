from flask import Flask, render_template, send_from_directory, request, redirect, Response
from datetime import datetime

app = Flask(__name__)

# Simple translations for navbar and major UI strings
translations = {
    'da': {
        'nav_projekter': 'Projekter',
        'nav_services': 'Services',
        'nav_om': 'Om os',
        'nav_kontakt': 'Kontakt',
        'hero_h1': 'Målbare resultater\nmed data som drivkraft',
        'hero_p': 'Vi hjælper virksomheder med at optimere og skalere gennem datadrevne beslutninger.\nVi kombinerer data, forretning og teknologi for at skabe målbare forbedringer.\nIngen standardpakker, kun skræddersyede resultater.',
        'projects_h2': 'Projektportefølje',
        'projects_subheading': 'Et udvalg af projekter, der har gjort vores kunder mere effektive, så de kan bruge tiden på det, de er bedst til.',
        'services_h2': 'Vores Services',
        'services_subheading': 'Vi er specialister i datadrevet procesoptimering og implementering af effektive løsninger. Hvert projekt er unikt – kontakt os, så finder vi den rette løsning til din virksomhed.',
        'founders_h2': 'Om Optimatix',
        'contact_h2': 'Kontakt os',
        'contact_description': 'Du er velkommen til at kontakte os for forretningshenvendelser eller spørgsmål.',
        'newsletter_label': 'Tilmeld nyhedsbrev',
        'newsletter_button': 'Tilmeld',
        'breadcrumb_back': '← Tilbage',
        'lang_code': 'da'
    },
    'en': {
        'nav_projekter': 'Projects',
        'nav_services': 'Services',
        'nav_om': 'About',
        'nav_kontakt': 'Contact',
        'hero_h1': 'Measurable results\nwith data as the driver',
        'hero_p': 'We help companies optimize and scale through data-driven decisions.\nWe combine data, business and technology to create measurable improvements.\nNo standard packages, only tailored results.',
        'projects_h2': 'Project portfolio',
        'projects_subheading': 'A selection of projects that have made our customers more efficient, allowing them to focus on what they do best.',
        'services_h2': 'Our Services',
        'services_subheading': 'We specialize in data-driven process optimization and implementation of effective solutions. Every project is unique – contact us and we\'ll find the right solution for your business.',
        'founders_h2': 'About Optimatix',
        'contact_h2': 'Contact us',
        'contact_description': 'You are welcome to contact us for business inquiries or questions.',
        'newsletter_label': 'Subscribe to our newsletter',
        'newsletter_button': 'Subscribe',
        'breadcrumb_back': '← Back',
        'lang_code': 'en'
    }
}


@app.context_processor
def inject_strings():
    lang = request.cookies.get('site_lang', 'da')
    strings = translations.get(lang, translations['da'])
    return dict(strings=strings)

# Favicons are served from the project's `static/` folder and referenced
# in templates using `url_for('static', filename=...)`. No explicit routes
# are required here.

# Serve favicon.ico from the `static/` folder (canonical location for static assets)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')


@app.route('/setlang/<lang>')
def set_language(lang):
    # Set language cookie and redirect back
    resp = redirect(request.referrer or '/')
    if lang in translations:
        resp.set_cookie('site_lang', lang, max_age=30*24*3600)
    return resp

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

# Founder detail pages
@app.route('/founder/simon-nyborg')
def founder_simon():
    # Render Danish or English founder page depending on language cookie
    lang = request.cookies.get('site_lang', 'da')
    if lang == 'en':
        return render_template('founder_simon_en.html', year=datetime.now().year)
    return render_template('founder_simon.html', year=datetime.now().year)

@app.route('/founder/albert-koba')
def founder_albert():
    return render_template('founder_albert.html', year=datetime.now().year)

# Footer info pages
@app.route('/privatliv')
def privatliv():
    return render_template('privatliv.html', year=datetime.now().year)

@app.route('/cookies')
def cookies():
    return render_template('cookies.html', year=datetime.now().year)

@app.route('/vilkar')
def vilkar():
    return render_template('vilkar.html', year=datetime.now().year)

# Service pages
@app.route('/services/dataanalyse')
def service_dataanalyse():
    # Render Danish or English Data Analysis page depending on language cookie
    lang = request.cookies.get('site_lang', 'da')
    if lang == 'en':
        return render_template('service_dataanalyse_en.html', year=datetime.now().year)
    return render_template('service_dataanalyse.html', year=datetime.now().year)

@app.route('/services/forretningsudvikling')
def service_forretningsudvikling():
    # Render Danish or English Business Development page depending on language cookie
    lang = request.cookies.get('site_lang', 'da')
    if lang == 'en':
        return render_template('service_forretningsudvikling_en.html', year=datetime.now().year)
    return render_template('service_forretningsudvikling.html', year=datetime.now().year)

@app.route('/services/automatisering')
def service_automatisering():
    # Render the Danish or English automation service page depending on language cookie
    lang = request.cookies.get('site_lang', 'da')
    if lang == 'en':
        return render_template('service_automatisering_en.html', year=datetime.now().year)
    return render_template('service_automatisering.html', year=datetime.now().year)

@app.route('/services/it-produktudvikling')
def service_it_produktudvikling():
    # Render Danish or English IT Product Development page depending on language cookie
    lang = request.cookies.get('site_lang', 'da')
    if lang == 'en':
        return render_template('service_it_produktudvikling_en.html', year=datetime.now().year)
    return render_template('service_it_produktudvikling.html', year=datetime.now().year)

# Dummy data for projekter
dummy_projects = {
    1: {
        'title': 'Dataautomatisering',
        'short_desc': 'Sådan hjalp vi en kunde med at digitalisere tusindvis af papirspørgeskemaer og spare dem mange timers manuelt arbejde på hver undersøgelse.',
        'customer': 'Kunde A',
        'date': 'Maj 2024',
        'category': 'Dataanalyse',
        'image': 'brugerundersøgelse forside.jpg',
        'gallery': ['spørgeskema i kurv.jpg'],
    },
    2: {
        'title': 'Appudvikling',
        'short_desc': '',
        'customer': 'Kunde B',
        'date': 'April 2024',
        'category': 'Automatisering',
        'image': 'appudvikling foto.jpg',
        'gallery': ['appudvikling foto.jpg'],
    },
    3: {
        'title': 'Projekt 3',
        'short_desc': '',
        'customer': 'Kunde C',
        'date': 'Marts 2024',
        'category': 'Forretningsudvikling',
        'image': '360_F_1109211029_VvNG1b6mN12FaJ1aQsQxBiAnPRFz1n0x.webp',
        'gallery': ['360_F_1109211029_VvNG1b6mN12FaJ1aQsQxBiAnPRFz1n0x.webp'],
    },
    4: {
        'title': 'Projekt 4',
        'short_desc': '',
        'customer': 'Kunde D',
        'date': 'Februar 2024',
        'category': 'IT-Produktudvikling',
        'image': 'Alpha_Ventus_Windmills.webp',
        'gallery': ['Alpha_Ventus_Windmills.webp'],
    },
}

@app.route('/projekter/<int:projekt_id>')
def projekt_detail(projekt_id):
    projekt = dummy_projects.get(projekt_id)
    if not projekt:
        return render_template('404.html', year=datetime.now().year), 404
    # Render English or Danish project page depending on language cookie
    lang = request.cookies.get('site_lang', 'da')
    if lang == 'en':
        return render_template('projekt_en.html', projekt=projekt, year=datetime.now().year)
    return render_template('projekt.html', projekt=projekt, year=datetime.now().year)

# SEO: robots.txt
@app.route('/robots.txt')
def robots():
    return "User-agent: *\nAllow: /\nSitemap: https://optimatix.dk/sitemap.xml", 200, {'Content-Type': 'text/plain; charset=utf-8'}

# SEO: sitemap.xml
@app.route('/sitemap.xml')
def sitemap():
    base_url = 'https://optimatix.dk'
    today = datetime.now().strftime('%Y-%m-%d')
    
    urls = [
        ('/', 'weekly', '1.0'),
    ]
    
    # Services
    services = [
        '/services/dataanalyse',
        '/services/forretningsudvikling',
        '/services/automatisering',
        '/services/it-produktudvikling',
    ]
    for service in services:
        urls.append((service, 'monthly', '0.8'))
    
    # Projects
    for projekt_id in dummy_projects.keys():
        urls.append((f'/projekter/{projekt_id}', 'monthly', '0.7'))
    
    # Legal/Info pages
    info_pages = [
        '/privatliv',
        '/cookies',
        '/vilkar',
    ]
    for page in info_pages:
        urls.append((page, 'yearly', '0.5'))
    
    # Build XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for path, changefreq, priority in urls:
        xml += '  <url>\n'
        xml += f'    <loc>{base_url}{path}</loc>\n'
        xml += f'    <lastmod>{today}</lastmod>\n'
        xml += f'    <changefreq>{changefreq}</changefreq>\n'
        xml += f'    <priority>{priority}</priority>\n'
        xml += '  </url>\n'
    
    xml += '</urlset>'
    
    return Response(xml, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True) 