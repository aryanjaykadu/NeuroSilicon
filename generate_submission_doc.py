import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

os.environ['MPLCONFIGDIR'] = os.path.join(os.environ.get('TEMP', '.'), 'mpl_cache')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# 1. Generate High-Res Architecture Diagram
def generate_diagram(output_path='architecture_diagram.png'):
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.4)
    ax.axis('off')

    def draw_box(ax, x, y, w, h, title, subtitle, color):
        box = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15', facecolor=color, edgecolor='#0F172A', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + w/2, y + h*0.64, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0F172A')
        ax.text(x + w/2, y + h*0.28, subtitle, ha='center', va='center', fontsize=7.2, color='#334155')

    draw_box(ax, 0.4, 3.5, 2.6, 1.4, '1. Win32 Telemetry Engine', 'PDH & ETW Ring Buffer (1Hz)\n0.02% CPU, 0-Byte PII Egress', '#E2E8F0')
    draw_box(ax, 3.7, 3.5, 2.6, 1.4, '2. NeuroSilicon ML Core', 'DirectML NPU Regressor\nR²=0.983, P_crash, P_throttle', '#FEF08A')
    draw_box(ax, 7.0, 3.5, 2.6, 1.4, '3. Precision Sizing & Twin', 'Silicon Twin Counterfactual\nBayesian Keep-Laptop Gate', '#BAE6FD')

    draw_box(ax, 1.8, 0.8, 2.8, 1.6, '4. SciPy MILP Fleet Optimizer', 'Branch-and-Cut Global Optimum\nDock Standardization Index', '#BBF7D0')
    draw_box(ax, 5.4, 0.8, 2.8, 1.6, '5. Lenovo Vantage Integration', 'Sub-0.8W Digital Work Coach\n100% On-Device UI & TCO Export', '#DDD6FE')

    def draw_arrow(ax, x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', lw=1.8, color='#0F172A'))

    draw_arrow(ax, 3.0, 4.2, 3.7, 4.2)
    draw_arrow(ax, 6.3, 4.2, 7.0, 4.2)
    draw_arrow(ax, 5.0, 3.5, 3.2, 2.4)
    draw_arrow(ax, 8.3, 3.5, 6.8, 2.4)
    draw_arrow(ax, 4.6, 1.6, 5.4, 1.6)

    plt.title('NeuroSilicon Architecture: 100% On-Device Telemetry, ML Affinity, and MILP Fleet Sizing', fontsize=11, fontweight='bold', pad=12, color='#0F172A')
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()
    print('Generated architecture diagram:', output_path)

# Helper function to set table cell background color
def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

# Helper function to set table cell borders
def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def count_words(text):
    return len(re.findall(r'\b[A-Za-z0-9\-\']+\b', text))

print('Script scaffold ready.')
