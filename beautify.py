import os
import sys
from bs4 import BeautifulSoup

def beautify_html(filepath):
    with open(filepath, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Add Google Fonts and Tailwind config
    head = soup.find('head')
    if head:
        if not head.find('link', href=lambda x: x and 'Inter' in x):
            new_tags = BeautifulSoup('''
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
                <script>
                    tailwind.config = {
                        theme: {
                            extend: {
                                fontFamily: {
                                    sans: ['Inter', 'sans-serif'],
                                },
                            },
                        },
                    }
                </script>
            ''', 'html.parser')
            for tag in new_tags:
                head.append(tag)

    # Update body
    body = soup.find('body')
    if body:
        body['class'] = 'bg-slate-50 font-sans flex h-screen text-slate-900'

    # Update sidebar
    sidebar = soup.find('aside', {'id': 'sidebar'})
    if sidebar:
        sidebar['class'] = 'bg-slate-900 text-slate-200 w-64 min-h-screen p-4 fixed md:relative transform -translate-x-full md:translate-x-0 transition-transform duration-200 ease-in-out z-30 flex-shrink-0'

        # Add close button
        if not sidebar.find('button', {'id': 'sidebar-close'}):
            close_button = BeautifulSoup('''<div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold text-white">CSE 1287 QnA</h2>
            <button id="sidebar-close" class="md:hidden">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
        </div>''', 'html.parser')
            sidebar.insert(0, close_button)

        nav = sidebar.find('nav')
        if nav and 'sidebar' not in nav.get('class', []):
            nav['class'] = 'h-full overflow-y-auto'

        # Update headings
        list_items = sidebar.find_all('li')
        for li in list_items:
            if 'font-bold' in li.get('class', []):
                li['class'] = 'py-2 px-4 font-bold text-slate-400'

        # Add transitions to links
        links = sidebar.find_all('a')
        for a in links:
            a['class'] = a.get('class', []) + ['transition-colors']
            a['class'] = [c.replace('hover:bg-gray-700', 'hover:bg-slate-700') for c in a.get('class', [])]


    # Update header and main content wrapper
    header = soup.find('header')
    if header and header.parent.name == 'body':
        wrapper = soup.new_tag('div')
        wrapper['class'] = 'flex flex-col flex-1 h-screen overflow-y-auto'
        main = soup.find('main')
        header.wrap(wrapper)
        if main:
            wrapper.append(main)

    if header:
        header['class'] = 'bg-white shadow-sm p-4 flex justify-between items-center border-b border-slate-200 sticky top-0'
        h1 = header.find('h1')
        if h1:
            h1['class'] = 'text-base md:text-xl font-semibold'
        p = header.find('p')
        if p:
            p['class'] = 'hidden md:block text-sm'

    # Update main
    main = soup.find('main')
    if main:
        main['class'] = 'p-4 md:p-8'

    section = soup.find('section')
    if section:
        h3 = section.find('h3')
        if h3:
            h3['class'] = "text-2xl font-bold mb-8 text-center"
            h3.string = h3.string.split('. ')[-1]

        articles = section.find_all('article')
        for article in articles:
            article['class'] = 'mb-4'

            h4 = article.find('h4')
            if h4:
                h4['class'] = 'bg-slate-200 p-4 rounded-t-lg font-bold'

            div = article.find('div')
            if div and 'text-gray-700' not in div.get('class', []):
                div['class'] = 'bg-white p-4 rounded-b-lg shadow-md hidden'

            # Apply styles to elements within the (now existing) div
            if div:
                for h5 in div.find_all('h5'):
                    h5['class'] = 'font-semibold mt-4'
                for ol in div.find_all('ol'):
                    ol['class'] = 'list-decimal list-inside'
                for ul in div.find_all('ul'):
                    ul['class'] = 'list-disc list-inside ml-4'
                for pre in div.find_all('pre'):
                    pre['class'] = 'bg-gray-200 p-4 rounded-md'
                for table in div.find_all('table'):
                    table['class'] = 'border-collapse border border-slate-500'
                    for th in table.find_all('th'):
                        th['class'] = 'border border-slate-400 p-2'
                    for td in table.find_all('td'):
                        td['class'] = 'border border-slate-400 p-2'

    with open(filepath, 'w') as f:
        f.write(str(soup.prettify()))

if __name__ == '__main__':
    filepath = sys.argv[1]
    beautify_html(filepath)
