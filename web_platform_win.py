from flask import Blueprint, render_template, send_from_directory

web_platform_win = Blueprint('web_platform_win', __name__)

@web_platform_win.route('/.well-known/appspecific/com.chrome.devtools.json')
def static_manifest():
    """Serve the static Chrome DevTools manifest file."""
    if not web_platform_win.debug:
        return "Not Found", 404
    return send_from_directory('static/.well-known/appspecific', 'com.chrome.devtools.json')