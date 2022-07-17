from fastapi.responses import HTMLResponse

def _css_style() -> str:
    css = '''
    <style>
    body  {
        text-align: center;
        font-family: Arial;
    }
    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 12px;
    }
    .diag-button {
        background-color: #A9A9A9; /* Grey */
        border: none;
        color: white;
        padding: 12px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        border-radius: 12px;
    }
    div {
        white-space: pre-wrap;
    }   
    /* Table Styling */
    .overview {
        border-collapse: collapse;
        width: 5%;
        margin-left: auto;
        margin-right: auto;
    }
    .overview td, .overview th {
        border: 1px solid #ddd;
        padding: 8px;
    }
    .overview tr:nth-child(even){background-color: #f2f2f2;}
    .overview tr:hover {background-color: #ddd;}
    .overview th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    '''
    return css

def _head() -> str:
    head = f'''
    <head>
        <title>Heroku Template</title>
        
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Starting Template for quick Heroku Apps">
        <meta name="author" content="Jan Tuziak">
        
        {_css_style()}
    </head>
    '''
    return head


def root() -> HTMLResponse:    
    html_content = f"""
    <html>
        {_head()}
        <body>
            <h1>Heroku Template</h1>
            <h2>Put your services here</h2>
            <a href="/" class="button">Service 1</a>
            <br><br>
            <a href="/" class="button">Service 2</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def cert(certificate) -> HTMLResponse:    
    html_content = certificate
    return HTMLResponse(content=html_content, status_code=200)