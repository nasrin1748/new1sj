import pandas as pd
from pyscript import display
import html2text
import io
def greet1():
    html_content = '''
    <tr>
    <th>Data 1</th>
    <th>Data 2</th>
    </tr>
    <tr>
    <td>Calcutta</td>
    <td>Orange</td>
    </tr>
    <tr>
    <td>Robots</td>
    <td>Jazz</td>
    </tr>
     ''' 
    text_content = html2text.html2text(html_content)
    return text_content
