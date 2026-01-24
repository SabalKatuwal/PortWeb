#!/usr/bin/env python3
import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the gallery structure - using a more flexible regex pattern
# Match each <li> in the gallery and wrap the images in a div

pattern = r'(<li>\s*(?!<div class="gallery-images-container">))((?:\s*<a class="image fitt">.*?</a>)+)'

def replace_func(match):
    li_start = match.group(1)
    images = match.group(2)
    return f'{li_start}<div class="gallery-images-container">{images}\n\t\t\t\t\t\t</div>'

# First, let's handle the specific case for each li
old = '''<li>
									<a class="image fitt"><img src="images/cips1.webp" title="Airchitecture II" alt="" /></a>
									<a class="image fitt"><img src="images/cips2.webp" title="Airchitecture II" alt="" /></a>
									<a class="image fitt"><img src="images/cips3.webp" title="Airchitecture II" alt="" /></a>
									<p>Connect IPS<br />
										Contributed to Nepal's interbank payment platform, including SMS mode payments, secure keychain storage, and cross-border payment features. <a href="https://apps.apple.com/np/app/connectips/id1449940087" target="_blank">AppStore</a> </p>
								</li>'''

new = '''<li>
									<div class="gallery-images-container">
										<a class="image fitt"><img src="images/cips1.webp" title="Airchitecture II" alt="" /></a>
										<a class="image fitt"><img src="images/cips2.webp" title="Airchitecture II" alt="" /></a>
										<a class="image fitt"><img src="images/cips3.webp" title="Airchitecture II" alt="" /></a>
									</div>
									<p>Connect IPS<br />
										Contributed to Nepal's interbank payment platform, including SMS mode payments, secure keychain storage, and cross-border payment features. <a href="https://apps.apple.com/np/app/connectips/id1449940087" target="_blank">AppStore</a> </p>
								</li>'''

content = content.replace(old, new)

old = '''<li>
									<a class="image fitt"><img src="images/elibrary1.png" title="Airchitecture II" alt="" /></a>
									<a class="image fitt"><img src="images/elibrary2.png" title="Airchitecture II" alt="" /></a>
									<p>e Library<br />
										An iOS library management app that serves librarians and students. <a href="https://github.com/SabalKatuwal/eLibrary" target="_blank">github</a> </p>
								</li>'''

new = '''<li>
									<div class="gallery-images-container">
										<a class="image fitt"><img src="images/elibrary1.png" title="Airchitecture II" alt="" /></a>
										<a class="image fitt"><img src="images/elibrary2.png" title="Airchitecture II" alt="" /></a>
									</div>
									<p>e Library<br />
										An iOS library management app that serves librarians and students. <a href="https://github.com/SabalKatuwal/eLibrary" target="_blank">github</a> </p>
								</li>'''

content = content.replace(old, new)

old = '''<li>
									<a class="image fitt"><img src="images/weatherApp1.png" title="Airchitecture II" alt="" /></a>
									<a class="image fitt"><img src="images/weatherApp2.png" title="Airchitecture III" alt="" /></a>
									
									<p>Weather App <br />
										Delivers weather information sourced from an external API. </p>
								</li>'''

new = '''<li>
									<div class="gallery-images-container">
										<a class="image fitt"><img src="images/weatherApp1.png" title="Airchitecture II" alt="" /></a>
										<a class="image fitt"><img src="images/weatherApp2.png" title="Airchitecture III" alt="" /></a>
									</div>
									<p>Weather App <br />
										Delivers weather information sourced from an external API. </p>
								</li>'''

content = content.replace(old, new)

old = '''<li>
									<a class="image fitt"><img src="images/sahaYatri1.png" title="The Anonymous Red" alt="" /></a>
									<a class="image fitt"><img src="images/sahaYatrii2.png" title="Another Image" alt="" /></a>
									<a class="image fitt"><img src="images/sahaYatri3.png" title="Another Image 2" alt="" /></a>
									<p>Saha Yatri<br />
									Facilitate the connection between passengers and buses by providing a tracking feature.</p>
								</li>'''

new = '''<li>
									<div class="gallery-images-container">
										<a class="image fitt"><img src="images/sahaYatri1.png" title="The Anonymous Red" alt="" /></a>
										<a class="image fitt"><img src="images/sahaYatrii2.png" title="Another Image" alt="" /></a>
										<a class="image fitt"><img src="images/sahaYatri3.png" title="Another Image 2" alt="" /></a>
									</div>
									<p>Saha Yatri<br />
									Facilitate the connection between passengers and buses by providing a tracking feature.</p>
								</li>'''

content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)

print("Gallery structure updated successfully!")
